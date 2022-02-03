# -*- coding: utf-8 -*-
"""
A Scoop of Blancmange
Problem 226
The blancmange curve is the set of points (x,y) such that 0  x  1 and  ,
where s(x) = the distance from x to the nearest integer.

The area under the blancmange curve is equal to ½, shown in pink in the diagram below.


Let C be the circle with centre (¼,½) and radius ¼, shown in black in the diagram.

What area under the blancmange curve is enclosed by C?
Give your answer rounded to eight decimal places in the form 0.abcdefgh


Answer:
0.11316017
Completed on Sat, 1 Jun 2013, 09:43

"""
import math


def s(n):
    a=abs(n-math.ceil(n))
    b=abs(n-math.floor(n))   
    if a>b:
        return b
    return a

def Circle(x):
    y=1.0/16-(x-1.0/4)**2
    y=y**.5
    #z=.5+y
    y=.5-y
     
    
    return y

def Blancmange(x):
    
    total=0
    
    for i in range(42):
        a=s((2**i)*x)/(2**i)
        total+=a
    return total

"""
t=1
while t<42:
    print t,Bl(t)
    t+=1
"""        
 
yold=0
x=0
y=0
inc=.000001
total=0
while x<=.5:
     
    B=Blancmange(x)
    C=Circle(x)
    if C>B:
        y=0
    else:
       # print x,B,C
        y=B-C
    z=inc*(y+yold)/2
    total+=z
    yold=y
    x+=inc
print total       



    
    
