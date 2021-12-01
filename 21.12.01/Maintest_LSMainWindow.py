import pickle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from LocaleSearcher import *
from PyQt5.QtCore import Qt
from BookMark import BookMark

food = '된장찌개'

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('음식 추천')

        self.resize(1080, 640)

        # Bookmark display window
        self.bmbtn = QPushButton()
        self.bmbtn.setText('Bookmark List')
        self.bmbtn.resize(300,300)

        self.rcmdbtn = QPushButton()
        self.rcmdbtn.setText('Recommend')
        self.rcmdbtn.resize(300,300)

        # Layout
        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.bmbtn)
        btnLayout.addWidget(self.rcmdbtn)
        self.setLayout(btnLayout)

        self.bmbtn.clicked.connect(self.bmbtnClicked)
        self.rcmdbtn.clicked.connect(self.rcmdClicked)

    def bmbtnClicked(self):
        widget.setCurrentIndex(widget.currentIndex() + 5)

    def rcmdClicked(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

class SurveyWindow1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('dfddfdf')
        self.resize(1080, 640)

        self.questionLabel1 = QLabel('주 재료 선택', self)
        self.answerEdit1 = QComboBox(self)
        self.answerEdit1.addItem('해산물')
        self.answerEdit1.addItem('육류')
        self.answerEdit1.addItem('국')
        self.answerEdit1.addItem('밥')
        self.answerEdit1.addItem('밀가루음식')
        self.answerEdit1.addItem('디저트')

        self.questionLabel2 = QLabel('떡볶이를 드실 때 어떻게 드시나요?', self)
        self.answerEdit2 = QComboBox(self)
        self.answerEdit2.addItem('집에서 배달시켜 먹는다')
        self.answerEdit2.addItem('직접 나가서 먹는다')

        self.questionLabel3 = QLabel('나는 음식을', self)
        self.answerEdit3 = QComboBox(self)
        self.answerEdit3.addItem('넉넉하게 먹는다')
        self.answerEdit3.addItem('딱 맞게 먹는다')
        self.answerEdit3.addItem('모자라게 먹는다')

        self.questionLabel4 = QLabel('먹을 음식을 정할 때 ', self)
        self.answerEdit4 = QComboBox(self)
        self.answerEdit4.addItem('계획적이다.')
        self.answerEdit4.addItem('잘 모르겠다.')
        self.answerEdit4.addItem('즉흥적이다.')

        self.questionLabel5 = QLabel('나는 음식을', self)
        self.answerEdit5 = QComboBox(self)
        self.answerEdit5.addItem('혼자서 먹는 것을 즐긴다.')
        self.answerEdit5.addItem('친구랑 같이 먹는 것을 즐긴다.')

        self.prevButton = QPushButton()
        self.prevButton.setText('이전')
        self.nextButton = QPushButton()
        self.nextButton.setText('다음')

        surveyLayout = QGridLayout()
        surveyLayout.addWidget(self.questionLabel1, 0, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit1, 1, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel2, 2, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit2, 3, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel3, 4, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit3, 5, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel4, 6, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit4, 7, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel5, 8, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit5, 9, 0, 1, 3)
        surveyLayout.addWidget(self.prevButton, 10, 1)
        surveyLayout.addWidget(self.nextButton, 10, 2)

        self.setLayout(surveyLayout)

        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.nextButton.clicked.connect(self.nextButtonClicked)

    def prevButtonClicked(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
    def nextButtonClicked(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)



class SurveyWindow2(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('dfddfdf')
        self.resize(1080, 640)

        self.questionLabel6 = QLabel('나는 요즘 잠을 ', self)
        self.answerEdit6 = QComboBox(self)
        self.answerEdit6.addItem('많이 잔다.')
        self.answerEdit6.addItem('적당히 잔다.')
        self.answerEdit6.addItem('부족하게 잔다.')

        self.questionLabel7 = QLabel('나는 지금 ', self)
        self.answerEdit7 = QComboBox(self)
        self.answerEdit7.addItem('화난다.')
        self.answerEdit7.addItem('기쁘다.')
        self.answerEdit7.addItem('우울하다.')
        self.answerEdit7.addItem('그저그렇다.')

        self.questionLabel8 = QLabel('오늘따라 힘이 없고 무기력하다.', self)
        self.answerEdit8 = QComboBox(self)
        self.answerEdit8.addItem('yes')
        self.answerEdit8.addItem('no')

        self.questionLabel9 = QLabel('나는 요즘 음식을 먹을 때 자주 체하거나 소화가 잘 안된다.', self)
        self.answerEdit9 = QComboBox(self)
        self.answerEdit9.addItem('yes')
        self.answerEdit9.addItem('no')

        self.questionLabel10 = QLabel('지금 시간대는 ', self)
        self.answerEdit10 = QComboBox(self)
        self.answerEdit10.addItem('아침')
        self.answerEdit10.addItem('낮')
        self.answerEdit10.addItem('오후')

        self.prevButton = QPushButton()
        self.prevButton.setText('이전')
        self.nextButton = QPushButton()
        self.nextButton.setText('다음')

        surveyLayout = QGridLayout()
        surveyLayout.addWidget(self.questionLabel6, 0, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit6, 1, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel7, 2, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit7, 3, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel8, 4, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit8, 5, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel9, 6, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit9, 7, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel10, 8, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit10, 9, 0, 1, 3)
        surveyLayout.addWidget(self.prevButton, 10, 1)
        surveyLayout.addWidget(self.nextButton, 10, 2)

        self.setLayout(surveyLayout)

        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.nextButton.clicked.connect(self.nextButtonClicked)

    def prevButtonClicked(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def nextButtonClicked(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

class RecommendWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('추천할 음식 목록')
        self.resize(1080, 640)

        self.rcmdLabel1 = QLabel('1순위', self)
        self.rcmdLabel1.setAlignment(Qt.AlignCenter)
        font1 = self.rcmdLabel1.font()
        font1.setPointSize(font1.pointSize() + 110)
        self.rcmdLabel1.setFont(font1)
        self.rcmdLabel2 = QLabel('2순위', self)
        self.rcmdLabel2.setAlignment(Qt.AlignCenter)
        font2 = self.rcmdLabel2.font()
        font2.setPointSize(font2.pointSize() + 65)
        self.rcmdLabel2.setFont(font2)
        self.rcmdLabel3 = QLabel('3순위', self)
        self.rcmdLabel3.setAlignment(Qt.AlignCenter)
        font3 = self.rcmdLabel3.font()
        font3.setPointSize(font3.pointSize() + 50)
        self.rcmdLabel3.setFont(font3)


        self.exitButton = QPushButton()
        self.exitButton.setText('끌래요:(')
        self.mapButton = QPushButton()
        self.mapButton.setText('지도 볼래요:)')

        self.exitButton.setMaximumHeight(100)
        self.mapButton.setMaximumHeight(100)

        rcmdLayout = QGridLayout()
        rcmdLayout.addWidget(self.rcmdLabel1, 0, 2, 1, 2)
        rcmdLayout.addWidget(self.rcmdLabel2, 0, 0, 1, 2)
        rcmdLayout.addWidget(self.rcmdLabel3, 0, 4, 1, 2)

        rcmdLayout.addWidget(self.exitButton, 1,2)
        rcmdLayout.addWidget(self.mapButton, 1,3)
        self.space = QLabel('', self)
        rcmdLayout.addWidget(self.space, 2, 0)
        rcmdLayout.setRowStretch(0,5)
        rcmdLayout.setRowStretch(1,5)
        rcmdLayout.setRowStretch(2,1)

        self.mapButton.clicked.connect(self.mapButtonClicked)
        self.setLayout(rcmdLayout)

    def mapButtonClicked(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LSMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []
        self.ReadRestaurantDB()

        self.resize(1080, 640)
        self.widget = QWidget()  # QGridLayout개체를 배치할 Widget 개체 생성
        self.setCentralWidget(self.widget)  # LSMainWindow의 CentralWidget 설정
        self.grid = QGridLayout(self.widget)  # QGridLayout 개체 생성

        self.setWindowTitle('내 거주지 주변 음식점 검색')  # 윈도우 타이틀
        self.query = QLineEdit()
        self.query.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.query, 0, 0)
        self.btnSearch = QPushButton()
        self.btnSearch.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnSearch, 1, 0)
        self.btnSearch.setText("내 거주지 입력 및 검색")

        self.lbox = QListWidget()
        self.grid.addWidget(self.lbox, 2, 0)  # row, column, row_span, column_span

        self.btnSave = QPushButton()
        self.btnSave.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnSave, 3, 0)
        self.btnSave.setText("해당 음식점 저장")

        self.btnBookmark = QPushButton()
        self.btnBookmark.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnBookmark, 4, 0)
        self.btnBookmark.setText("즐겨찾기 보기")

        self.webEngineView = QWebEngineView()
        self.grid.addWidget(self.webEngineView, 0, 1, 5, 1)  # row, column, row_span, column_span
        #self.webEngineView.load(QUrl("http://localhost/kookminMap/map.html"))
        self.webEngineView.load(QUrl("https://2wodnjs7.github.io/web1/"))
        self.grid.setRowStretch(0, 1)
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 16)
        self.grid.setRowStretch(3, 1)
        self.grid.setRowStretch(4, 1)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 4)

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
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Move(self, x, y):
        page = self.webEngineView.page()
        script = str.format("setMyCenter({0},{1});", y, x)
        page = page.runJavaScript(script)


