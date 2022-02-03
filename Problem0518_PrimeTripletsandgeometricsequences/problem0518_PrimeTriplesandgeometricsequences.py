"""
Prime triples and geometric sequences
Problem 518
Let S(n) = a+b+c over all triples (a,b,c) such that:

a, b, and c are prime numbers.
a < b < c < n.
a+1, b+1, and c+1 form a geometric sequence.
For example, S(100) = 1035 with the following triples:

(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71), (11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)

Find S(108).


Answer:
100315739184392
Completed on Tue, 3 Nov 2015, 08:11
"""


import sys
import math
import time
import copy
import itertools
import pickle
import random
r=time.time()
n=10**8
 
def is_Prime(n):
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
        
    if n==2 or n==3 or n==5 or n==7:
        return True
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
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

"""
sieve=[True]* n
primes=[2]

 
for i in range(4,n,2):
    sieve[i]=False
   
    
    
 


for i in range(3,n,2):
    
    
    if sieve[i]==True:
        primes.append(i)
        
       
    
        
        
         
        for j in range(i*i,n,i):
            sieve[j]=False
            
"""
primes=pickle.load(open("save.p","rb"))
print ("Primes calculated")
 

from math import sqrt 
def sqrfact(n):
    lim = sqrt(n) + 1
    x = 2
    while x <= lim:
        if n % x == 0:
            p = n/x
            if p % x == 0:
                return (x ** 2) * sqrfact(p/x)
            else:
                return sqrfact(p)
        x += 1

    # No factors.
    return 1

#god=pickle.load(open("fothersave.p","rb"))
god=pickle.load(open("ngothersave.p","rb"))

#primes.reverse()

"""
for index in range(4021369,len(primes)):                
    p=primes[index]
    if index%100000==0:
        print (index)
                   

    b=int(sqrt(sqrfact(p+1)))
    god[index]=b
pickle.dump(god,open("ngothersave.p","wb"))
sys.exit()
""" 



def GCD(a, b):

    if b == 0:
        return a
    else:
        return GCD(b, a % b)
def largestB(p):
    p=p+1
    factors=toad[p]
    
    result=1
    for i in factors:
        if i==1:
            continue
        j=0
        pr=p
        while pr/i==pr//i:
            pr=pr//i
            j+=1
        k=int(math.log(j,2))
        result*=i**k
       
            
            
    return result
rrr=time.time()
total=0
count=0

print("there are this many primes ",len(primes))
for index in range(0,len(primes)):
    p=primes[index]
   
    count+=1
    if count%10000==0:
        print ("count is ",count,int(time.time()-rrr))
    b=god[index]
    c=int(b*((n+1)/(p+1))**.5)
    for a in range(b+1,c+2):
   
        
        vv=p
        p2=(p+1)*a/b-1
       
        if p2>99999989:
            break
        if  is_Prime(p2):
            
            vv+=p2
            p3=(p2+1)*a/b-1
    
               
            if p3>99999989:
                break
            if is_Prime(p3):
  
                vv+=p3
                total+=vv
               
     
                
        
print(total)        
"""
total=95524079110204
total=95524079110204
total=94604286283689 got this down by making sure p2 and p3 were not greater then
10**8 the highest prime.. 
I got the same answer twice... sigh..
"""
"""
P+1 , (p+1)*k , (p+1)*k*k

p   , (p+1)*k -1 , (p+1)*k*k -1

k=a/b
m=maximum range
(p+1)*k*k-1< m
k<((m+1)/(p+1))**.5
k>1

b<a<b*((m+1)/(p+1))**.5

b**2 must be largest factor of p+1
find a from this b and last range
"""

"""
       
        vv=p
        p2=(p+1)*a/b-1
        if p2 in primes:
            vv+=p2
            p3=(p+1)*a*a/b/b-1
            if p3 in primes:
                vv+=p3
                total+=vv
                #print (p,p2,p3)
"""
