class SistemNilai:
    def __init__(self):
        self.data_siswa = {}

    def tambah_siswa(self, nama, nilai):
        self.data_siswa[nama] = {
            'Nilai': nilai,
            'Grade': self.hitung_grade(nilai)
        }
        print(f"Data {nama} berhasil ditambahkan!")

    def hitung_grade(self, nilai):
        if nilai >= 90:
            return 'A'
        elif nilai >= 80:
            return 'B'
        elif nilai >= 70:
            return 'C'
        elif nilai >= 60:
            return 'D'
        else:
            return 'E'

    def lihat_data(self):
        if not self.data_siswa:
            print("Belum ada data siswa!")
            return
        
        print("\nData Nilai Siswa:")
        print("=====================================")
        print("Nama\t\tNilai\t\tGrade")
        print("=====================================")
        for nama, info in self.data_siswa.items():
            print(f"{nama}\t\t{info['Nilai']}\t\t{info['Grade']}")
        print("=====================================")

def main():
    sistem = SistemNilai()
    
    while True:
        print("\nSistem Penginputan Nilai Siswa")
        print("1. Tambah Data Siswa")
        print("2. Lihat Data Siswa")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            while True:
                try:
                    nilai = float(input("Masukkan nilai siswa (0-100): "))
                    if 0 <= nilai <= 100:
                        break
                    else:
                        print("Nilai harus antara 0-100!")
                except ValueError:
                    print("Masukkan nilai yang valid!")
            sistem.tambah_siswa(nama, nilai)
            
        elif pilihan == '2':
            sistem.lihat_data()
            
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem ini!")
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()