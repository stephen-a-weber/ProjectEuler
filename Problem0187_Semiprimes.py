 """
Semiprimes
Problem 187
A composite is a number containing at least two prime factors. For example, 15 = 3  5; 9 = 3  3; 12 = 2  2  3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n  108, have precisely two, not necessarily distinct, prime factors?


Answer:
17427258
Completed on Sun, 17 Mar 2013, 21:49

""
#Note so slow made it c++
 
import time
ras=time.time()
n=(10**8)/2
prime=[]
 
 
numbers={}
 
prime.append(2)
 
sieve=[True]*n
 
for i in xrange(4,n,2):
    sieve[i]=False
   
  
for i in xrange(3,n,2):
  
    if sieve[i]==True:
        prime.append(i)
        
        
        for j in xrange(i*i,n,i):
            sieve[j]=False
      
 
print "Primes Done"
print "time:",time.time()-ras
m=0
print "there are ",len(prime), " primes"
for i in range(len(prime)):
    if i %100000==0:
        print "At the number prime check of :",i
    please=100000000/prime[i]
    for j in range(i,len(prime)):
  
         if prime[j]<=please:
            m=m+1
         else:
             break
print m
