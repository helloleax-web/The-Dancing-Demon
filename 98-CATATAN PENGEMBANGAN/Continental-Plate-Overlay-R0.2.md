# Continental–Plate Overlay R0.2

**Status:** CATATAN PENGEMBANGAN / NON-CANON / KANDIDAT REGISTRASI  
**Tanggal:** 2026-11-18

## 1. Tujuan

R0.2 menguji satu rotasi global bersama yang membuat enam siluet benua relatif kompak terhadap sembilan muka lempeng, tanpa mengembalikan syarat satu-benua-satu-lempeng dan tanpa memaksakan pasangan berdasarkan nama.

## 2. Pemilihan orientasi

- Geometri V1.0-R diputar sebagai satu benda tegar pada bola; tidak ada benua atau lempeng yang dipindah sendiri-sendiri.
- Diuji 3.000 rotasi Euler deterministik.
- Screening memakai raster kasar 2° bujur × 0,025 sin(latitude).
- Metrik: rata-rata tak berbobot dari proporsi tiap benua yang berada pada satu muka lempeng dominan. Ini metrik kekompakan kartografis, bukan kebenaran geologi.
- Kandidat terbaik screening: **87,50%**.
- Audit raster 576.000 sel: **87,25%**.
- Audit clipping poligon sferis: **87,25%**.
- R0.1 pada audit raster yang sama: **67,59%**.
- Pencarian 3.000 rotasi tidak membuktikan optimum global.

Konvensi rotasi: R = Rz(γ) × Ry(β) × Rx(α), dengan α = 261,93476°, β = 38,51291°, γ = 158,86401°. Deviasi ortogonalitas maksimum matriks rotasi: **1,11 × 10⁻¹⁶**.

## 3. Audit clipping poligon sferis

Untuk menghindari singularitas proyeksi pada daratan, chart stereografis dibangun dengan kutub di perairan terbuka pada lintang **−77,16143°**, bujur **−177,5°**. Titik ini berada pada muka North Ocean, sekitar 15,07° dari garis pantai terdekat dan 25,65° dari batas lempeng terdekat.

- Garis pantai SVG didensifikasi 3 subdivisi per segmen.
- Setiap sisi batas lempeng disampel menjadi 100 subdivisi.
- Poligon ditriangulasi dengan ear clipping.
- Irisan dihitung melalui clipping segitiga konveks.
- Luas sferis tiap poligon irisan dihitung memakai integral garis stereografis: (A = \oint 2(x\,dy-y\,dx)/(1+x^2+y^2)).

**Catatan presisi:** integral luas dievaluasi secara analitik untuk segmen lurus dari poligon hasil clipping. Geometri garis pantai dan batas lempeng tetap merupakan pendekatan poliline tersampel; ini bukan klaim bahwa kurva kontinu yang tidak diketahui telah dipotong secara eksak.

### Matriks irisan — persentase dari masing-masing benua

| Benua | Central | Verdant | Sands | Frost | Ashen | Veiled | North Ocean | West Ocean | Southeast Ocean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Frostbound | 0,00% | 0,00% | 9,81% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 90,19% |
| Verdant Wilds | 100,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Central Reach | 0,00% | 4,24% | 71,35% | 10,07% | 0,00% | 0,00% | 0,02% | 13,70% | 0,62% |
| Sunken Sands | 0,00% | 6,42% | 0,00% | 5,58% | 0,00% | 0,00% | 88,00% | 0,00% | 0,00% |
| Ashen Frontier | 0,00% | 0,00% | 0,00% | 94,10% | 0,00% | 0,00% | 5,90% | 0,00% | 0,00% |
| Veiled Continent | 0,00% | 79,87% | 0,00% | 0,00% | 0,00% | 0,00% | 13,07% | 7,06% | 0,00% |

### Luas muka lempeng

| Muka lempeng | Luas sferis |
|---|---:|
| Central | 18,00% |
| Verdant | 12,00% |
| Sands | 10,00% |
| Frost | 8,00% |
| Ashen | 7,00% |
| Veiled | 11,00% |
| North Ocean | 14,01% |
| West Ocean | 11,00% |
| Southeast Ocean | 9,00% |

Total luas enam benua: **30,00%** permukaan bola. Jumlah luas sembilan muka: **100,00%**. Deviasi target maksimum muka lempeng: sekitar **0,00906 poin persentase**. Deviasi target maksimum luas benua: sekitar **0,00016 poin persentase**.

North Ocean adalah muka yang memuat kutub chart. Karena itu poligon muka tersebut direpresentasikan sebagai komplemen delapan muka terbatas lainnya. Irisan North Ocean untuk setiap benua dihitung sebagai sisa luas setelah delapan irisan terbatas dijumlahkan. Luas North Ocean juga dihitung sebagai komplemen delapan muka lain. Penutupan luas ini dibangun lewat komplemen, bukan hasil clipping independen kesembilan.

## 4. Muka dominan tiap benua

- **Frostbound:** Southeast Ocean (90,19%).
- **Verdant Wilds:** Central (100,00%).
- **Central Reach:** Sands (71,35%).
- **Sunken Sands:** North Ocean (88,00%).
- **Ashen Frontier:** Frost (94,10%).
- **Veiled Continent:** Verdant (79,87%).

Rata-rata proporsi benua pada muka dominan: **87,25%**. Beberapa benua tetap melintasi batas lempeng. Tidak ada aturan bahwa muka dominan harus memiliki nama yang sama dengan benua; nama muka tidak menetapkan jenis kerak.

## 5. Pemeriksaan silang raster

Audit raster luas sama 576.000 sel menghasilkan total daratan 29,99896% dan jumlah luas muka 100%. Rata-rata dominasi 87,25%, konsisten dengan clipping poligon tersampel. Data raster tetap disimpan di JSON sebagai pemeriksaan silang, bukan matriks utama.

## 6. Batas validasi

- R0.2 adalah kandidat orientasi, belum final dan belum CANON.
- Hasil clipping bergantung pada sampling poliline; tingkat subdivisi dapat dinaikkan untuk uji konvergensi.
- Komposisi kerak, tipe batas, arah/kecepatan gerak, subduksi, pemekaran, dan sesar belum ditentukan.
- Relief, bathimetri, iklim, arus, dan hidrologi belum divalidasi.

**Dampak CANON: tidak ada.**