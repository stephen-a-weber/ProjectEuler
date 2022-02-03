"""
Pseudo-Fortunate Numbers
Problem 293
An even positive integer N will be called admissible, if it is a power of 2 or its distinct prime factors are consecutive primes.
The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.

If N is admissible, the smallest integer M  1 such that N+M is prime, will be called the pseudo-Fortunate number for N.

For example, N=630 is admissible since it is even and its distinct prime factors are the consecutive primes 2,3,5 and 7.
The next prime number after 631 is 641; hence, the pseudo-Fortunate number for 630 is M=11.
It can also be seen that the pseudo-Fortunate number for 16 is 3.

Find the sum of all distinct pseudo-Fortunate numbers for admissible numbers N less than 109.


Answer:
2209
Completed on Mon, 27 May 2013, 08:53

"""

import random

import itertools

        
 
def is_Prime(n):
    #Miller-Rabin test for prime
    if n==2:
        return True
    if n%2==0:
        print "CRASHED HERE SOMEHOW"
         
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
 
import time
import random
ras=time.time()
n=100
lastPrime=0
primes=[]
primes.append(2)
sieve=[True]*n
for i in xrange(4,n,2):
    sieve[i]=False
for i in xrange(3,n,2):
      if sieve[i]==True:
          primes.append(i)
          lastPrime=i
          if i*i<n:
           for j in xrange(i*i,n,i):
             sieve[j]=False
print "PRIMES DONE" ,time.time()-ras
f=1
d=10**9
e=[]
from math import log
them=[2, 3, 5, 7, 11, 13, 17, 19, 23]
num=len(them)
pos=[[] for r in range(num)]

x=0
for i in them:
    
    t=log(d,i)
    for a in range(int(t)):
            pos[x].append(i**(a+1))
    x=x+1
import itertools
tank=pos[0][:]
container=[]       
storage=pos[0][:]
for a in range(1,num):
    container=[]
    for i in itertools.product(tank,pos[a]):
       zoo=1
       for d in i:
           zoo*=d
       if zoo<=10**9:
           container.append(zoo)
    for p in container:
        storage.append(p)
    tank=container[:]
           
 


 
print len(storage)
total=0
storage=set(storage)
storage=list(storage)
print len(storage)
trash=set()
for i in storage:
        m=3
        while not is_Prime(i+m):
            m+=2
        trash.add(m)
        
print sum(trash)
