from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QComboBox, QMessageBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.Qt import QLabel
from foodDB import foods


class RecommendWindow(QWidget):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setWindowTitle('추천된 음식')

        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(234, 234, 234))
        self.setAutoFillBackground(True)
        self.setPalette(self.pal)

        self.rcmdLabel1 = QLabel('', self)
        self.rcmdLabel1.setMaximumHeight(245)
        self.rcmdLabel1.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.rcmdLabel1.setStyleSheet("font-size:75px;font-family:NanumBarunGothic;")

        self.rcmdLabel2 = QLabel('', self)
        self.rcmdLabel2.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.rcmdLabel2.setMaximumHeight(385)
        self.rcmdLabel2.setStyleSheet("font-size:75px;font-family:NanumBarunGothic;")

        self.rcmdLabel3 = QLabel('', self)
        self.rcmdLabel3.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.rcmdLabel3.setMaximumHeight(450)
        self.rcmdLabel3.setStyleSheet("font-size:75px;font-family:NanumBarunGothic;")

        self.rcmdLabel1_1 = QLabel('1st', self)
        self.rcmdLabel1_1.setMaximumHeight(365)
        self.rcmdLabel1_1.setAlignment(Qt.AlignHCenter)
        self.rcmdLabel1_1.setStyleSheet("font-size:50px;border-width:5px;border-style:solid solid none solid;border-color:#FF2E63;")

        self.rcmdLabel2_1 = QLabel('2nd', self)
        self.rcmdLabel2_1.setMaximumHeight(225)
        self.rcmdLabel2_1.setAlignment(Qt.AlignHCenter)
        self.rcmdLabel2_1.setStyleSheet("font-size:50px;border-width:5px;border-style:solid solid none solid;border-color:#FF2E63;")

        self.rcmdLabel3_1 = QLabel('3rd', self)
        self.rcmdLabel3_1.setMaximumHeight(160)
        self.rcmdLabel3_1.setAlignment(Qt.AlignHCenter)
        self.rcmdLabel3_1.setStyleSheet("font-size:50px;border-width:5px;border-style:solid solid none solid;border-color:#FF2E63;")

        self.firstButton = QPushButton()
        self.firstButton.setMaximumHeight(50)
        self.firstButton.setStyleSheet("color:#EAEAEA;background-color:#FF2E63;font-weight:bold;font-size:24px;font-family:NanumBarunGothic;")
        self.firstButton.setText('첫 화면 가기')

        self.foodRecommendButton = QPushButton()

        self.foodRecommendButton.setMaximumHeight(50)
        self.foodRecommendButton.setStyleSheet("color:#EAEAEA;background-color:#FF2E63;font-weight:bold;font-size:24px;font-family:NanumBarunGothic;")
        self.foodRecommendButton.setText('결과 보기')

        self.foodListCombobox = QComboBox(self)
        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)
        self.line_edit.setAlignment(Qt.AlignRight)
        self.foodListCombobox.setLineEdit(self.line_edit)
        self.foodListCombobox.setMaximumHeight(50)
        self.foodListCombobox.setStyleSheet("color:#EAEAEA;background-color:#FF2E63;font-weight:bold;font-size:24px;font-family:NanumBarunGothic;")

        self.mapButton = QPushButton()
        self.mapButton.setMaximumHeight(50)
        self.mapButton.setStyleSheet("color:#EAEAEA;background-color:#FF2E63;font-weight:bold;font-size:24px;font-family:NanumBarunGothic;")
        self.mapButton.setText('해당 음식점 검색')

        mainHbox = QVBoxLayout()
        resultVbox = QHBoxLayout()
        buttonVbox = QHBoxLayout()
        secondHbox = QVBoxLayout()
        firstHbox = QVBoxLayout()
        thirdHbox = QVBoxLayout()

        secondHbox.addWidget(self.rcmdLabel2)
        secondHbox.addWidget(self.rcmdLabel2_1)

        firstHbox.addWidget(self.rcmdLabel1)
        firstHbox.addWidget(self.rcmdLabel1_1)

        thirdHbox.addWidget(self.rcmdLabel3)
        thirdHbox.addWidget(self.rcmdLabel3_1)

        resultVbox.addLayout(secondHbox)
        resultVbox.addLayout(firstHbox)
        resultVbox.addLayout(thirdHbox)

        buttonVbox.addWidget(self.firstButton)
        buttonVbox.addWidget(self.foodRecommendButton)
        buttonVbox.addWidget(self.foodListCombobox)
        buttonVbox.addWidget(self.mapButton)

        mainHbox.addLayout(resultVbox)
        mainHbox.addLayout(buttonVbox)

        self.setLayout(mainHbox)

        self.mapButton.clicked.connect(self.mapButtonClicked)
        self.firstButton.clicked.connect(self.firstButtonClicked)
        self.foodRecommendButton.clicked.connect(self.foodRecommend)

    def firstButtonClicked(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 3)

    def foodRecommend(self):
        f = open("surveyAnswer1.txt", 'r')
        surveyList = f.read().split(' ')
        countWeight = [50, 15, 13, 12, 17, 21, 23, 14, 24, 30]
        foodSurvey_list = []

        for foodName, foodSurvey in foods.items():
            surveySum = 0
            for i in range(10):
                if str(type(foodSurvey[i])) == "<class 'list'>":
                    if int(surveyList[i]) in foodSurvey[i]:
                        surveySum += countWeight[i]
                else:
                    if int(surveyList[i]) == foodSurvey[i]:
                        surveySum += countWeight[i]
            foodSurvey_list.append((foodName, surveySum))

        foodSurvey_list_sorted = sorted(foodSurvey_list, key=lambda x: x[1], reverse=True)

        self.rcmdLabel1.setText(foodSurvey_list_sorted[0][0])
        self.rcmdLabel2.setText(foodSurvey_list_sorted[1][0])
        self.rcmdLabel3.setText(foodSurvey_list_sorted[2][0])

        self.foodListCombobox.clear()

        self.foodListCombobox.addItem(foodSurvey_list_sorted[0][0])
        self.foodListCombobox.addItem(foodSurvey_list_sorted[1][0])
        self.foodListCombobox.addItem(foodSurvey_list_sorted[2][0])

    def mapButtonClicked(self):
        if self.foodListCombobox.count() < 1:
            QMessageBox.about(self, '오류', '먼저 \'결과보기\'를 눌러 추천음식을 받아보세요.')
            return
        f = open("RecommendedFood.txt", 'w')
        f.write(self.foodListCombobox.currentText())
        f.close()
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
