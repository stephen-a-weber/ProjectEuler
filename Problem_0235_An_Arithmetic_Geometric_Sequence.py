# -*- coding: utf-8 -*-
"""
An Arithmetic Geometric sequence
Problem 235
Given is the arithmetic-geometric sequence u(k) = (900-3k)rk-1.
Let s(n) = Σk=1...nu(k).

Find the value of r for which s(5000) = -600,000,000,000.

Give your answer rounded to 12 places behind the decimal point.


Answer:
1.002322108633
Completed on Fri, 5 Apr 2013, 19:45
"""
#used count numpy power failed...
#feeling manual ;)

import numpy

def count(r):
    total=0
    coef=900
    for x in xrange(1,5001):
        coef=coef-3
        total+=coef*r**(x-1)
    print total


def run(r):
    total=0
    for k in xrange(1,5001):
        total+=int((900-3*k)*numpy.power(r,k-1))
        
    return total
    


#1.001817193317
         
while True:        
    var=raw_input("Enter a number :")
    print "-600000000000"
   
    print count(float(var))
