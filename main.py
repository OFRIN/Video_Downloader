import os
import sys
import threading

import urllib.request

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QTimer

def download_video_from_url(url, end_func):
    urllib.request.urlretrieve(url, os.path.basename(url)) 
    end_func()

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Downloader made by Sanghyeon'

        self.left = 50
        self.top = 50
        self.width = 440
        self.height = 100
        
        self.initUI()

        self.th = None
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(400, 20)

        self.button = QPushButton('Download', self)
        self.button.move(20, 60)
        
        self.button.clicked.connect(self.on_click)

        self.show()

    def end_func(self):
        self.th = None

        self.textbox.setEnabled(True)
        self.button.setEnabled(True)
        self.textbox.setText("")
    
    @pyqtSlot()
    def on_click(self):
        self.textbox.setEnabled(False)
        self.button.setEnabled(False)

        url = self.textbox.text()

        self.th = threading.Thread(target=download_video_from_url, args=(url, self.end_func, ))
        self.th.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./app.ico'))
    ex = App()
    sys.exit(app.exec_())