"""
The prime factorisation of binomial coefficients
Problem 231
The binomial coefficient 10C3 = 120.
120 = 23  3  5 = 2  2  2  3  5, and 2 + 2 + 2 + 3 + 5 = 14.
So the sum of the terms in the prime factorisation of 10C3 is 14. 

Find the sum of the terms in the prime factorisation of 20000000C15000000.


Answer:
7526965179680
Completed on Fri, 5 Apr 2013, 22:39
"""


total=0
terms=[]

x=20000000
y=15000000
"""
x=12
y=11
"""
lowB=0
highB=0
if x-y>y:
    lowB=y
    highB=x-y
else:
    lowB=x-y
    highB=y
    
lowB 
top=0
bottom=0

import math
import time
import random
ras=time.time()
n=x
lastPrime=0
 
sieve=[True]*(n+1)

for i in xrange(2,n+1):
      if i %100000==0:
          print i
      if sieve[i]==True:
          count=0
          if i<=lowB:
              bottom+=i
          if i>highB:
              top+=i
           
           
           
          for j in xrange(2*i ,n+1,i):
             
        
             sieve[j]=False
             if j<=lowB:
                 count=0
                 trial=j
                 while trial%i==0:
                     count+=1
                     trial/=i
                 bottom+=i*count
                  
             if j>highB:
                  
                 count=0
                 trial=j
                 while trial%i==0:
                     count+=1
                     trial/=i
                 top+=i*count
                 
print "PRIMES DONE" ,time.time()-ras
 
 
 
print top-bottom

print "top=",top
print "bottom=",bottom

print time.time()-ras
