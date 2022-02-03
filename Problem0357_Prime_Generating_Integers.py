# -*- coding: utf-8 -*-
#too slow made a sieve in C++ for prime check..same code though
"""
Prime generating integers
Problem 357
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.


Answer:
1739023853137
Completed on Thu, 23 May 2013, 18:22


"""

import time
ras=time.time()
n=8000000

import random

import itertools

        
 
def is_Prime(n):
    #Miller-Rabin test for prime
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
  
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(5):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

def div(n):
    if is_Prime(n):
        return False
    d=n
    v=set()
    for i in xrange(1,int((n+1)**.5)+1):
      
        if n%i==0:
             
            a=n/i
            b=a+i
            if not is_Prime(b):
                return False
    return True


total=3#numbers 1,2 
for i in xrange(3,10000001):
        m=div(i)
        if i%100000==0:
            print i,"TIME AT",time.time()-ras
            ras=time.time()
         
        if div(i):
            total+=i
		

print "Final answer:",total
