# The Dancing Demon — World Atlas Draft V1

**Status: CATATAN PENGEMBANGAN / NON-CANON.** Dokumen ini menggabungkan rancangan enam benua, komposisi makro, geometri lempeng, dan kerangka geografi fisik menjadi satu paket kerja. Tidak ada isi di bawah yang otomatis menjadi fakta CANON.

## 1. Keputusan dasar atlas

| Elemen | Baseline kerja |
|---|---|
| Planet | Planet terestrial dengan acuan ukuran dan parameter bergaya Bumi sebagai proposal kerja V0.6; belum CANON dan belum final |
| Benua utama | 6 |
| Wilayah lempeng | 9 |
| Triple junction | 14 |
| Segmen batas | 21 |
| Total daratan | 30% permukaan planet sebagai asumsi kerja sementara |
| Total samudra/perairan | 70% permukaan planet sebagai konsekuensi asumsi 30% daratan |
| Porsi luas relatif benua | Central 24%, Veiled 21%, Verdant 18%, Frostbound 15%, Sunken Sands 13%, Ashen 9% dari total daratan |
| Target luas lempeng | Central 18%, Verdant 12%, Sands 10%, Frost 8%, Ashen 7%, Veiled 11%, Samudra Utara 14%, Samudra Barat 11%, Samudra Timur-Selatan 9% dari seluruh permukaan planet |
| Susunan makro | Tiga benua kelompok utama dan tiga daratan terpencil |

**Catatan penyebut:** porsi benua dihitung dari total luas daratan. Porsi lempeng dihitung dari seluruh permukaan planet. Angka tersebut tidak boleh dibandingkan langsung.

## 2. Status geometri lempeng

### 2.1 Baseline yang dipilih

**V1.0-R adalah baseline geometri lempeng aktif untuk pengembangan.** V1.0-R merupakan rekonstruksi numerik baru yang mempertahankan topologi dan target luas yang dipublikasikan pada referensi V1.0, tetapi menggunakan koordinat planar dan bobot Tutte baru.

Hasil validasi V1.0-R:
- 14 simpul, 21 sisi, dan 9 muka; karakteristik Euler = 2;
- seluruh simpul berderajat 3 dan graf memiliki konektivitas 3;
- tidak ditemukan persilangan sisi non-insiden;
- delapan muka terbatas menutup poligon luar tanpa tumpang tindih planar;
- total luas permukaan 100%, dengan deviasi maksimum 0,002188 poin persentase;
- validator mandiri menghasilkan `RESULT: PASS`.

**V1.0-R bukan pemulihan identik V1.0.** Koordinat planar asli V1.0 dan input konstruksinya belum ditemukan. Karena itu:
- V1.0-reference tetap dipertahankan sebagai arsip hasil dan topologi historis;
- V1.0-R menjadi baseline numerik yang dapat direproduksi untuk tahap berikutnya;
- V1.1 Tutte dan prototipe V1.1 tetap arsip eksperimen;
- V1.0-R belum menguji containment enam benua, orientasi globe, geologi, atau geodinamika.

Rincian metode dan batas validasi tersedia dalam [Plate Geometry V1.0-R — Validation Report](World-Plate-Geometry-V1.0-R-Validation.md).

### 2.2 Pemetaan benua ke lempeng pembawa

| Benua | Lempeng pembawa | Porsi dari daratan | Target luas lempeng |
|---|---|---:|---:|
| The Central Reach | Central (CR) | 24% | 18% permukaan planet |
| The Verdant Wilds | Verdant (VW) | 18% | 12% permukaan planet |
| The Sunken Sands | Sands (SS) | 13% | 10% permukaan planet |
| The Frostbound Expanse | Frost (FR) | 15% | 8% permukaan planet |
| The Ashen Frontier | Ashen (AF) | 9% | 7% permukaan planet |
| The Veiled Continent | Veiled (VC) | 21% | 11% permukaan planet |

Satu benua utama ditempatkan pada masing-masing lempeng pembawa. Daratan tidak memenuhi seluruh lempeng; margin kerak samudra harus tersisa. Tiga lempeng samudra tidak membawa benua utama.

**Batas penting:** batas lempeng bukan garis pantai. Segmen batas dapat berada di dasar laut, jauh dari tepi daratan.

## 3. Susunan global konseptual

Susunan yang dipilih untuk sketsa makro:
- **Kelompok utama:** Central Reach sebagai jangkar; Verdant Wilds di sisi barat daya; Sunken Sands di sisi tenggara.
- **Frostbound Expanse:** kawasan lintang tinggi belahan utara, dipisahkan samudra luas dari kelompok utama.
- **Ashen Frontier:** belahan selatan pada lintang menengah, dipisahkan samudra dari kelompok utama.
- **Veiled Continent:** daratan paling terpencil dari jaringan kelompok utama, kandidat belahan selatan atau tenggara.

Skema hubungan (tidak berskala):

```text
                           UTARA

                  [FROSTBOUND EXPANSE]
                       samudra luas

 [VERDANT WILDS] -- laut regional -- [CENTRAL REACH]
          \                               /
           \--------- [SUNKEN SANDS] ----/

                       samudra luas

                    [ASHEN FRONTIER]

                samudra luas / akses jauh

                    [VEILED CONTINENT]

                           SELATAN
```

Diagram ini bukan proyeksi globe, bukan penetapan koordinat, dan tidak menunjukkan ukuran sebenarnya.

## 4. Rancangan enam benua

Semua siluet dan relief berikut merupakan arahan desain. Tidak ada fitur yang dianggap sudah ada sebelum pengesahan.

### 4.1 The Central Reach

**Peran makro:** daratan terbesar dan jangkar kelompok utama.

**Siluet:**
- melebar dan asimetris, bukan oval;
- tonjolan semenanjung besar ke arah timur;
- semenanjung panjang di barat laut;
- pantai utara memiliki beberapa teluk lebar;
- pantai selatan lebih terbuka dengan satu teluk besar;
- satu semenanjung mengarah ke benua kelompok utama lainnya.

**Relief awal:**
- rangkaian pegunungan panjang di barat atau barat laut;
- dataran tinggi lebih rendah di timur;
- cekungan atau dataran luas memisahkan dua sistem relief;
- dataran tengah terputus perbukitan dan lembah.

**Drainase:** sungai besar berasal dari dataran tinggi dan bercabang ke beberapa teluk/pesisir. Jangan membuat semua sungai mengalir ke satu sisi.

**Variasi lingkungan:** sediakan ruang untuk beberapa zona iklim; nama Central Reach tidak berarti seluruhnya subur.

### 4.2 The Verdant Wilds

**Peran makro:** anggota barat daya kelompok utama, dengan garis pantai kompleks.

**Siluet:**
- agak membulat tetapi asimetris;
- semenanjung panjang ke selatan;
- beberapa teluk dalam di timur;
- pantai barat terputus oleh tanjung dan teluk kecil;
- satu teluk besar menjorok dari timur.

**Relief awal:**
- busur pegunungan tidak sempurna dari barat laut ke bagian tengah;
- dataran tinggi dan perbukitan membagi daerah aliran sungai;
- dataran banjir, rawa, dan hutan lembap dapat ditempatkan di hilir jika iklim mendukung.

**Drainase:** beberapa sungai utama menuju teluk timur dan pesisir selatan; sungai pendek menuju pantai barat.

**Variasi lingkungan:** jangan jadikan seluruh benua hutan atau selalu basah.

### 4.3 The Sunken Sands

**Peran makro:** anggota tenggara kelompok utama; kawasan kering luas merupakan kemungkinan, bukan keseluruhan identitas.

**Siluet:**
- memanjang barat laut–tenggara;
- bagian tengah menyempit dan kedua ujung lebih lebar;
- teluk besar menjorok dari barat;
- sisi timur lebih terbuka;
- ujung tenggara memiliki semenanjung pendek dan pantai lebih kasar.

**Relief awal:**
- rangkaian pegunungan memanjang pada salah satu sisi;
- cekungan luas di tengah;
- dataran tinggi di sisi berlawanan yang dapat menciptakan bayangan hujan.

