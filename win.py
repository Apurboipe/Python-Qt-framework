import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        #self.title = 'PyQt5 simple window - pythonspot.com'
        #self.left = 70
        #self.top = 70
        #self.width = 640
        #self.height = 480
        self.setWindowTitle('PyQt5 simple window - pythonspot.com')
        self.setGeometry(70,70,640,480)
        self.show()
        #self.initUI()
 
    '''def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()'''
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())