class BookMark(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []

        self.resize(1080, 640)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.grid = QGridLayout(self.widget)

        self.lbox = QListWidget()
        self.grid.addWidget(self.lbox, 0, 0, 1, 3)

        self.btnDelete = QPushButton()
        self.btnDelete.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnDelete, 1, 2)
        self.btnDelete.setText("해당 음식점 삭제")

        self.btn = QPushButton()
        self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 1, 0)
        self.btn.setText("지도 이동")

        self.btnPrint = QPushButton()
        self.btnPrint.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnPrint, 1, 1)
        self.btnPrint.setText("즐겨찾기 출력")

        self.grid.setRowStretch(0, 10)
        self.grid.setRowStretch(1, 1)
        self.grid.setColumnStretch(0, 4)
        self.grid.setColumnStretch(1, 1)

        self.setLayout(self.grid)

        self.btnPrint.clicked.connect(self.showBookmarkDB)
        self.btn.clicked.connect(self.go)
        self.btnDelete.clicked.connect(self.delBookmarkDB)

        self.readBookmarkDB()
        self.showBookmarkDB()
        self.show()

    def go(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QStackedWidget()

    mainWindow = MainWindow()
    surveyWindow1 = SurveyWindow1()
    surveyWindow2 = SurveyWindow2()
    recommendWindow = RecommendWindow()
    lSMainWindow = LSMainWindow()
    bookMark = BookMark()

    widget.addWidget(mainWindow)
    widget.addWidget(surveyWindow1)
    widget.addWidget(surveyWindow2)
    widget.addWidget(recommendWindow)
    widget.addWidget(lSMainWindow)
    widget.addWidget(bookMark)

    widget.setFixedHeight(640)
    widget.setFixedWidth(1080)
    widget.show()

    app.exec_()