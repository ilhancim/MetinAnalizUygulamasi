import veriTabani
import os
import metinIsleme
import re
def arama_ve_filtreleme(dosya_yolu, anahtar_kelime):
    try:
        with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
            satirlar = dosya.readlines()
            
        # Anahtar kelimeyi düzenli ifade (regex) olarak kullanarak arama yap
        filtrelenmis_satirlar = [satir for satir in satirlar if re.search(anahtar_kelime, satir)]
        
        if filtrelenmis_satirlar:
            print(f"'{anahtar_kelime}' anahtar kelimesini içeren satırlar:")
            for satir in filtrelenmis_satirlar:
                print(satir.strip())
        else:
            print(f"'{anahtar_kelime}' anahtar kelimesini içeren hiçbir satır bulunamadı.")
    
    except FileNotFoundError:
        print(f"'{dosya_yolu}' dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def arama_calistir():
    calisma_dizini = os.getcwd()

    # Alt klasör adı
    alt_klasor_adi = "veri_tabani_klasörü"
    # kullanıcıya var olan dosyalar gösterilir
    print("\n hangi dosyaninin icinde arama yapmak istersiniz")
    veriTabani.veri_tabani_goster()
    # Kullanıcıdan dosya adını al
    dosya_adi = veriTabani.dosya_sec()

    # Dosya yolunu birleştirerek oluşturma
    dosya_yolu = os.path.join(calisma_dizini, alt_klasor_adi, dosya_adi)
    anahtar_kelime = input("Aranacak anahtar kelimeyi girin: ")
    islenmis_anahtar_kelime=metinIsleme.metinVerileriniIsle(anahtar_kelime)

    # Fonksiyonu çağır
    arama_ve_filtreleme(dosya_yolu, islenmis_anahtar_kelime)