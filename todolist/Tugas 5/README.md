# Proyek Django PBP - Tugas 5

**Nama   : Devina Hana Azhara**<br/>
**NPM    : 2106751032**<br/>
**Kelas  : E**<br/>


#### [Link Heroku Todolist](https://tugas-2-devina.herokuapp.com/todolist/)

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Sebenarnya ketiga jenis CSS tersebut memiliki fungsi yang sama, yakni untuk memperbaiki tampilan halaman dari suatu website. Yang membedakan ketiga jenis CSS ini adalah urutan prioritas serta kecepatan dalam memproses style yang diberikan. Inline CSS memiliki prioritas tertinggi, dilanjutkan dengan internal CSS, dan diakhiri dengan external CSS dengan prioritas terendah. Jika suatu elemen pada HTML terkena dua atau lebih style yang berbeda, jenis style dengan prioritas tertinggi yang akan dikenakan pada elemen tersebut.

### Inline CSS
Inline CSS akan menerapkan style melalui atribut *style* pada tag HTML. Jenis CSS ini sangat cocok untuk perubahan yang sederhana dan permanen. Akan tetapi, perubahan ini kurang fleksibel jika dibandingkan dengan internal ataupun external CSS.

### Internal CSS
Internal CSS ini umumnya berada pada elemen HTML dengan menggunakan tag style. Style yang berada dalam tag tersebut akan dikenakan hanya untuk halaman web tersebut. Hal ini menjadi kurang efektif sebab kita perlu menuliskan style untuk masing-masing halaman web secara terpisah. Jika terdapat jenis style yang sama, akan terjadi redundan dan menyebabkan halaman web menjadi lebih lambat untuk diproses

### External CSS
External CSS menggunakan file .css yang disambungkan dengan file .html dalam menerapkan style untuk suatu halaman web. Keuntungan dari External CSS ini adalah style yang digunakan dapat digunakan berulang kali untuk berbagai halaman web sehingga kita tidak perlu lagi menulis ulang untuk masing-masing halaman web. External CSS ini cocok digunakan untuk perubahan style yang kompleks.

##  Jelaskan tag HTML5 yang kamu ketahui.
Tag HTML merupakan sebuah penanda dari awalan dan akhiran dari suatu elemen di HTML. Tag ini ditulis dengan menggunakan kurung siku yang di dalamnya diisi dengan berbagai elemen HTML. Elemen-elemen ini memiliki karakteristiknya tersendiri yang dapat kita gunakan sesuai dengan kebutuhan.
Beberapa jenis tag HTML5 yang umum digunakan:
* \<a> : Hyperlink umumnya digunakan saat kita hendak menulis link pada halaman web.
* \<br> : Break ini mirip dengan new line dan umum digunakan untuk memberi jarak atau pindah ke baris baru dalam konteks tulisan.
* \<button> : Button digunakan jika kita ingin menampilkan button pada halaman web
* \<div> : Div ini digunakan untuk menyatukan berbagai elemen HTML dan umum digunakan untuk mendukung proses styling
* \<form> : Form digunakan ketika kita ingin meminta input dari user
* \<h1> to \<h6> : Heading digunakan untuk memberikan judul atau subjudul dari suatu tulisan. Umumnya, heading memiliki tulisan yang lebih tebal dan besar dari tulisan lainnya pada web.
*\<link> : Link digunakan untuk mendefinisikan hubungan antar file html dengan file external, seperti CSS dan JavaScript
* \<p> : Paragraph merupakan elemen yang umum digunakan ketika kita ingin menambahkan tulisan pada halaman web
* \<table> : Table digunakan untuk menampilkan tabel pada halaman web
* \<ul> : Unordered list digunakan jika kita ingin membuat suatu list tidak terurut pada halaman web
* \<ol> : Ordered list digunakan jika kita ingin membuat suatu list terurut pada halaman web. Nantinya, list button yang digunakan dapat berupa angka 1,2,3 atau abjad a,b,c, dst.
* \<title> : Title digunakan untuk menetapkan judul dari halaman web


## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
* **Tag Selector** <br>
Tag selector digunakan untuk mendefinisikan style untuk seluruh elemen dengan jenis tertentu pada halaman web. <br>
Contoh : <br>
p {} <br>

* **Class Selector** <br>
Class ini sangat umum digunakan untuk mendukung proses styling dari suatu halaman web. Nantinya, elemen-elemen yang memiliki style yang sama akan memiliki class yang sama pada bagian atributnya. Suatu elemen HTML dapat memiliki beberapa class sekaligus.<br>
Contoh: <br>
.className {....} <br>

* **ID Selector** <br>
ID ini memiliki fungsi yang mirip dengan class, akan tetapi ID ini bersifat unik. <br>
Contoh : <br>
#id1 {....} <br>

* **Attribute Selector** <br>
Atribut ini digunakan untuk elemen yang memiliki atribut-atribut di dalamnya, misalnya input yang memiliki atribut text. Pada kasus tersebut, kita dapat mendefinisikan style yang ingin digunakan secara spesifik. <br>
Contoh : <br>
input[type=text] {....} <br>

* **Universal Selector** <br>
Universal digunakan jika kita ingin mendefinisikan style untuk seluruh elemen dari suatu halaman web. Style yang berada di dalam blok ini akan berlaku untuk keseluruhan elemen, kecuali dia ditimpa dengan style lain yang memiliki prioritas yang lebih tinggi. <br>
Contoh : <br>
\* {....} <br>

* **Pseudo Selector** <br>
Selektor ini digunakan untuk mendefinisikan style pada elemen semu, seperti ketika elemen tersebut ditekan, dikenai kursor, dan sebagainya <br>
Contoh : <br>
a:hover {....} <br>

## Cara Implementasi 
* Menghubungkan file base.html dengan bootstrap untuk membantu proses styling 
* Menambahkan atribut style pada elemen (inline syling) dan tag style pada masing-masing file html (internal styling)
* Menggunakan class yang telah disediakan pada bootstrap seperti class btn, btn-dark, dan sebagainya untuk mendukung styling
* Membuat class yang diberlakukan untuk masing-masing task guna mendukung styling penampilan task
* Mengatur batas maksimal kelebaran dari elemen (width) serta jenis tampilan ketika terjadi overflow agar halaman web menjadi responsif dan dapat ditampilkan dengan baik pada berbagai device
