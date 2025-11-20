kontak = {
    "Ari": "0812678888",
    "Dina": "0876777776"
}
print("Kontak Ari:", kontak["Ari"])

kontak["Riko"] = "087654544"
print("Kontak setelah menambah Riko:", kontak)

kontak["Dina"] = "088999776"
print("Kontak setelah update Dina:", kontak)

print("Semua Nama:")
for nama in kontak.keys():
    print(nama)

print("Semua Nomor:")
for nomor in kontak.values():
    print(nomor)

print("Daftar Nama dan Nomor:")
for nama, nomor in kontak.items():
    print(f"{nama} : {nomor}")

del kontak["Dina"]
print("Kontak setelah Dina dihapus:", kontak)
