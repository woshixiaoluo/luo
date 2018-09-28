#!/bin/env/python
#-*- coding:utf-8-*-
import threading
from time import ctime,sleep
def music(func):
    for i in range(2):
        print("I was listening to %s.%s" %(func,ctime()))
        sleep(4)
def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)

A = []
t1 = threading.Thread(target = music,args=(u'怪咖',))
A.append(t1)
t2 = threading.Thread(target = move,args = (u'赌圣',))
A.append(t2)

if __name__ == '__main__':
    for t in A:
        t.setDaemon(True)
        # music(u"怪咖")
        # move(u" 赌圣")
        t.start()
    for t in A:
        t.join()
        print("all over %s" %ctime())


