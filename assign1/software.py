'''
app         = QApplication([])
app.setStyle('macos')
window      = QWidget()
v_layout    = QVBoxLayout()
window.resize(500,300)

btn_la = QPushButton('Addition on left')
btn_ls = QPushButton('Substraction on left')
btn_ra = QPushButton('Addition on right')
btn_rs = QPushButton('Substraction on right')

txt_str = QLabel('hello world')
txt_str.setAlignment(Qt.AlignmentFlag.AlignCenter)
v_layout.addWidget(txt_str)
v_layout.addWidget(btn_la)
v_layout.addWidget(btn_ls)
v_layout.addWidget(btn_ra)
v_layout.addWidget(btn_rs)

txt_str = 'caacacacacacac'

def on_btn1_clicked():
    alert = QMessageBox()
    alert.setText('this is an alert msg')
    alert.exec()

btn_la.clicked.connect(on_btn1_clicked)

window.setLayout(v_layout)
window.show()
app.exec()

txt_str.setText('eee')
'''
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import *
from real_state_grph import *
import time

class MainWindow(QWidget):
    def __init__(self,_game):
        super().__init__()

        # set window properties
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 800, 500)
        self.game = _game

        # create label
        self.label = QLabel("Hello World!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont('Arial',20))

        self.label_score = QLabel("score", self)
        self.label_score.setGeometry(390,60,100,100)
        self.label_score.setFont(QFont('Arial',50))

        rules = 'res % 2 == 0 --> -1\nres % 2 == 1 --> +1\nres >= 5 --> +2\nres < 5 --> -2\nHuman has to maximize\nAI has to minimize'
        self.label_rules = QLabel(rules,self)
        self.label_rules.setGeometry(0,0,150,150)

        # create buttons
        btnls = QPushButton('Substraction on left', self)
        btnla = QPushButton('Addition on left', self)
        btnrs = QPushButton('Substraction on right', self)
        btnra = QPushButton('Addition on right', self)

        # create vertical layout and add label and buttons
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btnls)
        vbox.addWidget(btnla)
        vbox.addWidget(btnrs)
        vbox.addWidget(btnra)
        btnls.clicked.connect(self.on_btnls_clicked)
        btnla.clicked.connect(self.on_btnla_clicked)
        btnrs.clicked.connect(self.on_btnrs_clicked)
        btnra.clicked.connect(self.on_btnra_clicked)


        # set main layout
        self.setLayout(vbox)
    
    def set_label_text(self, text):
        self.label.setText(text)

    def set_label_score(self, s):
        self.label_score.setText(str(s))

    def on_btnls_clicked(self):
        if len(self.game.children) <= 0:
            self.winner_is()
            return
        self.game = self.game.children[0]
        self.set_label_text(self.game.string)
        self.set_label_score(self.game.score)
        QTimer.singleShot(2000,lambda: self.ai_plays())

    def on_btnla_clicked(self):
        if len(self.game.children) <= 0:
            self.winner_is()
            return
        self.game = self.game.children[1]  
        self.set_label_text(self.game.string)
        self.set_label_score(self.game.score)
        QTimer.singleShot(2000,lambda: self.ai_plays())

    def on_btnrs_clicked(self):
        if len(self.game.children) <= 0:
            self.winner_is()
            return
        self.game = self.game.children[2]  
        self.set_label_text(self.game.string)
        self.set_label_score(self.game.score)
        QTimer.singleShot(2000,lambda: self.ai_plays())

    def on_btnra_clicked(self):
        if len(self.game.children) <= 0:
            self.winner_is()
            return
        self.game = self.game.children[3]
        self.set_label_text(self.game.string)
        self.set_label_score(self.game.score)
        QTimer.singleShot(2000,lambda: self.ai_plays())

    def ai_plays(self):
        if len(self.game.children) <= 0:
            self.winner_is()
            return
        best = 2
        for i in range(len(self.game.children)):
            if self.game.children[i].heu < self.game.children[best].heu:
                best = i
        self.game = self.game.children[best]
        self.set_label_text(self.game.string)
        self.set_label_score(self.game.score)
        if len(self.game.children) <= 0:
            self.winner_is()
            return

    def launchgame(self,start):
        self.set_label_text(self.game.string)
        self.set_label_score(self.game.score)
        self.show()
        if not start:
            QTimer.singleShot(2000,lambda: self.ai_plays())

    def winner_is(self):
        alert = QMessageBox()
        msg = ''
        if self.game.score > 0:
            msg = 'Human won the game !' 
        elif self.game.score < 0:
            msg = 'AI won the game !'
        else:
            msg = 'There is no winner !'
        alert.setText(msg)
        alert.exec()
        self.close()

class ChooseWindow(QWidget):
    def __init__(self):
        super().__init__()

        # set window properties
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 400, 300)

        # create label
        self.label = QLabel("Choose who will start the game :", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont('Arial',10))

        # create buttons
        btnhu = QPushButton('Human', self)
        btnai = QPushButton('AI', self)

        # create vertical layout and add label and buttons
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(btnhu)
        vbox.addWidget(btnai)

        btnhu.clicked.connect(self.on_btnhu_clicked)
        btnai.clicked.connect(self.on_btnai_clicked)
        
        self.setLayout(vbox)

    def on_btnhu_clicked(self):
        self.prepare_game(True)
    
    def on_btnai_clicked(self):
        self.prepare_game(False)

    def prepare_game(self,start):
        curr = gen(get_start_str(7),0)
        minimax(curr,start)
        self.window = MainWindow(curr)
        #window.show()
        self.window.launchgame(start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ChooseWindow()
    win.show()
    sys.exit(app.exec())
