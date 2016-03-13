# -*- coding: utf-8 -*-

class Node:
    def __init__(self, name, dlist):
        self.name = name
        self.destList = dlist

    def print_content(self):
        viewList = ""
        for i,item in enumerate(self.destList):
            viewList = viewList + item
            if i != len(self.destList) - 1:
                viewList = viewList + ", "
            if i % 6 == 5:
                viewList = viewList + "\n"

        print ("name:" + self.name +" , destinations:"+ viewList)