**Drainase:** sungai dari pegunungan dapat berakhir di laut, danau, atau cekungan pedalaman. Sistem endoreik hanya digunakan jika iklim dan elevasi mendukung.

**Variasi lingkungan:** gurun, dataran garam, stepa, dan kawasan kering lain dapat berdampingan; jangan menyamakan nama benua dengan satu bioma.

### 4.4 The Frostbound Expanse

**Peran makro:** daratan terpencil di lintang tinggi belahan utara.

**Siluet:**
- lebar dan tidak beraturan;
- satu tonjolan besar ke utara;
- dua semenanjung menjulur ke lintang lebih rendah;
- teluk panjang dan lekukan dalam di utara/timur;
- sisi selatan relatif lebih sederhana.

**Relief awal:**
- pegunungan atau dataran tinggi di tengah-utara;
- lembah mengarah ke pesisir;
- gletser, lembah glasial, dan fjord hanya jika sejarah glasiasi dan relief mendukung.

**Drainase:** sungai dari kawasan tinggi dapat mengalir ke selatan dan timur; danau glasial adalah kandidat bersyarat.

**Variasi lingkungan:** lintang tinggi mendukung lingkungan dingin, tetapi arus laut dan elevasi tetap memengaruhi iklim lokal. Tidak seluruh daratan harus tertutup es.

### 4.5 The Ashen Frontier

**Peran makro:** daratan terkecil, terpencil di belahan selatan pada lintang menengah.

**Siluet:**
- kompak, melengkung, dan asimetris;
- satu teluk besar di sisi dalam lengkungan;
- pesisir luar lebih tegas dan terbuka ke samudra;
- semenanjung sempit memanjang ke selatan.

**Relief awal:**
- zona pegunungan/dataran tinggi diagonal;
- kandidat busur vulkanik atau dataran vulkanik di salah satu sisi;
- lembah patahan atau cekungan memisahkan wilayah tinggi.

**Drainase:** sungai pendek dan deras mungkin muncul di sisi curam; sungai lebih panjang dapat mengalir dari cekungan ke teluk.

**Variasi lingkungan:** nama Ashen Frontier tidak berarti seluruh daratan aktif vulkanik, tandus, atau berbahaya.

### 4.6 The Veiled Continent

**Peran makro:** daratan terbesar kedua dan paling terpencil dari kelompok utama.

**Siluet:**
- memanjang diagonal;
- satu pesisir relatif halus dan sisi lain sangat berlekuk;
- teluk dalam atau laut pedalaman terhubung ke samudra melalui selat sempit;
- semenanjung panjang di timur;
- beberapa teluk kecil di barat;
- harus tetap terbaca sebagai satu benua, bukan gugus pulau.

**Relief awal:**
- pegunungan utama dekat salah satu pesisir panjang;
- dataran tinggi sekunder di sisi berlawanan;
- cekungan pedalaman dapat mengalir ke teluk tertutup atau danau besar.

**Drainase:** beberapa sungai menuju teluk dalam, lainnya menuju pesisir luar.

**Variasi lingkungan:** keterpencilan dijelaskan melalui jarak, arus, cuaca, dan navigasi jika kelak ditetapkan. Nama Veiled tidak menyiratkan kabut permanen atau ketiadaan penduduk.

## 5. Kerangka perairan global

Tiga wilayah lempeng samudra menjadi jangkar untuk pembagian perairan, tetapi nama lempeng tidak otomatis menjadi nama samudra.

| Wilayah lempeng | Fungsi konseptual |
|---|---|
| Samudra Utara (NO) | Wilayah kerak samudra yang menjadi bagian jaringan batas utara |
| Samudra Barat (WO) | Wilayah kerak samudra yang menjadi bagian jaringan batas barat |
| Samudra Timur-Selatan (SE) | Wilayah kerak samudra pada jaringan batas timur/selatan |

Kategori perairan yang dapat dipakai saat pemetaan rinci:
- open oceans;
- deep seas;
- storm belts;
- frozen waters;
- anomalous waters.

Kategori tersebut adalah klasifikasi desain, bukan nama atau lokasi perairan yang sudah disahkan. Jangan menetapkan arus, badai permanen, palung, atau jalur pelayaran sebelum orientasi dan geometri tersedia.

## 6. Kerangka relief, hidrologi, dan iklim

Urutan konstruksi fisik yang wajib dipakai:

1. Kunci bentuk makro daratan dan margin samudra.
2. Tetapkan orientasi globe, ekuator, kutub, dan asumsi kemiringan sumbu.
3. Tetapkan kerangka tektonik dan rangkaian pegunungan.
4. Bangun dataran tinggi, cekungan, lembah, dan cekungan drainase.
5. Tarik sungai dari daerah tinggi ke laut, danau, atau cekungan tertutup.
6. Tempatkan danau, rawa, delta, dan dataran banjir.
7. Tentukan arus laut dan pola angin global.
8. Turunkan zona iklim dan bioma dari lintang, elevasi, arus, dan curah hujan.
9. Tambahkan fitur lokal, pulau, selat, dan nama geografis setelah bentuk makro stabil.

### Aturan konsistensi

- Sungai mengikuti elevasi dan daerah aliran sungai.
- Sungai tidak menyeberangi punggung pegunungan tanpa celah, sumber, atau mekanisme yang jelas.
- Gurun tidak ditentukan hanya oleh nama benua; gunakan sirkulasi atmosfer, bayangan hujan, arus laut, dan jarak dari sumber kelembapan.
- Fjord memerlukan sejarah glasiasi dan relief yang sesuai.
- Vulkanisme memerlukan alasan tektonik atau hotspot yang konsisten.
- Iklim tidak ditentukan dari lintang saja; elevasi dan arus laut dapat mengubah kondisi lokal.
- Tidak ada bioma tunggal yang menutupi seluruh benua secara otomatis.

## 7. Geografi mana dan lokasi khusus

Kategori yang dapat dipakai untuk pemetaan kemudian:
- Mana-Rich;
- Mana-Depleted;
- Mana-Instability;
- Anomalous Region;
- Dead Zones.

Belum ditetapkan bahwa kategori tersebut benar-benar ada pada lokasi tertentu. Lokasi 13 Prasasti, fasilitas Bumi kuno, kota, negara, dan jalur ekspedisi tidak ditempatkan dalam draft ini.

Awal cerita menyebut ekspedisi pemetaan jalur utara oleh Tavian Rell. Frasa tersebut belum cukup untuk menyimpulkan bahwa ekspedisi berada di Frostbound Expanse.

## 8. Checklist kelulusan atlas

### Geometri
- [ ] Koordinat presisi V1.0 ditemukan atau V1.0-R direkonstruksi dan diberi label benar.
- [ ] 14 simpul, 21 segmen, dan 9 muka diverifikasi.
- [ ] Tidak ada persilangan segmen non-insiden.
- [ ] Luas sembilan wilayah menutup 100%.
- [ ] Deviasi luas terhadap target dicatat.
- [ ] Keenam benua terbukti berada di dalam lempeng pembawanya.

### Komposisi
- [ ] Tiga benua utama dan tiga daratan terpencil terbaca jelas.
- [ ] Porsi luas relatif keenam benua dipertahankan atau revisinya dijelaskan.
- [ ] Margin samudra dan pemisahan benua masuk akal.
- [ ] Tidak ada garis pantai yang disamakan dengan batas lempeng.

### Geografi fisik
- [ ] Orientasi globe dan garis lintang ditentukan.
- [ ] Relief konsisten dengan model tektonik.
- [ ] Sungai dan danau lolos pemeriksaan drainase.
- [ ] Iklim dan bioma konsisten dengan lintang, elevasi, arus, dan hujan.
- [ ] Pulau, selat, teluk, dan perairan besar terhubung secara spasial.

### Kontinuitas cerita
- [ ] Lokasi CANON tidak dipindah tanpa otorisasi.
- [ ] Lokasi 13 Prasasti belum dikunci tanpa keputusan.
- [ ] Lokasi ekspedisi Tavian tidak disimpulkan hanya dari kata “utara”.
- [ ] Semua penambahan geografis tetap NON-CANON sampai disahkan kreator.

