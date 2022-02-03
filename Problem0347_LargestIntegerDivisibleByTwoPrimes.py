
"""
Largest integer divisible by two primes
Problem 347
Published on 03 September 2011 at 04:00 pm [Server Time]
The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96=32*3=25*3. For two distinct primes p and q let M(p,q,N) be the largest positive integer ≤N only divisible by both p and q and M(p,q,N)=0 if such a positive integer does not exist.

E.g. M(2,3,100)=96.
M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
Also M(2,73,100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

Find S(10 000 000)."""

import sys

import time
import itertools
r=time.time()
n=5000000
sieve=[True]* n
primes=[2]
  
for i in xrange(4,n,2):
    sieve[i]=False
 


for i in xrange(3,n,2):

    if sieve[i]==True:
        primes.append(i)
        
         
        for j in xrange(i*i,n,i):
            sieve[j]=False



 
print time.time()-r," sigh primes"

limit=10000000#5000000
index=0
cage=True
extras=[]
frog=True


    
face={}    
ext=[]
cage=True
num=0
while cage:
    exp=1
    while primes[num]**exp<limit:
        
        face[primes[num]**exp]=primes[num]
        ext.append(primes[num]**exp)
        exp+=1
    num+=1
    if num>len(primes)-1:
        cage=False

g=primes+ext
g=list(set(g))
g.sort()

THETOTAL=[]
floored=0
x=len(g)
c=1
for i in range(x):
    if i%100==0:
        print i,floored
        if i==900:
            break
     
    for j in range(i+1,x):
        h=g[i]*g[j]
        if h>limit:
            break
        else:
            floored+=1
            THETOTAL.append([g[i],g[j],h])
            


        
v=0
w={}
for i in THETOTAL:
    if face[i[0]]==face[i[1]]:
        continue
    c=(sorted([face[i[0]],face[i[1]]]))
    if tuple(c) not in w:
        w[tuple(c)]=i[2]
        v+=i[2]
    elif i[2]>w[tuple(c)]:
        v-=w[tuple(c)]
        w[tuple(c)]=i[2]
        
        v+=i[2]
    

print v
#solution 11109800204052
