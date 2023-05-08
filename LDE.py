from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time
from PyQt5.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.components()

        self.show()
        
        return
    
    def components(self):

        self.setWindowTitle("LDE")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.number_label = QLabel("Número:")
        self.layout.addWidget(self.number_label)
        self.number_box = QLineEdit()
        self.layout.addWidget(self.number_box)

        self.position_label = QLabel("Posição:")
        self.layout.addWidget(self.position_label)
        self.position_box = QLineEdit()
        self.layout.addWidget(self.position_box)

        self.add_button = QPushButton("Adicionar na lista")
        self.add_button.clicked.connect(self.add_to_list)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remover da lista")
        self.remove_button.clicked.connect(self.remove)
        self.layout.addWidget(self.remove_button)

        self.search_button_el = QPushButton("Procurar elemento")
        self.search_button_el.clicked.connect(self.search_for_element)
        self.layout.addWidget(self.search_button_el)

        self.search_button_pos = QPushButton("Procurar posição")
        self.search_button_pos.clicked.connect(self.search_for_position)
        self.layout.addWidget(self.search_button_pos)

        self.count = 0
        self.list_label = QListWidget()
        self.list_label.setFlow(0)
        self.layout.addWidget(self.list_label)

        return

    ### AUXS ###
    def animate(self):
        self.list_label.repaint()
        self.list_label.viewport().update()
        time.sleep(0.4)

        return
    
        
    def remove_color(self):
        for i in range(self.list_label.count()):
            self.list_label.item(i).setBackground(QColor("transparent"))

        return
    
    def clear(self):
        self.list_label.clear()
        
        return
    
    ### METHODS LDE ###
    #### ADD
    def add_to_list(self):
        if self.position_box.text() != "" and self.number_box.text() != "":
            number = self.number_box.text()
            position = int(self.position_box.text())

            if self.list_label.count() == 0:
                QTimer.singleShot(500, lambda: self.list_label.addItem("H -->"))
                QTimer.singleShot(1500, lambda: self.list_label.insertItem(1, number))
                QTimer.singleShot(2500,lambda: self.list_label.addItem("<-- T"))
                self.count += 1

            else:
                if int(self.position_box.text()) <= 1:
                    self.add_to_list_start(number)
                
                elif int(self.position_box.text()) >= self.count + 1:
                    self.add_to_list_end(number)
                
                else:
                    #COMECANDO PELA CABECA
                    if position <= (self.count // 2):
                        nodes = 0
                        for i in range(self.list_label.count() - 1):
                            self.list_label.item(i).setBackground(QColor("transparent"))
                            self.animate()
                            if self.list_label.item(i).text().isnumeric():
                                nodes += 1
                            self.list_label.item(i).setBackground(QColor("grey"))
                            self.animate()
                            if nodes == position - 1:
                                self.list_label.item(i + 1).setBackground(QColor("green"))
                                self.animate()
                                self.remove_color()
                                self.animate()
                                i += 2
                                QTimer.singleShot(500, lambda: self.list_label.insertItem(i, "<-"))
                                QTimer.singleShot(1000, lambda: self.list_label.insertItem(i + 1, number))
                                QTimer.singleShot(1500, lambda: self.list_label.insertItem(i + 2, "->"))
                                QTimer.singleShot(2500, lambda: self.list_label.item(i + 1).setBackground(QColor("greenyellow")))
                                QTimer.singleShot(3500, lambda: self.list_label.item(i + 1).setBackground(QColor("white")))
                                self.count += 1
                                
                                break

                    else:
                        #COMECANDO PELA CAUDA 
                        nodes = 0
                        for i in range(self.list_label.count() - 1, 0, -1):
                            

                            if self.list_label.item(i).text().isnumeric():
                                nodes += 1

                            self.list_label.item(i).setBackground(QColor("grey"))
                            self.animate()

                            if nodes == self.count - (position-1):
                                self.list_label.item(i-1).setBackground(QColor("green"))
                                self.animate()

                                self.remove_color()
                                self.animate()

                                i += 1
                                QTimer.singleShot(500, lambda: self.list_label.insertItem(i - 1, "<-"))
                                QTimer.singleShot(1000, lambda: self.list_label.insertItem(i - 1, number))
                                QTimer.singleShot(1500, lambda: self.list_label.insertItem(i, "->"))
                                QTimer.singleShot(2500, lambda: self.list_label.item(i - 1).setBackground(QColor("greenyellow")))
                                QTimer.singleShot(3500, lambda: self.list_label.item(i - 1).setBackground(QColor("transparent")))
                                self.count += 1
                                
                                break
                            


                        
        return
    
    def add_to_list_start(self, number):
        QTimer.singleShot(500, lambda: self.list_label.item(0).setBackground(QColor("grey")))
        QTimer.singleShot(1000, lambda: self.list_label.item(0).setBackground(QColor("greenyellow")))
        QTimer.singleShot(1500, lambda: self.list_label.item(0).setBackground(QColor("white")))
        QTimer.singleShot(500, lambda: self.list_label.insertItem(1, "<-"))
        QTimer.singleShot(1000, lambda: self.list_label.insertItem(1, "->"))
        QTimer.singleShot(1500, lambda: self.list_label.insertItem(1, number))
        QTimer.singleShot(2000, lambda: self.list_label.item(1).setBackground(QColor("greenyellow")))
        QTimer.singleShot(3000, lambda: self.list_label.item(1).setBackground(QColor("white")))
        self.count += 1
        self.remove_color()

        return
    
    def add_to_list_end(self, number):
        end_tail = self.list_label.count()
        QTimer.singleShot(500, lambda: self.list_label.item(end_tail - 1).setBackground(QColor("grey")))
        QTimer.singleShot(1000, lambda: self.list_label.item(end_tail - 1).setBackground(QColor("greenyellow")))
        QTimer.singleShot(1500, lambda: self.list_label.item(end_tail - 1).setBackground(QColor("white")))
        end = self.list_label.count() - 1
        QTimer.singleShot(2000, lambda: self.list_label.insertItem(end, "->"))
        QTimer.singleShot(2500, lambda: self.list_label.insertItem(end + 1, "<-"))
        QTimer.singleShot(3000, lambda: self.list_label.insertItem(end + 2, number))
        QTimer.singleShot(3500, lambda: self.list_label.item(end + 2).setBackground(QColor("greenyellow")))
        QTimer.singleShot(4000, lambda: self.list_label.item(end + 2).setBackground(QColor("white")))
        self.count += 1
        self.remove_color()

        return
    
    #### REMOVE 
    def remove(self):
        if self.position_box.text() != "":
            position = int(self.position_box.text())
            if self.count == 1:
                self.clear()
                self.count = 0
                

            elif position <= 1:
                self.remove_start()
                

            elif position >= self.count:
                self.remove_final()
                
            
            else:
                #COMEÇANDO PELA CABECA
                if position <= (self.count // 2):
                    nodes = 0
                    for i in range(self.list_label.count() - 1):

                        if self.list_label.item(i).text().isnumeric():
                            nodes += 1

                        self.list_label.item(i).setBackground(QColor("grey"))
                        self.animate()

                        if nodes == position:

                            QTimer.singleShot(500, lambda: self.list_label.item(i).setBackground(QColor("red")))

                            for j in range(3):
            
                                QTimer.singleShot(1000+(j*500), lambda: self.remove_aux(i-2))

                            QTimer.singleShot(3000, lambda: self.list_label.item(i-1).setBackground(QColor("greenyellow")))
                            QTimer.singleShot(3000, lambda: self.list_label.item(i-2).setBackground(QColor("greenyellow")))
                            QTimer.singleShot(4000, lambda: self.list_label.item(i-1).setBackground(QColor("transparent")))
                            QTimer.singleShot(4000, lambda: self.list_label.item(i-2).setBackground(QColor("transparent")))
                            self.count -= 1
                            break
                
                            
                #COMECA PELA CAUDA
                else:

                    nodes = 0
                    for i in range(self.list_label.count() - 1, 0, -1):


                        if self.list_label.item(i).text().isnumeric():
                            nodes += 1

                        self.list_label.item(i).setBackground(QColor("grey"))
                        self.animate()

                        if nodes == self.count - (position - 1):

                            QTimer.singleShot(500, lambda: self.list_label.item(i).setBackground(QColor("red")))

                            for j in range(3):
            
                                QTimer.singleShot(1000+(j*500), lambda: self.remove_aux(i-2))

                            QTimer.singleShot(3000, lambda: self.list_label.item(i-1).setBackground(QColor("greenyellow")))
                            QTimer.singleShot(3000, lambda: self.list_label.item(i-2).setBackground(QColor("greenyellow")))

                            QTimer.singleShot(4000, lambda: self.list_label.item(i-1).setBackground(QColor("transparent")))
                            QTimer.singleShot(4000, lambda: self.list_label.item(i-2).setBackground(QColor("transparent")))
                            self.count -= 1
                            break
                    
        self.remove_color()
        return

    def remove_start(self):
        
        QTimer.singleShot(500, lambda: self.list_label.item(0).setBackground(QColor("grey")))
        QTimer.singleShot(1000, lambda: self.list_label.item(0).setBackground(QColor("greenyellow")))

        for i in range(3):
            
            QTimer.singleShot(1000+(i*500), lambda: self.remove_aux(1))

        QTimer.singleShot(3500, lambda: self.list_label.item(0).setBackground(QColor("transparent")))
        self.count -= 1

        return
    
    def remove_final(self):

        QTimer.singleShot(500, lambda: self.list_label.item(self.list_label.count() - 1).setBackground(QColor("grey")))
        QTimer.singleShot(1000, lambda: self.list_label.item(self.list_label.count() - 1).setBackground(QColor("greenyellow")))

        for i in range(3):

            QTimer.singleShot(1500+(i*500), lambda: self.remove_aux(self.list_label.count() - 2))

        QTimer.singleShot(3500, lambda: self.list_label.item(self.list_label.count() - 1).setBackground(QColor("transparent")))
        self.count -= 1

        return
    
    def remove_aux(self, position):
        self.list_label.removeItemWidget(self.list_label.item(position))
        self.list_label.takeItem(position)

        return
    
    #### SEARCH
    def search_for_element(self):
        self.remove_color()

        if self.number_box.text() != "":
            number = self.number_box.text()

            for i in range(self.list_label.count() - 1):
                if self.list_label.item(i).text() == "<-":
                    continue

                self.list_label.item(i).setBackground(QColor("grey"))
                self.animate()

                if i == 0:
                    self.list_label.item(i).setBackground(QColor("grey"))
                    self.animate()
                    self.list_label.item(i).setBackground(QColor("transparent"))
                    self.animate()

                else:
                    if self.list_label.item(i).text() == number:
                        self.list_label.item(i).setBackground(QColor("green"))
                        self.animate()
                        break
                    else:
                        if self.list_label.item(i).text() == "->":
                            self.list_label.item(i).setBackground(QColor("transparent"))
                            continue

                        self.list_label.item(i).setBackground(QColor("red"))
                        self.animate()          
        return

    def search_for_position(self):
        self.remove_color()

        node = 0

        if self.position_box.text() != "":
            position = int(self.position_box.text())
            if position <= 0:
                position = 1
            elif position >= self.count:
                position = self.count

            ### COMEÇA PELA CABEÇA
            if position <= self.count // 2:
                for i in range(self.list_label.count() - 1):
                    if self.list_label.item(i).text() == "<-":
                        continue
                    
                    if self.list_label.item(i).text().isnumeric():
                        node += 1

                    self.list_label.item(i).setBackground(QColor("grey"))
                    self.animate()

                    if i == 0:
                        self.list_label.item(i).setBackground(QColor("grey"))
                        self.animate()
                        self.list_label.item(i).setBackground(QColor("transparent"))
                        self.animate()

                    else:
                        if node == position:
                            self.list_label.item(i).setBackground(QColor("green"))
                            self.animate()
                            break
                        else:
                            if self.list_label.item(i).text() == "->":
                                self.list_label.item(i).setBackground(QColor("transparent"))
                                continue

                            self.list_label.item(i).setBackground(QColor("red"))
                            self.animate()

            ### COMEÇA PELA CAUDA
            else:
                for i in range(self.list_label.count() - 1, 0, -1):
                    if self.list_label.item(i).text() == "->":
                        continue
                    
                    if self.list_label.item(i).text().isnumeric():
                        node += 1

                    self.list_label.item(i).setBackground(QColor("grey"))
                    self.animate()

                    if i == self.list_label.count() - 1:
                        self.list_label.item(i).setBackground(QColor("grey"))
                        self.animate()
                        self.list_label.item(i).setBackground(QColor("transparent"))
                        self.animate()

                    else:
                        if node == self.count - position + 1:
                            self.list_label.item(i).setBackground(QColor("green"))
                            self.animate()
                            break
                        else:
                            if self.list_label.item(i).text() == "<-":
                                self.list_label.item(i).setBackground(QColor("transparent"))
                                continue

                            self.list_label.item(i).setBackground(QColor("red"))
                            self.animate()

### MAIN ###
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet('.QListWidget, .QLabel, .QPushButton, .QLineEdit { font-size: 14pt;}')
    sys.exit(app.exec_())    