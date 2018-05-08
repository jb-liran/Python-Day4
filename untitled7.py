# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:49:28 2018

@author: jbt
"""

#with open('gash.txt', 'r') as var:
#    for line in var:
#        print (line,end='')
#



class A(object):
    def __enter__(self):
        print ('enter')
    def __exit__(self,exceptType, value, traceback):
        print ('exit', exceptType)
        print(value)
        print(traceback)
    def f1(self):
        print("f1")

a1 = A()
a1.f1()

with A() as a2:
    print("hello")
    x=9
    y=10
    x=x/y
    print("bye")

