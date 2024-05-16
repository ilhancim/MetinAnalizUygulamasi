import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity #benzerlik hesabı icin gerekli kütüphaneler
def dosya_oku():
    with open("dosyaAdi1","r") as dosya:
        icerik=dosya.read()
    with open("dosyaAdi2.txt","r") as dosya:
        icerik1=dosya.read()
    with open("dosyaAdi3.txt","r") as dosya:
        icerik2=dosya.read()    
    return icerik , icerik1 , icerik2
def menu_benzerlik():
    x=input("\nkarsilastirmak istediginiz metinleri secin\n\nmetin1 icin 1'i\nmetin2 icin 2'i\n metin3 icin 3'u tuslayin\n\nilk dosyayi seçin tercih:")
    y=input("2. dosyayi secin tercih:")
    return x,y
class Benzerlik():
    def __init__(self,metin1,metin2):
        self.metin1=metin1
        self.metin2=metin2
    def benzerlik_analizi(self):

        vectorlestir = CountVectorizer().fit_transform([self.metin1,self.metin2]) # CountVectorizer kullanarak metinleri vektör temsiline dönüştürme
        
        cosine_sim = cosine_similarity(vectorlestir) # Cosine Similarity hesaplama
        return np.mean(cosine_sim) # cosine_similarity fonksiyonunun çıktısını ortalama alarak bir sayısal değer elde ediyoruz

def olc_benzerlik():
    tercih1,tercih2=menu_benzerlik()
    text1,text2,text3=dosya_oku()
    try:
        if tercih1=="1":
            kontrolEdilecek1=text1
        elif tercih1=="2":
            kontrolEdilecek1=text2
        elif tercih1=="3":
            kontrolEdilecek1=text3
        if tercih2=="1":
            kontrolEdilecek2=text1
        elif tercih2=="2":
            kontrolEdilecek2=text2
        elif tercih2=="3":
            kontrolEdilecek2=text3
        belge1=kontrolEdilecek1
        belge2=kontrolEdilecek2
        benzerlikObjesi=Benzerlik(belge1,belge2)
        skor=benzerlikObjesi.benzerlik_analizi()
        if skor>0.7:
            print(f"sectiginiz metinlerin benzerlik skoru 0-1 arası :{skor} metinler yüksek oranda benzer")
        elif skor>0.4:
            print(f"sectiginiz metinlerin benzerlik skoru 0-1 arası :{skor} metinler ortalama benzerlikte")
        elif skor>0.2:
            print(f"sectiginiz metinlerin benzerlik skoru 0-1 arası :{skor} metinler düsük benzer")
        else:
            print(f"sectiginiz metinlerin benzerlik oranı 0-1 arası: {skor} metinler benzer degil")
    except:
        print("!!!1/2/3 nolu tuslari tuslayin!!!")
olc_benzerlik()