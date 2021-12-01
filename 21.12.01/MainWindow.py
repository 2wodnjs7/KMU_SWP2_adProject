import sys
from SurveyWindow1 import *
from SurveyWindow2 import *
from RecommendWindow import *
from LSMainWindow import *
from BookMark import *

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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QStackedWidget()

    mainWindow = MainWindow()
    surveyWindow1 = SurveyWindow1(widget)
    surveyWindow2 = SurveyWindow2(widget)
    recommendWindow = RecommendWindow(widget)
    lSMainWindow = LSMainWindow(widget)
    bookMark = BookMark(widget)

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