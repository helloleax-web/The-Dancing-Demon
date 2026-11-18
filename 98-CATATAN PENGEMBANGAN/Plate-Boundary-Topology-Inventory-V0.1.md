# Plate Boundary Topology Inventory V0.1

**Status:** CATATAN PENGEMBANGAN / NON-CANON / TOPOLOGI SAJA  
**Tanggal:** 2026-11-19

## Tujuan

Mencatat pasangan muka lempeng yang berbagi setiap sisi pada geometri V1.0-R. Inventaris ini menjadi lapisan dasar sebelum arah gerak atau tipe batas ditentukan. Ia sengaja tidak menebak apakah suatu batas merupakan subduksi, pemekaran, atau sesar transform.

## Pemeriksaan struktur

- 14 simpul triple junction.
- 21 sisi batas.
- 9 muka lempeng.
- Setiap sisi menjadi batas tepat dua muka.
- Setiap simpul memiliki derajat tiga dan mempertemukan tiga muka.

Semua pemeriksaan topologi tersebut lolos pada data V1.0-R.

## Inventaris 21 batas

| ID | Simpul ujung | Muka yang berbagi batas |
|---:|---|---|
| B01 | TJ-01 — TJ-09 | Ashen ↔ Central |
| B02 | TJ-04 — TJ-05 | Ashen ↔ Sands |
| B03 | TJ-05 — TJ-09 | Ashen ↔ Veiled |
| B04 | TJ-01 — TJ-02 | Ashen ↔ Verdant |
| B05 | TJ-02 — TJ-04 | Ashen ↔ West Ocean |
| B06 | TJ-12 — TJ-13 | Central ↔ Frost |
| B07 | TJ-10 — TJ-12 | Central ↔ North Ocean |
| B08 | TJ-07 — TJ-08 | Central ↔ Southeast Ocean |
| B09 | TJ-07 — TJ-13 | Central ↔ Sands |
| B10 | TJ-08 — TJ-09 | Central ↔ Veiled |
| B11 | TJ-01 — TJ-10 | Central ↔ Verdant |
| B12 | TJ-11 — TJ-12 | Frost ↔ North Ocean |
| B13 | TJ-13 — TJ-14 | Frost ↔ Sands |
| B14 | TJ-11 — TJ-14 | Frost ↔ Verdant |
| B15 | TJ-10 — TJ-11 | North Ocean ↔ Verdant |
| B16 | TJ-06 — TJ-07 | Sands ↔ Southeast Ocean |
| B17 | TJ-06 — TJ-08 | Southeast Ocean ↔ Veiled |
| B18 | TJ-05 — TJ-06 | Sands ↔ Veiled |
| B19 | TJ-03 — TJ-14 | Sands ↔ Verdant |
| B20 | TJ-03 — TJ-04 | Sands ↔ West Ocean |
| B21 | TJ-02 — TJ-03 | Verdant ↔ West Ocean |

## Adjacency antarmuka lempeng

| Muka | Muka tetangga | Jumlah sisi bersama |
|---|---|---:|
| Central | Frost | 1 |
| Central | North Ocean | 1 |
| Central | Southeast Ocean | 1 |
| Central | Sands | 1 |
| Central | Veiled | 1 |
| Central | Verdant | 1 |
| Verdant | West Ocean | 1 |
| Sands | Southeast Ocean | 1 |
| Sands | Veiled | 1 |
| Sands | Verdant | 1 |
| Sands | West Ocean | 1 |
| Frost | North Ocean | 1 |
| Frost | Sands | 1 |
| Frost | Verdant | 1 |
| Ashen | Central | 1 |
| Ashen | Sands | 1 |
| Ashen | Veiled | 1 |
| Ashen | Verdant | 1 |
| Ashen | West Ocean | 1 |
| North Ocean | Verdant | 1 |
| Southeast Ocean | Veiled | 1 |

## 14 triple junction

| Simpul | Tiga muka yang bertemu |
|---|---|
| TJ-01 | Ashen / Central / Verdant |
| TJ-02 | Ashen / Verdant / West Ocean |
| TJ-03 | Sands / Verdant / West Ocean |
| TJ-04 | Ashen / Sands / West Ocean |
| TJ-05 | Ashen / Sands / Veiled |
| TJ-06 | Sands / Southeast Ocean / Veiled |
| TJ-07 | Central / Sands / Southeast Ocean |
| TJ-08 | Central / Southeast Ocean / Veiled |
| TJ-09 | Ashen / Central / Veiled |
| TJ-10 | Central / North Ocean / Verdant |
| TJ-11 | Frost / North Ocean / Verdant |
| TJ-12 | Central / Frost / North Ocean |
| TJ-13 | Central / Frost / Sands |
| TJ-14 | Frost / Sands / Verdant |

## Batas interpretasi

1. Pasangan muka hanya menyatakan adjacency topologis.
2. Tidak ada batas yang diberi label konvergen, divergen, atau transform.
3. Nama muka tidak menetapkan apakah keraknya benua atau samudra.
4. Tidak ada arah/kecepatan gerak, Euler pole, subduksi, pemekaran, atau pembentukan pegunungan yang ditetapkan.
5. Klasifikasi geologi harus menunggu model gerak lempeng yang konsisten pada seluruh simpul triple junction.

**Dampak CANON: tidak ada.**
