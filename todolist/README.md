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
* Mengatur batas maksimal kelebaran dari elemen (width) serta jenis tampilan ketika terjadi overflow agar halaman web menjadi responsif dan dapat ditampilkan dengan baik pada berbagai device <br>


# .

# Proyek Django PBP - Tugas 4

**Nama   : Devina Hana Azhara**<br/>
**NPM    : 2106751032**<br/>
**Kelas  : E**<br/>


#### [Link Heroku Todolist](https://tugas-2-devina.herokuapp.com/todolist/)

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF Token merupakan suatu nilai/token unik dan rahasia yang digunakan untuk mencegah serangan dari CSRF (Cross-Site Request Forgery (CSRF)). Token ini perlu dibuat unik setiap sesi *user* dan perlu divalidasi saat terdapat *request* guna menghindari penyerangan atau peretasan data *user*.
Dalam form, implementasi token CSRF ini dikirimkan menggunakan metode POST. Nantinya, token ini akan disisipkan sebagai parameter saat terdapat *request* yang dilakukan oleh klien. Jika CSRF tidak diimplementasikan dalam form, data *user* akan lebih rentan terhadap serangan dan keamanannya berkurang.

## Apakah kita dapat membuat elemen \<form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Tentunya kita dapat membuat elemen <form> secara manual. Generator seperti {{form.as_table}} yang kita gunakan di sini hanya berguna sebagai abstraksi untuk menampilkan form dalam bentuk tabel dengan tujuan memudahkan kita. Selain terdapat generator {{form.as_table}}, terdapat juga generator lain seperti {{ form.as_div }} (tag \<div>), {{ form.as_p }} (tag \<p>), dan {{ form.as_ul }} (tag \<li>) yang juga dapat kita gunakan. Meskipun demikian, jika semua generator tersebut belum dapat memenuhi kebutuhan kita, kita dapat membuat form secara manual dengan bantuan elemen-elemen input atau botton yang dilengkapi dengan berbagai atribut seperti *style*, *type*, dan sebagainya. 

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Saat *user* melakukan submisi melalui HTML form, HTTP *request* method POST yang telah dideklarasikan pada tag form akan dikirimkan kepada server. Server kemudian akan menerima *request* tersebut melalui `views.py`. `views.py` ini berisi fungsi-fungsi yang digunakan untuk menyimpan data yang telah diinput ke dalam database dan menghubungkannya dengan models. `views.py` kemudian juga akan mengembalikan data yang telah disimpan tersebut pada template yang disimpan dalam suatu berkas HTML yang ditampilkan kepada pengguna.

## Cara Implementasi 

#### Mengaktifkan *Virtual Environmnent*
* Membuat *virtual environment* dengan perintah `python -m venv env`
* Menyalakan *virtual environment* dengan perintah `env\Scripts\activate.bat`
* Melakukan instalasi *dependencies* yang dibutuhkan dengan perintah `pip install -r requirements.txt` 

#### Membuat Aplikasi Todolist
* Membuat aplikasi django bernama **todolist** dengan perintah `python manage.py startapp todolist`
* Mendaftarkan aplikasi **todolist** tersebut pada `settings.py` di folder `project_django`
* Mendaftarkan aplikasi **todolist** ke dalam urls.py pada folder `project_django`

#### Melakukan Konfigurasi Model
* Membuat skema model `todolist` yang memiliki atribut-atribut user, date, title, dan description pada `models.py`
* Mengimport `User` dan menggunakan tipe `models.ForeignKey` untuk menunjang atribut user 
* Melakukan migrasi data tersebut ke dalam database Django lokal dengan perintah `python manage.py makemigrations` dilanjutkan dengan `python manage.py migrate`

#### Menghubungkan Models, Views, dan Templates ,
* Membuat fungsi `show_todolist(request)` pada views.py untuk melakukan pengambilan data dari model `todolist`
* Membentuk `urls.py` di dalam folder aplikasi **todolist** untuk melakukan *routing* terhadap fungsi `show_todolist(request)` pada `views.py` dengan memanggil method path() di `urls.py`
* Membuat folder bernama `templates` dan membuat berkas `todolist.html`
* Membentuk tabel pada berkas `todolist.html` yang akan diisi dengan data-data Task dari model `todolist`

#### Menerapkan login dan logout bagi User
* Mengimport modul-modul yang dibutuhkan untuk membantu penerapan login serta logout, seperti `authenticate`, `login`, `logout`, `login_required`, `UserCreationForm`, `redirect`, `messages`, dan sebagainya
* Membuat fungsi `register` yang akan menghasilkan form registrasi secara otomatis dan membentuk suatu akun baru ketika dilakukan submisi form.
* Membentuk berkas `register.html` yang berfungsi untuk menampilkan form registrasi tersebut kepada *user*
* Membuat fungsi `login_user` yang akan menghasilkan form login secara otomatis dan mencocokkan data tersebut dengan informasi akun yang berada pada database.
* Membentuk berkas `login.html` yang berfungsi untuk menampilkan form login tersebut kepada *user*
* Membuat fungsi `logout_user` yang akan mengirimkan dan mengimplementasikan *request* logout yang dikirimkan oleh *user* kemudian melakukan *redirect* template ke halaman login dengan pesan "Berhasil logout"
* Setelah fungsi login dan logout telah diimplementasikan, halaman utama todolist akan direstriksi dengan menambahkan `@login_required(login_url='/todolist/login/')`
* Melakukan *routing* terhadap seluruh fungsi di atas pada dengan memanggil method path() di `urls.py`

#### Membuat fitur pembuatan task, pergantian status task, dan penghapusan task
* Membuat fungsi `create_task` yang akan membentuk form untuk diisi dengan task baru yang ingin ditambahkan. 
* Membentuk berkas `create_task.htmml` untuk menampilkan form kemudian menyimpan data dari form tersebut ke dalam database.
* Membuat fungsi `change_status` yang akan mengubah status task dengan id tertentu menjadi Done.
* Membuat fungsi `delete_task` yang akan menghapus suatu task dengan id tertentu pada database.
* Melakukan *routing* terhadap seluruh fungsi di atas pada dengan memanggil method path() di `urls.py`

#### Melakukan Deployment ke Heroku
* Melakukan deployment dengan menghubungkan repositori github dengan heroku

## Screenshot Aplikasi
![devina](/todolist/assets/akun_devina.png)
![pong](/todolist/assets/akun_pong.png)
