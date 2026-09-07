# PYTHON PROGRAMMING: PYTHON DATA STRUCTURES

# List - akses & manipulasi
print("=== List - akses & manipulasi ===")

profil_mahasiswa = ["Riefky Muhammad Haychal Mirzha", "8020230022", 3.98, "Teknik Informatika", 2023, "Jambi"]
print ("Profil Mahasiswa :", profil_mahasiswa)

print("Elemen pertama:", profil_mahasiswa[0])
print("Elemen terakhir:", profil_mahasiswa[-1])
print("Slicing [0:5:3]:", profil_mahasiswa[0:5:3])

print("\nSebelum append:", profil_mahasiswa)
profil_mahasiswa.append("Aktif")
print("Setelah append:", profil_mahasiswa)

print("\nSebelum insert:", profil_mahasiswa)
profil_mahasiswa.insert(3, "S1")
print("Setelah insert:", profil_mahasiswa)

print("\nSebelum extend:", profil_mahasiswa)
profil_mahasiswa.extend(["Quick Study", "Semester 7"])
print("Setelah extend:", profil_mahasiswa)

print("\nSebelum pop :", profil_mahasiswa)
item_hilang = profil_mahasiswa.pop()
print(f"Sesudah pop (item '{item_hilang}' dihapus):", profil_mahasiswa)
 
print("\nSebelum remove:", profil_mahasiswa)
profil_mahasiswa.remove("S1")
print("Sesudah remove 'S1':", profil_mahasiswa)

# Tuple – immutability & unpacking
print("\n=== Tuple – immutability & unpacking ===")

biodata_mahasiswa = ("Riefky Muhammad Haychal Mirzha", "8020230022", 3.98, "Teknik Informatika", 2023, "Jambi")
print("Tuple:", biodata_mahasiswa)
print("Panjang tuple:", len(biodata_mahasiswa))
print("Elemen indeks ke-0:", biodata_mahasiswa[0])
print("Elemen indeks ke-3:", biodata_mahasiswa[3])

nama, nim, *rest = biodata_mahasiswa
print("Nama:", nama)
print("NIM:", nim)
print("Sisa data lainnya (rest):", rest)

# Set – keunikan & operasi himpunan
print("\n=== Set – keunikan & operasi himpunan ===")
mata_kuliah_wajib = {
    "Pengolahan Citra",
    "Komputer dan Masyarakat",
    "Machine Learning 2",
    "Proyek Penelitian",
    "Komputer dan Masyarakat"
}

mata_kuliah_pilihan = {
    "Decision Support System",
    "Realitas Virtual dan Augmentasi",
    "Animasi dan Pemodelan 3D",
    "Cloud Computing",
    "Pengolahan Citra"  
}

print("Mata kuliah wajib ('Komputer dan Masyarakat' ditulis 2x akan muncul 1 kali):", mata_kuliah_wajib)
print("Mata kuliah pilihan:", mata_kuliah_pilihan)
 
print("\nUnion (|):", mata_kuliah_wajib | mata_kuliah_pilihan)
print("Intersection (&):", mata_kuliah_wajib & mata_kuliah_pilihan)
print("Difference (-):", mata_kuliah_wajib - mata_kuliah_pilihan)
print("Symmetric difference (^):", mata_kuliah_wajib ^ mata_kuliah_pilihan)

# Dictionary – key value pairs
print("\n=== Dictionary – key-value pairs ===")

mahasiswa = {
    "nama": "Riefky Muhammad Haychal Mirzha",
    "nim": "8020230022",
    "angkatan": 2023,
    "kota": "Jambi"
}

print("Dictionary awal:", mahasiswa)
 
mahasiswa["jurusan"] = "Teknik Informatika"
print("Setelah tambah key 'jurusan':", mahasiswa)
 
mahasiswa["kota"] = "Muaro Jambi"
print("Setelah ubah nilai 'kota':", mahasiswa)
 
del mahasiswa["angkatan"]
print("Setelah hapus key 'angkatan':", mahasiswa)
 
print("\nKeys  :", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items :", mahasiswa.items())
 
print("\nIterasi key: value")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Nested structures
print("\n=== Nested structures ===")

daftar_mahasiswa = [
    {"nama": "Riefky Muhammad Haychal Mirzha", "nim": "8020230022", "angkatan": 2023},
    {"nama": "Siti Rahma", "nim": "8020230008", "angkatan": 2021},
    {"nama": "Budi Santoso", "nim": "8020230005", "angkatan": 2023},
    {"nama": "Dewi Lestari", "nim": "8020230001", "angkatan": 2022},
]

print("Daftar semua nama mahasiswa:")
for mhs in daftar_mahasiswa:
    print("-", mhs["nama"])

angkatan_minimal = 2022
mahasiswa_baru = [mhs["nama"] for mhs in daftar_mahasiswa if mhs["angkatan"] >= angkatan_minimal]
print(f"\nMahasiswa angkatan >= {angkatan_minimal}:", mahasiswa_baru)

# Comprehension & Utility
print("\n=== Comprehension & Utility ===")

# List comprehension
angka = list(range(1, 21))
angka_genap = [n for n in angka if n % 2 == 0]
angka_kuadrat = [n*n for n in angka]
print("List genap (1-20):", angka_genap)
print("List kuadrat (1-20):", angka_kuadrat)

# Dict comprehension
status_angka = {n: ("genap" if n % 2 == 0 else "ganjil") for n in range(1, 11)}
print("Dict genap/ganjil (1-10):", status_angka)

# Set comprehension
kalimat = "Teknik Informatika Universitas Dinamika Bangsa"
huruf_unik = {huruf.lower() for huruf in kalimat if huruf.isalpha()}
print("Huruf unik:", huruf_unik)

# Keanggotaan & pencarian sederhana
print("\n=== Keanggotaan & pencarian sederhana ===")

data_dicari = "Jambi"
if data_dicari in profil_mahasiswa:
    print(f"'{data_dicari}' ditemukan di list pada indeks {profil_mahasiswa.index(data_dicari)}")
else:
    print(f"'{data_dicari}' tidak ditemukan di list")

matkul_dicari = "Cloud Computing"
print(f"'{matkul_dicari}' ada di mata_kuliah_pilihan?", matkul_dicari in mata_kuliah_pilihan)