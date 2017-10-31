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
        print(self.scoredb)
        
        
    def initUI(self):

        label1 = QLabel('Name: ', self)
        label1.move(15, 10)
        label2 = QLabel('Age: ', self)
        label2.move(215, 10)
        label3 = QLabel('Score: ', self)
        label3.move(415, 10)
        label4 = QLabel('Amount: ', self)
        label4.move(245, 45)
        label5 = QLabel('Key: ', self)
        label5.move(515, 45)
        label6 = QLabel('Result: ', self)
        label6.move(15, 150)

        AddButton = QPushButton("Add", self)
        AddButton.clicked.connect(self.doScoreDB())
        DelButton = QPushButton("Del", self)
        FindButton = QPushButton("Find", self)
        IncButton = QPushButton("Inc", self)
        ShowButton = QPushButton("Show", self)

        hbox = QHBoxLayout(self)
        hbox.addStretch(2)
        hbox.addWidget(AddButton)
        hbox.addWidget(DelButton)
        hbox.addWidget(FindButton)
        hbox.addWidget(IncButton)
        hbox.addWidget(ShowButton)

        lineName = QLineEdit(self)
        lineName.move(80, 10)
        lineAge = QLineEdit(self)
        lineAge.move(264, 10)
        lineScore = QLineEdit(self)
        lineScore.move(480, 10)
        lineAmount = QLineEdit(self)
        lineAmount.move(325, 45)
        lineAge.text(). = special
        print(special)
        result = QTextEdit(self)
        result.setOverwriteMode(True)
        result.setReadOnly(True)
        result.setGeometry(10, 185, 400, 100)

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
            self.scoredb =  pickle.load(fH)
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

    # def doScoreDB(self):
    #    while (True):
     #       parse1 =
      #      parse2 = lineAge(self)
       #     parse3 = lineScore(self)
        #    try:
         #       record = {'Name': parse1, 'Age': parse2, 'Score': parse3}
          #      self.scoredb += [record]
           #     print(self.scoredb)
            #except:
             #    continue
#
    def showScoreDB(self):
        pass


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





