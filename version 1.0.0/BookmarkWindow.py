import pickle
import webbrowser
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *


class BookMark(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []

        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(227, 253, 253))
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)

        self.lbox = QListWidget()
        self.lbox.setStyleSheet("border-style:none;background-color: #CBF1F5;font-size:16px;font-family:NanumBarunGothic;")

        self.firstButton = QPushButton()
        self.firstButton.setMaximumHeight(50)
        self.firstButton.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")
        self.firstButton.setText('첫 화면 가기')

        self.printButton = QPushButton()
        self.printButton.setMaximumHeight(50)
        self.printButton.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")
        self.printButton.setText('즐겨찾기 출력/갱신')

        self.webMove = QPushButton()
        self.webMove.setMaximumHeight(50)
        self.webMove.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")
        self.webMove.setText("웹 페이지 이동")

        self.deleteButton = QPushButton()
        self.deleteButton.setMaximumHeight(50)
        self.deleteButton.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")
        self.deleteButton.setText('해당 음식점 삭제')

        grid = QGridLayout()

        grid.addWidget(self.lbox, 0, 0, 1, 4)
        grid.addWidget(self.firstButton, 1, 0)
        grid.addWidget(self.printButton, 1, 1)
        grid.addWidget(self.webMove, 1, 2)
        grid.addWidget(self.deleteButton, 1, 3)

        grid.setRowStretch(0, 10)
        grid.setRowStretch(1, 1)

        self.setLayout(grid)

        self.firstButton.clicked.connect(self.firstButtonClicked)
        self.printButton.clicked.connect(self.showBookmarkDB)
        self.webMove.clicked.connect(self.webMoveClicked)
        self.deleteButton.clicked.connect(self.delBookmarkDB)

        self.readBookmarkDB()
        self.showBookmarkDB()
        self.show()

    def firstButtonClicked(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 5)

    def webMoveClicked(self):
        row = self.lbox.currentRow()
        if row == -1:
            QMessageBox.about(self, '오류', '즐겨찾기 목록이 비어있습니다.')
            return
        webbrowser.open(self.restaurantDB[row][3])

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
            msg ='[' + p[0] + '] - ' + p[1] + '\n' + p[2] + '\t' + p[3] + ' \t'
            self.lbox.addItem(msg)

        fH.close()

    def delBookmarkDB(self):
        self.readBookmarkDB()

        fH = open(self.dbfilename, 'wb')
        row = self.lbox.currentRow()
        if row == -1:
            QMessageBox.about(self, '오류', '즐겨찾기 목록이 비어있습니다.')
            return
        del self.restaurantDB[row]
        pickle.dump(self.restaurantDB, fH)
        fH.close()

        self.showBookmarkDB()




