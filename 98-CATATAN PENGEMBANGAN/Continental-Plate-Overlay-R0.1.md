# Continental–Plate Overlay R0.1

**Status:** CATATAN PENGEMBANGAN / NON-CANON / REGISTRASI ILUSTRATIF  
**Tanggal:** 2026-11-18

## 1. Tujuan

Membuat overlay koordinat yang dapat direproduksi antara siluet enam benua V0.6 dan partisi lempeng V1.0-R, lalu menghitung matriks irisan benua × lempeng. Ini pemeriksaan geometri awal, bukan penetapan peta dunia final.

## 2. Registrasi R0.1

Dipakai registrasi identitas (*identity registration*) dari proyeksi stereografis geometri lempeng ke bingkai geografis V0.6:
- Kutub proyeksi stereografis disejajarkan dengan Kutub Utara geografis.
- Sumbu planar +x disejajarkan dengan ekuator pada bujur 0°.
- Sumbu planar +y disejajarkan dengan ekuator pada bujur +90°.

Ini konvensi koordinat deterministik, **bukan klaim bahwa orientasi tersebut merupakan orientasi dunia yang dimaksud**.

## 3. Hasil overlay

Lihat [peta overlay benua dan batas lempeng R0.1](World-Atlas-Continental-Plate-Overlay-R0.1.svg).

### Metode pengukuran

- Raster luas sama (*equal-area raster*): langkah bujur 1° dan langkah sin(latitude) 0,005.
- Total 144.000 sel berluas sama.
- Titik tengah setiap sel diklasifikasikan terhadap poligon benua dan muka lempeng.
- Persentase irisan per benua dihitung terhadap jumlah sel daratan benua tersebut.
- Estimasi luas muka lempeng dihitung pada grid yang sama.

Ini estimasi raster, bukan clipping poligon sferis eksak. Kuantisasi grid dan klasifikasi titik tengah menghasilkan deviasi kecil.

### Matriks irisan — persentase dari masing-masing benua

| Benua | Central | Verdant | Sands | Frost | Ashen | Veiled | North Ocean | West Ocean | Southeast Ocean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Frostbound | 98,43% | 0,00% | 0,00% | 0,00% | 1,03% | 0,54% | 0,00% | 0,00% | 0,00% |
| Verdant Wilds | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 97,84% | 0,00% | 0,00% | 2,16% |
| Central Reach | 0,00% | 42,22% | 0,00% | 0,00% | 8,82% | 0,00% | 38,98% | 9,99% | 0,00% |
| Sunken Sands | 0,00% | 67,49% | 0,00% | 0,00% | 0,00% | 0,00% | 32,51% | 0,00% | 0,00% |
| Ashen Frontier | 0,00% | 22,96% | 0,00% | 0,00% | 0,92% | 0,00% | 0,00% | 76,11% | 0,00% |
| Veiled Continent | 0,00% | 18,30% | 22,07% | 23,57% | 0,00% | 0,00% | 23,11% | 12,96% | 0,00% |

Angka dibulatkan dua desimal. Nilai 0,00% berarti tidak ada sel raster yang terklasifikasi pada muka tersebut pada resolusi ini; bukan bukti bahwa irisan infinitesimal tidak ada.

### Pemeriksaan luas lempeng

| Muka lempeng | Luas raster |
|---|---:|
| Central | 18,00% |
| Verdant | 12,00% |
| Sands | 10,00% |
| Frost | 8,00% |
| Ashen | 7,01% |
| Veiled | 10,99% |
| North Ocean | 14,00% |
| West Ocean | 11,00% |
| Southeast Ocean | 9,00% |

Estimasi total daratan pada grid sekitar **30,00%** permukaan bola, mendekati target 30% dan audit V0.6 sekitar 30,00017%. Nilai muka lempeng mendekati target V1.0-R. Validasi geometri eksak tetap mengacu pada laporan validator V1.0-R, bukan audit raster ini.

## 4. Interpretasi

R0.1 memperlihatkan konsekuensi satu registrasi koordinat yang eksplisit: beberapa benua hampir seluruhnya berada pada satu muka, sementara benua lain terpotong oleh beberapa muka. Ini sesuai dengan aturan aktif banyak-ke-banyak, tetapi **tidak berarti registrasi ini sudah baik atau final**.

Nama muka lempeng tidak menetapkan jenis kerak. Karena itu, kemunculan daratan pada muka bernama North Ocean atau West Ocean tidak otomatis merupakan kontradiksi; labelnya masih identitas sementara.

## 5. Yang belum disimpulkan

- Orientasi globe terbaik atau final.
- Komposisi kerak benua/samudra pada tiap muka.
- Jenis batas lempeng, arah gerak, atau kecepatan gerak.
- Subduksi, pemekaran dasar samudra, sesar transform, atau busur vulkanik.
- Kelayakan geodinamika, relief, bathimetri, iklim, arus laut, dan hidrologi.
- Koordinat lokasi cerita.

## 6. Tahap berikutnya

1. Bandingkan beberapa registrasi global dengan metrik yang dinyatakan eksplisit, tanpa menganggap nama muka sebagai fakta geologi.
2. Pilih registrasi kerja berdasarkan komposisi daratan, kontinuitas geografis, dan kebutuhan cerita.
3. Ganti audit raster dengan clipping poligon sferis yang lebih presisi.
4. Setelah registrasi diterima, rancang tipe batas dan geodinamika.

**Dampak CANON: tidak ada.**