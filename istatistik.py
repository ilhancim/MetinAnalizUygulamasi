import string

class Istatistik:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi

    def noktalama_sil(self, metin):
        noktalama_isaretleri = string.punctuation
        temiz_metin = ""
        for karakter in metin:
            if karakter not in noktalama_isaretleri:
                temiz_metin += karakter
        return temiz_metin

    def bosluk_sil(self, metin):
        return "".join(metin.split())
    
    def bosluklara_ayir(self, metin):
        return metin.split()


    def harf_sayisi_bul(self):
        toplam = 0
        harf = []
        sayi = []

        with open(self.dosya_adi, "r+") as dosya:
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


    def kelime_sayisi_bul(self):
        with open(self.dosya_adi, "r+") as dosya:
            icerik = dosya.read()
            kelimeler = self.bosluklara_ayir(icerik)
            toplam = len(kelimeler)
            print("Girilen dosyadaki toplam kelime sayısı-->", toplam)


    def etkisiz_kelime_sayisi(self):
        etkisiz_kelimeler = ["ve", "veya", "ama", "ancak", "şu", "bu", "bir", "şey", "olarak", "olduğunu", "gibi", "ise", "ile", "o", "ki", "ile", "ile", "değil", "ise", "hepsi", "şöyle", "böyle", "şimdilik", "şöylelikle", "böylelikle", "zira", "çünkü", "şayet", "eğer", "her", "hep", "sadece", "yalnızca", "sanki", "mış", "miş", "muş", "müş", "diye", "oldu", "olduğu", "de", "da", "ile", "üzerinde", "altında", "içinde", "ardından", "sonra", "şimdi"]
        toplam = 0

        with open(self.dosya_adi, "r+") as dosya:
            icerik = dosya.read()
            yeni_icerik = self.bosluklara_ayir(self.noktalama_sil(icerik))

            for kelime in yeni_icerik:
                if kelime in etkisiz_kelimeler:
                    toplam += 1

            for j in etkisiz_kelimeler:
                if yeni_icerik.count(j) > 1:
                    toplam += 1

        print("Girilen dosyadaki etkisiz kelime sayısı-->", toplam)

    def kelime_kullanim_sayilari(self):
        kelime_sayilari = {}

        with open(self.dosya_adi, "r+",encoding="utf-8") as dosya:
            icerik = dosya.read()
            kelimeler = self.bosluklara_ayir(icerik)

            for kelime in kelimeler:
                if kelime not in kelime_sayilari:
                    kelime_sayilari[kelime] = 1
                else:
                    kelime_sayilari[kelime] += 1

        sorted_kelimeler = sorted(kelime_sayilari.items(), key=lambda x: x[1], reverse=True)

        print("\nEn çok kullanılan ilk 5 kelime:")
        for kelime, sayi in sorted_kelimeler[:5]:
            print(f"{kelime}: {sayi}")

        print("\nEn az kullanılan ilk 5 kelime:")
        for kelime, sayi in sorted_kelimeler[-5:]:
            print(f"{kelime}: {sayi}")

