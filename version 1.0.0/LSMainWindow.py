import pickle
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from LocaleSearcher import *


class LSMainWindow(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []
        self.ReadRestaurantDB()
        self.setWindowTitle('내 거주지 주변 음식점 검색')
        grid = QGridLayout()

        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(227, 253, 253))
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)

        self.query = QLineEdit()
        self.query.setStyleSheet("border-width:1px;border-color:#71C9CE;border-style:solid;background-color:#CBF1F5;font-size:20px;font-family:NanumBarunGothic;")
        self.query.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.btnSearch = QPushButton()
        self.btnSearch.setStyleSheet("background-color:#71C9CE;font-size:20px;font-family:NanumBarunGothic;")
        self.btnSearch.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnSearch.setText("내 거주지 입력 및 검색")

        self.lbox = QListWidget()
        self.lbox.setStyleSheet("border-width:1px;border-color:#71C9CE;border-style:solid;background-color:#CBF1F5;font-size:16px;font-family:NanumBarunGothic;")

        self.btnSave = QPushButton()
        self.btnSave.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")
        self.btnSave.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnSave.setText("해당 음식점 저장")

        self.btnBookmark = QPushButton()
        self.btnBookmark.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")
        self.btnBookmark.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnBookmark.setText("즐겨찾기 보기")

        self.webEngineView = QWebEngineView()
        self.webEngineView.load(QUrl("https://2wodnjs7.github.io/web1/"))

        grid.addWidget(self.query, 0, 0)
        grid.addWidget(self.btnSearch, 1, 0)
        grid.addWidget(self.lbox, 2, 0)
        grid.addWidget(self.btnSave, 3, 0)
        grid.addWidget(self.btnBookmark, 4, 0)
        grid.addWidget(self.webEngineView, 0, 1, 5, 1)
        grid.setRowStretch(0, 3)
        grid.setRowStretch(1, 3)
        grid.setRowStretch(2, 28)
        grid.setRowStretch(3, 3)
        grid.setRowStretch(4, 3)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 4)

        self.setLayout(grid)

        self.btnSearch.clicked.connect(self.Search)
        self.lbox.currentItemChanged.connect(self.LboxSelectChanged)
        self.btnSave.clicked.connect(self.RestaurantSave)
        self.btnBookmark.clicked.connect(self.BookmarkMove)


    def ReadRestaurantDB(self):
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

    def Search(self):
        if len(self.query.text()) < 1:
            QMessageBox.about(self, '오류', '먼저 거주지를 입력해주세요.')
            return
        f = open("RecommendedFood.txt", 'r')
        self.food = f.read()
        self.lbox.clear()
        text = self.query.text()
        try:
            x, y, self.locales = SearchLocale(text, self.food)
        except:
            QMessageBox.about(self, '오류', '거주지가 올바르지 않습니다.')
            return
        for locale in self.locales:
            self.lbox.addItem(locale.place_name)
        self.Move(x, y)

    def LboxSelectChanged(self):
        row = self.lbox.currentRow()
        if row == -1:
            return
        x = self.locales[row].x
        y = self.locales[row].y
        self.Move(x, y)

    def RestaurantSave(self):
        self.ReadRestaurantDB()
        fH = open(self.dbfilename, 'wb')
        row = self.lbox.currentRow()
        if row == -1:
            QMessageBox.about(self, '오류', '검색 목록이 비어있습니다.')
            return
        self.restaurantDB.append([self.food, self.locales[row].place_name, self.locales[row].address_name, self.locales[row].place_url])
        pickle.dump(self.restaurantDB, fH)
        fH.close()

    def BookmarkMove(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def Move(self, x, y):
        page = self.webEngineView.page()
        script = str.format("setMyCenter({0},{1});", y, x)
        page = page.runJavaScript(script)