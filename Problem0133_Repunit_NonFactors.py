"""
Repunit nonfactors
Problem 133
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Let us consider repunits of the form R(10n).

Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17. Yet there is no value of n for which R(10n) will divide by 19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred that can be a factor of R(10n).

Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10n).


Answer:
453647705
Completed on Mon, 8 Apr 2013, 10:45
"""
 

import time
import random
ras=time.time()
n=100000
 
primes=[2]
 
sieve=[True]*n
for i in xrange(4,n,2):
    sieve[i]=False
for i in xrange(3,n,2):
      if sieve[i]==True:
          
          primes.append(i)
          
          if i*i<n:
           for j in xrange(i*i,n,i):
             sieve[j]=False


print len(primes)
 

#primes.remove(5)
#primes.remove(3)
 
these=[]
for i in primes:
  if i in these:
      continue
  for x in range(1,20):
    if i in these:
        break
    if pow(10,10**x,9*i)==1:
        print i
        these.append(i)
       
dd=[r for r in primes if r not in these]
print "the answer",sum(dd)
 
             
print "PRIMES DONE" ,time.time()-ras
 
