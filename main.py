import istatistik
import benzerlik_tespit
import veriTabani
import aramaveFiltreleme
def main():
    print("\nMetin analiz uygulamasina hosgeldiniz!")
    devammi=True
    while devammi:
        secim1=input("\n1-veri tabanindaki verilerle islem yap\n2-veri tabanina git\n3-uygulamayi sonlandir\ntercih:")
        if secim1=="1":
            secim2=input("\n1-metin benzerlik tespiti\n2-metin istatistik bilgileri\n3-dosya icinde arama\ntercih:")
            if secim2=="1":
                benzerlik_tespit.olc_benzerlik()
            elif secim2=="2":
                istatistik.calistir()
            elif secim2=="3":
                aramaveFiltreleme.arama_calistir()
            else:
                print("\nhatali giris menu yeniden baslatılıyor")
                devammi=True
                
        elif secim1=="2":
            while True:
                secim3=input("\n1-dosya ekle\n2-dosyalari gorüntüle\n3-dosya sil\n4-dosya guncelle\n5-veri tabani menüsünden ayril\ntercih:")
                if secim3=="1":
                    veriTabani.klasore_ekle()
                elif secim3=="2":
                    veriTabani.veri_tabani_goster()
                elif secim3=="3":
                    veriTabani.dosya_sil()
                elif secim3=="4":
                    veriTabani.dosya_guncelle()
                elif secim3=="5":
                    devammi=True
                    break
                else:
                    print("\nhatali giris")
                    devammi=False
                    break
        elif secim1=="3":
            devammi=False
        else:
            print("\nhatali giris menu yeniden baslatılıyor")
            devammi=True
    print("\nuygulama sonlandi")
main()


