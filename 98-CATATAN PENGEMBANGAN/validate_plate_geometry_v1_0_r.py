#!/usr/bin/env python3
"""Validate the reconstructed The Dancing Demon plate geometry V1.0-R.

Run from any directory:
    python validate_plate_geometry_v1_0_r.py

The script uses only the Python standard library.
"""
from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "World-Plate-Geometry-V1.0-R-reconstructed.json"
TOL = 1e-8
AREA_TOL_PP = 0.01


def cross(a, b, c=None):
    if c is None:
        return a[0] * b[1] - a[1] * b[0]
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def signed_area_xy(poly):
    return 0.5 * sum(
        poly[i][0] * poly[(i + 1) % len(poly)][1]
        - poly[(i + 1) % len(poly)][0] * poly[i][1]
        for i in range(len(poly))
    )


def point_on_segment(p, a, b, eps=1e-10):
    if abs(cross(a, b, p)) > eps:
        return False
    return (min(a[0], b[0]) - eps <= p[0] <= max(a[0], b[0]) + eps
            and min(a[1], b[1]) - eps <= p[1] <= max(a[1], b[1]) + eps)


def segments_intersect(a, b, c, d, eps=1e-10):
    o1 = cross(a, b, c)
    o2 = cross(a, b, d)
    o3 = cross(c, d, a)
    o4 = cross(c, d, b)

    if ((o1 > eps and o2 < -eps) or (o1 < -eps and o2 > eps)) and \
       ((o3 > eps and o4 < -eps) or (o3 < -eps and o4 > eps)):
        return True
    return (point_on_segment(c, a, b, eps)
            or point_on_segment(d, a, b, eps)
            or point_on_segment(a, c, d, eps)
            or point_on_segment(b, c, d, eps))


def point_in_polygon(point, polygon):
    x, y = point
    inside = False
    for i, a in enumerate(polygon):
        b = polygon[(i + 1) % len(polygon)]
        if point_on_segment(point, a, b):
            return True
        if (a[1] > y) != (b[1] > y):
            x_hit = (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0]
            if x < x_hit:
                inside = not inside
    return inside


