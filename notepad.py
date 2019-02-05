import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtWidgets import (QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout)


#class App (QWidget):
#    
#    def __init__(self):
#        super().__init__()
#        self.title = 'Notepad'
#        self.left = 100
#        self.top = 100
#        self.width = 640 
#        self.height = 480
##        self.statusBar().showMessage("Hello world!!")
#        self.initUI()
#        
#    def initUI(self):
#        self.setWindowTitle(self.title)
#        self.setGeometry(self.left, self.top, self.width, self.height)
#        self.show()
#
#class Window (QMainWindow):
#    
#    def __init__(self):
#        super().__init__()
#        self.title = 'Notepad'
#        self.left = 100
#        self.top = 100
#        self.width = 640 
#        self.height = 480
#        self.statusBar().showMessage("Hello world!!")
#        self.initUI()
#        
#    def initUI(self):
#        self.setWindowTitle(self.title)
#        self.setGeometry(self.left, self.top, self.width, self.height)
#        self.show()
#
#class Button (QWidget):
#    
#    def __init__(self):
#        super().__init__()
#        self.title = 'Notepad'
#        self.left = 100
#        self.top = 100
#        self.width = 640 
#        self.height = 480
##        self.statusBar().showMessage("Hello world!!")
#        self.initUI()
#        
#    def initUI(self):
#        button = QPushButton('OK!!', self)
#        button.setToolTip('Just an instance')
#        button.move(300,400)
#        button.clicked.connect(self.on_click)
#        self.setWindowTitle(self.title)
#        self.setGeometry(self.left, self.top, self.width, self.height)
#        self.show()    
#        
#    def on_click(self):
#        print('pyqt button click!!')
    
 
class Dialog(QDialog):
 
    def slot_method(self):
        print('slot method called.')
     
    def __init__(self):
        super(Dialog, self).__init__()
        self.Button()
        button=QPushButton("Click")
        button.clicked.connect(self.slot_method)
         
#        mainLayout = QVBoxLayout()
#        mainLayout.addWidget(button)
         
#        self.setLayout(mainLayout)
#        self.setWindowTitle("Button Example - pythonspot.com")
        
    def Button(self):
        self.title = 'Notepad'
        self.left = 100
        self.top = 100
        self.width = 640 
        self.height = 480
#        self.statusBar().showMessage("Hello world!!")
        self.initUI()
        
    def initUI(self):
        button = QPushButton('OK!!', self)
        button.setToolTip('Just an instance')
        button.move(300,400)
        button.clicked.connect(self.on_click)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()    
        
    def on_click(self):
        print('pyqt button click!!')
        return
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
#    ex = App()
#    new = Window()
#    button = Button()
#    button.show()
    dialog = Dialog()
    
    sys.exit(app.exec_())