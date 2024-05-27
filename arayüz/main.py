from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
import panel0
import panel2
import panel3
import panel4
import a

class p0(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p0 = panel0.Ui_MainWindow()
        self.p0.setupUi(self)
        self.p2 = p2()
        self.p3 = p3()
        self.p4 = p4()
        self.p0.pb2.clicked.connect(self.buton2)
        self.p0.pb3.clicked.connect(self.buton3)
        self.p0.pb4.clicked.connect(self.buton4)

    def buton2(self):
        self.close()
        self.p2.show()

    def buton3(self):
        self.close()
        self.p3.show()

    def buton4(self):
        self.close()
        self.p4.show()

class p2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p2 = panel2.Ui_MainWindow()
        self.p2.setupUi(self)
        self.p2.pushButton.clicked.connect(self.anaEkran)
        self.p2.pushButton_2.clicked.connect(self.Istatistik)

    def anaEkran(self):
        self.close()
        self.p0 = p0()
        self.p0.show()

    def Istatistik(self):
        self.dosyaAdi = self.p2.lineEdit.text()
        self.temizMetin = a.a(self.dosyaAdi)
        print(self.temizMetin)

class p3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p3 = panel3.Ui_MainWindow()
        self.p3.setupUi(self)
        self.dosya1 = self.p3.lineEdit.text()
        self.dosya2 = self.p3.lineEdit_2.text()
        self.p3.pushButton.clicked.connect(self.anaEkran)
        self.p3.pushButton_2.clicked.connect(self.benzerlik)

    def anaEkran(self):
        self.close()
        self.p0 = p0()
        self.p0.show()

    def benzerlik(self):
        return 0

class p4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p4 = panel4.Ui_MainWindow()
        self.p4.setupUi(self)
        self.dosyaAdi = self.p4.lineEdit.text()
        self.kelime =self.p4.lineEdit_2.text()
        self.p4.pushButton.clicked.connect(self.anaEkran)
        self.p4.pushButton_2.clicked.connect(self.arama)

    def anaEkran(self):
        self.close()
        self.p0 = p0()
        self.p0.show()

    def arama(self):
        return 0
    
app = QApplication([])
pencere = p0()
pencere.show()
app.exec_()