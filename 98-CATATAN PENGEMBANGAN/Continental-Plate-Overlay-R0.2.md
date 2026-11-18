# Continental–Plate Overlay R0.2

**Status:** CATATAN PENGEMBANGAN / NON-CANON / KANDIDAT REGISTRASI  
**Tanggal:** 2026-11-18

## 1. Tujuan

R0.2 menguji apakah satu rotasi global bersama dapat membuat siluet enam benua lebih kompak terhadap sembilan muka lempeng, tanpa mengembalikan syarat satu-benua-satu-lempeng dan tanpa memaksakan pasangan berdasarkan nama.

## 2. Metode pemilihan orientasi

- Geometri lempeng V1.0-R diputar sebagai satu benda tegar pada bola; tidak ada benua atau lempeng yang dipindah sendiri-sendiri.
- Diuji 3.000 rotasi Euler deterministik.
- Screening memakai raster kasar 2° bujur × 0,025 sin(latitude).
- Metrik: rata-rata tak berbobot dari proporsi tiap benua yang berada pada satu muka lempeng dominan. Ini mengukur kekompakan overlay, bukan kebenaran geologi.
- Kandidat terbaik pada screening memiliki rata-rata **87,50%**. Audit raster resolusi lebih tinggi menghasilkan **87,27%**.
- R0.1 memiliki rata-rata dominan sekitar **67,61%** pada audit grid yang sama. Dengan metrik ini, R0.2 adalah kandidat kerja yang lebih baik.
- Pencarian 3.000 rotasi tidak membuktikan optimum global; optimasi lebih luas masih mungkin menemukan orientasi lain.

Konvensi rotasi: R = Rz(γ) × Ry(β) × Rx(α), dengan α = 261,93476°, β = 38,51291°, γ = 158,86401°.

## 3. Hasil raster resolusi audit

Raster luas sama: langkah bujur 1° dan langkah sin(latitude) 0,005, total 144.000 sel. Matriks berikut menunjukkan persentase dari luas masing-masing benua.

| Benua | Central | Verdant | Sands | Frost | Ashen | Veiled | North Ocean | West Ocean | Southeast Ocean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Frostbound | 0,00% | 0,00% | 9,79% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 90,21% |
| Verdant Wilds | 100,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Central Reach | 0,00% | 4,24% | 71,41% | 10,09% | 0,00% | 0,00% | 0,02% | 13,64% | 0,61% |
| Sunken Sands | 0,00% | 6,43% | 0,00% | 5,57% | 0,00% | 0,00% | 88,00% | 0,00% | 0,00% |
| Ashen Frontier | 0,00% | 0,00% | 0,00% | 94,07% | 0,00% | 0,00% | 5,93% | 0,00% | 0,00% |
| Veiled Continent | 0,00% | 79,96% | 0,00% | 0,00% | 0,00% | 0,00% | 12,96% | 7,08% | 0,00% |

### Muka lempeng — pemeriksaan luas

| Muka lempeng | Luas raster |
|---|---:|
| Central | 18,01% |
| Verdant | 12,00% |
| Sands | 10,00% |
| Frost | 8,00% |
| Ashen | 6,99% |
| Veiled | 11,02% |
| North Ocean | 14,00% |
| West Ocean | 11,00% |
| Southeast Ocean | 8,98% |

Hasil luas muka tetap mendekati target V1.0-R. Total luas daratan pada grid mendekati 30%. Angka irisan merupakan estimasi raster, bukan clipping sferis eksak.

## 4. Benua dan muka dominan

- **Frostbound:** Southeast Ocean (90,21%).
- **Verdant Wilds:** Central (100,00%).
- **Central Reach:** Sands (71,41%).
- **Sunken Sands:** North Ocean (88,00%).
- **Ashen Frontier:** Frost (94,07%).
- **Veiled Continent:** Verdant (79,96%).

Sebagian benua tetap melintasi lebih dari satu muka. Tidak ada aturan bahwa muka dominan harus memiliki nama yang sama dengan benua. Nama muka tidak menetapkan jenis kerak.

## 5. Batas validasi

- Orientasi ini kandidat, belum final dan belum CANON.
- Raster bukan clipping poligon sferis eksak.
- Komposisi kerak, tipe batas, arah gerak, kecepatan, subduksi, pemekaran, dan sesar belum ditentukan.
- Relief, bathimetri, iklim, arus, dan hidrologi belum divalidasi.

**Dampak CANON: tidak ada.**