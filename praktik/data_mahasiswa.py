def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if not data:
        return 0
    return sum(info["nilai"] for info in data.values()) / len(data)

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# Pencarian data
for nim in ["A003", "A999"]:
    hasil = cari_mahasiswa(data_mahasiswa, nim)
    if hasil is not None:
        print(f"{nim}: {hasil}")
    else:
        print(f"{nim}: Data tidak ditemukan")

# Tambah mahasiswa
data_mahasiswa["A006"] = {
    "nama": "Fajar", "kelas": "B", "nilai": 80
}

# Ubah nilai
data_mahasiswa["A002"]["nilai"] = 82

# Tampilkan seluruh data
print("\nRekap Data Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(nim, info)

print(f"\nRata-rata nilai: {rata_rata_nilai(data_mahasiswa):.2f}")
