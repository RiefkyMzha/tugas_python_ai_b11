# PYTHON PROGRAMMING: FUNCTIONS & CLASSES
# Functions
def greet(nama: str) -> str:
    """Mengembalikan teks sapaan."""
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b

def rata_rata(angka: list[float]) -> float:
    """Mengembalikan rata-rata angka, 0.0 jika list kosong."""
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)

# Classes
class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []

    def tambah_nilai(self, skor: float) -> None:
        """Menambah satu nilai ke dalam list nilai."""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Menghitung rata-rata nilai memakai function rata_rata()."""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """Mengembalikan LULUS jika rata-rata >= threshold."""
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"

    def __str__(self) -> str:
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"

# Demo
if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Riefky"))
    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10)  :", tambah(10))
    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([])           :", rata_rata([]))

    print("\n=== CLASS STUDENT ===")

    mhs1 = Student("Riefky Muhammad Haychal Mirzha", "8020230022")
    mhs1.tambah_nilai(85.5)
    mhs1.tambah_nilai(92.0)
    mhs1.tambah_nilai(88.0)
    print(mhs1)
    print("Rata-rata:", mhs1.rata_nilai(), "| Status:", mhs1.status())

    mhs2 = Student("Siti Rahma", "8020230008")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.0)
    print(mhs2)
    print("Rata-rata:", mhs2.rata_nilai(), "| Status:", mhs2.status())