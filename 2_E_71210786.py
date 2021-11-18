#Membuat Program pengecekan status suhu tubuh sederhana.
suhutubuh = float(input("Masukkan suhu tubuh anda :"))
#Jika suhu tubuh diatas 50°C = Anda bukan Manusia.
#Jika suhu tubuh kurang dari 32°C = Kedinginan.
#Jika suhu tubuh lebih dari 37,5°C hingga 50°C = Demam.
#Jika suhu tubuh berkisar 32°C hingga 37,5°C = Normal.
if suhutubuh >= 50 :
    #mencetak Anda bukan manusia karena suhu tubuh lebih dari 50°C
    print("Anda bukan manusia :)")
if suhutubuh < 32 :
    #mencetak Anda Kedinginan karena suhu tubuh kurang dari 32°C
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
if suhutubuh > 37.5 and suhutubuh <= 50 :
    #mencetak Anda demam karena suhu tubuh lebih dari 37.5°C hingga 50°C
    print("Anda demam! Jangan berpergian ke tempat fasilitas umum.")
if suhutubuh > 32 and suhutubuh <= 37.5 :
    #mencetak Suhu anda normal karena suhu tubuh lebih dari 32°C hingga 37.5°C
    print("Suhu anda normal!")
