# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:05:34 2018

@author: jbt
"""

class Account(object): 
    def __init__(self, initial):
        self._balance = initial 
    def deposit(self, amt):
        self._balance = self._balance + amt 
    def withdraw(self,amt):
        self._balance = self._balance - amt 
    def getbalance(s):
        return s._balance
    def __str__(self):
        return "Balance:" + str(self._balance)


class Checking(Account):
    def __init__(self):
        super(Checking,self).__init__(0)
#    def __str__(self):
#        return "Balance:" + str(self._balance)

class Bank(object):
    def __init__(self):
        self._accounts = []
    def __len__(self):
        return len(self._accounts)
    def __getitem__(self,key):
        return self._accounts[key]
    def __setitem__(self,key,value):
         self._accounts[key] = value
    def __delitem__(self,key):
        del self._accounts[key]
    def __contains__(self,item):
        return item in self.accounts
    def next(self):
        if not self._accounts:
           raise StopIteration
        return self._accounts.pop()

    def __iter__(self):
        for a in self._accounts:
            yield a.getbalance()
    def Add(self,account):
        self._accounts.append(account)
class Person(object):
    def __init__(self): 
        self.name = "{} {}".format("First","Last")

class Employee(Person):
    def introduce(self): 
        print("Hi! My name is {}".format(self.name))

    
d = Checking()
print (d)


b = Bank()
b.Add(Account(10))
b.Add(d)
b.Add(Account(2))

print (len(b))
print (b[0].getbalance())

b[0].deposit(1000)

print (b[0].getbalance())

del b[0]

print (len(b))

print (b[1].getbalance())

for a in b:
    print (a)

