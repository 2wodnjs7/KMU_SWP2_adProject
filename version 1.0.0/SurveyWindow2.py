from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import QLabel
from PyQt5.Qt import QComboBox


class SurveyWindow2(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setWindowTitle('성격조사')
        self.survey1filename = 'surveyAnswer2.txt'

        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(227, 253, 253))
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)

        self.questionLabel6 = QLabel('나는 요즘 잠을 ', self)
        self.questionLabel6.setAlignment(Qt.AlignRight)
        self.questionLabel6.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit6 = QComboBox(self)
        self.answerEdit6.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit6.addItem('많이 잔다.')
        self.answerEdit6.addItem('적당히 잔다.')
        self.answerEdit6.addItem('부족하게 잔다.')

        self.questionLabel7 = QLabel('나는 지금 ', self)
        self.questionLabel7.setAlignment(Qt.AlignRight)
        self.questionLabel7.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit7 = QComboBox(self)
        self.answerEdit7.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit7.addItem('화가 난다.')
        self.answerEdit7.addItem('기쁘다.')
        self.answerEdit7.addItem('우울하다.')
        self.answerEdit7.addItem('그저 그렇다.')

        self.questionLabel8 = QLabel('오늘따라 힘이 없고 무기력하다.', self)
        self.questionLabel8.setAlignment(Qt.AlignRight)
        self.questionLabel8.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit8 = QComboBox(self)
        self.answerEdit8.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit8.addItem('yes')
        self.answerEdit8.addItem('no')

        self.questionLabel9 = QLabel('나는 요즘 자주 체하거나 소화가 잘 안된다.', self)
        self.questionLabel9.setAlignment(Qt.AlignRight)
        self.questionLabel9.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit9 = QComboBox(self)
        self.answerEdit9.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit9.addItem('yes')
        self.answerEdit9.addItem('no')

        self.questionLabel10 = QLabel('지금 시간대는 ', self)
        self.questionLabel10.setAlignment(Qt.AlignRight)
        self.questionLabel10.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit10 = QComboBox(self)
        self.answerEdit10.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit10.addItem('아침')
        self.answerEdit10.addItem('낮')
        self.answerEdit10.addItem('저녁')
        self.answerEdit10.addItem('밤')

        self.prevButton2 = QPushButton()
        self.prevButton2.setText('이전')
        self.prevButton2.setMaximumHeight(40)
        self.prevButton2.setMaximumWidth(200)
        self.prevButton2.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")

        self.nextButton2 = QPushButton()
        self.nextButton2.setText('다음')
        self.nextButton2.setMaximumHeight(40)
        self.nextButton2.setMaximumWidth(200)
        self.nextButton2.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")

        mainHbox = QVBoxLayout()
        rowVbox1 = QHBoxLayout()
        rowVbox2 = QHBoxLayout()
        rowVbox3 = QHBoxLayout()
        rowVbox4 = QHBoxLayout()
        rowVbox5 = QHBoxLayout()
        rowVbox6 = QHBoxLayout()

        rowVbox1.addWidget(self.questionLabel6)
        rowVbox1.addWidget(self.answerEdit6)
        rowVbox2.addWidget(self.questionLabel7)
        rowVbox2.addWidget(self.answerEdit7)
        rowVbox3.addWidget(self.questionLabel8)
        rowVbox3.addWidget(self.answerEdit8)
        rowVbox4.addWidget(self.questionLabel9)
        rowVbox4.addWidget(self.answerEdit9)
        rowVbox5.addWidget(self.questionLabel10)
        rowVbox5.addWidget(self.answerEdit10)
        rowVbox6.addWidget(self.prevButton2)
        rowVbox6.addWidget(self.nextButton2)

        mainHbox.addLayout(rowVbox1)
        mainHbox.addLayout(rowVbox2)
        mainHbox.addLayout(rowVbox3)
        mainHbox.addLayout(rowVbox4)
        mainHbox.addLayout(rowVbox5)
        mainHbox.addLayout(rowVbox6)

        self.setLayout(mainHbox)

        self.prevButton2.clicked.connect(self.prevButtonClicked)
        self.nextButton2.clicked.connect(self.nextButtonClicked)

    def prevButtonClicked(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def nextButtonClicked(self):
        f = open("surveyAnswer1.txt", 'a')
        f.write(str(self.answerEdit6.currentIndex() + 1)+' ')
        f.write(str(self.answerEdit7.currentIndex() + 1)+' ')
        f.write(str(self.answerEdit8.currentIndex() + 1)+' ')
        f.write(str(self.answerEdit9.currentIndex() + 1)+' ')
        f.write(str(self.answerEdit10.currentIndex() + 1))
        f.close()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)