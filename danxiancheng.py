#!/bin/env/python
#-*- coding:utf-8-*-
from time import ctime,sleep
def music():
    for i in range(2):
        print("i was listening to music.$s",ctime())
        sleep(1)
def move():
    for j in range(2):
        print("I was at the movies! $s",ctime())
        sleep(5)
if __name__=='__name__':
    music()
    move()
move()
music()
print("all over $s",ctime())