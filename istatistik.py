import string
import veriTabani
import os
# Alt klasör adı
alt_klasor_adi = "veri_tabani_klasörü"
class Istatistik:

    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi
        self.etkisiz_kelimeler = ["ve", "veya", "ama", "ancak", "şu", "bu", "bir", "şey", "olarak", "olduğunu", "gibi", "ise", "ile", "o", "ki", "değil", "hepsi", "şöyle", "böyle", "şimdilik", "şöylelikle", "böylelikle", "zira", "çünkü", "şayet", "eğer", "her", "hep", "sadece", "yalnızca", "sanki", "mış", "miş", "muş", "müş", "diye", "oldu", "olduğu", "de", "da", "üzerinde", "altında", "içinde", "ardından", "sonra", "şimdi"]
    def noktalama_sil(self, metin):
        noktalama_isaretleri = string.punctuation
        temiz_metin = "".join([karakter for karakter in metin if karakter not in noktalama_isaretleri])
        return temiz_metin

    def bosluk_sil(self, metin):
        return "".join(metin.split())

    def harf_sayisi_bul(self):
        toplam = 0
        harf = []
        sayi = []

        with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            yeni_icerik = self.noktalama_sil(icerik)
            yeni_icerik2 = self.bosluk_sil(yeni_icerik)

            for i in yeni_icerik2:
                if i not in harf:
                    harf.append(i)
                    sayi.append(1)
                else:
                    sayi[harf.index(i)] += 1

            for j in range(len(harf)):
                toplam += sayi[j]
        
        print("Dosyadaki toplam harf sayısı -->", toplam)
        return toplam

    def kelime_sayisi_bul(self):
        with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            kelimeler = self.bosluklara_ayir(icerik)
            toplam = len(kelimeler)
            print("Girilen dosyadaki toplam kelime sayısı -->", toplam)
            return toplam

    def etkisiz_kelime_sayisi(self):
        toplam = 0

        with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            yeni_icerik = self.bosluklara_ayir(self.noktalama_sil(icerik))

            for kelime in yeni_icerik:
                if kelime in self.etkisiz_kelimeler:
                    toplam += 1

        print("Girilen dosyadaki etkisiz kelime sayısı -->", toplam)
        return toplam

    @staticmethod
    def hizli_sirala(liste):
        if len(liste) <= 1:
            return liste

        pivot = liste[len(liste) // 2]
        küçükler = [x for x in liste if x[1] < pivot[1]]
        orta = [x for x in liste if x[1] == pivot[1]]
        büyükler = [x for x in liste if x[1] > pivot[1]]

        return Istatistik.hizli_sirala(büyükler) + orta + Istatistik.hizli_sirala(küçükler)

    def bosluklara_ayir(self, metin):
        return metin.split()

    def kelime_kullanim_sayilari(self):
        kelime_sayilari = {}
        dosyaya_yazilacak_az_kullanilan_kelimeler={}
        dosyaya_yazilacak_cok_kullanilan_kelimeler={}

        with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            kelimeler = self.bosluklara_ayir(icerik)

            for kelime in kelimeler:
                if kelime not in self.etkisiz_kelimeler:
                    if kelime not in kelime_sayilari:
                        kelime_sayilari[kelime] = 1
                    else:
                        kelime_sayilari[kelime] += 1

        siralanmis_kelimeler = self.hizli_sirala(list(kelime_sayilari.items()))
        print("\nEn az kullanılan ilk 5 kelime:")
        for kelime, sayi in siralanmis_kelimeler[-5:]:
            print(f"{kelime}: {sayi}")
            dosyaya_yazilacak_az_kullanilan_kelimeler[kelime]=sayi

        print("\nEn çok kullanılan ilk 5 kelime:")
        for kelime, sayi in siralanmis_kelimeler[:5]:
            print(f"{kelime}: {sayi}")
            dosyaya_yazilacak_cok_kullanilan_kelimeler[kelime]=sayi
         
        return dosyaya_yazilacak_az_kullanilan_kelimeler,dosyaya_yazilacak_cok_kullanilan_kelimeler
def calistir():
    calisma_dizini = os.getcwd()

    # Alt klasör adı
    alt_klasor_adi = "veri_tabani_klasörü"
    #kullnıcıya var olan dosyaları gösterme
    print("bilgilerini görmek istediginiz dosyayi secin")
    veriTabani.veri_tabani_goster()
    dosya_adi=veriTabani.dosya_sec()
    dosya_yolu = os.path.join(calisma_dizini, alt_klasor_adi, dosya_adi)

    # Örnek kullanım
    istatistik = Istatistik(dosya_yolu)
    istatistik.harf_sayisi_bul()
    istatistik.kelime_sayisi_bul()
    istatistik.etkisiz_kelime_sayisi()
    istatistik.kelime_kullanim_sayilari()

    harf_sayisi=istatistik.harf_sayisi_bul()
    kelime_sayisi=istatistik.kelime_sayisi_bul()
    etkisiz_kelime_sayisi=istatistik.etkisiz_kelime_sayisi()
    az_kullanilan_5_kelime,cok_kullanilan_5_kelime=istatistik.kelime_kullanim_sayilari()
    dosya_adi2="metin istatistik bilgileri.txt"
    bilgiendirme_dosya_yolu = os.path.join(alt_klasor_adi, dosya_adi2)

    with open(bilgiendirme_dosya_yolu,"a",encoding="utf-8") as dosya:
        dosya.write(f"{dosya_adi} dosyasi bilgileri\nharf sayisi={harf_sayisi}\nkelime sayisi={kelime_sayisi}\netkisiz kelime sayisi={etkisiz_kelime_sayisi}\nen az kullanilan ilk 5 kelime={az_kullanilan_5_kelime}\nen cok kullanilan 5 kelime={cok_kullanilan_5_kelime}\n\n")
