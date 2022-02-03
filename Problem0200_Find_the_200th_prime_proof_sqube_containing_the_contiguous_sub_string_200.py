"""
Find the 200th prime-proof sqube containing the contiguous sub-string "200"
Problem 200
We shall define a sqube to be a number of the form, p2q3, where p and q are distinct primes.
For example, 200 = 5223 or 120072949 = 232613.

The first five squbes are 72, 108, 200, 392, and 500.

Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; we shall call such numbers, prime-proof. The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.

Find the 200th prime-proof sqube containing the contiguous sub-string "200".


Answer:
229161792008
Completed on Mon, 17 Jun 2013, 15:22
"""S


import time
RAS=time.time()

import random

import itertools

        
 
def is_Prime(n):
    if n==0:
        return False
    #Miller-Rabin test for prime
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

n=500000  
 
 
primes=[2]
sieve=[True]*n
 
 
 
for i in xrange(4,n,2):
     
    sieve[i]=False
for i in xrange(3,n,2):
     
    if sieve[i]:
       
        primes.append(i)
        for j in xrange(i+i,n,i):
                sieve[j]=False

goat=[]
lamb=0
 
pr2=[r*r for r in primes]
pr3=[r*r*r for r in primes]
print len(primes)
for x in range(len(pr2)):
    i=pr2[x]
    for y in range(len(pr3)):
        j=pr3[y]
        
 
    
        
        a=i*j
        if a>8143805520077:
            break
        s=str(a)
        if s.count("200")>0:
            #print i*j
            goat.append(a)
            lamb+=1
goat.sort
goat=[str(r) for r in goat]
 
import math
#print time.time()-RAS
#goat.sort()
hamster=[]
x=0
for sqube in goat:
   
    s=len(sqube) 
    cat=True 
    d=""
    for i in range(s):
        if cat==False:
            break
        for c in range(0,10):
            if i==0:
               d=sqube[:-1]+str(c)
            elif i+1==s:
                if c!=0:
                    d=str(c)+sqube[1:]
                else:
                    continue
            else:
                d=sqube[:-i-1]+str(c)+sqube[s-i:]
                
            
             
           
            if is_Prime(int(d)):
                  #print "PRINME"
                  cat=False
                  break
    if cat:
        #print sqube
        hamster.append(sqube)
        
        
h=[int(r) for r in hamster]
print "THe answer ",h[199]
        
