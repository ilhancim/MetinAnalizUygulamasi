from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
import panel
import panel1
import panel1_2
import panel1_3
import panel2
import panel2_1
import panel2_2
import panel2_3
import panel2_4
from yeniPanel import panel1_1
import veriTabani as veriTabani
import yeniPanel.benzerlik_tespit as benzerlik_tespit
import yeniPanel.istatistik as istatistik
import yeniPanel.aramaveFiltreleme as aramaveFiltreleme

class Panel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p = panel.Ui_MainWindow()
        self.p.setupUi(self)
        self.p1 = Panel1()
        self.p2 = Panel2()
        self.p.pushButton.clicked.connect(self.buton1)
        self.p.pushButton_2.clicked.connect(self.buton2)

    def buton1(self):
        self.close()
        self.p1.show()

    def buton2(self):
        self.close()
        self.p2.show()

class Panel1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p1 = panel1.Ui_MainWindow()
        self.p1.setupUi(self)
        self.p1_1 = Panel1_1()
        self.p1_2 = Panel1_2()
        self.p1_3 = Panel1_3()
        self.p1.pushButton.clicked.connect(self.buton1)
        self.p1.pushButton_2.clicked.connect(self.buton2)
        self.p1.pushButton_3.clicked.connect(self.buton3)
        self.p1.pushButtonG.clicked.connect(self.geriDon)

    def buton1(self):
        self.close()
        self.p1_1.show()

    def buton2(self):
        self.close()
        self.p1_2.show()

    def buton3(self):
        self.close()
        self.p1_3.show()

    def geriDon(self):
        self.close()
        self.p = Panel()
        self.p.show()

class Panel1_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p1_1 = panel1_1.Ui_MainWindow()
        self.p1_1.setupUi(self)
        self.p1_1.pushButtonG.clicked.connect(self.geriDon)
        self.p1_1.pushButton.clicked.connect(self.Benzerlik)

        self.listele()

    def listele(self):
        try:
            dosyalar = veriTabani.veri_tabani_goster()

            # Model oluşturun
            model = QStandardItemModel()

            # ListView'e dosya adlarını ekleyin
            for dosya in dosyalar:
                item = QStandardItem(dosya)
                model.appendRow(item)

            # ListView modelini ayarlayın
            self.p1_1.listView.setModel(model)

        except Exception as e:
            print(f"Hata: {e}")
            QMessageBox.critical(self, "Hata", f"Dosya isimlerini yüklerken bir hata oluştu: {str(e)}")

    def geriDon(self):
        self.close()
        self.p1 = Panel1()
        self.p1.show()

    def Benzerlik(self):
        try:
            self.dosyaNumarasi1 = self.p1_1.lineEdit.text()
            self.dosyaNumarasi2 = self.p1_1.lineEdit_2.text()
            benzerlik = benzerlik_tespit.olc_benzerlik(self.dosyaNumarasi1, self.dosyaNumarasi2)
            msg = QMessageBox()
            msg.setWindowTitle('Benzerlik')
            msg.setText(benzerlik)
            msg.setStandardButtons(QMessageBox.Ok)

            # Mesaj kutusunu göster
            msg.exec_()
        except Exception as e:
            print("Hata oluştu:", e)


class Panel1_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p1_2 = panel1_2.Ui_MainWindow()
        self.p1_2.setupUi(self)
        self.dosyaNumarasi = self.p1_2.lineEdit.text()
        self.p1_2.pushButtonG.clicked.connect(self.geriDon)
        self.p1_2.pushButton.clicked.connect(self.istatistik)

        self.listele()

    def listele(self):
        try:
            dosyalar = veriTabani.veri_tabani_goster()

            # Model oluşturun
            model = QStandardItemModel()

            # ListView'e dosya adlarını ekleyin
            for dosya in dosyalar:
                item = QStandardItem(dosya)
                model.appendRow(item)

            # ListView modelini ayarlayın
            self.p1_2.listView.setModel(model)

        except Exception as e:
            print(f"Hata: {e}")
            QMessageBox.critical(self, "Hata", f"Dosya isimlerini yüklerken bir hata oluştu: {str(e)}")

    def geriDon(self):
        self.close()
        self.p1 = Panel1()
        self.p1.show()

    def istatistik(self):
        try:
            self.dosyaNumarasi1 = self.p1_2.lineEdit.text()
            bilgi = istatistik.calistir(self.dosyaNumarasi1)
            msg = QMessageBox()
            msg.setWindowTitle('Istatistik')
            msg.setText(bilgi)
            msg.setStandardButtons(QMessageBox.Ok)
            # Mesaj kutusunu göster
            msg.exec_()

        except Exception as e:
            print("Hata oluştu:", e)

