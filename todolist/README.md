# Proyek Django PBP - Tugas 4

**Nama   : Devina Hana Azhara**<br/>
**NPM    : 2106751032**<br/>
**Kelas  : E**<br/>


### [todolist HTML](https://tugas-2-devina.herokuapp.com/todolist/html/)
### [todolist XML](https://tugas-2-devina.herokuapp.com/todolist/xml/)
### [todolist JSON](https://tugas-2-devina.herokuapp.com/todolist/json/)


## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF Token merupakan suatu nilai/token unik dan rahasia yang digunakan untuk mencegah serangan dari CSRF (Cross-Site Request Forgery (CSRF)). Token ini perlu dibuat unik setiap sesi *user* dan perlu divalidasi saat terdapat *request* guna menghindari penyerangan atau peretasan data *user*.
Dalam form, implementasi token CSRF ini dikirimkan menggunakan metode POST. Nantinya, token ini akan disisipkan sebagai parameter saat terdapat *request* yang dilakukan oleh klien. Jika CSRF tidak diimplementasikan dalam form, data *user* akan lebih rentan terhadap serangan dan keamanannya berkurang.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


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
# Mengimport `User` dan menggunakan tipe `models.ForeignKey` untuk menunjang atribut user 
* Melakukan migrasi data tersebut ke dalam database Django lokal dengan perintah `python manage.py makemigrations` dilanjutkan dengan `python manage.py migrate`

#### Menghubungkan Models, Views, dan Templates ,

* Membuat fungsi `show_todolist(request)` pada views.py untuk melakukan pengambilan data dari model `todolist`
* Membentuk `urls.py` di dalam folder aplikasi **todolist** untuk melakukan *routing* terhadap fungsi `show_todolist(request)` pada `views.py` dengan memanggil method path()
* Membuat folder bernama `templates` dan membuat berkas `todolist.html`
* Membentuk tabel pada berkas `todolist.html` yang diisi dengan data-data Task dari model `todolist`

##### Menerapkan login dan logout bagi User

* Mengimport modul-modul yang dibutuhkan untuk membantu penerapan login serta logout, seperti `authenticate`, `login`, `logout`, `login_required`, `UserCreationForm`, `redirect`, `messages`, dan sebagainya
* Membuat fungsi register yang menerima parameter request



#### Melakukan Deployment ke Heroku

* Melakukan deployment dengan menghubungkan repositori github dengan heroku

#### Membentuk Unit Test

* Membentuk berkas `tests.py`
* Mengimport `TestCase`
* Membentuk class baru yang merupakan child class dari `TestCase`
* Membentuk fungsi untuk mengecek apakah URL html, xml, dan json yang telah dibuat mengembalikan respon HTTP 200 atau tidak
* Melakukan *testing* dengan perintah `python manage.py test`

## Postman

![Postman HTML](/todolist/assets/postman_html.jpg)
![Postman XML](/todolist/assets/postman_xml.jpg)
![Postman JSON](/todolist/assets/postman_json.jpg)