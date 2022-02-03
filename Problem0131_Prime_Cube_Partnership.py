"""
Prime cube partnership
Problem 131
There are some prime values, p, for which there exists a positive integer, n, such that the expression n3 + n2p is a perfect cube.

For example, when p = 19, 83 + 8219 = 123.

What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?


Answer:
173
Completed on Wed, 3 Apr 2013, 18:26
"""



import time
ras=time.time()
import random
import math


#assume n+b is the winning cube.
#n**3+3b**2n+3b*n**2+b**3=n**3+n**2p
#solve for n and the n**3 drop out
#leaving quadratic to solve for n
#solution of quadratic points to an integer solution
#so mod (%) is a check
# the range of b in terms of p is also set to p/3 max.

#will probably take an hour to run...



ras=time.time()
n=1000000 
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
goods=[]
bbb=[]
nnn=[]
count=0
f=primes[-1]*4/3
square={}
for i in range(f):
    x=i*i
    y=-3*x
    z=y*x
    square[i]=(x,y,z)
print "Sorry for the wait.."
for T in range(4,len(primes)):
    
    i=primes[T]
    #if T%1000==0:
        #print "WE ARE ON PRIME NUMBER ",i," with count ",count," ..time: ",time.time()-ras
      
    k= i/3
    answer=False
    for b in range(1,k):
        q=6*b-2*i
     
        x,y,m=square[b]
         
      
        z=m+4*i*x*b
      
        zz=math.sqrt(z)
        if zz!=int(zz):
            continue
        else:
            z=int(zz)
        g=y-z
        if g%q==0:
            n=g/q
            print "prime",i,"  n= ",n,"addition to n:",b,"cube ",n+b
            print  "is it still",n**3+n**2*i,"and",(n**3+n**2*i)**(1/3.)
            count+=1
            print"thie one above is :",count
            print"_____________________________________"
            goods.append(i)
            bbb.append(b)
            nnn.append(n)
            answer=True
            break
            #print":::", g/q,i,b,n+b
##    if not answer:
##      for b in range(k+1,4*k/3+1):
##        q=6*b-2*i
##     
##        x,y,m=square[b]
##         
##      
##        z=m+4*i*x*b
##      
##        z=math.sqrt(z)
##        m
##        g=y+z
##        if g%q==0:
##            #n=g/q
##             
##            count+=1
##            answer=True
##            break
##            #print":::", g/q,i,b,n+b
print count
print time.time()-ras
        
