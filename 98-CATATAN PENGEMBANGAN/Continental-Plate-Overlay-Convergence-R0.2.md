# Continental–Plate Overlay R0.2 — Raster Convergence Audit

**Status:** CATATAN PENGEMBANGAN / NON-CANON / PEMERIKSAAN SILANG INDEPENDEN  
**Tanggal:** 2026-11-19

## Tujuan

Menguji apakah matriks irisan benua–lempeng R0.2 sensitif terhadap resolusi grid. Pemeriksaan ini memakai klasifikasi titik langsung pada grid luas-sama, bukan triangulasi atau clipping poligon. Dengan demikian, ia menjadi pemeriksaan silang yang relatif independen terhadap metode clipping poligon tersampel yang dipakai sebagai hasil utama R0.2.

## Metode

- Grid memakai bujur seragam dan nilai `sin(latitude)` seragam; setiap sel memiliki luas sferis yang sama.
- Titik tengah setiap sel diklasifikasikan terhadap poligon benua V0.6 pada koordinat geografis SVG.
- Untuk klasifikasi lempeng, titik geografis diputar balik memakai transpose matriks R0.2, lalu diproyeksikan balik ke bidang stereografis lokal V1.0-R.
- Delapan muka terbatas diuji dengan point-in-polygon terhadap siklus muka V1.0-R. Titik yang tidak masuk salah satu dari delapan muka tersebut diklasifikasikan sebagai Central, sesuai konstruksi muka komplemen.
- Rotasi, geometri, dan sumber input sama dengan audit R0.2. Hanya resolusi grid yang berubah.

## Resolusi dan hasil

| Grid bujur × sin(latitude) | Sel | Rata-rata muka dominan |
|---|---:|---:|
| 1° × 0,005 | 144.000 | 87,27466% |
| 0,5° × 0,0025 | 576.000 | 87,24988% |
| 0,25° × 0,00125 | 2.304.000 | 87,25730% |
| 0,125° × 0,000625 | 9.216.000 | 87,25443% |

Perbandingan matriks irisan antarresolusi:

| Perbandingan | Selisih maksimum satu sel matriks | Sel yang paling berubah | Perubahan rata-rata dominasi |
|---|---:|---|---:|
| 0,5° → 0,25° | 0,06595 poin persentase | Veiled Continent × North Ocean | 0,00742 poin |
| 0,25° → 0,125° | 0,01317 poin persentase | Veiled Continent × North Ocean | 0,00286 poin |
| 0,5° → 0,125° | 0,05278 poin persentase | Veiled Continent × North Ocean | 0,00456 poin |

Selisih maksimum antar dua tingkat resolusi terakhir turun sekitar lima kali dibanding interval sebelumnya. Rata-rata dominasi juga berubah makin kecil: 0,00742 menjadi 0,00286 poin persentase. Ini menunjukkan bahwa estimasi raster mendekati nilai stabil pada resolusi 0,125°.

Pada grid tertinggi, luas enam benua masing-masing terukur sekitar 4,49997%; 5,40003%; 7,20023%; 3,89993%; 2,70003%; dan 6,30008% dari permukaan bola. Nilai ini sangat dekat dengan target kerja V0.6. Luas sembilan muka lempeng juga mendekati target V1.0-R; penyimpangan kecil yang tersisa konsisten dengan diskretisasi grid.

## Keputusan

**Tidak perlu mengubah geometri, rotasi, atau matriks clipping utama R0.2.** Pertahankan clipping poligon sferis sebagai hasil utama dan simpan raster 9,216 juta sel sebagai pemeriksaan silang independen. Hasil konvergensi cukup stabil untuk melanjutkan ke audit geologi konseptual, tetapi belum membenarkan penetapan tipe kerak atau tipe batas lempeng.

## Batas validasi

- Klasifikasi raster tetap pendekatan titik-tengah sel, bukan irisan poligon eksak.
- Uji ini mengukur sensitivitas numerik terhadap resolusi grid, bukan kebenaran bentuk garis pantai atau geometri lempeng.
- Rata-rata muka dominan adalah metrik kekompakan kartografis, bukan hukum geologi.
- Arah gerak, kecepatan lempeng, subduksi, pemekaran, sesar, jenis kerak, relief, dan bathimetri belum divalidasi.

**Dampak CANON: tidak ada.**
