# -*- coding: utf-8 -*-
"""
Primonacci
Problem 304
For any positive integer n the function next_prime(n) returns the smallest prime p 
such that p>n.

The sequence a(n) is defined by:
a(1)=next_prime(1014) and a(n)=next_prime(a(n-1)) for n>1.

The fibonacci sequence f(n) is defined by: f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n>1.

The sequence b(n) is defined as f(a(n)).

Find ∑b(n) for 1≤n≤100 000. Give your answer mod 1234567891011.


Answer:
283988410192
Completed on Mon, 9 Sep 2013, 08:29
"""



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



def next_Prime(n):
    if n%2==0:
        n+=1
    b=False
    while not b:
        n=n+2
        b=is_Prime(n)
    return n

"""
 
"""    
m=[[0,1],[1,1]]

def mulMat(a,b):
    c=[[0,0,],[0,0]]
   
    c[0][0]=(a[0][0]*b[0][0]+a[1][0]*b[0][1])%1234567891011
    c[1][0]=(a[0][0]*b[1][0]+a[1][0]*b[1][1])%1234567891011
    c[0][1]=(a[0][1]*b[0][0]+a[1][1]*b[0][1])%1234567891011
    c[1][1]=(a[0][1]*b[1][0]+a[1][1]*b[1][1])%1234567891011
    return c


def Mpos(a,p):
    if p==1:
        return a
    if p%2:
        return mulMat(a,Mpos(a,p-1))
    X=Mpos(a,p/2)
    return mulMat(X,X)

def fib(n):
    if n==1:
        return 1
    T=[[0,1],[1,1]]
    T=Mpos(T,n-1)
    total=(T[0][0]+T[0][1])%1234567891011
    return total

 
finaltotal=0

n=100001
f=[0]*n
b=1
k=10**14
while b<n:
    k=next_Prime(k)
    #f[b]=k
    finaltotal=(finaltotal+fib(k))%1234567891011

    b+=1
    if b%1000==0:
        print b,finaltotal

print "The answer is ",finaltotal
