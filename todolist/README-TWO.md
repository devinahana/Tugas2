# Proyek Django PBP - Tugas 6

**Nama   : Devina Hana Azhara**<br/>
**NPM    : 2106751032**<br/>
**Kelas  : E**<br/>


#### [Link Heroku Todolist](https://tugas-2-devina.herokuapp.com/todolist/)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
### Asynchronous Programming
Asynchronous programming merupakan pemrograman berbasis multithread. Programming jenis ini memungkinkan beberapa operasi yang ada dapat berjalan secara beriringan tanpa perlu menunggu operasi lainnya selesai terlebih dahulu. Hal ini disebabkan program tidak berjalan secara sekuensial, melainkan secara paralel. Berbagai request yang masuk ini nantinya dapat berjalan secara independen tanpa memengaruhi satu sama lain.

### Synchronous Programming
Synchronous programming merupakan pemrograman berbasis single-thread. Programming jenis ini akan menjalankan operasi-operasinya secara sekuensial dengan urutan yang sesuai. Hal ini menyebabkan ketika suatu operasi tengah berjalan, instruksi untuk menjalankan operasi lainnya akan diblokir dan baru bisa dijalankan ketika operasi sebelumnya telah selesai dijalankan.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event driven programming merupakan pemrograman yang mendukung komununikasi tidak langsung antarentitas dengan pengiriman pesan melalui suatu perantara. Jenis pemrograman ini memungkinkan kode untuk memberikan respon terhadap berbagai event yang muncul. Event tersebut umumnya ditrigger oleh pengguna, seperti *button click*, *input text*, dan sebagainya. Ketika sistem mendeteksi munculnya event tersebut, maka program akan merespon sesuai dengan fungsi yang dapat dikustomisasi.<br>
Contoh penerapan event-driven programming pada tugas ini adalah ketika button dengan id create-button diklik, program akan merespon dengan memanggil fungsi posting dan fetchdata yang didefinisikan pada \<script>

## Jelaskan penerapan asynchronous programming pada AJAX.
AJAX merupakan suatu teknik yang memungkinkan suatu web untuk melakukan *update* secara asinkronus. Ketika terjadi suatu perubahan yang tidak terlalu besar, kita tidak perlu untuk me-reload seluruh page sebab kita dapat meminta AJAX untuk melakukan request kepada server dan mengirimkan informasi perubahan tersebut. Nantinya program akan terus berjalan tanpa perlu menunggu respons tersebut sampai terlebih dahulu. Barulah ketika respons telah didapatkan, program akan secara otomatis melakukan *update* terhadap halaman web.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Membuat fungsi show_json pada views.py yang akan mengembalikan data Task dalam bentuk json
* Menambahkan path json/ pada urls.py yang terhubung dengan fungsi show_json
* Membuat fungsi add_task pada views.py yang akan merespons request POST dengan mengambil data pada form, lalu membentuk task baru sesuai data tersebut
* Menambahkan path add/ pada urls.py yang terhubung dengan fungsi add_task
* Membuat button Add Task pada navbar dan menghubungkannya dengan modal yang berisi form penambahan Task
* Membentuk form penambahan Task pada modal dan button Create yang terhubung dengan AJAX
* Membentuk fungsi yang dapat merespons event klik button Create dengan mengambil data dari form dan memanggil fungsi add_task
* Membentuk fungsi fetchData dan update untuk melakukan *update* template dengan GET data dari JSON yang memanfaatkan fungsi show_json