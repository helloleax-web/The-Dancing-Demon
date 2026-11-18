# Plate Geometry V1.0-R — Validation Report

**Status:** CATATAN PENGEMBANGAN / NON-CANON  
**Tanggal:** 2026-11-18  
**Hasil:** PASS — geometri planar dan target luas tervalidasi ulang

## 1. Ringkasan

V1.0-R adalah rekonstruksi numerik baru dari geometri lempeng yang sebelumnya didokumentasikan sebagai V1.0. Rekonstruksi mempertahankan topologi dan target luas yang dipublikasikan, tetapi menggunakan koordinat planar dan bobot Tutte yang baru.

**V1.0-R bukan pemulihan identik dari koordinat asli V1.0.** Koordinat planar asli V1.0 tidak ditemukan pada histori sumber yang diperiksa. Karena itu, V1.0-R diberi nomor versi tersendiri dan tidak menggantikan arsip referensi V1.0.

## 2. Hasil validasi

| Pemeriksaan | Hasil |
|---|---:|
| Simpul | 14 |
| Sisi | 21 |
| Muka | 9 |
| Karakteristik Euler | 14 − 21 + 9 = 2 |
| Derajat semua simpul | 3 |
| Konektivitas simpul | 3 |
| Bobot Tutte | Positif dan tersedia untuk seluruh sisi |
| Persilangan sisi non-insiden | 0 |
| Batas luar | Cembung; radius dan metadata sudut dapat direproduksi |
| Poligon setiap muka | Valid |
| Delapan muka terbatas menutup poligon luar | Ya |
| Luas tumpang tindih planar | Mendekati 0 (presisi floating point) |
| Jumlah target dan hasil luas permukaan | 100% |
| Deviasi luas maksimum | 0,002188 poin persentase |

Semua 7 simpul interior berada di dalam batas luar. Koordinat interior dapat direproduksi dari bobot sisi positif yang tersimpan menggunakan persamaan barycentric Tutte. Radius batas, sudut simpul, dan celah sudut berjumlah 2π juga lolos pemeriksaan. Proyeksi inverse stereographic menghasilkan titik pada bola satuan.

## 3. Luas permukaan

| Wilayah | Target | Hasil V1.0-R | Deviasi |
|---|---:|---:|---:|
| Central | 18,00% | 18,000249% | +0,000249 pp |
| Verdant | 12,00% | 12,001698% | +0,001698 pp |
| Sands | 10,00% | 10,002188% | +0,002188 pp |
| Frost | 8,00% | 7,999276% | −0,000724 pp |
| Ashen | 7,00% | 7,000405% | +0,000405 pp |
| Veiled | 11,00% | 11,000375% | +0,000375 pp |
| North Ocean | 14,00% | 13,999195% | −0,000805 pp |
| West Ocean | 11,00% | 10,998698% | −0,001302 pp |
| Southeast Ocean | 9,00% | 8,997917% | −0,002083 pp |
| **Total** | **100,00%** | **100,000000%** | **0,000000 pp** |

Toleransi penerimaan validator adalah 0,01 poin persentase. Deviasi maksimum aktual berada di bawah 0,003 poin persentase.

## 4. Metode

1. Topologi graf planar 3-terhubung dipertahankan: 14 simpul, 21 sisi, dan 9 siklus muka.
2. Tujuh simpul batas muka Central ditempatkan pada lingkaran cembung dengan jarak sudut yang dioptimalkan.
3. Tujuh simpul interior dihitung menggunakan embedding barycentric Tutte dengan bobot sisi simetris positif.
4. Bidang dipetakan ke bola satuan menggunakan inverse stereographic projection:
   - (X = 2x/(1+x^2+y^2))
   - (Y = 2y/(1+x^2+y^2))
   - (Z = (x^2+y^2-1)/(1+x^2+y^2))
5. Luas muka dihitung dengan integral batas:
   [
   A = oint \frac{2(x\,dy-y\,dx)}{1+x^2+y^2}
   ]
6. Central dihitung sebagai komplemen bola dari delapan muka terbatas lainnya.

## 5. Berkas

- [Data geometri V1.0-R](World-Plate-Geometry-V1.0-R-reconstructed.json) — koordinat planar, bobot sisi, topologi, proyeksi, target, dan hasil luas.
- [Validator Python](validate_plate_geometry_v1_0_r.py) — pemeriksaan mandiri menggunakan standard library Python.
- [Pratinjau planar V1.0-R](World-Plate-Geometry-V1.0-R-planar.svg) — visual embedding matematis, bukan peta geografis.
- [Referensi V1.0 asli](World-Plate-Geometry-V1.0-reference.json) — arsip hasil dan topologi yang dipublikasikan sebelum rekonstruksi.

Jalankan validator dari direktori yang sama dengan kedua berkas data dan script:

```bash
python validate_plate_geometry_v1_0_r.py
```

Hasil uji pada versi yang diunggah: **RESULT: PASS**.

## 6. Batas validasi

V1.0-R memvalidasi geometri dan pembagian luas pada bola satuan, bukan geologi planet yang sebenarnya.

Belum diuji:
- Penempatan enam siluet benua di dalam enam lempeng pembawa.
- Margin samudra di sekitar setiap benua.
- Orientasi geografis final dan rotasi globe.
- Kesesuaian batas lempeng dengan subduksi, pemekaran dasar laut, transform fault, dan dinamika mantel.
- Kesesuaian geografi dengan iklim, arus laut, relief, serta hidrologi.

Koordinat lintang-bujur yang diturunkan dari proyeksi hanya bersifat matematis. Jangan menganggapnya sebagai orientasi dunia yang telah dipilih.

## 7. Keputusan penggunaan

- **V1.0-R menjadi baseline geometri lempeng yang dapat direproduksi untuk pekerjaan pengembangan berikutnya.**
- V1.0 asli tetap disimpan sebagai referensi historis; koordinat planar aslinya belum ditemukan.
- V1.1 Tutte candidate tetap menjadi arsip eksperimen dan tidak dipakai sebagai baseline luas karena target permukaannya tidak terpenuhi.
- Tidak ada perubahan CANON. Seluruh peta dan geometri tetap CATATAN PENGEMBANGAN / NON-CANON.
