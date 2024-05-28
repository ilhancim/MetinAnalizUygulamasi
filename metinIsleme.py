import string
import nltk
from nltk.corpus import stopwords

def metinVerileriniIsle(metin):
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
