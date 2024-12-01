# simple-paraphrase-t5-webapp

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge uses-html](http://ForTheBadge.com/images/badges/uses-html.svg)](http://ForTheBadge.com)

Model menggunakan [humarin/chatgpt_paraphraser_on_T5_base](https://huggingface.co/humarin/chatgpt_paraphraser_on_T5_base))

## Deskripsi Proyek

Paraphrase Text Generator adalah sebuah aplikasi berbasis web yang dirancang untuk memproses dan mengubah teks yang diberikan oleh pengguna menjadi versi yang berbeda tanpa mengubah makna aslinya. Aplikasi ini dibangun dengan menggunakan model T5 yang telah dilatih khusus untuk tugas parafrase, diintegrasikan dengan framework Flask untuk backend, dan dilengkapi dengan tampilan berbasis HTML dan CSS untuk antarmuka pengguna.

Aplikasi ini cocok digunakan untuk berbagai kebutuhan, seperti membantu penulisan ulang dokumen, menciptakan variasi konten untuk media sosial, atau meningkatkan kualitas teks dalam berbagai bahasa, termasuk bahasa Inggris dan bahasa Indonesia (masih dalam pengembangan).
<p align="center"><img src="https://github.com/DaffaAminuddin/simple-paraphrase-t5-webapp/blob/main/image2.PNG?raw=true" alt="image2"></p>

## Fitur

<p align="center"><img src="https://github.com/DaffaAminuddin/simple-paraphrase-t5-webapp/blob/main/image.PNG?raw=true" alt="image"></p>

1. Parafrase Kalimat dan Paragraf
Menggunakan model T5 (fine-tuned untuk parafrase) untuk menghasilkan teks yang lebih natural dan berbeda namun tetap mempertahankan arti aslinya.
Mendukung teks panjang dengan memecah paragraf menjadi kalimat-kalimat yang diproses secara individu sebelum digabungkan kembali.
2. Input dan Output Interaktif
Input: Pengguna dapat memasukkan teks dalam kotak teks di antarmuka.
Output: Hasil parafrase ditampilkan langsung dalam format yang bersih dan mudah dibaca.
3. Desain Modern dan Responsif
Tampilan dirancang menggunakan HTML dan CSS untuk memberikan pengalaman pengguna yang intuitif.
Responsif untuk berbagai perangkat, baik desktop maupun mobile.
4. Optimasi Kinerja
Memanfaatkan perangkat keras (GPU jika tersedia) untuk meningkatkan kecepatan pemrosesan.
Pengaturan hyperparameter seperti beam search dan diversity penalty untuk menghasilkan parafrase yang lebih bervariasi.
5. Validasi Input
Sistem memeriksa apakah teks input kosong sebelum diproses dan memberikan notifikasi jika tidak ada teks yang dimasukkan.
6. Kompatibilitas Multibahasa
Mendukung bahasa Inggris secara optimal, dengan kinerja yang baik untuk bahasa lain (tergantung pada model yang digunakan).
