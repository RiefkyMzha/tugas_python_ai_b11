# Deklarasi Variabel dan Tipe Data 
print("==== DEKLARASI VARIABEL DAN TIPE DATA ====")
nama_mahasiswa = "Riefky Muhammad Haychal Mirzha"
nim = 8020230022
ipk = 3.98
status_aktif = True
daftar_mata_kuliah = [
    "Pengolahan Citra", 
    "Komputer dan Masyarakat", 
    "Machine Learning 2", 
    "Proyek Penelitian", 
    "Decision Support System", 
    "Realitas Virtual dan Augmentasi", 
    "Animasi dan Pemodelan 3D", 
    "Cloud Computing"
    ]

print("Nama         :", nama_mahasiswa)
print("NIM          :", nim)
print("IPK          :", ipk)
print("Status Aktif :", status_aktif)
print("Daftar Matkul:", daftar_mata_kuliah)

# Manipulasi String
print("\n==== MANIPULASI STRING ====")
info_mahasiswa = "Nama : " + nama_mahasiswa + "\nNIM : " + str(nim) 
print(info_mahasiswa)

panjang_nama = len(nama_mahasiswa)
print("Panjang nama : " + str(panjang_nama) + " karakter")

upper = nama_mahasiswa.upper()
lower = nama_mahasiswa.lower()
print("Nama huruf besar : ", upper)
print("Nama huruf kecil : ", lower)

# Operasi Matermatika
print("\n==== OPERASI MATEMATIKA ====")
panjang = 20
lebar = 10

luas = panjang * lebar
keliling = 2 * (panjang + lebar)
lebar_persegi = (keliling / 2) - panjang
panjang_persegi = luas / lebar

print(f"Panjang = {panjang} \nLebar = {lebar}")
print("Luas persegi panjang :", luas)
print("Keliling persegi panjang :", keliling)
print("Lebar persegi :", lebar_persegi)
print("Panjang persegi :", panjang_persegi)

# List dan Akses Elemen
print("\n==== LIST DAN AKSES ELEMEN ====")
print("Daftar Mata Kuliah :", daftar_mata_kuliah)

print("Matkul pertama :", daftar_mata_kuliah[0])
print("Matkul terakhir :", daftar_mata_kuliah[7])

daftar_mata_kuliah.append("Sistem Informasi Geografis")
print("Setelah ditambahkan :", daftar_mata_kuliah)

daftar_mata_kuliah.remove("Komputer dan Masyarakat")
print("Setelah dihapus :", daftar_mata_kuliah)

mata_kuliah_terurut = sorted(daftar_mata_kuliah)
print("Daftar matkul terurut :", mata_kuliah_terurut)

matkul_terhapus = daftar_mata_kuliah.pop()
print("Item yang dipop   :", matkul_terhapus)
print("Setelah pop       :", daftar_mata_kuliah)

# Penggunaan Input dari User
print("\n==== PENGGUNAAN INPUT DARI USER ====")
nama_input = input("Masukkan nama Anda: ")
nim_input = input("Masukkan NIM Anda: ")

perkenalan = f"Halo, nama saya {nama_input} dengan NIM {nim_input}"
print(perkenalan)