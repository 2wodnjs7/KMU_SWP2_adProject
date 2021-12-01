from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import QLabel
from PyQt5.Qt import QComboBox

class SurveyWindow2(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setWindowTitle('성격조사')
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
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def nextButtonClicked(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)