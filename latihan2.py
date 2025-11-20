data_mhs = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\n=== MENU PROGRAM NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))

        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

        data_mhs[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": nilai_akhir
        }

        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        if nama in data_mhs:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru: "))
            uas = float(input("Nilai UAS baru: "))

            nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

            data_mhs[nama] = {
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": nilai_akhir
            }

            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")

    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        if nama in data_mhs:
            del data_mhs[nama]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    elif pilihan == "4":
        if len(data_mhs) == 0:
            print("Belum ada data.")
        else:
            print("\n===== DAFTAR NILAI MAHASISWA =====")
            print("Nama\tTugas\tUTS\tUAS\tAkhir")
            print("-" * 40)
            for nama, nilai in data_mhs.items():
                print(f"{nama}\t{nilai['tugas']}\t{nilai['uts']}\t{nilai['uas']}\t{nilai['akhir']:.2f}")

    elif pilihan == "5":
        nama = input("Masukkan nama mahasiswa yang dicari: ")
        if nama in data_mhs:
            print("\nData ditemukan!")
            print(f"Nama  : {nama}")
            print(f"Tugas : {data_mhs[nama]['tugas']}")
            print(f"UTS   : {data_mhs[nama]['uts']}")
            print(f"UAS   : {data_mhs[nama]['uas']}")
            print(f"Akhir : {data_mhs[nama]['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid, silakan pilih 1-6.")
