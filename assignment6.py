import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        #첫번째박스에 사용할 객체 생성
        name = QLabel("Name:", self)
        age = QLabel("Age:",self)
        score = QLabel("Score:",self)
        self.nametext = QLineEdit()
        self.agetext = QLineEdit()
        self.scoretext = QLineEdit()
        #첫번째 QHBox Layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(name)
        hbox1.addWidget(self.nametext)
        hbox1.addWidget(age)
        hbox1.addWidget(self.agetext)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoretext)
        #두번째 박스에 사용할 객체 생성
        amount = QLabel("Amount:",self)
        key = QLabel("Key:",self)
        self.amounttext = QLineEdit()
        self.keycombo = QComboBox()
        self.keycombo.addItems(["Name","Age","Score"])
        #두번째 QHBox Layout
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amounttext)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keycombo)
        #세번째 박스에 사용할 객체 생성
        add = QPushButton("Add",self)
        delB = QPushButton("Del",self)
        find = QPushButton("Find",self)
        inc = QPushButton("Inc",self)
        show = QPushButton("Show",self)
        #세번째 박스 레이아웃
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(add)
        hbox3.addWidget(delB)
        hbox3.addWidget(find)
        hbox3.addWidget(inc)
        hbox3.addWidget(show)
        #네번째 박스에 사용할 객체 생성
        result = QLabel("Result:",self)
        #네번째 박스 레이아웃
        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)
        #다섯번째 박스에 사용할 객체 생성
        self.Resulttext = QTextEdit()
        #다섯번째 박스 레이아웃
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.Resulttext)
        #QVBox에 QHBox넣기
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)
        #버튼을 눌렀을때 반응하게 만들기
        add.clicked.connect(self.ButtonClick)
        delB.clicked.connect(self.ButtonClick)
        find.clicked.connect(self.ButtonClick)
        inc.clicked.connect(self.ButtonClick)
        show.clicked.connect(self.ButtonClick)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    #버튼을 눌렀을때 동작하게 만듬
    def ButtonClick(self):
        sender = self.sender()

        if (sender.text() == "Add"):
            record = {'Name': self.nametext.text(), 'Age': int(self.agetext.text()), 'Score': int(self.scoretext.text())}
            self.scoredb +=[record]
            self.showScoreDB()

        elif (sender.text() == "Del"):
            for p in self.scoredb:
                if p['Name'] == self.nametext.text():
                    self.scoredb.remove(p)
                    if p['Name'] == self.nametext.text():
                        self.scoredb.remove(p)
            self.showScoreDB()

        elif (sender.text() == "Find"):
            for p in self.scoredb:
                if p['Name'] != self.nametext.text():
                    self.scoredb.remove(p)
            self.showScoreDB()


        elif (sender.text() == "Inc"):
            for p in self.scoredb:
                if p['Name'] == self.nametext.text():
                    num = p['Score']
                    num += int(self.amounttext.text())
                    p['Score'] = num
            self.showScoreDB()

        elif (sender.text() == "Show"):
            self.showScoreDB(self.keycombo.currentText())







    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')

        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
            for p in self.scoredb:
                p['Score'] = int(p['Score'])
                p['Age'] = int(p['Age'])
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname = "Score"):
        Resultlist = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                Resultlist += attr + "=" + str(p[attr]) + " "
            Resultlist += "\n"
            self.Resulttext.setText(Resultlist)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
