import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('PyQt5 messagebox - pythonspot.com')
        self.setGeometry(70,70,1024,600)
 
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to save?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        if buttonReply == QMessageBox.No:
            print('No clicked.')
        if buttonReply == QMessageBox.Cancel:
            print('Cancel')

        self.show()        
    @pyqtSlot()
    def on_click(self):
       print('PyQt5 button click')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())