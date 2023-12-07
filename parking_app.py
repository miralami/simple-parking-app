from datetime import datetime
from pwinput import pwinput
from math import ceil

#TO DO LIST:

array_plat = [] #Merupakan list kosong, atau himpunan kosong (list menggunakan brackets [])
array_waktu = []
transaksi_dict = {} #Merupakan dictionary kosong, atau himpunan kosong (dictionary menggunakan kurung kurawal{})
transaksi_count = 0
tarif = 10_000 #Menggunakan "_" untuk readability
jml = 1
#Pendefinisian Fungsi
def hitung_waktu(start_time): #Pendefinisian fungsi dan menggunakan parameter start_time
    now = datetime.now() #Mengambil waktu sekarang ke variabel now menggunakan modul datetime, dengan class datetime, beserta fungsi now()
    waktu_elapsed = now - start_time #Variabel start_time di line ini dapat diganti oleh variabel lain nantinya di kode lain
    return waktu_elapsed #Mengembalikan value waktu_elapsed ke fungsi, jadi value waktu_elapsed melekat di fungsi.

def menu():
    while True: #Menggunakan while True untuk membuat loop tanpa kondisi, karena akan menggunakan break dibawah
        try: #Menggunakan try untuk menjalankan persyaratan kesesuaian tipe data
            print("\nPARKIRAN TELKOM UNIVERSITY")
            print("1. Masuk Area Parkir")
            print("2. Keluar Area Parkir")
            print("3. Admin Parkir")
            print("0. Exit")
            pilihan = int(input("Pilih menu [1/2/3/0]: "))
            break #Keluar dari loop, dan akan lanjut ke kode yang berindent sama dengan while
        except ValueError: #Selogika dengan if else. Except disini kita gunakan untuk mengecek jika terjadi ValueError
                           #atau tipe data tidak sesuai dengan ketentuan variabel pilihan
            print("Gunakan format angka[integer]")
    return pilihan

def admin_menu():
    while True:
        try:
            print("\n====== MENU ADMIN ======")
            print("\n1. Cek Daftar Kendaraan")
            print("2. Cek Transaksi")
            print("0. Exit")
            pil = int(input("Pilih Menu [1/2/0]: "))
            break
        except ValueError:
            print("Gunakan format angka[integer]")
    return pil #Fungsi admin_menu() kurang lebih sama dengan fungsi menu()
    
def masuk():
    while True:
        plat = input("Masukkan Plat Kendaraan: ").upper()
        if plat.strip():
            print("!!Silahkan Masuk!!")
            waktu_masuk = datetime.now()
            return plat, waktu_masuk #Fungsi dapat me-return lebih dari satu variabel
        else:
            print("Format plat tidak valid")
    
def admin_pin():
    pin = 2023
    try:
        check_pin = int(pwinput(prompt ="Enter your password: ", mask="*"))
    except ValueError:
        print("Invalid input. Masukkan PIN numeric.")
        return False
    
    if check_pin != pin: #Mengecek jika inputan pin tidak sama dengan pin
        print("Pin salah")
        status = False #Menggunakan boolean untuk set status
    else:
        status = True
    return status

def hitung_taraf(durasi):
    waktu_taraf = hitung_waktu(durasi).seconds
    print(waktu_taraf)
    return waktu_taraf


#Mulai program
choice = menu() #Menjalankan menu() dan mengambil value yang sudah di return ke variabel choice, yaitu pilihan
while choice != 0:
    if (choice == 1 and len(array_plat) < 11): #Dalam program ini saya memberi contoh kapasitas parkiran maksimal adalah 10
        plat, waktu_masuk = masuk() #Memanggil 2 value yang sudah di return
        if plat not in array_plat: #Jika plat tidak didalam array_plat[list], "not in"
            array_plat.append(plat) #Memasukkan inputan plat dari fungsi masuk() ke array_plat[list]
            array_waktu.append(waktu_masuk) #Memasukkan perhitungan waktu(datetime.now()) dari fungsi masuk() ke array_waktu[list]          
        else:
            print("Kendaraan sudah didalam")
        
    elif choice == 2:
        plat = input("Masukkan Plat Kendaraan: ").upper()
        if plat in array_plat:
            
            durasi = hitung_waktu(waktu_masuk)
            waktu_keluar = datetime.now()
            durasi_detik = durasi.seconds
            print(f"\nKendaraan ini sudah diparkiran selama: {durasi_detik} detik")
            print("Kendaraan ini keluar di", waktu_keluar.strftime("%X"))
            waktu_menit = ceil(durasi_detik / 60)
            bayar = tarif * waktu_menit
            if waktu_menit >= 6:
                denda = bayar + (bayar * 0.25)
                print("Karena anda parkir lebih dari 6 menit, maka dikenakan denda 25%")
            elif waktu_menit >= 4:
                denda = bayar + (bayar * 0.1)
                print("Karena anda parkir lebih dari 4 menit, maka dikenakan denda 10%")
                
            print(f"Tarif parkir anda: {bayar:,}\n")
            while True:
                nominal = int(input("Masukkan nominal: "))
                kembalian = nominal - bayar
                if nominal < bayar:
                    print("Uang kamu kurang, coba ambil uang lagi")
                else:
                    if kembalian > 0:
                        print(f"Kembalian: {kembalian}")
                    else:
                        print("Uang anda pas!")
                    break
            transaksi_count += 1
            if plat in transaksi_dict:
                transaksi_dict[plat] = [jml+1, waktu_masuk.strftime("%X"), waktu_keluar.strftime("%X"), durasi_detik, bayar] #Memasukkan waktu_masuk yang di format ke key value plat
            else:
                transaksi_dict[plat] = [jml, waktu_masuk.strftime("%X"), waktu_keluar.strftime("%X"), durasi_detik, bayar] #Memasukkan waktu_masuk yang di format ke key value plat
            
            print("Terima Kasih, sampai jumpa\n")
            if waktu_masuk in array_waktu:
                array_waktu.remove(waktu_masuk)
            array_plat.remove(plat)
            
        else:
            print(f"Error: Tidak ada kendaraan berplat nomor {plat}")
    elif choice == 3:
        status = admin_pin()
        if status:
            pil_admin = admin_menu()
            while pil_admin != 0:
                if pil_admin == 1:
                    if (len(array_plat) != 0):
                        print("Format: [Plat       , ...]")
                        print("Format: [Waktu Masuk, ...]")
                        array_waktu_fix = [datetime.strftime("%X") for datetime in array_waktu]
                        print (array_plat)
                        print(array_waktu_fix)
                        
                    else:
                        print("Belum ada kendaraan didalam parkiran")
                elif pil_admin == 2: #CEK TRANSAKSI                                                              
                    if len(transaksi_dict) != 0:
                        print("Berikut adalah transaksi parkir:\n")
                        print("Format: (Plat, [Berapa kali masuk, Waktu masuk terakhir, Waktu keluar terakhir, durasi terakhir, taraf terakhir])")
                        for plat in transaksi_dict.items():
                            print(plat)
                        print(f"\nTotal sudah ada {transaksi_count} transaksi")
                        
                    else:
                        print("Belum ada transaksi")
                else:
                    print("Pilihan tidak tersedia")
                pil_admin = admin_menu()
    else:
        print("Pilihan tidak tersedia")
    print("\nKembali ke menu utama...")
    choice = menu() 
