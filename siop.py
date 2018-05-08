# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:11:07 2018

@author: jbt
"""

class A(object):
    num = 100
    def __init__(self):
        A.num += 1
    def f1(self):
        print("hello")
    @classmethod
    def getnum(*f):
        print(f)
        return A.num
    
a1=A()
print (A.getnum())
