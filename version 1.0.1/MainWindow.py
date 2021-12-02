import sys
from SurveyWindow1 import *
from SurveyWindow2 import *
from RecommendWindow import *
from LSMainWindow import *
from BookmarkWindow import *


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('음식 추천')
        self.resize(1080, 640)

        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(234, 234, 234))
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)

        self.aLabel = QLabel('    오늘은\n        뭐 먹지', self)
        self.aLabel.setMaximumHeight(300)
        self.aLabel.setStyleSheet("color:#252A34;font-size:130px;font-family:NanumBarunGothic;")
        self.aLabel.setAlignment(Qt.AlignVCenter)

        self.bLabel = QLabel('Version 1.0.0', self)
        self.bLabel.setMaximumHeight(15)
        self.bLabel.setStyleSheet("color:#252A34;font-size:15px;font-family:NanumBarunGothic;")
        self.bLabel.setAlignment(Qt.AlignTop)
        self.bLabel.setAlignment(Qt.AlignHCenter)

        self.bmbtn = QPushButton()
        self.bmbtn.setText('음식점 즐겨찾기')
        self.bmbtn.setMaximumHeight(100)
        self.bmbtn.setMaximumWidth(300)
        self.bmbtn.setStyleSheet("color:#EAEAEA;background-color: #FF2E63;font-weight:bold;font-size:30px;font-family:NanumBarunGothic;")

        self.rcmdbtn = QPushButton()
        self.rcmdbtn.setText('음식 추천받기')
        self.rcmdbtn.setMaximumHeight(100)
        self.rcmdbtn.setMaximumWidth(300)
        self.rcmdbtn.setStyleSheet("color:#EAEAEA;background-color: #FF2E63;font-weight:bold;font-size:30px;font-family:NanumBarunGothic;")

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.aLabel, 0, 0, 1, 2)
        mainLayout.addWidget(self.bLabel, 1, 0, 1, 2)
        mainLayout.addWidget(self.bmbtn, 2, 0)
        mainLayout.addWidget(self.rcmdbtn, 2, 1)

        self.setLayout(mainLayout)

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