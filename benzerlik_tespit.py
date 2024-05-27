import veriTabani
import os
import metinIsleme
def dosya_oku(dosyaAdi1,dosyaAdi2):
    with open(dosyaAdi1,"r",encoding="utf-8") as dosya:
        icerik1=dosya.read()
    with open(dosyaAdi2,"r",encoding="utf-8") as dosya:
        icerik2=dosya.read()    
    return icerik1 , icerik2
class Benzerlik():
    def __init__(self,metin1,metin2):
        self.metin1=metin1
        self.metin2=metin2
    def uzun_metin_bul(self):
        metinUzunluklari=[]
        len1=len(self.metin1)
        len2=len(self.metin2)
        metinUzunluklari.append(len1)
        metinUzunluklari.append(len2)
        metinUzunluklari.sort()
        uzun_metin=metinUzunluklari[-1]
        return uzun_metin


    def benzerlik_analizi(self):
        # Her iki metni de birer sözlüğe dönüştür
        frekans_sozlugu1={}
        frekans_sozlugu2={}
        for karakter in self.metin1:
            frekans_sozlugu1[karakter]=frekans_sozlugu1.get(karakter, 0)+1
        for karakter in self.metin2:
            frekans_sozlugu2[karakter]=frekans_sozlugu2.get(karakter, 0)+1
        
        # Ortak karakterlerin bulunduğu bir küme oluştur
        ortak_karakterler =set(frekans_sozlugu1.keys())&set(frekans_sozlugu2.keys())
        ortak_alt_dizgi=""
        # Ortak karakterlerin en uzun alt dizgisini iki metinde geçen ortak kelimeler
        for karakter in ortak_karakterler:
            ortak_alt_dizgi+=karakter*min(frekans_sozlugu1[karakter],frekans_sozlugu2[karakter])
    
        return len(ortak_alt_dizgi)
        
def olc_benzerlik():
    calisma_dizini = os.getcwd()

    # Alt klasör adı
    alt_klasor_adi = "veri_tabani_klasörü"
    #kullnıcıya var olan dosyaları gösterme
    veriTabani.veri_tabani_goster()
    # Kullanıcıdan dosya adını al
    print("!!!1. dosyayi secin!!!")
    dosya_adi1 = veriTabani.dosya_sec()
    print("!!!2. dosyayi secin!!!")
    dosya_adi2= veriTabani.dosya_sec()

    # Dosya yolunu birleştirerek oluştur
    dosya_yolu1 = os.path.join(calisma_dizini, alt_klasor_adi, dosya_adi1)
    dosya_yolu2= os.path.join(calisma_dizini, alt_klasor_adi, dosya_adi2)

    kontrolEdilecek1,kontrolEdilecek2=dosya_oku(dosya_yolu1,dosya_yolu2)
    
    belge1=metinIsleme.metinVerileriniIsle(kontrolEdilecek1)
    belge2=metinIsleme.metinVerileriniIsle(kontrolEdilecek2)
    
    benzerlikObjesi=Benzerlik(belge1,belge2)
    skor=benzerlikObjesi.benzerlik_analizi()/benzerlikObjesi.uzun_metin_bul()*100 

    dosya_adi="metin benzerlik bilgileri.txt"
    bilgiendirme_dosya_yolu = os.path.join(alt_klasor_adi, dosya_adi)

    with open(bilgiendirme_dosya_yolu,"a",encoding="utf-8") as dosya:
        dosya.write(f"{dosya_adi1}, {dosya_adi2} dosyalari arasindaki benzerlik skoru=%{skor:.0f}\n\n")
   
    if skor>80:
        print(f"sectiginiz metinlerin benzerlik skoru:%{skor:.0f} metinler yüksek oranda benzer")
    elif skor>50:
        print(f"sectiginiz metinlerin benzerlik skoru :%{skor:.0f} metinler benzer")
    elif skor>25:
        print(f"sectiginiz metinlerin benzerlik skoru :%{skor:.0f} metinler düsük benzer")
    else:
        print(f"sectiginiz metinlerin benzerlik skoru:%{skor:.0f} metinler benzer degil")