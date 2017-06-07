import re
from random import randint
import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox, QDesktopWidget, QLineEdit, QLabel, \
    QTextEdit
from PyQt5.QtGui import QIcon

FILE_NAME = 'static/ochrona-QA.tex'


def find_questions():
    result = []
    file = open(FILE_NAME, 'r')
    string = file.read()
    file.close()
    lines = re.split("\r?\n", string)
    reobj_q = re.compile('\A\\\question')
    for line in lines[:]:
       if reobj_q.search(line):
            result.append(re.sub('\A\\\question', '', line))
    return result


def random_question():
    questions = find_questions()
    number = len(questions)
    rand_number = randint(0, number)
    return (questions[rand_number])


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(500, 300)
        self.move(300, 300)
        self.setWindowTitle('Random Ochrona Danych')
        button = QPushButton("Losuj Pytanie", self)
        button.move(200, 50)
        label = QTextEdit(self)
        label.setFixedWidth(460)
        label.setFixedHeight(70)
        label.setReadOnly(True)
        label.move(20, 100)
        self.setWindowIcon(QIcon('static/101.jpg'))
        self.center()
        self.show()

        button.clicked.connect(lambda x: label.setText(random_question()))

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Czy jesteś pewien, że chcesz przerwać naukę do Ochrony? xD", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
