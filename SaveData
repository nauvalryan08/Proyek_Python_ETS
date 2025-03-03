# Nama : Nauval Khairiyan
# Kelas : 1A - D4
# NIM : 241524021
# Desc : Menyimpan data pasien (BPJS, Asuransi, Mandiri) dalam file .txt

import os

KuotaAntrianPoli = 5 

if not os.path.exists("data"): # Memastikan file ada
    os.makedirs("data")

# Menghitung jumlah pasien yang sudah terdaftar dalam suatu poli berdasarkan file.
def hitung_pasien(file_path, poli):
     if not os.path.exists(file_path):
        return 0  # Jika file belum ada, berarti belum ada pasien

    count = 0
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if f"Poli: {poli}" in line:
                count += 1
    return count
