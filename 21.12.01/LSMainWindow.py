import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from LocaleSearcher import *

food = '떡볶이'

class LSMainWindow(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []
        self.ReadRestaurantDB()
        self.resize(1080, 640)
        #self.widget = QWidget()  # QGridLayout개체를 배치할 Widget 개체 생성
        #self.setCentralWidget()  # LSMainWindow의 CentralWidget 설정
        grid = QGridLayout()  # QGridLayout 개체 생성

        self.setWindowTitle('내 거주지 주변 음식점 검색')  # 윈도우 타이틀
        self.query = QLineEdit()
        self.query.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.query, 0, 0)
        self.btnSearch = QPushButton()
        self.btnSearch.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.btnSearch, 1, 0)
        self.btnSearch.setText("내 거주지 입력 및 검색")

        self.lbox = QListWidget()
        grid.addWidget(self.lbox, 2, 0)  # row, column, row_span, column_span

        self.btnSave = QPushButton()
        self.btnSave.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.btnSave, 3, 0)
        self.btnSave.setText("해당 음식점 저장")

        self.btnBookmark = QPushButton()
        self.btnBookmark.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.btnBookmark, 4, 0)
        self.btnBookmark.setText("즐겨찾기 보기")

        self.webEngineView = QWebEngineView()
        grid.addWidget(self.webEngineView, 0, 1, 5, 1)  # row, column, row_span, column_span
        #self.webEngineView.load(QUrl("http://localhost/kookminMap/map.html"))
        self.webEngineView.load(QUrl("https://2wodnjs7.github.io/web1/"))
        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 1)
        grid.setRowStretch(2, 16)
        grid.setRowStretch(3, 1)
        grid.setRowStretch(4, 1)
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
        self.lbox.clear()
        text = self.query.text()
        x, y, self.locales = SearchLocale(text, food)
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
        fH = open(self.dbfilename, 'wb')
        row = self.lbox.currentRow()
        self.restaurantDB.append([food, self.locales[row].place_name, self.locales[row].address_name, self.locales[row].place_url])
        pickle.dump(self.restaurantDB, fH)
        fH.close()

    def BookmarkMove(self):
        #fH = open(self.dbfilename, 'rb')
        #a = pickle.load(fH)
        #print(a)
        #fH.close()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def Move(self, x, y):
        page = self.webEngineView.page()
        script = str.format("setMyCenter({0},{1});", y, x)
        page = page.runJavaScript(script)