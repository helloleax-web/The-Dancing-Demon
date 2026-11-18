# Editorial and Repository Maintenance Policy

**Status:** KEBIJAKAN ADMINISTRATIF — bukan lore dan bukan CANON dunia cerita.  
**Berlaku mulai:** 2026-11-18

## 1. Mandat editorial

Kreator telah memberikan mandat editorial luas kepada pengelola proyek untuk merapikan, mengembangkan, mengoreksi, dan memperbarui repository secara langsung tanpa meminta persetujuan untuk setiap perubahan kecil.

Mandat ini mencakup:
- Perbaikan ejaan, tata bahasa, istilah, format, struktur, dan navigasi.
- Pemeriksaan serta perbaikan konsistensi lintas dokumen.
- Penyelarasan ringkasan dengan dokumen rujukan yang lebih otoritatif.
- Penyelesaian ambiguitas administratif atau prosedural yang dapat diturunkan secara aman dari keputusan yang sudah ada.
- Pengembangan materi cerita, karakter, lokasi, organisasi, sistem, dan geografi sebagai CATATAN PENGEMBANGAN.
- Perbaikan data teknis dan visual draft selama metode, batas validasi, serta versi dicatat dengan benar.
- Commit dan upload langsung ke branch utama jika perubahan telah diperiksa.

## 2. Batas editorial

Mandat luas bukan izin untuk menghapus identitas proyek atau merusak misteri yang menjadi fondasi cerita.

Prinsip berikut harus dipertahankan:
1. Premis utama tetap berpusat pada dunia fantasi yang dibangun di atas peninggalan peradaban Bumi kuno.
2. Kehancuran peradaban Bumi tidak otomatis berarti seluruh kehidupan musnah.
3. Entitas kosmik tetap merupakan Abstract Existence; jangan mengubahnya menjadi monster konvensional atau final boss tanpa alasan naratif yang kuat.
4. Great War, Resonansi Hitam, NVR AGAIN, jubah mana hitam, LEAX, dan 13 Prasasti harus tetap konsisten dengan fakta yang sudah dicatat.
5. Prolog asal-usul LEAX tetap dipisahkan dari cerita utama kecuali struktur proyek secara eksplisit menggabungkannya.
6. Sistem mana tidak boleh menjadi penjelasan otomatis bagi entitas kosmik, Great War, Resonansi Hitam, jubah hitam, atau kekuatan LEAX.
7. Identitas, motivasi, hubungan, dan sejarah yang sengaja menjadi MYSTERY tidak boleh dibocorkan hanya untuk mengisi profil atau sinopsis.

## 3. Status materi baru

Gunakan status berikut secara konsisten:
- **CANON:** keputusan cerita yang telah ditetapkan dan menjadi acuan lintas dokumen.
- **CATATAN PENGEMBANGAN:** rancangan kreatif yang dapat dikembangkan, diuji, diubah, atau dibuang.
- **UNKNOWN:** belum ditentukan; tidak otomatis berarti harus dijawab.
- **MYSTERY:** informasi yang sengaja ditahan untuk kebutuhan cerita.
- **OPEN QUESTION:** keputusan yang masih membutuhkan penyelesaian.

Materi baru boleh dikembangkan secara mandiri sebagai CATATAN PENGEMBANGAN. Jangan menyamarkan ide baru sebagai fakta lama. Jika suatu rancangan dipromosikan menjadi CANON, catat perubahan dan dokumen yang terdampak di Canon Changelog.

## 4. Standar kualitas

Setiap dokumen yang diperbarui harus:
- Memiliki tujuan dan status yang jelas.
- Menggunakan istilah yang konsisten dengan dokumen inti.
- Memisahkan fakta, inferensi, usulan, dan misteri.
- Menautkan sumber internal yang relevan.
- Tidak mengulang informasi secara berlebihan jika dapat merujuk ke satu sumber utama.
- Menjelaskan batas dan asumsi ketika memuat angka, peta, geometri, statistik, atau hasil teknis.
- Menghindari detail yang tidak memiliki fungsi naratif atau operasional.
- Memiliki tautan relatif yang valid jika merujuk file repository lain.

## 5. Hierarki sumber

Jika dua dokumen tampak berbeda:
1. Dokumen CANON khusus menjadi rujukan utama untuk domain yang dibahas.
2. Dokumen inti `00-CORE/` menjadi ringkasan dan navigasi; selaraskan dengan sumber CANON khusus.
3. Dokumen `98-CATATAN PENGEMBANGAN/` tidak mengubah CANON.
4. Dokumen administrasi `99-ADMIN/` mencatat status, keputusan, dan proses; tidak menciptakan lore dengan sendirinya.
5. Jika perbedaan tidak dapat diselesaikan dari sumber yang ada, tandai dan dokumentasikan, jangan memilih secara diam-diam.

## 6. Prosedur perubahan

- Perbaikan dokumentasi dan tautan dapat langsung dilakukan.
- Klarifikasi yang sudah memiliki dasar eksplisit dapat diterapkan ke semua ringkasan terkait.
- Pengembangan baru disimpan dalam folder pengembangan sampai statusnya ditetapkan.
- Retcon atau perubahan fondasi harus dijelaskan secara terbuka dalam Canon Changelog.
- Jangan menghapus arsip teknis atau versi peta lama hanya karena ada versi baru; tandai statusnya sebagai superseded, archive, atau reference.
- Setelah perubahan, verifikasi file yang diunggah, tautan, status, dan ringkasan yang terdampak.

## 7. Prioritas kerja berkelanjutan

Urutan umum pemeliharaan:
1. Integritas canon dan kontinuitas.
2. Kualitas premis, struktur cerita, dan karakter.
3. Kelengkapan lokasi, organisasi, sistem dunia, dan kebutuhan Buku I.
4. Kualitas atlas, geografi, dan aset teknis.
5. Konsistensi indeks, README, changelog, dan navigasi.
6. Pengembangan buku II–VIII sesuai kesiapan fondasi cerita.

Prioritas dapat berubah jika kebutuhan cerita menunjukkan ketergantungan yang lebih mendesak.

## 8. Prinsip akhir

Tujuan repository bukan sekadar memiliki banyak halaman. Tujuannya adalah menjadi world bible yang dapat dipercaya, mudah dibaca, konsisten, dan cukup kuat untuk mendukung penulisan cerita panjang.

**Kualitas kontinuitas lebih penting daripada banyaknya lore. Misteri yang bekerja lebih baik daripada jawaban yang dipaksakan.**
