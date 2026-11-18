# Plate Containment — Common Orientation Search V0.1

**Status:** CATATAN PENGEMBANGAN / NON-CANON  
**Continent geometry:** V0.6  
**Plate geometry:** V1.0-R reconstructed baseline  
**Result:** No common global orientation was found in the exploratory search.

## 1. Question

Can the six V0.6 continent footprints be placed entirely inside their assigned carrier-plate faces by applying one common rotation to the globe, without independently moving or reshaping continents?

Assignments follow the atlas framework:
- Frostbound Expanse → Frost
- Verdant Wilds → Verdant
- The Central Reach → Central
- The Sunken Sands → Sands
- The Ashen Frontier → Ashen
- The Veiled Continent → Veiled

## 2. Method

The plate geometry uses an inverse-stereographic mapping from planar coordinates to a unit sphere. Continent vertices from the V0.6 SVG were converted to unit-sphere coordinates, subjected to a common 3D rotation, and mapped back into the plate model's stereographic plane.

The bounded plate faces were tested using point-in-polygon checks. Central is the complementary spherical face, so its samples must lie outside the outer boundary polygon.

The screening set sampled every sixth rendered SVG vertex, approximately two samples per original coastline edge. A deterministic search tested 40,000 pseudo-random global rotations with a fixed seed, in addition to a coarse 30-degree Euler-angle grid.

## 3. Best sampled result

No tested common rotation placed all six continents inside their assigned plate faces.

At the best sampled rotation, only Sunken Sands passed all its sampled points:

| Continent | Correctly contained samples |
|---|---:|
| Frostbound Expanse | 0 / 60 |
| Verdant Wilds | 16 / 62 |
| The Central Reach | 35 / 74 |
| The Sunken Sands | 50 / 50 |
| The Ashen Frontier | 0 / 54 |
| The Veiled Continent | 14 / 68 |
| **Total** | **115 / 368** |

Only one of six continents was fully contained at the best sampled orientation.

## 4. Important distinction: area fit versus shape/placement fit

The target area of every continent is smaller than the nominal area of its assigned plate:

| Pair | Continent area | Carrier plate area |
|---|---:|---:|
| Frostbound / Frost | 4.5% | 8% |
| Verdant / Verdant | 5.4% | 12% |
| Central / Central | 7.2% | 18% |
| Sunken Sands / Sands | 3.9% | 10% |
| Ashen / Ashen | 2.7% | 7% |
| Veiled / Veiled | 6.3% | 11% |

This means the nominal area budget is sufficient, but area arithmetic alone does not establish geometric containment. The current shapes, positions, and plate-face geometry are not yet reconciled.

## 5. What this result means

This is **not a mathematical proof** that no common orientation exists. The search is a reproducible exploratory screen, and sampled points do not replace exact polygon-edge intersection or full spherical topology validation.

However, it is sufficient to reject the claim that V0.6 currently passes plate containment. The next design decision is whether to preserve the continent macro-layout or the reconstructed plate partition as the stronger constraint.

Recommended next step: preserve the V0.6 area targets, then test a deliberate re-placement of continent footprints within their assigned carrier faces. If that produces unacceptable global geography, revisit the plate partition or face assignments instead.

All findings remain NON-CANON. No story locations, nations, characters, organizations, or mysteries were changed.

Structured results: [Plate Containment Orientation Search V0.1 JSON](Plate-Containment-Orientation-Search-V0.1.json).
