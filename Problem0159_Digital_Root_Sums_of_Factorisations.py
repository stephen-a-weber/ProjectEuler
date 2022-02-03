"""
Digital root sums of factorisations.
Problem 159
A composite number can be factored many different ways. For instance, not including multiplication by one, 24 can be factored in 7 distinct ways:

24 = 2x2x2x3
24 = 2x3x4
24 = 2x2x6
24 = 4x6
24 = 3x8
24 = 2x12
24 = 24
Recall that the digital root of a number, in base 10, is found by adding together the digits of that number, and repeating that process until a number is arrived at that is less than 10. Thus the digital root of 467 is 8.

We shall call a Digital Root Sum (DRS) the sum of the digital roots of the individual factors of our number.
The chart below demonstrates all of the DRS values for 24.

Factorisation	Digital Root Sum
2x2x2x3
9
2x3x4
9
2x2x6
10
4x6
10
3x8
11
2x12
5
24
6
The maximum Digital Root Sum of 24 is 11.
The function mdrs(n) gives the maximum Digital Root Sum of n. So mdrs(24)=11.
Find mdrs(n) for 1  n  1,000,000.


Answer:
14489159
Completed on Thu, 23 May 2013, 11:17

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
 
    for i in range(7):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  
divs={}
adivs={}
 
def div(n):
    global divs
    
    if n in divs:
        return divs[n]
    if is_Prime(n):
        setting(n,[[n]])
        return(set(tuple([n])))
    d=n
    theend=tuple([n])
    v=set()
    v.add(theend)
    for i in xrange(2,int((n+1)**.5)+1):
      
        if n%i==0:
             
            a=n/i
            v.add(tuple([i,a]))
            if not is_Prime(i) and not is_Prime(a):
                jjj=div(i)
                q=list(jjj)
                mmm=div(a)
                w=list(mmm)
                 
                for h in q:
                    for g in w:
                        k=list(h)+list(g)
                        k.sort()
                        
                        v.add(tuple(k))
            elif not is_Prime(i):
                jjj=div(i)
                q=list(jjj)
                for h in q:
                    k=list(h)+[a]
                    k.sort()
                    v.add(tuple(k))
                    

            elif not is_Prime(a):
                
                mmm=div(a)
                w=list(mmm)
                
                for g in w:
                     
                    k=[i]+list(g)
                    k.sort()
                    v.add(tuple(k))
    c=setting(n,v)
  
    divs[n]=c
    return 
 
def setting(n,v):
    global adivs
    global divs
    maximum=0
    best=[]
     
    for i in list(v):
        total=0
        for j in list(i):
            h=str(j)
            r=[int(a) for a in h]
            key=sum(r)
            while key>=10:
                gg=key
                h=str(gg)
                r=[int(a) for a in h]
                key=sum(r)
            total+=key
         
            
        if total>maximum:
            maximum=total
            best=tuple(i)
    adivs[n]=maximum
    b=set()
    b.add(best)
    return b
            
total=0  
for i in range(2,1000000):
    if i%10000==0:
        print i
    div(i)
    
    total+=adivs[i]
print total
 
