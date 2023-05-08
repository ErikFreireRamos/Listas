import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configura a janela principal
        self.setWindowTitle('Menu')
        self.setGeometry(100, 100, 600, 600)
        self.window
        self.setStyleSheet('background-color: #d3d3d3')
        
        # Cria os botões
        self.btn_lista_sequencial = QPushButton('SEQUENCIAL', self)
        self.btn_lista_sequencial.move(200,50)
        self.btn_lista_sequencial.setFixedSize(200,50)
        self.btn_lista_sequencial.clicked.connect(self.lista_sequencial)
        self.btn_lista_sequencial.setStyleSheet("""
            QPushButton {
                background-color: #add8e6;
                color: #fff;
                border-style: solid;
                border-width: 2px;
                border-color: #add8e6;
                padding: 5px 10px;
                font-family: League Spartan;
                font-size: 16px;
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #add8e6;
            }
        """)

        
        self.btn_simplesmente_encadeada = QPushButton('LSE', self)
        self.btn_simplesmente_encadeada.move(200, 250)
        self.btn_simplesmente_encadeada.setFixedSize(200,50)
        self.btn_simplesmente_encadeada.clicked.connect(self.lista_simplesmente_encadeada)
        self.btn_simplesmente_encadeada.setStyleSheet("""
            QPushButton {
                background-color: #90ee90;
                color: #fff;
                border-style: solid;
                border-width: 2px;
                border-color: #90ee90;
                padding: 5px 10px;
                font-family: League Spartan;
                font-size: 16px;
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #90ee90;
            }
        """)
        
        self.btn_duplamente_encadeada = QPushButton(QIcon('LDE.png'),'LDE', self)
        self.btn_duplamente_encadeada.move(200, 450)
        self.btn_duplamente_encadeada.setFixedSize(200,50)
        self.btn_duplamente_encadeada.clicked.connect(self.lista_duplamente_encadeada)
        self.btn_duplamente_encadeada.setStyleSheet("""
            QPushButton {
                background-color: #ffb6c1;
                color: #fff;
                border-style: solid;
                border-width: 2px;
                border-color: #ffb6c1;
                padding: 5px 10px;
                font-family: League Spartan;
                font-size: 16px;
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #ffb6c1;
            }
        """)
        
    def lista_sequencial(self):
        subprocess.call(['python', 'ListaSequencial.py'])
        
    def lista_simplesmente_encadeada(self):
        subprocess.call(['python', 'LSE.py'])
        
    def lista_duplamente_encadeada(self):
        subprocess.call(['python', 'LDE.py'])
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())
