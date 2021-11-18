#Membuat program pengurutan bilangan sederhana
#Terdapat 3 buah bilangan dalam input
Bil1 = int(input("Masukkan bilangan 1 :"))
Bil2 = int(input("Masukkan bilangan 2 :"))
Bil3 = int(input("Masukkan bilangan 3 :"))

#Mengurutkan bilangan dari yang terkecil 
#Jika Bil1 lebih besar dari Bil2 dan Bil2 lebih kecil dari Bil3
if (Bil1<Bil2) and (Bil2<Bil3):
    #Jika Bil2 lebih kecil dari Bil3
    if (Bil2<Bil3):
        #Mencetak Urutan bilangan dari yang terkecil
        print ("Urutan bilangan dari yang terkecil adalah", Bil1, Bil2, Bil3)
    else : 
        print("Urutan bilangan dari yang terkecil adalah", Bil1, Bil2, Bil3)
#Jika Bil2 lebih kecil dari Bil3 dan Bil2 lebih kecil dari Bil1
elif (Bil2<Bil3) and (Bil2<Bil1) :
    #Jika Bil3 lebih kecil dari Bil1
    if (Bil3<Bil1):
        #Mencetak Urutan bilangan dari yang terkecil
        print ("Urutan bilangan dari yang terkecil adalah", Bil2, Bil3, Bil1)
    else :
        print("Urutan bilangan dari yang terkecil adalah", Bil2, Bil1, Bil3)
else :
    #Jika Bil1 lebih kecil dari Bil2 
    if (Bil1<Bil2):
        #Mencetak Urutan bilangan dari yang terkecil
        print ("Urutan bilangan dari yang terkecil adalah", Bil3, Bil1, Bil2)
    else :
        print("Urutan bilangan dari yang terkecil adalah", Bil3, Bil2, Bil1)