## 9. Keputusan kerja dan keluaran

**Keputusan aktif:**
- V1.0-R menjadi baseline geometri lempeng yang dapat direproduksi.
- V1.0-reference dipertahankan sebagai arsip historis; koordinat planar asli V1.0 belum ditemukan.
- V1.1 dan prototipe terkait dipertahankan sebagai arsip eksperimen, bukan baseline aktif.
- Enam benua terpisah dan komposisi satu kelompok utama plus beberapa daratan terpencil merupakan draft pengembangan terpilih, bukan CANON.

Paket atlas ini menjadi acuan kerja untuk:
1. menguji containment enam siluet benua pada enam lempeng pembawa;
2. menyelesaikan margin samudra dan garis pantai;
3. menentukan orientasi globe dan kerangka koordinat geografis;
4. menyelesaikan relief, hidrologi, iklim, dan bioma;
5. menguji konsistensi geografi dengan rute serta kebutuhan cerita;
6. menyiapkan peta final setelah ketergantungan teknis selesai.

**Status:** atlas tetap CATATAN PENGEMBANGAN / NON-CANON. V1.0-R lolos validasi topologi dan target luas, tetapi belum lolos uji containment benua atau validasi geologi/geodinamika. Dokumen ini bukan peta geografis final.


## Lampiran teknis: referensi geometri V1.0

Data simpul, sisi, siklus muka, dan tabel luas V1.0 yang berhasil dipulihkan dari dokumentasi historis tersedia di `World-Plate-Geometry-V1.0-reference.json`. Ini adalah transkripsi terstruktur dari data yang dipublikasikan, bukan file koordinat planar asli. Koordinat simpulnya dibulatkan dua desimal; karena itu file tersebut tidak dapat dipakai untuk mengklaim reproduksi independen atas presisi luas V1.0.

Audit pemulihan dicatat di bagian 7.38 `World-Map-Framework.md`. Sampai koordinat planar asli ditemukan atau rekonstruksi numerik baru selesai divalidasi, atlas ini tetap berupa draft konseptual NON-CANON dan belum menjadi peta globe produksi.


## Pratinjau koordinat triple junction

Pratinjau locator visual untuk 14 simpul V1.0 tersedia di [World-Plate-V1.0-coordinate-locator.svg](World-Plate-V1.0-coordinate-locator.svg). Garis pada pratinjau adalah panduan geodesik terpendek untuk membantu membaca hubungan antarsimpul; garis tersebut bukan batas asli V1.0. Gunakan hanya sebagai locator NON-CANON, bukan peta lempeng final.


## 10. Studi siluet enam benua

Pratinjau visual pertama tersedia di [World-Atlas-Continental-Silhouette-Draft.svg](World-Atlas-Continental-Silhouette-Draft.svg). Sketsa menerjemahkan susunan makro dan arahan siluet enam benua menjadi satu bidang lintang-bujur konseptual agar hubungan spasialnya dapat dibaca.

Sketsa ini adalah interpretasi desain baru, bukan koordinat geografis yang dipulihkan. Bentuk garis pantai, posisi, ukuran tampak, dan jarak antarbenua belum diukur terhadap target luas; proyeksi equirectangular juga mendistorsi luas dan bentuk terutama di lintang tinggi. Karena itu, gambar hanya dipakai untuk menilai komposisi kasar dan arah siluet. Jangan gunakan untuk klaim persentase luas, containment lempeng, jarak navigasi, atau geografi CANON.

Catatan desain pada iterasi berikutnya:
- Central Reach menjadi jangkar kelompok utama dengan bentuk melebar dan asimetris.
- Verdant Wilds berada di barat daya dan memakai garis pantai lebih terfragmentasi.
- Sunken Sands berada di tenggara kelompok utama dan memanjang diagonal.
- Frostbound Expanse menempati lintang tinggi utara.
- Ashen Frontier menjadi daratan kompak di belahan selatan.
- Veiled Continent menjadi daratan terpencil di bagian tenggara.

**Status:** siluet konseptual V0.1, NON-CANON, belum lolos audit luas dan containment.


## Studi siluet makro enam benua — V1

Pratinjau visual pertama susunan daratan tersedia pada [World-Atlas-Continental-Silhouette-Draft.svg](World-Atlas-Continental-Silhouette-Draft.svg).

### Susunan yang divisualisasikan
- Kelompok utama: Verdant Wilds di barat daya, Central Reach sebagai jangkar tengah, dan Sunken Sands di tenggara.
- Daratan terpencil: Frostbound Expanse di lintang tinggi utara, Ashen Frontier di belahan selatan lintang menengah, dan Veiled Continent sebagai daratan paling terpencil.
- Siluet tiap benua menerjemahkan arahan bentuk pada Bagian 4 menjadi bentuk visual awal, termasuk semenanjung, teluk, dan asimetri garis pantai.

### Batas validasi
Gambar adalah studi komposisi dan siluet, bukan proyeksi kartografis atau geometri terukur. Posisi, jarak, ukuran visual, luas poligon, orientasi lintang, containment pada lempeng, dan hubungan garis pantai dengan batas lempeng belum divalidasi. SVG tidak boleh digunakan untuk mengambil koordinat atau menghitung luas. Target porsi luas relatif benua tetap tercatat pada Bagian 1; gambar ini belum membuktikan target tersebut.

**Keputusan desain sementara:** pertahankan susunan tiga benua kelompok utama dan tiga daratan terpencil sebagai komposisi makro V1. Jangan menambah negara, kota, atau lokasi canon pada siluet ini.

## 11. Revisi siluet dan audit luas — V0.2

V0.2 adalah revisi terpisah dari sketsa V0.1. Sumber V0.1 dan auditnya dipertahankan tanpa perubahan.

Berkas:
- [World-Atlas-Continental-Silhouette-V0.2.svg](World-Atlas-Continental-Silhouette-V0.2.svg)
- [World-Atlas-Continental-Polygon-Audit-V0.2.json](World-Atlas-Continental-Polygon-Audit-V0.2.json)

### Hasil pengukuran bidang SVG

| Benua | Target porsi daratan | Hasil V0.2 | Selisih |
|---|---:|---:|---:|
| Frostbound Expanse | 15% | 15.00% | 0.00 pp |
| Verdant Wilds | 18% | 18.00% | 0.00 pp |
| The Central Reach | 24% | 24.00% | 0.00 pp |
| The Sunken Sands | 13% | 13.00% | 0.00 pp |
| The Ashen Frontier | 9% | 9.00% | 0.00 pp |
| The Veiled Continent | 21% | 21.00% | 0.00 pp |

### Pemeriksaan geometri bidang

- Enam poligon benua terdeteksi.
- Seluruh titik poligon berada di dalam bingkai peta SVG.
- Tidak ditemukan pasangan poligon yang saling berpotongan atau bertumpang tindih pada pemeriksaan segmen dan point-in-polygon.
- Bentuk Sunken Sands mengalami transformasi area-preserving dan reposisi ke bagian selatan untuk menghindari tabrakan dengan Central Reach, Ashen Frontier, dan Veiled Continent.

### Batas klaim

Hasil 15/18/24/13/9/21 persen adalah proporsi luas pada bidang gambar SVG berdasarkan rumus Shoelace. Angka ini bukan luas permukaan geodesik planet dan tidak membuktikan proporsi daratan sebenarnya pada globe. Proyeksi, orientasi kutub, koordinat geografis, jarak, serta containment terhadap lempeng belum divalidasi. Label dan keterbacaan visual tetap memerlukan inspeksi desain.

**Status:** V0.2 lulus audit luas bidang, bingkai, dan non-overlap. Tetap NON-CANON dan bukan peta geografis final.

## 12. Presentation refinement — V0.3

V0.3 merupakan revisi presentasi dari geometri V0.2. Koordinat keenam poligon tidak diubah, sehingga hasil audit proporsi bidang V0.2 tetap berlaku.

Berkas:
- [World-Atlas-Continental-Silhouette-V0.3.svg](World-Atlas-Continental-Silhouette-V0.3.svg)
- [World-Atlas-Continental-Polygon-Audit-V0.3.json](World-Atlas-Continental-Polygon-Audit-V0.3.json)

