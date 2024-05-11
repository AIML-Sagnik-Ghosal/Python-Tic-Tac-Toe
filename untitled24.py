# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:29:21 2023

@author: SAGNIK GHOSHAL
"""

def ch(s1):
    for i in range(8):
         if set(b[i])&set(s1)==set(b[i]):
             print(b[i])
             return True
    return False
def c():
    global s1
    global s2
    s1=[]
    s2=[]
    t1.clear()
    t.clear()
    t1.penup()
    t1.goto(-50,150)
    t1.pendown()
    t1.goto(-50,-150)
    t1.penup()
    t1.goto(50,150)
    t1.pendown()
    t1.goto(50,-150)
    t1.penup()
    t1.goto(150,50)
    t1.pendown()
    t1.goto(-150,50)
    t1.penup()
    t1.goto(-150,-50)
    t1.pendown()
    t1.goto(150,-50)
    t1.penup()
    t1.goto(0,0)
    t1.pendown()
def u():
    if int(t1.pos()[1])!=100:
        t1.penup()
        t1.lt(90)
        t1.fd(100)
        t1.pendown()
        t1.rt(90)
def d():
    if int(t1.pos()[1])!=-100:
        t1.penup()
        t1.rt(90)
        t1.fd(100)
        t1.pendown()
        t1.lt(90)
def r():
    if int(t1.pos()[0])!=100:
        t1.penup()
        t1.fd(100)
        t1.pendown()
def l():
    if int(t1.pos()[0])!=-100:
        t1.penup()
        t1.bk(100)
        t1.pendown()
def o():
    x,y=t1.pos()
    if [x,y] not in ch:
        ch.append([x,y])
        if len(s1)==len(s2):
            t.pensize(10)
            t.penup()
            t.goto(x,y)
            t.pendown()
            t.goto(x-25,y-25)
            t.goto(x+25,y+25)
            t.goto(x,y)
            t.goto(x+25,y-25)
            t.goto(x-25,y+25)
            t.goto(x,y)
            s1.append(tuple(map(int,t1.pos())))
        else:
            t1.dot(75,"white")
            s2.append(tuple(map(int,t1.pos())))
        if len(s1)>=3:
            if ch(s1):
                print("a")
                c()
        if len(s2)>=3:
                if ch(s2):
                    print("b")
                    c()
import turtle as t
import tkinter as k
k.Tk()
t1=t.Turtle()
t1.speed(0.1)
t.speed(0.1)
ch=[]
a=[[(-100,100),(0,100),(100,100)],[(-100,0),(0,0),(100,0)],[(-100,-100),(0,-100),(100,-100)]]
b=[[(-100,100),(0,100),(100,100)],[(-100,0),(0,0),(100,0)],[(-100,-100),(0,-100),(100,-100)],
   [(-100,100),(-100,0),(-100,-100)],[(0,100),(0,0),(0,-100)],[(100,100),(100,0),(100,-100)],
   [(-100,100),(0,0),(100,-100)],[(100,100),(0,0),(-100,-100)]]
t1.shape("circle")
t1.shapesize(2)
t1.color("red")
t.bgcolor("yellow")
k.Button(text="create",command=c).grid()
k.Button(text="up",command=u).grid()
k.Button(text="down",command=d).grid()
k.Button(text="right",command=r).grid()
k.Button(text="left",command=l).grid()
k.Button(text="ok",command=o).grid()
t.done()