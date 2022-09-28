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
