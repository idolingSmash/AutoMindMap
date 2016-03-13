# -*- coding: utf-8 -*-

import sys
import re
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from PyQt4 import QtGui, QtCore

wikiURL = "https://ja.wikipedia.org/wiki/"

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
        self.setGeometry(200,200,300,200)

        self.submitBtn = QtGui.QPushButton("Submit", self);
        self.submitBtn.move(100, 80)
        self.submitBtn.clicked.connect(self.btnSubmit)
        self.submitBtn.clicked.connect(self.showTextModal)

    def btnSubmit(self):
        #ToDo Beautiful Soup4
        self.oLabel.setText(self.qText.text())

    def showTextModal(self):
        modal = QtGui.QDialog()
        modal.tagTitle = QtGui.QLabel( "[Title:]" + self.qText.text(), modal)
        modal.tagContent = QtGui.QLabel(modal)
        
        pile = scrapingLink(self.qText.text())
        bList = brushUpList(pile)

        wordStr = ""
        for i,item in enumerate(bList):
            wordStr = wordStr + item
            if i % 3 == 2:
                wordStr = wordStr + "\n"
            else:
                wordStr = wordStr + ", "
            

        modal.tagContent.setText(wordStr)  

        modal.tagTitle.move(25,25)
        modal.tagContent.move(25,40)        
        
        modal.setGeometry(300,100,500,700)
        modal.setWindowTitle("tag view")
        modal.setWindowModality(QtCore.Qt.WindowModal)
        modal.exec_()


#wikipedia内にあるキーワードリンクを抽出
def scrapingLink(query):
    linkList = []
    qURL = wikiURL + urllib.request.quote(query)
    html = urllib.request.urlopen(qURL).read()
    soup = BeautifulSoup(html, "html.parser")
    f = soup.find_all("p")

    for t in f:
        if t.a is not None:
            alist = t.find_all("a")
            for word in alist:
                linkList.append(word.text)
    return linkList

def brushUpList(list):
    result = []
    pattern = r"\d+年|\d+世紀|\d+月\d+日|\[[\d]+\]|いつ\?|\?"
    #pattern = r"\["

    for item in list:
        matchOB = re.match(pattern, item)
        if matchOB is None and 0 < len(item.strip()):
            result.append(item)

    return result


def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()