# -*- coding: utf-8 -*-

"""
Divisor Square Sum
Problem 211
For a positive integer n, let σ2(n) be the sum of the squares of its divisors. For example,

σ2(10) = 1 + 4 + 25 + 100 = 130.
Find the sum of all n, 0  n  64,000,000 such that σ2(n) is a perfect square.


Answer:
1922364685
Completed on Tue, 21 May 2013, 22:33

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
        return(1+n*n)
    d=n
    v=set()
    for i in xrange(1,int((n+1)**.5)+1):
      
        if n%i==0:
            v.add(i)
            a=n/i
            v.add(a)
    t=0
    for i in v:
        t+=i*i
    return t


total=0  
for i in xrange(1,64000000):
        m=div(i)
        if i%100000==0:
            print i,"TIME AT",time.time()-ras
            ras=time.time()
         
        b=m**.5
        if (int(b))**2==m:
           total+=i
           print i,m,total
		

print "Final answer:",total
