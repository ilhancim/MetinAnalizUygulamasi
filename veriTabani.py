import os
import metinIsleme

klasor_adi = 'veri_tabani_klasörü'
klasor_yolu = os.path.abspath(klasor_adi)
dosya_secenek = {}  # Dosyaları numaralandırmak için kullanılan sözlük
dosya_numarasi=1
def klasor_olustur():
    try:
        os.mkdir(klasor_adi)
    except FileExistsError: # dosya zaten varsa
        print("")
def klasore_ekle(dosya_adi ,dosya_icerigi):
    islenmis_dosya_icerigi= metinIsleme.metinVerileriniIsle(dosya_icerigi)
    # Klasörün tam yolunu bulmak için os.path.abspath() fonksiyonunu kullanıldı
    klasor_olustur()
    # Dosya yolunu ve adını birleştirme
    dosya_yolu = os.path.join(klasor_yolu, dosya_adi)

    # Dosya oluşturma ve yazma işlemi
    with open(dosya_yolu, 'w') as dosya:
        dosya.write(islenmis_dosya_icerigi)
#Klasördeki dosyaları listeleme
def veri_tabani_goster():
    dosyalar = os.listdir(klasor_yolu)
    global dosya_numarasi
    # Dosyaları ekrana yazdırma
    for dosya in dosyalar:
        dosya_secenek[dosya]=dosya_numarasi  #dosya adi ve numaralara göre sözlük oluştur
        dosya_numarasi+=1
    dosya_numarasi=1
def dosya_sec(dosya_tercih1):
    for veri1 in dosya_secenek.keys():
        if dosya_secenek[veri1]==int(dosya_tercih1):
            secilen_dosya=veri1
    return secilen_dosya
def dosya_sil(dosyaNumarasi):
    veri_tabani_goster()
    # Silinecek dosyanın bulunduğu alt klasörün adı
    alt_klasor_adi = klasor_adi
    dosya_adi=dosya_sec(dosyaNumarasi)
    try:
        dosya_yolu = os.path.join(alt_klasor_adi, dosya_adi) # silinecek klosörün tanımlı olduğu yer
        os.remove(dosya_yolu)
    except FileNotFoundError:
        print(f"{dosya_adi} dosyası bulunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
def dosya_guncelle(dosyaNumarasi,dosyaIcerik):
    veri_tabani_goster()
    guncellenecekDosya=dosya_sec(dosyaNumarasi)
    try:
        calisma_dizini = os.getcwd()

        # Alt klasör adı
        alt_klasor_adi = klasor_adi
        # Dosya yolunu birleştirerek oluşturma
        dosya_yolu = os.path.join(calisma_dizini, alt_klasor_adi, guncellenecekDosya)
        with open(dosya_yolu,"w") as dosya:
            dosya.write(dosyaIcerik)
    except:
        print("dosya ")