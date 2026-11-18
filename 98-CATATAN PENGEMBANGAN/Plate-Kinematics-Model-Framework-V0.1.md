# Plate Kinematics Model Framework V0.1

**Status:** CATATAN PENGEMBANGAN / NON-CANON / SPESIFIKASI METODE  
**Tanggal:** 2026-11-19

## 1. Tujuan

Menentukan cara membangun model gerak lempeng yang konsisten dengan geometri V1.0-R, registrasi R0.2, 21 batas, dan 14 triple junction. Dokumen ini belum memilih arah atau kecepatan gerak. Tujuannya mencegah klasifikasi geologi dibuat berdasarkan nama muka atau kebutuhan plot.

## 2. Parameter gerak

Setiap lempeng diperlakukan sebagai benda tegar di permukaan bola dengan satu vektor kecepatan sudut:

[
\mathbf{v}_i(\mathbf{r})=\boldsymbol{\omega}_i\times\mathbf{r}
]

Untuk sembilan lempeng terdapat 27 komponen skalar mentah. Penambahan vektor rotasi sudut yang sama ke semua lempeng tidak mengubah gerak relatif, sehingga ada tiga derajat kebebasan gauge. Model gerak relatif memiliki **24 parameter independen** sebelum kendala tambahan.

Belum ada satuan waktu, radius planet, Euler pole, atau lempeng referensi yang dipilih. Menetapkan satu lempeng bernilai nol kelak hanya boleh menjadi pilihan kerangka koordinat, bukan klaim bahwa lempeng itu diam secara absolut.

## 3. Gerak relatif pada batas

Untuk dua muka (i) dan (j):

[
\mathbf{v}_{ij}(\mathbf{r})=(\boldsymbol{\omega}_j-\boldsymbol{\omega}_i)\times\mathbf{r}
]

Di setiap titik batas, gerak relatif diuraikan terhadap:
- **normal batas** (\mathbf{n}_{ij}), diarahkan dari muka (i) menuju muka (j);
- **tangen batas** (\mathbf{t}_{ij}), mengikuti arah lokal garis batas.

Komponennya:

[
v_n=\mathbf{v}_{ij}\cdot\mathbf{n}_{ij},\qquad
v_t=\mathbf{v}_{ij}\cdot\mathbf{t}_{ij}
]

Dengan konvensi normal tersebut, (v_n>0) berarti pemisahan dan (v_n<0) berarti konvergensi. Komponen tangensial mengukur gerak sejajar batas. Batas oblique dapat memiliki kedua komponen yang berarti.

Klasifikasi tidak boleh dilakukan hanya pada dua simpul ujung. Setiap batas harus disampel sepanjang kurvanya. Jika tanda (v_n) berubah sepanjang satu sisi, sisi tersebut harus diperiksa sebagai beberapa segmen kinematik atau diberi status campuran.

## 4. Syarat triple junction

Pada triple junction, tiga lempeng bertemu. Satu kecepatan titik pertemuan (\mathbf{u}_{TJ}) harus memenuhi kendala normal dari ketiga batas yang bertemu:

[
(\mathbf{u}_{TJ}-\mathbf{v}_i(\mathbf{r}))\cdot\mathbf{n}_{ij}=0
]

Kecepatan junction dibatasi pada bidang singgung bola. Tiga kendala normal harus menghasilkan satu solusi bersama dengan residual dalam toleransi numerik yang dinyatakan.

Selisih kecepatan relatif berpasangan memang memenuhi penutupan aljabar secara otomatis, tetapi itu **belum cukup** untuk membuktikan triple junction dapat bergerak secara konsisten. Uji kecepatan junction tetap wajib dilakukan.

## 5. Aturan klasifikasi sementara

| Kategori | Kondisi kinematik |
|---|---|
| Divergen | (v_n) positif secara konsisten |
| Konvergen | (v_n) negatif secara konsisten |
| Transform | (v_n) mendekati nol dan (v_t) berarti |
| Oblique/campuran | Komponen normal dan tangensial sama-sama berarti, atau tanda normal berubah |
| Belum terklasifikasi | Besaran gerak di bawah resolusi atau toleransi |

Ambang “mendekati nol” dan “berarti” belum ditentukan. Ambang harus ditetapkan berdasarkan skala dan presisi model, bukan dipilih setelah melihat hasil yang diinginkan.

## 6. Gerak tidak sama dengan jenis kerak

Kinematika saja tidak menentukan seluruh geologi:
- Konvergensi tidak otomatis menentukan lempeng mana yang menunjam.
- Subduksi membutuhkan alasan independen mengenai densitas, daya apung, umur, dan kondisi litosfer.
- Tumbukan benua, subduksi samudra, dan pemekaran samudra memerlukan konteks kerak yang berbeda.
- Pegunungan, busur vulkanik, dan cekungan harus diturunkan dari proses batas yang telah lolos uji, bukan ditempelkan langsung ke peta.
- Nama Central, Verdant, Sands, Frost, Ashen, Veiled, North Ocean, West Ocean, dan Southeast Ocean tidak menetapkan komposisi kerak.

## 7. Gerbang penerimaan model

1. Seluruh 21 batas memiliki dua muka tetangga dan konvensi normal yang konsisten.
2. Seluruh 14 triple junction lolos uji residual kecepatan junction.
3. Klasifikasi batas stabil saat sampling kurva diperhalus.
4. Peta jenis kerak dibuat dan diaudit terpisah.
5. Polaritas subduksi memiliki alasan densitas/umur kerak.
6. Tidak ada tipe batas yang ditetapkan hanya untuk membenarkan pegunungan atau lokasi cerita yang diinginkan.

## 8. Status

**Belum ditetapkan:** semua vektor kecepatan sudut, Euler pole, kecepatan, arah gerak, jenis kerak, polaritas subduksi, pusat pemekaran, sesar transform, dan sabuk pegunungan.

Dokumen ini hanya spesifikasi metode untuk tahap berikutnya. Tidak ada geodinamika yang diklaim telah tervalidasi.

**Dampak CANON: tidak ada.**
