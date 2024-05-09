dosya_adi=input("Lütfen harf sayısını hesaplayacağınız dosya adını giriniz--> ")
toplam=0
harf=[]
sayi=[]

with open (dosya_adi,"r+") as dosya:

    icerik=dosya.read()
    yeni_icerik="".join(icerik.split()) #metindeki boşlukları siler

    for i in(yeni_icerik):

        if not (i in harf): #
            harf.append(i) #eğer harf lsitesinde i yoksa eklenir
            sayi.append(1) #eğer sayı listesinde i yoksa 1 olur
        else:
            sayi[harf.index(i)]=sayi[harf.index(i)]+1 #eğer girilen metinde i indexteki harften bir tane daha varsa sayı 1 artar
    
    for j in range(len(harf)): #harf sayısını hesaplar
        toplam+=sayi[j]
        
    print("Dosyadaki toplam harf sayısı-->",toplam)
