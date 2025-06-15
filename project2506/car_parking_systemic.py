#!/bin/env python

import time
from datetime import datetime

# Inisialisasi Variabel
# parkiran = {plat : waktu_masuk (timestamp)}
parkiran = {}
MAX_SLOT = 10
TARIF_PER_JAM = 5000

def show_menu():
  print("\n===== SISTEM PARKIR =====")
  print("1. Parkir Mobil")
  print("2. Keluarkan Mobil")
  print("3. Lihat Daftar Parkir")
  print("4. Keluar\n")

def car_parking():
  if len(parkiran) >= MAX_SLOT :
    print('Area parkir telah penuh.')
    return
      
  else :
    plat = input('Masukan nomor kendaraan: ').strip().upper()
    if plat in parkiran :
      print(f'Mobil {plat} sudah terparkir.')
      return
    # Mencatat waktu masuk  
    waktu_masuk = time.time()
    parkiran[plat] = waktu_masuk
    waktu_str = datetime.fromtimestamp(waktu_masuk).strftime('%Y-%m-%d %H:%M:%S')
      
    print(f'Mobil {plat} berhasil diparkir.')
    print(f'Waktu parkir: {waktu_str}')

def take_out():
  plat = input('Masukan nomor kendaraan: ').strip().upper()
  if plat not in parkiran :
    print(f'Mobil {plat} tidak ada di dalam area parkir.')
    return
    
  waktu_masuk = parkiran[plat]
  # Memulai hitung durasi parkir
  waktu_keluar = time.time()
  durasi_detik = waktu_keluar - waktu_masuk
  jam = int(durasi_detik // 3600)
  if durasi_detik % 3600 > 0 :
    jam += 1
  biaya = TARIF_PER_JAM * jam
    
  waktu_masuk_str = datetime.fromtimestamp(waktu_masuk).strftime('%H:%M:%S')
  waktu_keluar_str = datetime.fromtimestamp(waktu_keluar).strftime('%H:%M:%S')
    
  # Mencetak detail data parkir
  print(f'Mobil {plat} berhasil keluar.')
  print(f'Masuk: {waktu_masuk_str}')
  print(f'Keluar: {waktu_keluar_str}')
  print(f'Durasi: {durasi_detik:.2f} detik')
  print(f'Total biaya: Rp{biaya:,}')
  
  # Menghapus data parkir
  del parkiran[plat]
    
def show_list_of_parking():
  print('Daftar mobil terparkir:')
  if not parkiran :
    print('Untuk saat ini, belum ada mobil terparkir.')
  else :
    for i, (plat, waktu) in enumerate(parkiran.items(), 1):
      waktu_str = datetime.fromtimestamp(waktu).strftime('%Y-%m-%d %H:%M:%S')
      print(f'{i}. {plat} Waktu: {waktu_str}')
  print(f'Slot tersisa: {MAX_SLOT - len(parkiran)}')

def main():
  # Menjalankan seluruh program
  while True:
    show_menu()
    option = input('Pilih Menu [1-4]: ')
    match option :
      case '1' :
        car_parking()
      case '2' :
        take_out()
      case '3' :
        show_list_of_parking()
      case '4' :
        print('Exit')
        break
      case _ : # else
        print('Tidak ada pilihan tersebut.')

if __name__ == '__main__':
  main()