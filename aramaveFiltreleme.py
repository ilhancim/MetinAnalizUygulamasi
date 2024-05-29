import os
import veriTabani
import metinIsleme
import re
def arama_ve_filtreleme(dosya_yolu, anahtar_kelime):
    try:
        with open(dosya_yolu, 'r', encoding='latin-1') as dosya:
            satirlar = dosya.readlines()
            
        # Anahtar kelimeyi düzenli ifade (regex) olarak kullanarak arama yap
        filtrelenmis_satirlar = [satir for satir in satirlar if re.search(anahtar_kelime, satir)]
        sonuc = ""
        if filtrelenmis_satirlar:
            for satir in filtrelenmis_satirlar:
                sonuc+= (satir.strip()) + "\n"
        else:
            sonuc = (f"'{anahtar_kelime}' anahtar kelimesini içeren hiçbir satır bulunamadı.")

        return sonuc
    except FileNotFoundError:
        print(f"'{dosya_yolu}' dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def arama_calistir(dosyaNumarasi1,anahtar_kelime):
    calisma_dizini = os.getcwd()

    # Alt klasör adı
    alt_klasor_adi = "veri_tabani_klasörü"
    # kullanıcıya var olan dosyalar gösterilir
    veriTabani.veri_tabani_goster()
    # Kullanıcıdan dosya adını al
    dosya_adi = veriTabani.dosya_sec(dosyaNumarasi1)

    # Dosya yolunu birleştirerek oluşturma
    dosya_yolu = os.path.join(calisma_dizini, alt_klasor_adi, dosya_adi)
    islenmis_anahtar_kelime= metinIsleme.metinVerileriniIsle(anahtar_kelime)

    # Fonksiyonu çağır
    return arama_ve_filtreleme(dosya_yolu, islenmis_anahtar_kelime)
