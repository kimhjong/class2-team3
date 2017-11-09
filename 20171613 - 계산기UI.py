from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
import math

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        
        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]
        # 줄인 거
        for i in range(0, 10):
            self.digitButton[i] = Button(str(i), self.buttonClicked)
        # 줄이기 전
        #self.digitButton[0] = Button('0', self.buttonClicked)
        #self.digitButton[1] = Button('1', self.buttonClicked)
        #self.digitButton[2] = Button('2', self.buttonClicked)
        #self.digitButton[3] = Button('3', self.buttonClicked)
        #self.digitButton[4] = Button('4', self.buttonClicked)
        #self.digitButton[5] = Button('5', self.buttonClicked)
        #self.digitButton[6] = Button('6', self.buttonClicked)
        #self.digitButton[7] = Button('7', self.buttonClicked)
        #self.digitButton[8] = Button('8', self.buttonClicked)
        #self.digitButton[9] = Button('9', self.buttonClicked)
        
        # . and = Buttons
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*', self.buttonClicked)
        self.divButton = Button('/', self.buttonClicked)
        self.addButton = Button('+', self.buttonClicked)
        self.subButton = Button('-', self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.buttonClicked)
        self.rparButton = Button(')', self.buttonClicked)

        # Clear Button
        self.clearButton = Button('C', self.buttonClicked)

        self.piButton = Button('pi', self.buttonClicked)
        self.lightButton = Button('빛의 이동 속도 (m/s)', self.buttonClicked)
        self.soundButton = Button('소리의 이동 속도 (m/s)', self.buttonClicked)
        self.disButton = Button('태양과의 평균 거리 (km)', self.buttonClicked)

        self.facButton = Button('factorial(!)', self.buttonClicked)
        self.tobinButton = Button('-> binary', self.buttonClicked)
        self.todecButton = Button('binary -> dec', self.buttonClicked)
        self.toromButton = Button('-> roman', self.buttonClicked)
        self.romtodecButton = Button('roman -> dec', self.buttonClicked)


        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        # 줄인 거
        for i in range(1, 10):
            numLayout.addWidget(self.digitButton[i], (9-i) / 3, (i+2) % 3)
        numLayout.addWidget(self.digitButton[0], 3, 0)
        # 줄이기 전
        #numLayout.addWidget(self.digitButton[1], 2, 0)
        #numLayout.addWidget(self.digitButton[2], 2, 1)
        #numLayout.addWidget(self.digitButton[3], 2, 2)
        #numLayout.addWidget(self.digitButton[4], 1, 0)
        #numLayout.addWidget(self.digitButton[5], 1, 1)
        #numLayout.addWidget(self.digitButton[6], 1, 2)
        #numLayout.addWidget(self.digitButton[7], 0, 0)
        #numLayout.addWidget(self.digitButton[8], 0, 1)
        #numLayout.addWidget(self.digitButton[9], 0, 2)

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)
        
        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        plusLayout = QGridLayout()

        plusLayout.addWidget(self.piButton, 0, 0)
        plusLayout.addWidget(self.lightButton, 1, 0)
        plusLayout.addWidget(self.soundButton, 2, 0)
        plusLayout.addWidget(self.disButton, 3, 0)
        
        mainLayout.addLayout(plusLayout, 2, 0)

        ppLayout = QGridLayout()
        ppLayout.addWidget(self.facButton, 0, 0)
        ppLayout.addWidget(self.tobinButton, 1, 0)
        ppLayout.addWidget(self.todecButton, 2, 0)
        ppLayout.addWidget(self.toromButton, 3, 0)
        ppLayout.addWidget(self.romtodecButton, 4, 0)

        mainLayout.addLayout(ppLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
