tautan adaptable : https://kelontong.adaptable.app/main/
tautan repositori : https://github.com/renamartha/kelontong.git

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
a. Membuat proyek Django baru
- Pertama membuat direktori utama kelontong di komputer lokal.
- Masuk ke direktori tersebut menggunakan command prompt dan membuat virtual environment dengan perintah "python -m venv env". Setelah itu, virtual environment diaktifkan dengan perintah "env\Scripts\activate.bat".
- Pada direktori kelontong membuat berkas requirements.txt yang berisikan beberapa dependencies 
(django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3)
- Masih dalam kondisi virtual environment yang aktif, saya memasang dependencies yang sudah dimasukkan pada berkas requirements.txt dengan menjalankan perintah "pip install -r requirements.txt"
- Membuat proyek Django baru dengan nama kelontong, dengan menjalankan perintah "django-admin startproject kelontong ."
- Setelah proyek baru terbentuk, saya mengonfigurasikan proyek dan menjalankan server dengan menambahkan "*" pada ALLOWED_HOSTS di settings.py agar mendapat izin akses dari semua host. Lalu saya menjalankan perintah "python manage.py runserver" dan saat membuka http://localhost:8000 pada peramban web, ada animasi roket yang menandakan aplikasi Django berhasil dibuat.
- Setelah itu saya mengunggah proyek ke repositori di github (membuat repositori baru di github dengan nama kelontong serta menambahkan berkas .gitignore (seperti pada tutorial 0), lalu melakukan add, commit, push dari direktori lokal "kelontong")

b. Membuat aplikasi dengan nama main pada proyek kelontong
- Dengan kondisi berada pada direktori utama kelontong dan virtual environment yang aktif, saya menjalankan perintah "python manage.py startapp main" untuk membuat aplikasi baru dengan nama main (setelah menjalankan perintah tersebut terbentuk direktori baru bernama main).
- Setelah terbentuk direktori baru bernama main pada direktori proyek kelontong, saya mendaftarkan aplikasi main ke dalam proyek dengan menambahkan 'main' pada variabel INSTALLED_APPS di berkas settings.py dalam direktori proyek kelontong. 
- Aplikasi bernama main sudah didaftarkan ke dalam proyek kelontong.
- Membuat template untuk tampilan
     * Membuat direktori baru bernama templates pada direktori aplikasi main
     * Membuat berkas baru bernama main.html pada direktori templates dan diisi dengan
     <h1>Kelontong</h1>

     <h5>Name: </h5>
     <p>{{ name }}</p>
     <h5>Class: </h5>
     <p>{{ class }}</p> 
- Membuat model
     * Mengisi berkas models.py pada direktori aplikasi main dengan 
     from django.db import models

     class Item(models.Model):
          name = models.CharField(max_length=255)
          amount = models.IntegerField()
          harga = models.IntegerField()
          tanggal = models.DateField(auto_now_add=True)
          description = models.TextField()
     * Melakukan migrasi model dengan menjalankan perintah "python manage.py makemigrations" untuk migrasi model dan menjalankan perintah "python manage.py migrate" untuk migrasi ke dalam basis data lokal
     notes: setiap melakukan perubahan pada model, perlu dilakukan migrasi
- Menghubungkan view dengan template yang sudah dibuat
     * Mengisi berkas views.py yang ada pada direktori aplikasi main dengan  
     from django.shortcuts import render

     def show_main(request):
          context = {
               'name': 'Rena Martha Ulima',
               'class': 'PBP E'
          }
          return render(request, "main.html", context)

c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
- Routing URL aplikasi main
Membuat berkas urls.py pada direktori aplikasi main dan diisi dengan 
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

- Routing URL proyek
Menambahkan impor fungsi include "from django.urls import path, include" dan menambahkan rute URL dalam variabel urlpatterns "path('main/', include('main.urls'))" pada berkas urls.py pada direktori proyek kelontong (bukan direktori aplikasi main)

- Menjalankan proyek dengan perintah "python manage.py runserver" dan halaman web dapat dilihat

d. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib (name, amount, description)
(Dijelaskan pada poin b bagian membuat model)

e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
(Dijelaskan pada poin b bagian menghubungkan view dengan template)

f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
(Dijelaskan pada poin c bagian routing URL aplikasi main)

g. Membuat dan menjalankan test
- Mengisi berkas tests.py pada direktori aplikasi main dengan 
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

menjalankan test dengan perintah "python manage.py test", dan tes berhasil.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
![Alt text](image-2.png) atau bisa dilihat pada link berikut https://drive.google.com/file/d/1tJFIxfI85HxyIpVAfe0UJGIG91bl2ufl/view?usp=sharing 
(1) Client meminta request untuk mengakses halaman atau fitur pada web aplikasi 
(2) URL routing, urls.py akan menentukan pola URL yang akan mengarahkan request dari client ke tampilan/views yang sesuai
(3) views.py akan mengambil request yang diterima URL dan berkomunikasi dengan model (models.py) untuk mengambil atau menyimpan data yang dibutuhkan
(4) Setelah melakukan komunikasi dengan model, views akan mengembalikan respon yang sesuai dengan yang ada pada template (html file)
(5) Dikembalikan respons kepada client sesuai dengan request (dengan tampilan halaman html file yang sesuai)


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab:
Kita menggunakan virtual environment untuk mengisolasi package dan dependencies proyek aplikasi agar tidak bertabrakan dengan versi lain yang ada di komputer atau mempengaruhi proyek lain. Bisa saja membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun mungkin akan menyebabkan kompleksitas dependencies proyek.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Jawab:
MVC, MVT, MVVM merupakan model-model/konsep arsitektur yang digunakan dalam mengembangkan software/perangkat lunak khususnya dalam aplikasi berbasis web. Model-model tersebut memisahkan komponen-komponen utama dari aplikasi agar pengembang dapat mengelola dan mengorganisasikan kode dengan lebih terstruktur. 

(1) MVC (Model View Controller)
- Model berisi logika dan data yang ada dalam aplikasi. Model bertugas mendapatkan, memanipulasi data, berkomunikasi dengan controller, interaksi dengan database.
- View berkaitan dengan interface client (html, css) serta menyajikan data yang sesuai dengan request client. Komponen ini juga berinteraksi dengan model (menerima data dari model dan mengirimkan ke controller).
- Controller berperan sebagai perantara antara view dan model. Controller menerima input dari client melalui view, memproses input, lalu melakukan mengkomunikasikannya dengan model jika ada perubahan data.

(2) MVT (Model View Template)
- Model dan view pada MVT juga memiliki peran dan tanggung jawab yang sama dengan model dan view pada MVC
- Template komponen yang berfungsi mengatur tampilan client. Template digunakan untuk merancang tampilan yang akan diisi dengan data dari model melalui view. Template memisahkan html dengan logika aplikasi.

(3) MVVM (Model View ViewModel)
- Model dan view pada MVVM juga memiliki peran dan tanggung jawab yang sama dengan model dan view pada MVC dan MVT
- ViewModel merupakan komponen yang memisahkan view dari model. Komponen ini berinteraksi dengan model dimana data yang akan diteruskan ke view

Ketiga arsitektur tersebut memiliki perbedaan pada bagaimana komponen-komponen utama aplikasi dipisahkan.

Referensi:
* https://www.dicoding.com/blog/tips-design-pattern-mvvm/
* https://medium.com/@ankit.sinhal/mvc-mvp-and-mvvm-design-pattern-6e169567bbad
* Tutorial 0 dan Tutorial 1

