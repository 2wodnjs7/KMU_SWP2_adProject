from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import QLabel
from PyQt5.Qt import QComboBox


class SurveyWindow1(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setWindowTitle('성격조사')
        self.surveyfilename1 = 'surveyAnswer1.txt'

        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(227, 253, 253))
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)

        self.questionLabel1 = QLabel('먹고 싶은 음식 종류   ', self)
        self.questionLabel1.setAlignment(Qt.AlignRight)
        self.questionLabel1.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit1 = QComboBox(self)
        self.answerEdit1.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit1.addItem('밥')
        self.answerEdit1.addItem('면')
        self.answerEdit1.addItem('국, 탕, 찌개')
        self.answerEdit1.addItem('육류')
        self.answerEdit1.addItem('야채')
        self.answerEdit1.addItem('패스트푸드')

        self.questionLabel2 = QLabel('떡볶이를 드실 때 어떻게 드시나요?   ', self)
        self.questionLabel2.setAlignment(Qt.AlignRight)
        self.questionLabel2.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit2 = QComboBox(self)
        self.answerEdit2.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit2.addItem('집에서 배달시켜 먹는다.')
        self.answerEdit2.addItem('직접 나가서 먹는다.')

        self.questionLabel3 = QLabel('나는 음식을   ', self)
        self.questionLabel3.setAlignment(Qt.AlignRight)
        self.questionLabel3.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit3 = QComboBox(self)
        self.answerEdit3.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit3.addItem('넉넉하게 먹는다.')
        self.answerEdit3.addItem('딱 맞게 먹는다.')
        self.answerEdit3.addItem('모자라게 먹는다.')

        self.questionLabel4 = QLabel('나는 먹을 음식을 정할 때   ', self)
        self.questionLabel4.setAlignment(Qt.AlignRight)
        self.questionLabel4.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit4 = QComboBox(self)
        self.answerEdit4.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit4.addItem('계획적이다.')
        self.answerEdit4.addItem('잘 모르겠다.')
        self.answerEdit4.addItem('즉흥적이다.')

        self.questionLabel5 = QLabel('나는 음식을   ', self)
        self.questionLabel5.setAlignment(Qt.AlignRight)
        self.questionLabel5.setStyleSheet("font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit5 = QComboBox(self)
        self.answerEdit5.setStyleSheet("background-color: #A6E3E9;font-size:24px;font-family:NanumBarunGothic;")
        self.answerEdit5.addItem('혼자서 먹는 것을 즐긴다.')
        self.answerEdit5.addItem('친구랑 같이 먹는 것을 즐긴다.')

        self.prevButton1 = QPushButton()
        self.prevButton1.setText('이전')
        self.prevButton1.setMaximumHeight(40)
        self.prevButton1.setMaximumWidth(200)
        self.prevButton1.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")

        self.nextButton1 = QPushButton()
        self.nextButton1.setText('다음')
        self.nextButton1.setMaximumHeight(40)
        self.nextButton1.setMaximumWidth(200)
        self.nextButton1.setStyleSheet("background-color: #71C9CE;font-size:20px;font-family:NanumBarunGothic;")

        mainHbox = QVBoxLayout()
        rowVbox1 = QHBoxLayout()
        rowVbox2 = QHBoxLayout()
        rowVbox3 = QHBoxLayout()
        rowVbox4 = QHBoxLayout()
        rowVbox5 = QHBoxLayout()
        rowVbox6 = QHBoxLayout()

        rowVbox1.addWidget(self.questionLabel1)
        rowVbox1.addWidget(self.answerEdit1)
        rowVbox2.addWidget(self.questionLabel2)
        rowVbox2.addWidget(self.answerEdit2)
        rowVbox3.addWidget(self.questionLabel3)
        rowVbox3.addWidget(self.answerEdit3)
        rowVbox4.addWidget(self.questionLabel4)
        rowVbox4.addWidget(self.answerEdit4)
        rowVbox5.addWidget(self.questionLabel5)
        rowVbox5.addWidget(self.answerEdit5)
        rowVbox6.addWidget(self.prevButton1)
        rowVbox6.addWidget(self.nextButton1)

        mainHbox.addLayout(rowVbox1)
        mainHbox.addLayout(rowVbox2)
        mainHbox.addLayout(rowVbox3)
        mainHbox.addLayout(rowVbox4)
        mainHbox.addLayout(rowVbox5)
        mainHbox.addLayout(rowVbox6)

        self.setLayout(mainHbox)

        self.prevButton1.clicked.connect(self.prevButtonClicked)
        self.nextButton1.clicked.connect(self.nextButtonClicked)

    def prevButtonClicked(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
    def nextButtonClicked(self):
        f = open("surveyAnswer1.txt", 'w')
        f.write(str(self.answerEdit1.currentIndex() + 1)+' ')
        f.write(str(self.answerEdit2.currentIndex() + 1)+' ')
        f.write(str(self.answerEdit3.currentIndex() + 1)+' ')
        f.write(str(self.answerEdit4.currentIndex() + 1)+' ')
        f.write(str(self.answerEdit5.currentIndex() + 1)+' ')
        f.close()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)