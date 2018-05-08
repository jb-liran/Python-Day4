# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:15:57 2018

@author: jbt
"""

class Rect(object):
    __num = 0
    def __init__(self,h1=0,w1=0):
        Rect.__num +=1
        if h1 >0:
            self.__h = h1
        else:
            self.__h = 0
        self.__w = w1  
    def __add__(self,t):
        res = Rect(self.__h + t.__h , self.__w + t.__w)
        return res
#    def __del__(self):
#        print("delete")
#    @staticmethod
    @classmethod
    def getnum(g):
        return Rect.__num
    def __printheader(self):
        print("*************")
    def f1(self,v):
        print("f1")
    def f2(self):
        self.__printheader()
        print("f2",self.__h,self.__w)
        self.__printheader()
        

a1 = Rect(100,200)

a2= Rect(30,40)

a1.f2()
a2.f2()

