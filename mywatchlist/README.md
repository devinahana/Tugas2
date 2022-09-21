# Proyek Django PBP - Tugas 3

**Nama   : Devina Hana Azhara**<br/>
**NPM    : 2106751032**<br/>
**Kelas  : E**<br/>


### [MyWatchList HTML](https://tugas-2-devina.herokuapp.com/mywatchlist/html/)
### [MyWatchList XML](https://tugas-2-devina.herokuapp.com/mywatchlist/xml/)
### [MyWatchList JSON](https://tugas-2-devina.herokuapp.com/mywatchlist/json/)


## Perbedaan antara JSON, XML, dan HTML

Hypertext Markup Languange atau biasa dikenal dengan HTML merupakan bahasa standar yang digunakan untuk membuat halaman suatu situs web. HTML berisikan kumpulan *tag* yang di dalamnya berisikan *attribute* yang merupakan data-data yang ingin ditampilkan pada halaman web. Umumnya, HTML ini dipakai untuk menampilkan data dan bukan untuk menyimpan suatu data.
Berbeda dengan HTML, XML dan JSON merupakan dua format yang paling umum dalam melakukan penyimpanan serta pertukaran data (*data delivery*). XML (*Extensible Markup Language*) merupakan bahasa *markup* yang telah disesuaikan untuk menyimpan data. XML mempermudah pertukaran data dengan membentuk konfigurasi yang dinamis, pemuatan variabel, dan menyediakan struktur data yang jelas. Sementara itu, JSON (*JavaScript Object Notation*) merupakan sebuat format map (key - value) yang sering digunakan untuk menyimpan, membaca, ataupun menukar informasi dari server. JSON dikenal karena kemudahan, kejelasan, dan kecepatannnya dalam pemodelan data sebab ringan dan menggunakan sedikit memori. 


## Fungsi *Data Delivery*

*Data delivery* diperlukan dalam pengimplementasian sebuah platform untuk mempermudah proses pengiriman data dari satu *stack* ke *stack* lainnya. Data yang dikirimkan tersebut dapat bermacam-macam bentuknya, mulai dari HTML, XML, JSON, dan sebagainya. Maka dari itu, guna terciptanya efisiensi, proses *data delivery* ini menjadi penting untuk dilakukan.


## Cara Implementasi 

#### Mengaktifkan *Virtual Environmnent*

* Membuat *virtual environment* dengan perintah `python -m venv env`
* Menyalakan *virtual environment* dengan perintah `env\Scripts\activate.bat`
* Melakukan instalasi *dependencies* yang dibutuhkan dengan perintah `pip install -r requirements.txt` 


#### Membuat Aplikasi Mywatchlist

* Membuat aplikasi django bernama **mywatchlist** dengan perintah `python manage.py startapp mywatchlist`
* Mendaftarkan aplikasi **mywatchlist** tersebut pada `settings.py` di folder `project_django`
* Mendaftarkan aplikasi **mywatchlist** ke dalam urls.py pada folder `project_django`

#### Melakukan Konfigurasi Model

* Membuat skema model `MyWatchList` yang memiliki atribut-atribut watched, title, rating, release_date, dan review pada `models.py`
* Melakukan migrasi data tersebut ke dalam database Django lokal
* Membuat folder bernama `fixtures` dan membuat berkas bernama `initial_mywatchlist_data.json`
* Mengisi berkas `initial_mywatchlist_data.json` dengan data-data film sesuai atribut yang telah dibuat
* Memasukkan data tersebut ke dalam database Django lokal dengan perintah `python manage.py loaddata initial_mywatchlist_data.json`

#### Menghubungkan Models, Views, dan Templates 

* Membuat fungsi `show_mywatchlist(request)` pada views.py untuk melakukan pengambilan data dari model `MyWatchList`
* Membentuk `urls.py` di dalam folder aplikasi **mywatchlist** untuk melakukan *routing* terhadap fungsi `show_mywatchlist(request)` pada `views.py` dengan memanggil method path()
* Membuat folder bernama `templates` dan membuat berkas `mywatchlist.html`
* Membentuk tabel pada berkas `mywatchlist.html` yang diisi dengan data-data film dari model `MyWatchList`

#### Mengembalikan Data dalam Bentuk XML dan JSON

* Membuat fungsi `show_mywatchlist_xml(request)` pada `views.py` untuk melakukan pengembalian data dalam bentuk XML
* Membuat fungsi `show_mywatchlist_json(request)` pada `views.py` untuk melakukan pengembalian data dalam bentuk JSON  
* Melakukan *routing* terhadap fungsi `show_mywatchlist_xml(request)`, dan `show_mywatchlist_json(request)` pada `views.py` dengan memanggil method path()

#### Melakukan Deployment ke Heroku

* Menambahkan `&& python manage.py loaddata initial_mywatchlist_data.json` pada Procfile
* Melakukan deployment dengan menghubungkan repositori github dengan heroku

### Membentuk Unit Test

* Membentuk berkas `tests.py`
* Mengimport `TestCase`
* Membentuk class baru yang merupakan child class dari `TestCase`
* Membentuk fungsi untuk mengecek apakah URL html, xml, dan json yang telah dibuat mengembalikan respon HTTP 200 atau tidak
* Melakukan *testing* dengan perintah `python manage.py test`

## Postman

![Postman HTML](/assets/postman_html.jpg)
![Postman XML](/assets/postman_xml.jpg)
![Postman JSON](/assets/postman_json.jpg)