### Perubahan
- Garis putus-putus dan label ekuator dihapus. Orientasi globe dan posisi lintang belum ditetapkan, sehingga penandaan ekuator sebelumnya terlalu dini.
- Kontras, ukuran, dan jarak visual label benua dirapikan.
- Grid ditegaskan sebagai grid ilustratif, bukan koordinat geografis.
- Judul, versi, dan catatan status diperjelas.

### Validasi
- Enam poligon tetap berada di dalam bingkai.
- Tidak ditemukan tumpang tindih antarbenua.
- Koordinat poligon identik dengan V0.2.
- Porsi luas bidang SVG tetap 15% / 18% / 24% / 13% / 9% / 21%.

**Status:** V0.3 lulus pemeriksaan presentasi dasar dan geometri bidang. Ini bukan redesign garis pantai, bukan proyeksi globe, bukan validasi luas geodesik, dan bukan uji containment lempeng. Seluruhnya tetap NON-CANON.



## 13. Coastline refinement — V0.4

V0.4 merupakan redesign geometri garis pantai berdasarkan arahan bentuk pada Bagian 4. Versi V0.1, V0.2, dan V0.3 tidak ditimpa.

Berkas:
- [World-Atlas-Continental-Silhouette-V0.4.svg](World-Atlas-Continental-Silhouette-V0.4.svg)
- [World-Atlas-Continental-Polygon-Audit-V0.4.json](World-Atlas-Continental-Polygon-Audit-V0.4.json)

### Perubahan siluet
- **Frostbound Expanse:** tonjolan utara lebih tegas, dua tonjolan semenanjung ke selatan, dan lekukan pesisir lebih dalam.
- **Verdant Wilds:** semenanjung selatan diperjelas; pesisir barat lebih terfragmentasi dan sisi timur memiliki teluk yang lebih kuat.
- **The Central Reach:** semenanjung timur dan barat laut diperjelas, dengan beberapa teluk pada sisi utara dan lekukan besar di sisi selatan.
- **The Sunken Sands:** siluet diputar menjadi diagonal barat laut–tenggara, dengan bagian pesisir berlekuk dan ujung yang lebih tegas.
- **The Ashen Frontier:** bentuk kompak melengkung dipertahankan, dengan teluk sisi dalam dan tonjolan sempit ke selatan.
- **The Veiled Continent:** pesisir lebih asimetris, dengan teluk dalam yang masuk dari sisi selatan dan semenanjung timur. Lekukan tersebut masih berupa teluk konseptual; belum ditetapkan sebagai laut pedalaman yang tersambung selat.

### Audit geometri bidang
- Enam poligon tertutup dan valid.
- Semua poligon berada di dalam bingkai peta.
- Tidak ditemukan tumpang tindih antarbenua.
- Porsi luas bidang SVG hasil pengukuran: Frostbound 15.000013%, Verdant 18.000064%, Central 23.999861%, Sunken Sands 13.000027%, Ashen 8.999998%, dan Veiled 21.000037%.
- Deviasi maksimum dari target: 0.000684 poin persentase.

Pengukuran menggunakan rumus Shoelace pada koordinat bidang SVG setelah penyederhanaan titik dan normalisasi luas. Persentase tersebut hanya menunjukkan proporsi luas pada bidang gambar, bukan luas permukaan geodesik planet.

### Batas validasi
V0.4 belum menetapkan proyeksi, orientasi globe, koordinat geografis, jarak nyata, bentuk relief, sistem drainase, atau containment terhadap lempeng. Grid tetap ilustratif. Garis pantai tidak boleh ditafsirkan sebagai batas lempeng.

**Status:** V0.4 lulus audit geometri bidang, bingkai, dan non-overlap. Tetap NON-CANON dan merupakan studi desain garis pantai, bukan peta geografis final.


## Kerangka koordinat geografis — V0.5

**Status: CATATAN PENGEMBANGAN / NON-CANON.** V0.5 menambahkan kerangka orientasi dan koordinat sementara pada studi siluet. Versi ini bukan peta geografis final dan tidak mengesahkan koordinat dunia sebagai CANON.

Berkas:
- [World-Atlas-Continental-Silhouette-V0.5.svg](World-Atlas-Continental-Silhouette-V0.5.svg)
- [World-Atlas-Geographic-Framework-Audit-V0.5.json](World-Atlas-Geographic-Framework-Audit-V0.5.json)

### 13.1 Referensi orientasi

- Utara berada di atas; timur di kanan.
- Rentang koordinat kerja pada bingkai: lintang +90° sampai −90° dan bujur −180° sampai +180°.
- Garis ekuator ditempatkan pada garis tengah vertikal bingkai (0° lintang).
- Meridian utama 0° ditempatkan pada garis tengah horizontal bingkai.
- Tepi kiri dan kanan diperlakukan sebagai sambungan bujur ±180°.
- Grid diberi interval 30°.

Pemetaan koordinat dilakukan secara linear dari posisi SVG ke label lintang/bujur. Ini hanya *coordinate scaffold*. Belum ada proyeksi kartografis yang dipilih atau divalidasi; rasio bingkai tidak boleh dianggap sebagai bukti skala atau bentuk geografis yang akurat.

### 13.2 Koreksi posisi makro

Penerapan kerangka lintang memperlihatkan bahwa posisi V0.4 menempatkan bagian selatan Sunken Sands terlalu dekat dengan kutub selatan. Ashen Frontier juga terlalu jauh ke selatan untuk kandidat lintang menengah. Karena itu, dua poligon digeser tanpa mengubah bentuk atau luasnya:

| Benua | Translasi SVG | Kisaran lintang perkiraan | Kisaran bujur perkiraan |
|---|---:|---:|---:|
| Frostbound Expanse | Tidak digeser | +40.61° sampai +82.36° | −37.16° sampai +38.10° |
| Verdant Wilds | Tidak digeser | −42.42° sampai +25.52° | −123.50° sampai −60.32° |
| Central Reach | Tidak digeser | −12.80° sampai +33.65° | −33.37° sampai +75.35° |
| Sunken Sands | 90 unit ke utara | −66.15° sampai −16.33° | +23.74° sampai +86.07° |
| Ashen Frontier | 50 unit ke utara | −64.69° sampai −24.34° | −40.05° sampai +9.55° |
| Veiled Continent | Tidak digeser | −61.73° sampai −6.51° | +93.59° sampai +179.85° |

Rentang di atas merupakan konversi *bounding box* SVG ke kerangka sementara, bukan koordinat garis pantai yang presisi. Kisaran tersebut tidak boleh dipakai untuk navigasi atau perhitungan jarak.

### 13.3 Pemeriksaan

- Enam poligon tetap valid dan seluruh titiknya berada di dalam bingkai.
- Dua perubahan posisi berupa translasi kaku; bentuk dan luas bidang poligon tidak berubah.
- *Bounding box* seluruh benua tetap saling terpisah setelah translasi.
- Audit proporsi bidang V0.4 tetap berlaku: Frostbound 15.000013%, Verdant 18.000064%, Central 23.999861%, Sunken Sands 13.000027%, Ashen 8.999998%, dan Veiled 21.000037%.
- Deviasi maksimum yang diwarisi dari audit V0.4 adalah 0.000684 poin persentase.

### 13.4 Hal yang belum disahkan atau belum diselesaikan

Bagian ini membedakan parameter yang sudah memiliki proposal kerja dari keputusan yang belum dibuat. Nilai V0.6 pada Bagian 14 merupakan model referensi bergaya Bumi untuk menjaga konsistensi perhitungan; nilai tersebut **belum disahkan sebagai CANON** dan masih dapat diubah.

- Ukuran planet, panjang keliling, dan skala jarak: tersedia acuan kerja bergaya Bumi pada V0.6, belum final.
- Kemiringan sumbu, periode rotasi, orbit, panjang tahun, dan musim: tersedia proposal V0.6, belum final.
- Lingkar tropis dan lingkar kutub: hanya konsekuensi matematis jika proposal kemiringan sumbu 23,44° dipakai.
- Proyeksi peta final dan koreksi distorsi: belum ditentukan.
- Luas geodesik, jarak antarbenua, arus laut, angin, iklim, bioma, dan containment lempeng: belum diselesaikan.

