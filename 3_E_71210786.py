#Membuat program untuk menampung siswa.
#Membuat Input Daftar siswa.
Daftarsiswa = ((input("Masukkan daftar siswa :")))
#Mencetak Daftar siswa.
print ("daftar siswa :" ,Daftarsiswa.title().split(","))
#Menambahkan Input Data siswa yang ingin ditambahkan
Menambahkan = ((input("Masukkan siswa yang ingin ditambahkan :")))
#Jika menambahkan not di daftarsiswa.
if Menambahkan not in Daftarsiswa:
    #Mencetak hasil penambahan pada daftar siswa.
    print("Hasil penambahan pada daftar siswa :" ,[Daftarsiswa.title() ,Menambahkan.upper()])
else:
    #Mencetak siswa jika sudah ada di dalam daftar siswa.
    print("Siswa atas nama" ,(Menambahkan.upper()) ,"sudah berada dalam daftar siswa")