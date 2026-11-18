# Plate–Continent Relationship Framework V0.1

**Status:** CATATAN PENGEMBANGAN / NON-CANON  
**Tanggal:** 2026-11-18  
**Keputusan kerja:** geometri lempeng dan geometri benua diperlakukan sebagai dua sistem spasial yang saling beririsan, bukan pasangan satu-benua-satu-lempeng.

## 1. Ringkasan keputusan

Model satu-benua-satu-lempeng pembawa yang digunakan dalam rancangan terdahulu dihentikan sebagai syarat desain. Enam benua tidak diwajibkan berada sepenuhnya di dalam enam muka lempeng yang namanya berpadanan.

**Prinsip aktif:**
1. Benua adalah satuan geografis/garis pantai; lempeng adalah satuan tektonik.
2. Batas benua tidak harus berimpit dengan batas lempeng.
3. Satu benua boleh melintasi dua atau lebih lempeng.
4. Satu lempeng boleh mencakup kerak benua dan kerak samudra.
5. Satu lempeng juga boleh didominasi kerak samudra atau memiliki fragmen kerak benua/pulau.
6. Nama Central, Verdant, Sands, Frost, Ashen, Veiled, North Ocean, West Ocean, dan Southeast Ocean dipertahankan sementara sebagai label muka/region pada model geometri. Nama tersebut bukan bukti jenis kerak, bukan nama CANON, dan bukan penetapan bahwa benua terkait harus berada seluruhnya di atas muka bernama sama.

Dengan prinsip ini, geometri lempeng V1.0-R tidak perlu dipaksa mengikuti garis pantai V0.6. Keduanya dapat dipertahankan sebagai baseline matematis terpisah sampai orientasi geografis bersama dipilih dan overlay sferis dihitung.

## 2. Status artefak

| Artefak | Hasil yang sudah didukung | Batas yang belum terjawab |
|---|---|---|
| Siluet benua V0.6 | Enam poligon; total luas sferis hasil render sekitar 30,00017% permukaan bola | Orientasi globe, posisi geografis final, dan relasi terhadap muka lempeng |
| Geometri lempeng V1.0-R | 14 simpul, 21 sisi, 9 muka; partisi bola 100%; deviasi target luas maksimum 0,002188 poin persentase; validator PASS | Orientasi geografis, tipe batas, gerak lempeng, dan geodinamika |
| Uji containment V0.1 | Menguji hipotesis lama bahwa setiap benua harus berada dalam satu lempeng bernama sama; 40.000 rotasi dan grid kasar tidak menemukan orientasi yang meloloskan semua enam pasangan | Bukan uji overlay benua–lempeng yang sudah direvisi; bukan bukti bahwa partisi V1.0-R tidak dapat dipakai |
| Hubungan benua–lempeng V0.1 | Aturan desain satu-ke-satu diganti dengan relasi irisan banyak-ke-banyak | Belum ada angka luas irisan karena orientasi geografis belum ditetapkan |

## 3. Interpretasi ulang hasil containment terdahulu

Uji [Plate Containment Orientation Search V0.1](Plate-Containment-Orientation-Search-V0.1.md) benar untuk pertanyaan yang diajukan pada saat itu: apakah keenam benua dapat ditempatkan seluruhnya di dalam muka lempeng yang namanya berpadanan melalui satu rotasi globe bersama?

Jawabannya: tidak ditemukan orientasi demikian dalam pencarian eksploratif tersebut. Hasil itu tetap dicatat dan tidak dihapus.

Namun, pertanyaan satu-ke-satu tersebut bukan lagi syarat penerimaan model. Karena sebuah benua dapat melintasi batas lempeng dan sebuah lempeng dapat memuat kerak benua maupun samudra, kegagalan pasangan ketat tidak otomatis berarti geometri lempeng atau siluet benua harus dibuang.

**Kesimpulan yang sah:** rancangan satu-benua-satu-lempeng tidak didukung oleh pencarian orientasi yang telah dilakukan.  
**Kesimpulan yang tidak sah:** geometri V1.0-R mustahil dipakai, atau enam benua tidak dapat ditempatkan di permukaan planet.

## 4. Aturan overlay yang berlaku

Ketika orientasi globe dipilih, proses overlay harus:
- menggunakan satu rotasi globe yang sama untuk semua benua dan seluruh jaringan lempeng;
- memproyeksikan garis pantai dan batas lempeng dari geometri sferis, bukan menggeser masing-masing benua secara terpisah;
- menghitung irisan setiap poligon benua dengan seluruh muka lempeng;
- melaporkan luas daratan per lempeng dan proporsi setiap benua yang berada pada masing-masing lempeng;
- memeriksa apakah ada poligon yang terpotong oleh seam proyeksi atau melewati kutub secara keliru;
- memisahkan hasil ukur dari interpretasi geologi.

Tidak ada persentase irisan yang ditetapkan sebelumnya. Jangan memaksakan enam benua masing-masing memiliki satu lempeng dominan sebelum hasil overlay tersedia.

## 5. Hal yang belum boleh disimpulkan

- Nama muka lempeng tidak menetapkan komposisi kerak.
- Muka bernama North Ocean, West Ocean, atau Southeast Ocean belum terbukti sepenuhnya samudra.
- Muka bernama Central, Verdant, Sands, Frost, Ashen, atau Veiled belum terbukti seluruhnya memiliki kerak benua.
- Batas lempeng tidak otomatis berupa subduksi, punggung tengah samudra, sesar transform, atau batas pasif.
- Tidak ada arah atau kecepatan gerak lempeng yang telah dipilih.
- Belum ada pegunungan, palung, busur vulkanik, hotspot, atau umur kerak yang dapat diturunkan dari geometri ini.
- Belum ada koordinat geografis CANON atau lokasi cerita yang ditempatkan.

## 6. Urutan kerja atlas berikutnya

1. Tetapkan orientasi geografis kerja untuk satu globe.
2. Buat overlay sferis V0.6 dan V1.0-R dalam orientasi yang sama.
3. Hitung matriks irisan luas benua × muka lempeng; verifikasi jumlah luas dan toleransi numerik.
4. Tentukan tipe batas lempeng hanya setelah geometri dan kebutuhan geologi mendukungnya.
5. Turunkan relief besar, cekungan samudra, dan busur vulkanik dari model tektonik yang sudah dipilih.
6. Baru setelah itu audit iklim, arus laut, hidrologi, dan bioma terhadap geografi fisik.

## 7. Dampak terhadap dokumen lama

Bagian lama yang memasangkan setiap benua dengan satu lempeng pembawa tetap dipertahankan sebagai riwayat rancangan. Bagian tersebut tidak lagi menjadi aturan aktif. Target luas enam benua dan sembilan muka lempeng tidak diubah.

**Dampak CANON: tidak ada.** Semua artefak dan keputusan dalam dokumen ini tetap NON-CANON.