Tidak ada garis batas lempeng yang ditambahkan pada tahap V0.5. Garis pantai tidak sama dengan batas lempeng. Seluruh penempatan dan koreksi pada V0.5 tetap NON-CANON.

## 14. Parameter planet dan kerangka lintang iklim — V0.6

**Status: CATATAN PENGEMBANGAN / NON-CANON.** V0.6 menetapkan satu baseline fisik bergaya Bumi agar tahap geografi fisik dapat dihitung secara konsisten. Nilai-nilai ini merupakan proposal kerja, bukan fakta CANON.

Berkas:
- [World-Atlas-Climate-Latitude-Framework-V0.6.svg](World-Atlas-Climate-Latitude-Framework-V0.6.svg)
- [World-Atlas-Planetary-Parameters-Audit-V0.6.json](World-Atlas-Planetary-Parameters-Audit-V0.6.json)

### 14.1 Baseline parameter planet

| Parameter | Nilai kerja | Status |
|---|---:|---|
| Radius rata-rata | 6.371 km | Proposal referensi Bumi |
| Massa | 5,972 × 10²⁴ kg | Proposal referensi Bumi |
| Gravitasi permukaan rata-rata | 9,81 m/s² | Konsisten dengan massa dan radius referensi |
| Keliling rata-rata | ±40.030 km | Turunan radius, dibulatkan |
| Luas permukaan | ±510,1 juta km² | Turunan radius, dibulatkan |
| Rotasi hari matahari | 24 jam | Proposal |
| Rotasi sideris | ±23 jam 56 menit | Referensi Bumi |
| Kemiringan sumbu | 23,44° | Proposal |
| Periode orbit tropis | 365,2422 hari | Proposal |
| Eksentrisitas orbit | 0,0167 | Referensi Bumi |
| Jarak orbit rata-rata | 1 AU | Referensi orbit bintang bermassa Matahari |
| Luminositas bintang | 1 luminositas Matahari | Acuan bintang setara Matahari |
| Irradiasi rata-rata di puncak atmosfer | ±1.361 W/m² | Referensi Bumi |

Parameter ini membentuk model planet terestrial yang mendekati Bumi dalam ukuran, gravitasi, rotasi, kemiringan sumbu, dan penerimaan energi bintang. Itu pilihan teknis sementara agar iklim dan geografi dapat dibangun tanpa mengarang skala baru pada setiap tahap.

### 14.2 Konsekuensi kemiringan sumbu

Dengan kemiringan sumbu 23,44°:
- Tropic of Cancer berada pada 23,44° LU.
- Tropic of Capricorn berada pada 23,44° LS.
- Arctic Circle berada pada 66,56° LU.
- Antarctic Circle berada pada 66,56° LS.

Garis tersebut merupakan batas astronomis lintang, bukan batas otomatis gurun, hutan, tundra, atau iklim tertentu. Dua belahan mengalami fase musim yang berlawanan. Intensitas musim tetap dipengaruhi eksentrisitas orbit, atmosfer, distribusi daratan-lautan, dan sirkulasi samudra.

### 14.3 Kerangka sirkulasi atmosfer awal

Sebagai model konseptual, sirkulasi global dapat dimulai dari tiga sel per belahan:
- **Hadley:** kira-kira 0°–30°.
- **Ferrel:** kira-kira 30°–60°.
- **Polar:** kira-kira 60°–90°.

Batas sel tidak tetap pada garis lintang yang presisi. Posisi dan kekuatannya bergeser menurut musim dan dipengaruhi distribusi daratan, pegunungan, serta suhu permukaan laut. Karena itu, rentang ini hanya kerangka awal, bukan peta angin final.

### 14.4 Asumsi daratan dan perairan

Asumsi kerja sebelumnya tetap 30% daratan dan 70% perairan. Dengan luas permukaan referensi sekitar 510,1 juta km², konsekuensinya:
- Daratan: sekitar 153,0 juta km².
- Perairan: sekitar 357,1 juta km².

Angka ini hanya hasil aritmetika dari asumsi 30/70. Belum ada pengukuran geodesik atas enam benua dan belum ada keputusan CANON mengenai luas planet atau persentase lautan.

### 14.5 Hal yang belum ditetapkan

- Komposisi, tekanan, massa, dan kelembapan atmosfer.
- Konsentrasi gas rumah kaca dan perilaku awan.
- Bulan, pasang surut, dan konfigurasi sistem planet.
- Arus laut, pola angin, curah hujan, dan distribusi panas.
- Suhu rata-rata global dan rentang suhu regional.
- Batas bioma, gurun, hutan, tundra, gletser, dan tutupan es.
- Proyeksi kartografis final dan validasi geodesik.

**Peringatan:** lingkar tropis dan lingkar kutub pada SVG hanya diturunkan dari kemiringan sumbu usulan. Jangan menganggapnya sebagai batas iklim atau bioma. Peta V0.6 belum merupakan peta iklim.

**Status keputusan:** baseline Bumi dipilih sebagai proposal kerja NON-CANON untuk melanjutkan pemodelan. Tidak ada perubahan pada siluet benua, geometri lempeng, lokasi cerita, atau CANON.


## 15. Kerangka sirkulasi global — V0.7

**Status: CATATAN PENGEMBANGAN / NON-CANON.** V0.7 menerjemahkan baseline planet V0.6 menjadi model konseptual sirkulasi atmosfer Bumi-referensi. Ini merupakan kerangka arah dan sabuk global, bukan simulasi iklim atau peta cuaca.

Berkas:
- [World-Atlas-Global-Circulation-Framework-V0.7.svg](World-Atlas-Global-Circulation-Framework-V0.7.svg)
- [World-Atlas-Global-Circulation-Audit-V0.7.json](World-Atlas-Global-Circulation-Audit-V0.7.json)

### 15.1 Tiga sel sirkulasi per belahan

Kerangka awal mempertahankan tiga sel atmosfer pada masing-masing belahan:
- **Hadley (sekitar 0°–30°):** udara cenderung naik di sekitar ITCZ dan turun di wilayah subtropis.
- **Ferrel (sekitar 30°–60°):** sirkulasi lintang menengah yang terutama digerakkan oleh sistem cuaca dan gelombang atmosfer.
- **Polar (sekitar 60°–90°):** sirkulasi lintang tinggi yang berinteraksi dengan udara dingin kutub dan front polar.

Batas sel tidak tetap dan bukan garis iklim yang kaku. Posisi serta intensitasnya berubah menurut musim dan kondisi permukaan.

### 15.2 Sabuk tekanan konseptual

| Sabuk | Lintang perkiraan | Peran umum |
|---|---|---|
| Tekanan rendah ekuatorial / ITCZ | Sekitar ekuator; bermigrasi ke belahan yang sedang mengalami musim panas | Konvergensi angin pasat dan gerak naik udara |
| Tekanan tinggi subtropis | Sekitar 25°–35° LU dan LS | Subsiden udara; wilayah kering dapat terbentuk, tetapi tidak otomatis |
| Tekanan rendah subpolar | Sekitar 50°–65° LU dan LS | Zona pertemuan massa udara dan aktivitas siklon lintang menengah |
| Tekanan tinggi kutub | Lintang kutub tinggi | Udara dingin cenderung turun; posisi persis tidak dikunci |

ITCZ bukan garis permanen di 0°. Pergerakannya mengikuti pergeseran musiman pemanasan maksimum dan dipengaruhi distribusi daratan-lautan.

### 15.3 Angin permukaan dominan

| Sabuk angin | Lintang perkiraan | Arah umum |
|---|---|---|
| Angin pasat timur laut | 0°–30° LU | Timur ke barat, dengan komponen menuju ekuator |
| Angin pasat tenggara | 0°–30° LS | Timur ke barat, dengan komponen menuju ekuator |
| Westerlies utara | 30°–60° LU | Barat ke timur |
| Westerlies selatan | 30°–60° LS | Barat ke timur |
| Easterlies kutub utara | 60°–90° LU | Timur ke barat |
| Easterlies kutub selatan | 60°–90° LS | Timur ke barat |

