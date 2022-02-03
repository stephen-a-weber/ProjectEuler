#Problem0007.py
#Author(s) Stephen A. Weber
#Creation 2013 Jan. through March.
"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


Answer:
104743
Completed on Tue, 22 Jan 2013, 20:07

"""

import time
import itertools
r=time.time()
n=200000
sieve=[True]* n
primes=[2]
count=1 
for i in range(4,n,2):
    sieve[i]=False
 


for i in range(3,n,2):

    if sieve[i]==True:
        primes.append(i)
        count+=1
        if count==10001:
            print "The Answer is ",i
            break
        
         
        for j in range(i*i,n,i):
            sieve[j]=False



 
print time.time()-r
 
