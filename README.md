# project-uas

# Deskripsi Umum
Program ini adalah aplikasi sederhana untuk mencatat pengeluaran harian. Program ini dibangun dengan menggunakan konsep Object-Oriented Programming (OOP) dan modular, yang memisahkan logika data, tampilan, dan proses bisnis ke dalam kelas-kelas terpisah. Pengguna dapat menambah, menghapus, dan menampilkan pengeluaran dengan antarmuka berbasis teks.

**1. Kelas `Data`**

Kelas ini bertanggung jawab untuk menyimpan dan mengelola data pengeluaran. Ada beberapa bagian dalam kelas Data, yaitu:

**- Atribut:**
  - `pengeluaran` yaitu: List yang menyimpan semua pengeluaran dalam bentuk dictionary, di mana setiap dictionary berisi deskripsi dan jumlah pengeluaran.

**- Metode:**
  - `__init__(self)` yaitu: Konstruktor yang menginisialisasi list `pengeluaran` sebagai list kosong.
  - `tambah_pengeluaran(self, deskripsi, jumlah)` yaitu: Metode untuk menambahkan pengeluaran baru ke dalam list. Menerima dua parameter: `deskripsi` (string) dan `jumlah` (float).
  - `hapus_pengeluaran(self, index)` yaitu: Metode untuk menghapus pengeluaran berdasarkan indeks yang diberikan. Mengembalikan `True` jika pengeluaran berhasil dihapus, dan `False` jika indeks tidak valid.
  - `get_pengeluaran(self)` yaitu: Metode untuk mengambil semua data pengeluaran yang telah dicatat.

**2. Kelas `View`**

Kelas ini bertanggung jawab untuk menampilkan data pengeluaran kepada pengguna. Yang berisi:

**- Metode:**
  - `tampilkan_pengeluaran(pengeluaran)`: Metode statis yang menerima list pengeluaran dan mencetaknya dalam format tabel. Menampilkan nomor, deskripsi, dan jumlah pengeluaran dengan format yang rapi.

**3. Kelas `Process`**

Kelas ini mengelola logika bisnis dan interaksi dengan pengguna. Diantaranya yaitu:

**- Atribut:**
  - `data`: Instance dari kelas `Data` untuk mengelola data pengeluaran.
  - `view`: Instance dari kelas `View` untuk menampilkan data pengeluaran.

**- Metode:**
  - `__init__(self)`: Konstruktor yang menginisialisasi objek `data` dan `view`.
  - `input_pengeluaran(self)`: Metode untuk meminta input dari pengguna mengenai pengeluaran baru. Melakukan validasi untuk memastikan jumlah pengeluaran lebih dari 0. Jika input tidak valid, akan menampilkan pesan kesalahan.
  - `hapus_pengeluaran(self)`: Metode untuk menghapus pengeluaran. Menampilkan daftar pengeluaran yang ada dan meminta pengguna untuk memasukkan nomor pengeluaran yang ingin dihapus. Melakukan validasi untuk memastikan nomor yang dimasukkan valid.
  - `tampilkan_pengeluaran(self)`: Metode untuk menampilkan semua pengeluaran yang telah dicatat. Jika tidak ada pengeluaran, akan menampilkan pesan bahwa belum ada pengeluaran yang dicatat.

**4. Fungsi `main()`**

Fungsi ini adalah titik masuk program. Fungsi ni juga menyediakan menu interaktif untuk pengguna. Diantaranya adalah:

**- Proses:**
  - Menampilkan menu dengan pilihan untuk menambah, menghapus, menampilkan pengeluaran, atau keluar dari program.
  - Menggunakan loop untuk terus meminta input dari pengguna hingga mereka memilih untuk keluar.
  - Memanggil metode yang sesuai dari kelas `Process` berdasarkan pilihan pengguna.

**5. Eksekusi Program**
- Program dimulai dengan memanggil fungsi `main()` jika file dijalankan sebagai program utama.
- Selanjutnya, Pengguna dapat berinteraksi dengan program melalui menu yang disediakan, dan semua input akan divalidasi untuk memastikan keakuratan data.

## Kesimpulan dari penjelasan dari program ini adalah: 
Program pengeluaran harian ini adalah contoh yang baik dari penerapan OOP dan modularitas dalam pemrograman Python. Dengan memisahkan logika data, tampilan, dan proses, program ini menjadi lebih terstruktur dan mudah untuk dipelihara. Pengguna dapat dengan mudah mencatat dan mengelola pengeluaran harian mereka dengan antarmuka yang sederhana dan intuitif.
