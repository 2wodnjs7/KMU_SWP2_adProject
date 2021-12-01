import pickle
from PyQt5.QtWidgets import *

food = '떡볶이'

class BookMark(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []

        self.resize(1080, 640)
        #self.widget = QWidget()
        #self.setCentralWidget()
        grid = QGridLayout()

        self.lbox = QListWidget()
        grid.addWidget(self.lbox, 0, 0, 1, 3)

        self.btnDelete = QPushButton()
        self.btnDelete.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.btnDelete, 1, 2)
        self.btnDelete.setText("해당 음식점 삭제")

        self.btn = QPushButton()
        self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.btn, 1, 0)
        self.btn.setText("지도 이동")

        self.btnPrint = QPushButton()
        self.btnPrint.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.btnPrint, 1, 1)
        self.btnPrint.setText("즐겨찾기 출력")

        grid.setRowStretch(0, 10)
        grid.setRowStretch(1, 1)
        grid.setColumnStretch(0, 4)
        grid.setColumnStretch(1, 1)

        self.setLayout(grid)

        self.btnPrint.clicked.connect(self.showBookmarkDB)
        self.btn.clicked.connect(self.go)
        self.btnDelete.clicked.connect(self.delBookmarkDB)

        self.readBookmarkDB()
        self.showBookmarkDB()
        self.show()

    def go(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def readBookmarkDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.restaurantDB = []
            return
        try:
            self.restaurantDB = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    def showBookmarkDB(self):
        fH = open(self.dbfilename, 'rb')
        try:
            self.restaurantDB = pickle.load(fH)
        except:
            pass
        else:
            pass
        self.lbox.clear()
        for p in self.restaurantDB:
            msg = p[0] + ' \t' + p[1] + '\t\t' + p[2] + ' \t' + p[3] + ' \t'
            self.lbox.addItem(msg)

        fH.close()

    def delBookmarkDB(self):
        fH = open(self.dbfilename, 'wb')
        row = self.lbox.currentRow()
        del self.restaurantDB[row]
        pickle.dump(self.restaurantDB, fH)
        fH.close()

        self.showBookmarkDB()