Arah pada diagram adalah pola dominan rata-rata, bukan arah angin yang berlaku setiap hari. Benua, pegunungan, perbedaan suhu laut, dan sistem cuaca akan membelokkan atau mengganggu pola zonal tersebut.

### 15.4 Kerangka arus samudra

V0.7 belum menggambar jalur arus laut spesifik. Secara umum, planet dengan rotasi dan sirkulasi atmosfer mirip Bumi dapat memiliki:
- kandidat gyre subtropis pada cekungan samudra luas yang cukup terbuka dan saling terhubung;
- arus permukaan ekuatorial yang cenderung bergerak ke barat, dengan kemungkinan arus balik ekuatorial ke timur pada cekungan tertentu;
- arus batas barat yang cenderung sempit dan mengalir ke arah kutub;
- arus batas timur yang cenderung lebih lebar dan mengalir ke arah ekuator.

Pola ini merupakan ekspektasi umum dari model Bumi, bukan bukti bahwa setiap cekungan di peta ini memiliki gyre lengkap. Jumlah gyre, pusat pusaran, jalur arus hangat/dingin, upwelling, kecepatan, dan sirkulasi laut dalam belum ditentukan. Penetapannya menunggu geometri cekungan samudra dan batimetri yang lebih kuat.

### 15.5 Batas interpretasi iklim

V0.7 tidak menetapkan suhu regional, angka curah hujan, lokasi gurun, hutan, padang rumput, monsun, bayangan hujan, maupun tutupan es. Tekanan tinggi subtropis dapat mendukung kondisi kering, tetapi gurun tidak boleh ditempatkan hanya berdasarkan lintang. Relief, jarak dari sumber kelembapan, arus laut, dan pola hujan harus diperiksa terlebih dahulu.

### 15.6 Batas validasi

- Diagram memakai kerangka koordinat linear SVG dari V0.6; belum ada proyeksi kartografis final.
- Panah angin adalah simbol pola lintang global dan tidak mengikuti topografi atau garis pantai.
- Tidak ada simulasi numerik atmosfer atau samudra.
- Geometri cekungan samudra dan batimetri belum divalidasi.
- Tidak ada perubahan pada poligon benua, geometri lempeng, atau lokasi cerita.
- Seluruh isi tetap NON-CANON.

**Status keputusan:** V0.7 menyediakan baseline konseptual untuk melanjutkan pemodelan. Tahap berikutnya yang logis adalah membangun relief makro dan batimetri konseptual sebelum menurunkan arus laut rinci, pola hujan, dan bioma.


## 16. Kerangka relief makro dan batimetri — V0.8

**Status: CATATAN PENGEMBANGAN / NON-CANON.** V0.8 menerjemahkan arahan relief yang telah tercatat pada Bagian 4 menjadi kerangka visual awal. Penanda relief adalah kandidat desain, bukan pengukuran elevasi atau keputusan CANON. Bagian batimetri hanya menetapkan kosakata bentuk dasar laut dan belum menempatkan fitur bawah laut pada koordinat tertentu.

Berkas:
- [World-Atlas-Relief-Bathymetry-Framework-V0.8.svg](World-Atlas-Relief-Bathymetry-Framework-V0.8.svg)
- [World-Atlas-Relief-Bathymetry-Audit-V0.8.json](World-Atlas-Relief-Bathymetry-Audit-V0.8.json)

### 16.1 Prinsip konstruksi

- Relief mengikuti arahan desain yang sudah tercatat pada Bagian 4; V0.8 tidak membuat pegunungan baru berdasarkan tebakan batas lempeng.
- Ketinggian hanya dibedakan secara relatif: pegunungan/dataran tinggi, perbukitan, dataran rendah, dan cekungan. Tidak ada angka meter yang diberikan.
- Garis pantai tetap berasal dari siluet draft terdahulu; tidak diubah.
- Batas lempeng tidak diperlakukan sebagai garis pantai.
- Tidak ada sungai final yang digambar sebelum punggung bukit, elevasi, dan daerah aliran sungai diselesaikan.
- Tidak ada palung, punggung tengah samudra, atau busur vulkanik yang ditempatkan hanya dari simpul triple junction.

### 16.2 Kandidat relief per benua

| Benua | Kandidat relief dari catatan desain | Status spasial |
|---|---|---|
| The Central Reach | Pegunungan panjang di barat/barat laut; dataran tinggi lebih rendah di timur; cekungan atau dataran luas pemisah; perbukitan dan lembah di dataran tengah | Zona barat laut dan dataran tinggi timur ditampilkan sebagai skema; cekungan tengah masih kandidat |
| The Verdant Wilds | Busur pegunungan tidak sempurna dari barat laut ke tengah; dataran tinggi dan perbukitan pembagi DAS | Busur ditampilkan secara skematis; elevasi dan ujung busur belum dikunci |
| The Sunken Sands | Pegunungan memanjang pada salah satu sisi; cekungan luas di tengah; dataran tinggi di sisi berlawanan | Cekungan ditandai sebagai kandidat; sisi pegunungan dan dataran tinggi sengaja belum dipilih |
| The Frostbound Expanse | Pegunungan atau dataran tinggi tengah-utara; lembah menuju pesisir | Dataran tinggi tengah-utara ditampilkan sebagai kandidat; fitur glasial belum digambar |
| The Ashen Frontier | Zona pegunungan/dataran tinggi diagonal; kandidat busur vulkanik atau dataran vulkanik di salah satu sisi; lembah patahan atau cekungan | Zona tinggi diagonal ditampilkan; vulkanisme dan patahan belum ditetapkan |
| The Veiled Continent | Pegunungan dekat salah satu pesisir panjang; dataran tinggi sekunder di sisi berlawanan; cekungan pedalaman | Cekungan ditandai; sisi pegunungan dan dataran tinggi sengaja belum dipilih |

### 16.3 Batimetri: kelas bentuk dasar laut

Penampang pada SVG hanya menjelaskan bentuk umum margin benua dan dasar laut, bukan profil kedalaman aktual. Kerangka istilah yang dipakai:
- **Landas kontinen (continental shelf):** tepian dangkal yang berlanjut dari benua.
- **Lereng kontinen (continental slope):** transisi curam menuju laut dalam.
- **Kaki lereng (continental rise):** zona akumulasi sedimen yang dapat berkembang di kaki lereng.
- **Dataran abisal (abyssal plain):** dasar laut dalam yang relatif datar.
- **Punggung samudra, palung, gunung laut, dan dataran tinggi samudra:** fitur yang mungkin ada, tetapi belum dipetakan.

Tidak ada kedalaman numerik atau lokasi cekungan yang ditetapkan pada tahap ini. Tiga wilayah lempeng samudra (NO, WO, SE) tetap merupakan label muka lempeng dalam referensi geometri; label itu tidak otomatis menjadi nama samudra atau deskripsi kedalaman.

### 16.4 Hubungan dengan tektonik

Referensi V1.0 yang dipulihkan memuat 14 triple junction, 21 segmen, dan 9 muka lempeng, tetapi koordinat planar asli tidak tersedia. Koordinat lintang-bujur simpul dibulatkan dan tidak cukup untuk mereproduksi batas secara presisi. Dokumen referensi juga menyatakan belum ada kinematika gerak lempeng.

Karena itu, V0.8 tidak menyimpulkan:
- batas konvergen, divergen, atau transform;
- arah dan laju gerak setiap lempeng;
- lokasi zona subduksi, rift, atau sesar transform;
- posisi palung, punggung tengah samudra, busur vulkanik, atau hotspot.

Vulkanisme Ashen Frontier tetap berupa kemungkinan desain, bukan hasil turunan yang sudah dibuktikan dari geometri lempeng.

### 16.5 Hidrologi yang ditunda

Sungai, danau, delta, rawa, dan cekungan endoreik belum ditempatkan. Tahap berikutnya harus menetapkan:
1. punggung topografi dan elevasi relatif;
2. batas daerah aliran sungai;
3. arah aliran dari daerah tinggi menuju laut/danau/cekungan;
4. titik muara dan danau;
5. pemeriksaan bahwa sungai tidak melintasi punggung topografi tanpa celah atau mekanisme yang masuk akal.

