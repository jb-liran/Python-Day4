# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:20:05 2018

@author: jbt
"""

class MyException(Exception):
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    def __str__(self):
        return "bla bla" + str(self.__a)

def fn():
    try:
        f1 = open("myfile2.txt")
        print("ok")
    finally:
        print ("fn finally")

def f1(a,b):
    if b == 0:
        raise MyException(10,20,30)
    return a/b

try:
    x=9
    y=10
    f1(6,0)
#    fn()
    f=open("myfile.txt")
    print(f.readline())
    x=x/y
    print("end")
except IOError as myerr:
    print("error not found",myerr)
except ZeroDivisionError:
    print("divide by 0")
except Exception as err:
    print("other error",err)
else:
    fn()
finally:
    print("finally")


print("bye")



