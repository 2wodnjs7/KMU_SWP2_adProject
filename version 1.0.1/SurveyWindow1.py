from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import QLabel
from PyQt5.Qt import QComboBox
from SurveyDB import SurveyQusAns1


class SurveyWindow1(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setWindowTitle('성격조사')

        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(234, 234, 234))
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)

        self.questionLabel = [x for x in range(0, 5)]
        self.answerEdit = [x for x in range(0, 5)]

        for i in range(5):
            self.questionLabel[i] = QLabel(SurveyQusAns1[i][0], self)
            self.questionLabel[i].setAlignment(Qt.AlignRight)
            self.questionLabel[i].setStyleSheet("color:#252A34;font-size:24px;font-family:NanumBarunGothic;")
            self.answerEdit[i] = QComboBox(self)
            self.answerEdit[i].setStyleSheet("color:#252A34;background-color: #FFD5DF;font-size:24px;font-family:NanumBarunGothic;")
            for j in SurveyQusAns1[i][1]:
                self.answerEdit[i].addItem(j)

        self.prevButton1 = QPushButton()
        self.prevButton1.setText('이전')
        self.prevButton1.setMaximumHeight(60)
        self.prevButton1.setMaximumWidth(250)
        self.prevButton1.setStyleSheet("color:#EAEAEA;background-color:#FF2E63;font-weight:bold;font-size:24px;font-family:NanumBarunGothic;")

        self.nextButton1 = QPushButton()
        self.nextButton1.setText('다음')
        self.nextButton1.setMaximumHeight(60)
        self.nextButton1.setMaximumWidth(250)
        self.nextButton1.setStyleSheet("color:#EAEAEA;background-color:#FF2E63;font-weight:bold;font-size:24px;font-family:NanumBarunGothic;")

        mainHbox = QVBoxLayout()

        rowVbox = [x for x in range(0, 6)]

        for i in range(5):
            rowVbox[i] = QHBoxLayout()
            rowVbox[i].addWidget(self.questionLabel[i])
            rowVbox[i].addWidget(self.answerEdit[i])
            mainHbox.addLayout(rowVbox[i])

        rowVbox[5] = QHBoxLayout()
        rowVbox[5].addWidget(self.prevButton1)
        rowVbox[5].addWidget(self.nextButton1)
        mainHbox.addLayout(rowVbox[5])

        self.setLayout(mainHbox)

        self.prevButton1.clicked.connect(self.prevButtonClicked)
        self.nextButton1.clicked.connect(self.nextButtonClicked)

    def prevButtonClicked(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def nextButtonClicked(self):
        f = open("surveyAnswer1.txt", 'w')
        for i in range(5):
            f.write(str(self.answerEdit[i].currentIndex() + 1) + ' ')
        f.close()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)