def spherical_edge_area(a, b):
    """Exact line-integral contribution for a straight edge after inverse stereographic projection."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    aa = dx * dx + dy * dy
    bb = 2.0 * (a[0] * dx + a[1] * dy)
    cc = 1.0 + a[0] * a[0] + a[1] * a[1]
    determinant = 4.0 * aa * cc - bb * bb
    planar_cross = a[0] * b[1] - a[1] * b[0]

    if aa < 1e-15:
        integral = 1.0 / cc
    else:
        root = math.sqrt(max(determinant, 0.0))
        if root < 1e-15:
            raise ValueError("Degenerate spherical edge integral")
        integral = (2.0 / root) * (
            math.atan((2.0 * aa + bb) / root) - math.atan(bb / root)
        )
    return 2.0 * planar_cross * integral


def spherical_face_area(coords, cycle):
    total = 0.0
    for i, node in enumerate(cycle):
        nxt = cycle[(i + 1) % len(cycle)]
        total += spherical_edge_area(coords[node], coords[nxt])
    return abs(total)


def connected(nodes, edges):
    if not nodes:
        return True
    adjacency = {n: set() for n in nodes}
    for a, b in edges:
        if a in adjacency and b in adjacency:
            adjacency[a].add(b)
            adjacency[b].add(a)
    start = next(iter(nodes))
    seen = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for nxt in adjacency[node] - seen:
            seen.add(nxt)
            stack.append(nxt)
    return seen == set(nodes)


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    coords = {n: tuple(v["planar_xy"]) for n, v in data["nodes"].items()}
    edges = [tuple(e) for e in data["edges"]]
    edge_set = {tuple(sorted(e)) for e in edges}
    faces = data["faces"]
    boundary = data["boundary"]["nodes"]
    all_nodes = set(coords)
    interior = all_nodes - set(boundary)
    checks = []

    def record(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    record("14 vertices", len(coords) == 14, str(len(coords)))
    record("21 edges", len(edges) == 21, str(len(edges)))
    record("9 faces", len(faces) == 9, str(len(faces)))
    record("Euler characteristic", len(coords) - len(edges) + len(faces) == 2,
           f"{len(coords)} - {len(edges)} + {len(faces)} = {len(coords)-len(edges)+len(faces)}")

    degrees = {n: 0 for n in all_nodes}
    for a, b in edges:
        if a not in all_nodes or b not in all_nodes:
            raise ValueError(f"Unknown edge endpoint: {(a, b)}")
        degrees[a] += 1
        degrees[b] += 1
    record("all vertex degrees are 3", all(v == 3 for v in degrees.values()), str(degrees))

    record("graph connected", connected(all_nodes, edges))
    three_connected = True
    for count in (1, 2):
        for removed in combinations(all_nodes, count):
            remaining = all_nodes - set(removed)
            remaining_edges = [e for e in edges if e[0] in remaining and e[1] in remaining]
            if not connected(remaining, remaining_edges):
                three_connected = False
                break
        if not three_connected:
            break
    record("vertex connectivity at least 3", three_connected)

    face_edge_counts = {}
    for face_name, cycle in faces.items():
        record(f"{face_name}: no repeated vertices", len(cycle) == len(set(cycle)))
        face_edges = []
        for i, node in enumerate(cycle):
            nxt = cycle[(i + 1) % len(cycle)]
            key = tuple(sorted((node, nxt)))
            face_edges.append((coords[node], coords[nxt]))
            record(f"{face_name}: edge {node}-{nxt} exists", key in edge_set)
            face_edge_counts[key] = face_edge_counts.get(key, 0) + 1
        simple = True
        for i, (a, b) in enumerate(face_edges):
            for j in range(i + 1, len(face_edges)):
                if j == i + 1 or (i == 0 and j == len(face_edges) - 1):
                    continue
                c, d = face_edges[j]
                if segments_intersect(a, b, c, d):
                    simple = False
        record(f"{face_name}: simple polygon", simple)

    incidence_ok = all(face_edge_counts.get(edge, 0) == 2 for edge in edge_set)
    record("face-edge incidence matches closed partition", incidence_ok)

    boundary_xy = [coords[n] for n in boundary]
    turns = [cross(boundary_xy[i], boundary_xy[(i + 1) % len(boundary_xy)],
                   boundary_xy[(i + 2) % len(boundary_xy)])
             for i in range(len(boundary_xy))]
    convex = all(t > 1e-10 for t in turns) or all(t < -1e-10 for t in turns)
    record("outer boundary is convex", convex)
    record("all interior vertices are inside boundary",
           all(point_in_polygon(coords[n], boundary_xy) for n in interior))

    radius = float(data["boundary"]["radius"])
    angles = data["boundary"]["angles_rad"]
    gaps = data["boundary"]["gaps_rad"]
    radius_error = max(abs(math.hypot(*coords[n]) - radius) for n in boundary)
    gap_sum = sum(float(gaps[n]) for n in boundary)
    angle_error = 0.0
    for i, node in enumerate(boundary):
        next_node = boundary[(i + 1) % len(boundary)]
        expected = (float(angles[node]) + float(gaps[node])) % (2.0 * math.pi)
        actual = float(angles[next_node]) % (2.0 * math.pi)
        difference = abs(expected - actual)
        angle_error = max(angle_error, min(difference, 2.0 * math.pi - difference))
        coord_angle = math.atan2(coords[node][1], coords[node][0]) % (2.0 * math.pi)
        difference = abs(coord_angle - float(angles[node]) % (2.0 * math.pi))
        angle_error = max(angle_error, min(difference, 2.0 * math.pi - difference))
    record("boundary radius and angular metadata reproduce",
           radius_error < 1e-8 and abs(gap_sum - 2.0 * math.pi) < 1e-8 and angle_error < 1e-8,
           f"radius error={radius_error:.3e}; gap sum error={abs(gap_sum-2.0*math.pi):.3e}; angle error={angle_error:.3e}")

    crossing_pairs = []
    for i, (a, b) in enumerate(edges):
        for j in range(i + 1, len(edges)):
            c, d = edges[j]
            if len({a, b, c, d}) < 4:
                continue
            if segments_intersect(coords[a], coords[b], coords[c], coords[d]):
                crossing_pairs.append((i, j))
    record("zero nonincident edge crossings", not crossing_pairs, str(crossing_pairs))

    bounded_names = [name for name in faces if name != "Central"]
    bounded_planar_area = sum(abs(signed_area_xy([coords[n] for n in faces[name]]))
                              for name in bounded_names)
    outer_planar_area = abs(signed_area_xy(boundary_xy))
    record("bounded face areas equal outer polygon area",
           abs(bounded_planar_area - outer_planar_area) < 1e-8,
           f"bounded={bounded_planar_area:.12f}; outer={outer_planar_area:.12f}")

    weights = {tuple(sorted(item["edge"])): float(item["weight"])
               for item in data["edge_weights"]}
    adjacency = {n: [] for n in all_nodes}
    for a, b in edges:
        w = weights[tuple(sorted((a, b)))]
        adjacency[a].append((b, w))
        adjacency[b].append((a, w))
    barycentric_error = 0.0
    for node in interior:
        total_w = sum(w for _, w in adjacency[node])
        expected_x = sum(coords[nxt][0] * w for nxt, w in adjacency[node]) / total_w
        expected_y = sum(coords[nxt][1] * w for nxt, w in adjacency[node]) / total_w
        error = math.hypot(coords[node][0] - expected_x, coords[node][1] - expected_y)
        barycentric_error = max(barycentric_error, error)
    record("Tutte weighted coordinates reproduce", barycentric_error < 1e-8,
           f"max error={barycentric_error:.3e}")

    sphere_error = 0.0
    for x, y in coords.values():
        den = 1.0 + x*x + y*y
        xyz = (2*x/den, 2*y/den, (x*x + y*y - 1.0)/den)
        sphere_error = max(sphere_error, abs(sum(v*v for v in xyz) - 1.0))
    record("inverse stereographic points lie on unit sphere", sphere_error < 1e-10,
           f"max norm error={sphere_error:.3e}")

    bounded_areas = {
        name: spherical_face_area(coords, faces[name])
        for name in bounded_names
    }
    sphere_area = 4.0 * math.pi
    measured = {name: area / sphere_area * 100.0
                for name, area in bounded_areas.items()}
    measured["Central"] = 100.0 - sum(measured.values())
    targets = data["target_percent_surface"]
    deviations = {name: measured[name] - targets[name] for name in targets}
    max_deviation = max(abs(v) for v in deviations.values())
    record("surface area sums to 100%", abs(sum(measured.values()) - 100.0) < 1e-8,
           f"sum={sum(measured.values()):.12f}%")
    record("surface area targets met", max_deviation <= AREA_TOL_PP,
           f"max deviation={max_deviation:.6f} percentage points; tolerance={AREA_TOL_PP}")

    print(f"Plate Geometry {data['version']} validation")
    print("-" * 60)
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f" — {detail}" if detail else ""))
    print("-" * 60)
    print("Measured area percentages:")
    for name in targets:
        print(f"  {name:16s} {measured[name]:10.6f}%  target {targets[name]:6.2f}%  deviation {deviations[name]:+.6f} pp")
    failures = [name for name, ok, _ in checks if not ok]
    print("-" * 60)
    print("RESULT:", "PASS" if not failures else "FAIL")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
