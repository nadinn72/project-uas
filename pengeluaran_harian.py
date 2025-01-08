class Data:
    def __init__(self):
        self.pengeluaran = []

    def tambah_pengeluaran(self, deskripsi, jumlah):
        self.pengeluaran.append({
            'deskripsi': deskripsi,
            'jumlah': jumlah
        })

    def hapus_pengeluaran(self, index):
        if 0 <= index < len(self.pengeluaran):
            self.pengeluaran.pop(index)
            return True
        return False

    def get_pengeluaran(self):
        return self.pengeluaran


class View:
    @staticmethod
    def tampilkan_pengeluaran(pengeluaran):
        print("\nDaftar Pengeluaran Harian:")
        print(f"{'No':<5} {'Deskripsi':<30} {'Jumlah':<10}")
        print("=" * 50)
        for index, item in enumerate(pengeluaran, start=1):
            print(f"{index:<5} {item['deskripsi']:<30} {item['jumlah']:<10}")
        print("=" * 50)


class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def input_pengeluaran(self):
        try:
            deskripsi = input("Masukkan deskripsi pengeluaran: ")
            jumlah = float(input("Masukkan jumlah pengeluaran: "))

            if jumlah <= 0:
                raise ValueError("Jumlah pengeluaran harus lebih dari 0.")

            self.data.tambah_pengeluaran(deskripsi, jumlah)
            print("Pengeluaran berhasil ditambahkan.")
        except ValueError as e:
            print(f"Input tidak valid: {e}")

    def hapus_pengeluaran(self):
        try:
            self.view.tampilkan_pengeluaran(self.data.get_pengeluaran())
            index = int(input("Masukkan nomor pengeluaran yang ingin dihapus: ")) - 1

            if self.data.hapus_pengeluaran(index):
                print("Pengeluaran berhasil dihapus.")
            else:
                print("Nomor pengeluaran tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor yang benar.")

    def tampilkan_pengeluaran(self):
        pengeluaran = self.data.get_pengeluaran()
        if pengeluaran:
            self.view.tampilkan_pengeluaran(pengeluaran)
        else:
            print("Belum ada pengeluaran yang dicatat.")


def main():
    process = Process()
    while True:
        print("\nMenu:")
        print("1. Tambah Pengeluaran")
        print("2. Hapus Pengeluaran")
        print("3. Tampilkan Pengeluaran")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            process.input_pengeluaran()
        elif pilihan == '2':
            process.hapus_pengeluaran()
        elif pilihan == '3':
            process.tampilkan_pengeluaran()
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()