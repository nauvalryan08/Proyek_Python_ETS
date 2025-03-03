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

# Menyimpan data pasien ke dalam file berdasarkan kategori (BPJS, Asuransi, Mandiri).
def simpan_pasien(kategori, nama, nik, poli, dokter, tanggal_temu, jenis_asuransi=None, pembayaran=None):
     # Menentukan file berdasarkan kategori
    file_map = {
        "BPJS": "data/bpjs.txt",
        "Asuransi": "data/asuransi.txt",
        "Mandiri": "data/mandiri.txt"
    }
    
    if kategori not in file_map:
        print("Kategori tidak valid.")
        return False
    
    file_path = file_map[kategori]

    # Cek apakah kuota masih tersedia
    jumlah_pasien = hitung_pasien(file_path, poli)
    if jumlah_pasien >= KUOTA_ANTRIAN:
        print(f"⚠️ Kuota untuk Poli {poli} sudah penuh! Pendaftaran tidak dapat dilakukan.")
        return False

    # Format data yang akan disimpan
    pasien_data = (
        f"Nama: {nama}\n"
        f"NIK: {nik}\n"
        f"Poli: {poli}\n"
        f"Dokter: {dokter}\n"
        f"Tanggal Temu: {tanggal_temu}\n"
    )

    # Data khusus Asuransi & Mandiri
    if kategori == "Asuransi":
        pasien_data += f"Jenis Asuransi: {jenis_asuransi}\n"
    if kategori in ["Asuransi", "Mandiri"]:
        pasien_data += f"Pembayaran: {pembayaran}\n"

    pasien_data += "-" * 30 + "\n"  # Pembatas antar data pasien

    # Simpan ke file
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(pasien_data)

    print(f"✅ Data pasien berhasil disimpan ke {file_path}")
    return True
