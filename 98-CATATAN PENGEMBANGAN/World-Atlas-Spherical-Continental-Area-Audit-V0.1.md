# World Atlas — Spherical Continental Area Audit V0.1

**Status:** CATATAN PENGEMBANGAN / NON-CANON  
**Source geometry:** `World-Atlas-Continental-Silhouette-V0.5.svg`  
**Result:** The existing planar area targets do not represent the spherical land shares of the current V0.5 coastline paths.

## 1. Why this audit exists

Earlier polygon audits measured the six continent shapes with the shoelace formula in SVG canvas coordinates. That is valid for checking the proportions of the drawing, but the V0.5 frame maps longitude and latitude linearly. Equal canvas areas at different latitudes do not represent equal areas on a sphere.

This audit measures the current six polygon paths on a unit sphere using their encoded longitude/latitude coordinates. It does not redraw the continents or promote any geography to CANON.

## 2. Coordinate transform

The SVG map frame is (x=100\ldots1700), (y=120\ldots850). Its exact linear coordinate transform is:

- Longitude: `lon = ((x - 100) / 1600) × 360 − 180`
- Latitude: `lat = 90 − ((y - 120) / 730) × 180`

This is an equirectangular / Plate Carrée coordinate layout. It is useful as a coordinate scaffold, but it is not equal-area. The fact that the SVG is linear in longitude and latitude must not be confused with a validated production map projection.

## 3. Measurement method

Each straight SVG polygon edge is interpreted as linear interpolation in longitude and latitude between its endpoints. On a unit sphere, the signed area contribution can be evaluated from the boundary integral of `sin(latitude) d(longitude)`. For a segment with changing latitude:

`Δλ × (cos(φ_start) − cos(φ_end)) / (φ_end − φ_start)`

For a horizontal segment, the contribution is `Δλ × sin(φ_start)`. The absolute signed polygon area is used, selecting the smaller region.

Area fractions are independent of sphere radius. A radius of 6,371 km is used below only to provide an intuitive Earth-sized area conversion.

## 4. Results

| Continent | Previous planar target | Measured spherical share of six continents | Difference |
|---|---:|---:|---:|
| Frostbound Expanse | 15.00% | 9.19% | −5.81 pp |
| Verdant Wilds | 18.00% | 21.57% | +3.57 pp |
| Central Reach | 24.00% | 28.76% | +4.76 pp |
| Sunken Sands | 13.00% | 11.75% | −1.25 pp |
| Ashen Frontier | 9.00% | 8.21% | −0.79 pp |
| Veiled Continent | 21.00% | 20.51% | −0.49 pp |

The six polygons cover **26.44% of the sphere**, not the current 30% working land assumption. With an illustrative Earth radius, the mapped area is about **134.86 million km²**; reaching 30% would require about **18.16 million km²** more land. The percentage result is the important one; the km² values depend on the illustrative radius.

## 5. What this does and does not prove

**Proven for this audit:**
- Six polygon elements were measured from the V0.5 SVG.
- The map frame can be transformed deterministically to longitude and latitude.
- Under the stated edge interpretation, the spherical continent shares differ materially from the old planar targets.
- The total mapped land fraction differs from the 30% working assumption.

**Not proven:**
- That the V0.5 coastlines are the final intended shapes.
- That the six continents fit inside their named carrier plates.
- That the plate partition has a geographically meaningful orientation.
- That the plate boundaries are geodynamically plausible.
- That any relief, drainage, climate, or biome is correct.

The old 15/18/24/13/9/21 figures remain useful as **planar design targets**, but they must not be described as measured spherical land shares.

## 6. Decisions required before the next atlas version

1. Choose whether to preserve the old relative continent shares or accept the measured V0.5 spherical shares as the new design baseline.
2. Decide whether the 30% land assumption remains a target. If yes, add or enlarge land geometry deliberately rather than silently treating the current SVG as 30%.
3. Establish a globe rotation and test each continent against its assigned spherical carrier-plate face.
4. Only after those checks pass, derive final relief, watersheds, rivers, climate, and biomes.

**Recommendation:** do not draw more rivers or assign regional biomes yet. First resolve continent area targets, global land coverage, and plate containment. Otherwise later geography will be built on a map whose scale and placement are still unsettled.

All results remain NON-CANON. No story location, country, character, organization, or mystery was changed.
