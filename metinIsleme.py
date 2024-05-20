import string
import nltk
from nltk.corpus import stopwords

def metinVerileriniIsle():
    #kullanicidan secim degiskeni alinir
    secim = int(input(" 1-Dosyadan cekim\n 2-Elle giris\n "))

    #secim eger 1 ise girilen dosya adinin icindeki metin "metin" degiskenine esitlenir
    if secim == 1:
        dosyaAdi = input("dosya adi giriniz (ornek.txt):")
        oku = open(dosyaAdi,"r")
        metin = oku.read()

    #secim eger 2 ise direkt kullanicidan metin degiskeni alinir.
    elif secim == 2:
        metin = input("metin giriniz: ")

    #secim eger 1 ve 2 den farkli ise metin otomatik metine esitlenir.
    else:
        print("Boyle bir islem yok, metin otomatik metine atanıyor.")
        metin = "Bu modul metnin icindeki, noktalama isaretlerini (. ! ?) ve etkisiz kelimeleri (ve veya ile) kaldirmaktadir."
        print(f"metin = {metin}")

    #metin degiskeninin harfleri kucultulup tekrardan metin degiskenine esitlenir.
    metin = metin.lower()

    #noktalamaIsaret degiskeni string fonksiyonunun punctuation komutuyla noktalama isaretlerine esitlenir.
    #metnin karakterleri tek tek kontrol edilir eger noktalamaIsaret listesinin icindeki herhangi bir elemanla
    #uyusmuyor ise noktalamasizMetin degiskenine eklenir.
    noktalamaIsaret = string.punctuation
    noktalamasizMetin = ""
    for i in metin:
        if i not in noktalamaIsaret:
            noktalamasizMetin += i

    #noktalamasizMetin metni bosluklarına ayrılarak kelimeler listesine esitlenir.
    kelimeler = noktalamasizMetin.split()

    #etkisizKelimeler nltk kütüphanesi yardımıyla etkisiz kelimelere esitlenir
    #kelimeler listesi tek tek kontrol edilir eger etkisizKelimeler listesinin icindeki herhangi bir elemanla
    #uyusmuyor ise etkiliMetin degiskenine eklenir.
    etkisizKelimeler = stopwords.words('turkish')
    etkiliMetin = ""
    for i in kelimeler:
        if i not in etkisizKelimeler:
            etkiliMetin += i + " "

    #etkili metin dondurulur.
    return etkiliMetin

metinVerileriniIsle()