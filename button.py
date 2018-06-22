import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 button - pythonspot.com')
        self.setGeometry(80,80,620,500)
 
        button = QPushButton('PyQt5 button', self)
        button.move(200,70) 
        button.clicked.connect(self.on_click)
        self.show()
    @pyqtSlot()
    def on_click(self):
       print('PyQt5 button click')
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())