class Panel1_3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p1_3 = panel1_3.Ui_MainWindow()
        self.p1_3.setupUi(self)
        self.p1_3.pushButtonG.clicked.connect(self.geriDon)
        self.p1_3.pushButton.clicked.connect(self.arama)

        self.listele()

    def listele(self):
        try:
            dosyalar = veriTabani.veri_tabani_goster()

            # Model oluşturun
            model = QStandardItemModel()

            # ListView'e dosya adlarını ekleyin
            for dosya in dosyalar:
                item = QStandardItem(dosya)
                model.appendRow(item)

            # ListView modelini ayarlayın
            self.p1_3.listView.setModel(model)

        except Exception as e:
            print(f"Hata: {e}")
            QMessageBox.critical(self, "Hata", f"Dosya isimlerini yüklerken bir hata oluştu: {str(e)}")

    def geriDon(self):
        self.close()
        self.p1 = Panel1()
        self.p1.show()

    def arama(self):
        try:
            self.dosyaNumarasi1 = self.p1_3.lineEdit.text()
            self.anahtar_kelime = self.p1_3.lineEdit_2.text()
            sonuc = aramaveFiltreleme.arama_calistir(self.dosyaNumarasi1,self.anahtar_kelime)
            msg = QMessageBox()
            msg.setWindowTitle('Arama')
            msg.setText(sonuc)
            msg.setStandardButtons(QMessageBox.Ok)
            # Mesaj kutusunu göster
            msg.exec_()

        except Exception as e:
            print("Hata oluştu:", e)

class Panel2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p2 = panel2.Ui_MainWindow()
        self.p2.setupUi(self)
        self.p2_1 = Panel2_1()
        self.p2_2 = Panel2_2()
        self.p2_3 = Panel2_3()
        self.p2_4 = Panel2_4()
        self.p2.pushButton.clicked.connect(self.buton1)
        self.p2.pushButton_2.clicked.connect(self.buton2)
        self.p2.pushButton_3.clicked.connect(self.buton3)
        self.p2.pushButton_4.clicked.connect(self.buton4)
        self.p2.pushButtonG.clicked.connect(self.geriDon)

    def geriDon(self):
        self.close()
        self.p = Panel()
        self.p.show()

    def buton1(self):
        self.close()
        self.p2_1.show()

    def buton2(self):
        self.close()
        self.p2_2.show()

    def buton3(self):
        self.close()
        self.p2_3.show()

    def buton4(self):
        self.close()
        self.p2_4.show()

class Panel2_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p2_1 = panel2_1.Ui_MainWindow()
        self.p2_1.setupUi(self)
        self.p2_1.pushButtonG.clicked.connect(self.geriDon)

    def geriDon(self):
        self.close()
        self.p2 = Panel2()
        self.p2.show()
class Panel2_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p2_2 = panel2_2.Ui_MainWindow()
        self.p2_2.setupUi(self)
        self.p2_2.pushButtonG.clicked.connect(self.geriDon)

        self.listele()

    def listele(self):
        try:
            dosyalar = veriTabani.veri_tabani_goster()

            # Model oluşturun
            model = QStandardItemModel()

            # ListView'e dosya adlarını ekleyin
            for dosya in dosyalar:
                item = QStandardItem(dosya)
                model.appendRow(item)

            # ListView modelini ayarlayın
            self.p2_2.listView.setModel(model)

        except Exception as e:
            print(f"Hata: {e}")
            QMessageBox.critical(self, "Hata", f"Dosya isimlerini yüklerken bir hata oluştu: {str(e)}")

    def geriDon(self):
        self.close()
        self.p2 = Panel2()
        self.p2.show()
class Panel2_3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p2_3 = panel2_3.Ui_MainWindow()
        self.p2_3.setupUi(self)
        self.p2_3.pushButtonG.clicked.connect(self.geriDon)

        self.listele()

    def listele(self):
        try:
            dosyalar = veriTabani.veri_tabani_goster()

            # Model oluşturun
            model = QStandardItemModel()

            # ListView'e dosya adlarını ekleyin
            for dosya in dosyalar:
                item = QStandardItem(dosya)
                model.appendRow(item)

            # ListView modelini ayarlayın
            self.p2_3.listView.setModel(model)

        except Exception as e:
            print(f"Hata: {e}")
            QMessageBox.critical(self, "Hata", f"Dosya isimlerini yüklerken bir hata oluştu: {str(e)}")

    def geriDon(self):
        self.close()
        self.p2 = Panel2()
        self.p2.show()
class Panel2_4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p2_4 = panel2_4.Ui_MainWindow()
        self.p2_4.setupUi(self)
        self.p2_4.pushButtonG.clicked.connect(self.geriDon)

        self.listele()

    def listele(self):
        try:
            dosyalar = veriTabani.veri_tabani_goster()

            # Model oluşturun
            model = QStandardItemModel()

            # ListView'e dosya adlarını ekleyin
            for dosya in dosyalar:
                item = QStandardItem(dosya)
                model.appendRow(item)

            # ListView modelini ayarlayın
            self.p2_4.listView.setModel(model)

        except Exception as e:
            print(f"Hata: {e}")
            QMessageBox.critical(self, "Hata", f"Dosya isimlerini yüklerken bir hata oluştu: {str(e)}")

    def geriDon(self):
        self.close()
        self.p2 = Panel2()
        self.p2.show()

app = QApplication([])
pencere = Panel()
pencere.show()
app.exec_()
