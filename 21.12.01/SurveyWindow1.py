from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import QLabel
from PyQt5.Qt import QComboBox

class SurveyWindow1(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setWindowTitle('성격조사')

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
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
    def nextButtonClicked(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)