# Proyek Django PBP - Tugas 2

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama   : Devina Hana Azhara**<br/>
**NPM    : 2106751032**<br/>
**Kelas  : E**<br/>


### [Heroku Application Link](https://tugas-2-devina.herokuapp.com/katalog/)


## Client Request to Django Web Application

![Client Request](/assets/bagan.png)

Ketika client ingin menjalankan suatu web aplikasi berbasis Django, client perlu melakukan request ke HTTP. Request yang masuk tersebut kemudian diproses melalui URL dan diarahkan menuju views yang telah ditentukan oleh developer untuk menangani permintaan. Nantinya, jika terdapat kebutuhan untuk mengakses database, views akan memanggil query ke models kemudian database mengembalikan hasil query ke views. Selanjutnya, hasil proses request tersebut akan di-*mapping* ke dalam file HTML dan dikembalikan sebagai objek respons bagi client.


## Virtual Environment

Virtual environment merupakan suatu lingkungan virtual terisolasi yang diciptakan untuk memberikan dependensi bagi suatu proyek. Virtual environment diperlukan agar kita dapat menspesifikasi versi dan jenis dari tiap *tools* yang digunakan. Hal ini dapat mencegah proyek kita dari perubahan atau eror yang tidak diinginkan jika misalnya terdapat pembaharuan pada *tools* tersebut yang mungkin tidak mendukung jalannya proyek. 

Meskipun demikian, suatu proyek Django tetap dapat berjalan tanpa menggunakan virtual environment. Akan tetapi, proyek tersebut menjadi rentan terhadap eror bila versi dari Django atau *tools* lainnya berubah secara global untuk komputer dan tak lagi dapat mendukung proyek tersebut. 


## Implementasi MVT pada Django

#### Membuat Aplikasi Katalog

* Membuat repositori baru dengan menggunakan [template](https://github.com/pbp-fasilkom-ui/assignment-repository) yang telah disediakan
* Melakukan *clone* repositori tersebut pada komputer
* Membuat dan mengaktifkan *virtual environment* untuk repositori tersebut
* Melakukan instalasi *dependencies* yang diperlukan
* Membuat aplikasi django bernama **katalog**
* Mendaftarkan aplikasi **katalog** tersebut pada settings.py di folder project_django

#### Melakukan Konfigurasi Model

* Menyiapkan migrasi skema model yang berisikan data CatalogItem pada models.py ke dalam database lokal Django
* Menerapkan skema model yang telah disiapkan ke dalam database lokal Django
* Memasukkan data lengkap dari CatalogItem yang berada pada katalog\fixtures\initial_catalog_data.json ke dalam database lokal Django

#### Implementasi Views

* Membuat fungsi show_katalog(request) pada views.py untuk melakukan pengambilan data dari model berupa CatalogItem dan dikembalikan ke katalog.html 
* Membentuk urls.py di dalam folder aplikasi katalog untuk melakukan *routing* terhadap fungsi show_katalog(request) pada views.py dengan memanggil method path()
* Mendaftarkan aplikasi **katalog** pada urls.py di dalam folder project_django dengan memanggil method path()

#### Menggabungkan Models, Views, dan Templates

* Melakukan pengambilan data dari database dengan mengimport model ke dalam views.py
* Memanggil model database dan menyimpan hasilnya pada variabel context
* Melakukan return fungsi show_katalog(request) dengan render(request, "katalog.html", context)
* Melakukan mapping data dari masing-masing objek context ke katalog.html dengan sintaks {{nama_variabel}}

#### Melakukan Deployment ke Heroku

* Membuat aplikasi baru pada Heroku
* Menambahkan secret berupa HEROKU_APP_NAME dan HEROKU_API_KEY
* Melakukan deployment dengan menghubungkan repositori github dengan heroku



## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.