Fjord, lembah glasial, dan danau glasial hanya dapat ditambahkan jika sejarah glasiasi dan reliefnya mendukung.

### 16.6 Audit dan batas klaim

- Enam poligon benua diwarisi tanpa perubahan dari V0.6.
- Tidak ada geometri lempeng atau koordinat triple junction yang diubah.
- Tidak ada elevasi absolut, kedalaman laut, atau gradien lereng yang diklaim.
- Tidak ada sistem sungai atau danau yang disahkan.
- Diagram memakai kerangka koordinat linear sementara, bukan proyeksi kartografis tervalidasi.
- Seluruh fitur tetap NON-CANON.

**Status keputusan:** V0.8 menyediakan inventaris relief makro dan kosakata batimetri. Sebelum arus laut rinci dan bioma, pekerjaan berikutnya adalah menyelesaikan model elevasi relatif dan drainase utama tanpa mengunci lokasi cerita.


## 17. Kerangka daerah aliran sungai dan hidrologi — V0.9

**Status: CATATAN PENGEMBANGAN / NON-CANON.** V0.9 menerjemahkan kandidat relief V0.8 menjadi kerangka hidrologi awal. Garis pembagi DAS, zona cekungan, dan panah arah drainase hanya bersifat skematis. V0.9 bukan model elevasi digital (DEM), peta sungai, atau simulasi hidrologi.

Berkas:
- [World-Atlas-Watershed-Hydrology-Framework-V0.9.svg](World-Atlas-Watershed-Hydrology-Framework-V0.9.svg)
- [World-Atlas-Watershed-Hydrology-Audit-V0.9.json](World-Atlas-Watershed-Hydrology-Audit-V0.9.json)

### 17.1 Prinsip konstruksi
- Garis pembagi DAS kandidat hanya mengikuti simbol pegunungan/dataran tinggi yang sudah ada pada V0.8.
- Garis tersebut bukan punggung topografi terukur dan belum menjadi batas DAS tervalidasi.
- Panah menunjukkan kecenderungan arah turun secara umum dari relief tinggi; bukan jalur sungai, anak sungai, atau lokasi muara.
- Zona cekungan menandai kandidat tampungan/topografi rendah. Status tertutup (endorheik) atau terbuka ke laut (eksorheik) belum diputuskan.
- Tidak ada garis pantai, poligon benua, atau geometri lempeng yang diubah.

### 17.2 Kandidat pembagi DAS
| Benua | Dasar kandidat | Batas pengetahuan |
|---|---|---|
| The Central Reach | Sabuk pegunungan barat laut | Jejak punggung, batas DAS, dan hubungan dengan cekungan tengah belum tervalidasi |
| The Verdant Wilds | Busur pegunungan barat laut–tengah | Ujung busur dan pembagian daerah tangkapan belum dikunci |
| The Frostbound Expanse | Dataran tinggi tengah-utara | Lembah, outlet pesisir, dan pengaruh glasial belum dipetakan |
| The Ashen Frontier | Dataran tinggi diagonal | Hubungan dengan patahan/vulkanisme dan batas DAS belum diketahui |

### 17.3 Zona cekungan kandidat
- **The Central Reach:** cekungan tengah tetap kandidat. Belum diketahui apakah cekungan tertutup, memiliki outlet permukaan, atau hanya dataran rendah luas.
- **The Sunken Sands:** cekungan tengah tetap kandidat. Tidak ada dasar yang cukup untuk menyatakan sistem danau garam atau drainase endoreik.
- **The Veiled Continent:** cekungan pedalaman tetap kandidat. Hubungannya dengan laut, teluk tertutup, atau danau belum ditentukan.

### 17.4 Hal yang belum digambar atau disahkan
- Tidak ada sungai utama, anak sungai, danau, delta, rawa, atau muara yang ditempatkan.
- Tidak ada nama perairan yang dibuat.
- Tidak ada sistem glasial, fjord, atau danau glasial yang disimpulkan.
- Tidak ada bioma, curah hujan, atau iklim regional yang diturunkan dari kerangka ini.
- Tidak ada lokasi cerita yang dipindahkan atau ditambahkan.

### 17.5 Validasi dan keterbatasan
- Enam poligon benua diwarisi tanpa perubahan; garis pantai dan geometri lempeng tetap.
- Tidak ada data elevasi numerik, DEM, gradien lereng, atau simulasi hidrologi.
- Topologi DAS, jalur aliran menurun, dan outlet cekungan belum diverifikasi.
- Kerangka koordinat linear SVG tetap bukan proyeksi kartografis tervalidasi.
- Seluruh fitur V0.9 tetap NON-CANON.

**Status keputusan:** V0.9 menyediakan kerangka untuk menyusun hidrologi tanpa mengarang sungai. Tahap selanjutnya memerlukan urutan elevasi relatif dan punggung topografi yang lebih pasti, penentuan outlet cekungan, serta pemeriksaan bahwa aliran tidak menembus pembagi DAS. Sungai baru layak digambar setelah pemeriksaan tersebut.


## 18. Kelas elevasi relatif dan topologi drainase — V1.0

**Status: CATATAN PENGEMBANGAN / NON-CANON.** V1.0 mengelompokkan kandidat relief yang sudah tercatat menjadi kelas elevasi relatif kualitatif. Versi ini tidak memberikan angka ketinggian, tidak membandingkan elevasi antarbenua, dan belum menetapkan topologi drainase final.

Berkas:
- [World-Atlas-Relative-Elevation-Drainage-Topology-Framework-V1.0.svg](World-Atlas-Relative-Elevation-Drainage-Topology-Framework-V1.0.svg)
- [World-Atlas-Relative-Elevation-Drainage-Topology-Audit-V1.0.json](World-Atlas-Relative-Elevation-Drainage-Topology-Audit-V1.0.json)

### 18.1 Kelas elevasi kualitatif

| Kode | Kelas | Penggunaan |
|---|---|---|
| R1 | Kandidat relief tinggi | Pegunungan dan dataran tinggi yang sudah tercatat |
| R2 | Kandidat relief menengah | Plateau lebih rendah, perbukitan, atau upland |
| R3 | Kandidat relief rendah | Cekungan atau dataran rendah luas |
| RX | Belum terklasifikasi | Sisi, kesinambungan, atau hubungan relief belum diketahui |

Kode tersebut bukan rentang meter, bukan hasil pengukuran, dan tidak boleh dipakai untuk menyimpulkan bahwa R1 di satu benua lebih tinggi daripada R1 di benua lain. Klasifikasi hanya membantu mengorganisasi deskripsi relief yang sudah tersedia.

### 18.2 Penilaian per benua

| Benua | Kandidat yang dapat diklasifikasikan | Bagian yang tetap belum diketahui |
|---|---|---|
| The Central Reach | R1: sabuk pegunungan barat laut; R2: plateau timur yang lebih rendah; R3: cekungan tengah | Jejak punggung persis, lantai cekungan, dan outlet |
| The Verdant Wilds | R1: busur pegunungan barat laut–tengah; R2: dataran tinggi dan perbukitan | Ujung busur, kesinambungan, dan urutan elevasi lokal |
| The Sunken Sands | R3: cekungan tengah | Sisi pegunungan memanjang dan dataran tinggi lawan belum dipilih |
| The Frostbound Expanse | R1: dataran tinggi tengah-utara | Ketinggian, gradien lembah, dan jalur keluar ke pesisir |
| The Ashen Frontier | R1: zona pegunungan/dataran tinggi diagonal; R2: kandidat upland diagonal | Hubungan antarzona, keberadaan lembah patahan, dan urutan elevasi |
| The Veiled Continent | R3: cekungan pedalaman | Pesisir yang membawa pegunungan utama dan posisi plateau sekunder |

Kelas yang belum didukung catatan relief tidak dipaksakan. Area tersebut tetap RX atau tidak diklasifikasikan.

### 18.3 Topologi drainase dan status cekungan

