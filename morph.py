# -*- coding: utf-8 -*-

import sys
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from PyQt4 import QtGui, QtCore

wikiURL = "https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8"

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()

    def initUI(self):
        self.qLabel = QtGui.QLabel("Keyword :",self)
        self.qLabel.move(50,25)
        self.oLabel = QtGui.QLabel("",self)
        self.oLabel.move(50,100)
        self.qText = QtGui.QLineEdit(self)
        self.qText.move(50,50)
        self.qText.setFixedWidth(120)
        self.setGeometry(300,300,300,200)

        self.submitBtn = QtGui.QPushButton("Submit", self);
        self.submitBtn.move(100, 80)
        self.submitBtn.clicked.connect(self.btnSubmit)

    def btnSubmit(self):
        #ToDo Beautiful Soup4
        self.oLabel.setText(self.qText.text())

def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()