from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
import random

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("main.ui")

        self.game = [[None for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setStyleSheet('font-size: 24px')
                tb.setStyleSheet(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.ui.sgrid.addWidget(tb, i, j)

        self.ui.show()

        self.ui.btn_newgame.clicked.connect(self.newgame)
        self.ui.btn_checkgame.clicked.connect(self.check)

    def check(self):
        # check rows
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j] and self.game[row][i] != self.game[row][j] and self.game[row][i].text() != " ":
                        self.game[row][i].setStylesheet('font: 24px; background-color: pink')

        # check columns
        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col] and self.game[i][col] != self.game[j][col] and self.game[i][col].text() != " ":
                        self.game[i][col].setStylesheet('font: 24px; background-color: pink')

    def newgame(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText(" ")
        r = random.randint(1,6)
        file_path = f"data/s{r}.txt"
        print(file_path)

        f = open(file_path, "r")
        teexxt = f.read()
        rows = teexxt.split("\n")

        for i in range(9) :
            numbers = rows[i].split(" ")
            for j in range(9):
                if numbers[j] != 0:
                    self.game[i][j].setStyleSheet('font-size: 24px')
                    self.game[i][j].setText(numbers[j])

                else:
                    self.game[i][j].setStyleSheet('font-size: 24px; color:lightblue')






app = QApplication([])
window = Mainwindow()
app.exec()