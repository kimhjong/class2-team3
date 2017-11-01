import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,QHBoxLayout,
                              QVBoxLayout, QApplication, QLabel,
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

        Name = QLabel('Name: ', self)
        Age = QLabel('Age: ', self)
        Score = QLabel('Score: ', self)
        Amount = QLabel('Amount: ', self)
        Key = QLabel('Key: ', self)
        Result = QLabel('Result: ', self)

        self.lineName = QLineEdit()
        self.lineAge = QLineEdit()
        self.lineScore = QLineEdit()
        self.lineAmount = QLineEdit()

        Addbtn = QPushButton("Add", self)
        Delbtn = QPushButton("Del", self)
        Findbtn = QPushButton("Find", self)
        Incbtn = QPushButton("Inc", self)
        Showbtn = QPushButton("Show", self)

        self.key = QComboBox()
        self.key.addItems(["Name", "Age", "Score"])

        self.Result = QTextEdit()

        Addbtn.clicked.connect(self.AddButton)
        Delbtn.clicked.connect(self.DelButton)
        Findbtn.clicked.connect(self.FindButton)
        Incbtn.clicked.connect(self.IncButton)
        Showbtn.clicked.connect(self.ShowButton)

        hb1 = QHBoxLayout()
        hb1.addWidget(Name)
        hb1.addWidget(self.lineName)
        hb1.addWidget(Age)
        hb1.addWidget(self.lineAge)
        hb1.addWidget(Score)
        hb1.addWidget(self.lineScore)

        hb2 = QHBoxLayout()
        hb2.addWidget(Amount)
        hb2.addWidget(self.lineAmount)
        hb2.addWidget(Key)
        hb2.addWidget(self.key)

        hb3 = QHBoxLayout()
        hb3.addWidget(Addbtn)
        hb3.addWidget(Delbtn)
        hb3.addWidget(Findbtn)
        hb3.addWidget(Incbtn)
        hb3.addWidget(Showbtn)

        hb4 = QHBoxLayout()
        hb4.addWidget(Result)

        hb5 = QHBoxLayout()
        hb5.addWidget(self.Result)

        vb = QVBoxLayout()
        vb.addLayout(hb1)
        vb.addLayout(hb2)
        vb.addLayout(hb3)
        vb.addLayout(hb4)
        vb.addLayout(hb5)

        self.setLayout(vb)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

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
        fH.close()

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def AddButton(self):
        sender = self.sender()
        if (sender.text() == "Add"):
            record = {"Name": self.lineName.text(), "Age": int(self.lineAge.text()), "Score": int(self.lineScore.text())}
            self.scoredb = self.scoredb + record
            self.showScoreDB()

    def DelButton(self):
        sender = self.sender()
        if (sender.text() == "Del"):
            for p in self.scoredb:
                if p['Name'] == self.lineName.text():
                    self.scoredb.remove(p)
            self.showScoreDB()

    def FindButton(self):
        sender = self.sender()
        result = ""
        if (sender.text() == "Find"):
            for p in self.scoredb:
                if p['Name'] == self.lineName.text():
                    result = result + "Name = " + p['Name'] + "Score = " + p['Score'] + "Age = " + p['Age']
                result = result + "\n"
            self.Result.setText(result)

    def IncButton(self):
        sender = self.sender()
        if (sender.text() == "Inc"):
            for p in self.scoredb:
                if p['Name'] == self.lineName.text():
                    amount = p['Amount']
                    amount = amount + int(self.lineAmount.text())
                    p['Score'] = amount
            self.showScoreDB()

    def ShowButton(self):
        sender = self.sender()
        if (sender.text() == "Show"):
            self.showScoreDB(self.key.currentText())

    def showScoreDB(self, keyname = "Name"):
        list = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                list = list + attr + "=" + str(p[attr]) + "  "
            list = list + "\n"
            self.Result.setText(list)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
