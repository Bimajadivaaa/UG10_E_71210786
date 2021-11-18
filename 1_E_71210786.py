#Membuat Kalkulator akar dan pangkat sederhana
print("===== Kalkulator Akar dan Pangkat =====")
print("Pilihan menu:")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar Kuadrat")
#Membuat menu yang akan kita pilih
menupilihan = int(input("Masukkan menu yang anda pilih:"))
#Test Case 1 Membuat Pemangkatan bilangan pangkat 2/kuadrat
if menupilihan == 1:
    bilanganpertama = int(input("Masukkan bilangan yang ingin dipangkatkan:"))
    kuadratdua = bilanganpertama ** 2
    #Mencetak hasil dari pemangkatan bilangan kuadrat
    print ("Hasil dari pemangkatan bilangan" ,bilanganpertama ,"dengan 2 (kuadrat) adalah", kuadratdua)
#Test Case 2 Membuat Pemangkatan bilangan pangkat 3
elif menupilihan == 2:
    bilanganpertama = int(input("Masukkan bilangan yang ingin dipangkatkan:"))
    kuadrattiga = bilanganpertama ** 3
    #Mencetak hasil dari pemangkatan bilangan pangkat 3
    print ("Hasil dari pemangkatan bilangan" ,bilanganpertama ,"dengan 3 (kubik) adalah", kuadrattiga)
#Test Case 3 Membuat Akar kuadrat/akar dua
elif menupilihan == 3:
    bilanganpertama = int(input("Masukkan bilangan yang ingin diakarkan:"))
    akardua = bilanganpertama ** (1.0/2)
    #Mencetak hasil dari pemangkatan akar kuadrat/dua
    print ("Hasil dari akar kuadrat dari bilangan" ,bilanganpertama ,"adalah",akardua)
#Test Case 4 Membuktikan jika ada pilihan menu yang tidak sesuai
else:
    #Mencetak jika ada pilihan menu yang tidak sesuai
    print ("Pilihan menu yang dimasukkan tidak sesuai!")