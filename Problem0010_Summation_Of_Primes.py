"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


Answer:
142913828922
Completed on Tue, 22 Jan 2013, 22:11
"""
import time
ras=time.time()
 
n=2000000
count=2
#primes.add(2) 
sieve=[True]*n
for i in range(4,n,2):
    sieve[i]=False
for i in range(3,n,2):
      if sieve[i]==True:
          count+=i
          for j in range(i*i,n,i):
             sieve[j]=False


print "The answer for sum of primes under 2 million is:",count

print
print"This took this much time :",time.time()-ras