Tiga cekungan kandidat masih belum memiliki status outlet:
- **Central Reach:** belum diketahui apakah cekungan tengah merupakan depresi tertutup, dataran rendah dengan outlet permukaan, atau dataran luas yang tidak membentuk cekungan tertutup.
- **Sunken Sands:** belum diputuskan apakah air mengalir keluar ke laut atau tertahan dalam sistem endoreik.
- **Veiled Continent:** belum diketahui apakah cekungan pedalaman terhubung ke laut, teluk tertutup, danau, atau tidak memiliki outlet permukaan.

Istilah *exorheic* dan *endorheic* hanya menjadi kategori yang akan dipakai setelah elevasi ambang dan jalur keluar ditentukan. V1.0 belum menetapkan satu pun cekungan sebagai exorheic atau endorheic.

### 18.4 Aturan sebelum menggambar sungai

1. Tetapkan kesinambungan punggung topografi dan titik pelana (saddle/pass).
2. Tentukan urutan elevasi relatif antara punggung, lembah, cekungan, dan ambang outlet.
3. Pastikan batas DAS mengikuti punggung dan tidak terpotong jalur aliran yang tidak masuk akal.
4. Bentuk graf elevasi dan hubungan outlet yang saling konsisten.
5. Baru setelah itu gambar sungai utama, anak sungai, danau, serta muara.

### 18.5 Audit dan batas klaim

- Tidak ada angka elevasi, DEM, kontur hasil perhitungan, atau gradien lereng.
- Tidak ada urutan elevasi lintas benua yang divalidasi.
- Tidak ada outlet cekungan, batas DAS, atau graf drainase yang disahkan.
- Tidak ada sungai, danau, delta, rawa, atau nama perairan yang ditambahkan.
- Geometri benua, garis pantai, lempeng, dan lokasi cerita tidak diubah.
- Kerangka koordinat SVG tetap bukan proyeksi kartografis tervalidasi.
- Seluruh isi V1.0 tetap NON-CANON.

**Status keputusan:** V1.0 menyediakan kosakata dan klasifikasi awal untuk relief yang telah dideskripsikan. Langkah berikutnya bukan langsung menggambar sungai, melainkan menyelesaikan sisi relief yang belum dipilih, hubungan punggung–pelana–cekungan, serta ambang outlet setiap cekungan.


---

## Referensi geometri lempeng — versi terpisah

Penomoran versi pada dokumen atlas dan geometri lempeng berjalan terpisah:
- **World Atlas Draft V1 / V1.0** di dokumen ini mengacu pada tahap klasifikasi relief relatif dan kerangka drainase.
- **Plate Geometry V1.0-R** mengacu pada rekonstruksi matematis partisi sembilan wilayah lempeng.

Geometri lempeng kerja yang dapat direproduksi kini tersedia:
- [Plate Geometry V1.0-R — JSON](World-Plate-Geometry-V1.0-R-reconstructed.json)
- [Plate Geometry V1.0-R — Validation Report](World-Plate-Geometry-V1.0-R-Validation.md)
- [Plate Geometry V1.0-R — Planar SVG](World-Plate-Geometry-V1.0-R-planar.svg)
- [Plate Geometry V1.0-R — Python Validator](validate_plate_geometry_v1_0_r.py)

V1.0-R belum menguji containment enam benua dan bukan peta geografis final. Jangan mencampur statusnya dengan klasifikasi relief/drainase V1.0 dalam dokumen ini.

## 19. Audit luas sferis siluet V0.5

Audit bidang sebelumnya mengukur porsi poligon menggunakan shoelace pada koordinat SVG. Itu hanya mengukur proporsi gambar. Karena V0.5 memakai koordinat lintang-bujur yang dipetakan secara linear, luas bidang yang sama pada lintang berbeda tidak mewakili luas permukaan bola yang sama.

Audit baru [World Atlas — Spherical Continental Area Audit V0.1](World-Atlas-Spherical-Continental-Area-Audit-V0.1.md) mengukur enam poligon V0.5 pada bola menggunakan transformasi koordinat dari bingkai SVG dan integral luas sferis. Hasilnya:

| Benua | Target bidang lama | Porsi sferis terukur dari enam benua |
|---|---:|---:|
| Frostbound Expanse | 15% | 9,19% |
| Verdant Wilds | 18% | 21,57% |
| Central Reach | 24% | 28,76% |
| Sunken Sands | 13% | 11,75% |
| Ashen Frontier | 9% | 8,21% |
| Veiled Continent | 21% | 20,51% |

Enam poligon yang sekarang tergambar menutup sekitar **26,44% permukaan bola**, bukan asumsi kerja 30%. Angka km² dalam laporan memakai radius Bumi hanya sebagai ilustrasi; fraksi permukaan tidak bergantung pada radius.

**Koreksi status angka:** target 15/18/24/13/9/21 tetap sah sebagai target proporsi bidang desain historis, tetapi tidak boleh disebut sebagai porsi luas daratan sferis yang sudah terukur. Asumsi 30% daratan juga belum diwujudkan oleh siluet V0.5.

Berkas audit terstruktur: [World-Atlas-Spherical-Continental-Area-Audit-V0.1.json](World-Atlas-Spherical-Continental-Area-Audit-V0.1.json).

**Keputusan kerja:** jangan lanjut mengunci relief rinci, sungai, atau bioma. Tahap berikutnya adalah memilih target luas relatif benua, menyelesaikan selisih terhadap asumsi 30%, menentukan rotasi globe, dan menguji containment tiap benua pada lempeng pembawanya. Semua tetap NON-CANON.

## 20. Siluet benua dengan luas sferis dinormalisasi — V0.6

V0.6 adalah kandidat geometri baru yang menindaklanjuti audit V0.5. Target proporsi historis dipertahankan sebagai target luas relatif daratan: Frostbound 15%, Verdant 18%, Central 24%, Sunken Sands 13%, Ashen 9%, dan Veiled 21%. Dengan asumsi daratan global 30%, target masing-masing menjadi 4,5%, 5,4%, 7,2%, 3,9%, 2,7%, dan 6,3% dari seluruh permukaan planet.

Berkas:
- [Siluet enam benua V0.6 — SVG](World-Atlas-Continental-Silhouette-V0.6.svg)
- [Audit normalisasi luas V0.6 — JSON](World-Atlas-Continental-Area-Normalization-Audit-V0.6.json)

### Metode dan hasil

- Bentuk V0.5 diproyeksikan ke koordinat silinder luas-sama: (x=\lambda), (y=\sin\varphi).
- Tiap benua diskalakan terhadap centroid luas-sama untuk mencapai target luas sferis.
- Frostbound diperlebar terutama pada sumbu bujur, bukan diperbesar ke arah kutub, agar tetap berada di dalam rentang lintang.
- Seluruh globe diberi rotasi bujur −10° untuk menempatkan Veiled Continent di dalam bingkai tanpa memotong garis tanggal.
- Setiap sisi hasil transformasi didensifikasi menjadi 12 segmen sebelum diproyeksikan kembali ke bingkai SVG lintang-bujur.
- Audit sferis pada koordinat hasil render menghasilkan total **30,00017%** permukaan planet; deviasi gabungan sekitar 0,00017 poin persentase.

| Benua | Target permukaan planet | Hasil terukur |
|---|---:|---:|
| Frostbound Expanse | 4,50% | 4,50002% |
| Verdant Wilds | 5,40% | 5,40003% |
| Central Reach | 7,20% | 7,20001% |
| Sunken Sands | 3,90% | 3,90005% |
| Ashen Frontier | 2,70% | 2,70002% |
| Veiled Continent | 6,30% | 6,30004% |

### Batas validasi

V0.6 memperbaiki target luas dan bingkai koordinat, tetapi belum menyelesaikan:
- containment setiap benua pada lempeng pembawanya;
- orientasi geografis yang dipilih terhadap geometri lempeng V1.0-R;
- geodinamika, batas lempeng aktif, relief, hidrologi, iklim, dan bioma;
- pulau-pulau kecil dan garis pantai rinci.

**Status:** V0.6 adalah kandidat geometri kerja NON-CANON. Ia menggantikan V0.5 sebagai kandidat luas sferis untuk pengujian berikutnya, bukan sebagai peta final.
