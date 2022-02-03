"""
Prime square remainders
Problem 123
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280  5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 1010.


Answer:
21035
Completed on Sat, 16 Mar 2013, 05:31

"""
import time
ras=time.time()
n=10000000
prime=[0]
 
 
prime.append(2)
sieve=[True]*n
 
for i in xrange(4,n,2):
    sieve[i]=False
  
for i in xrange(3,n,2):
  
    if sieve[i]==True:
        prime.append(i)
        for j in xrange(i*i,n,i):
            sieve[j]=False


 
 
def fun(n):
    return(((prime[n]-1)**n+(prime[n]+1)**n)%(prime[n]**2))

print fun(7037)
n=10**10
x=7037
while fun(x)<=n:
    x=x+1
    if x%10000==0:
        print "we are at x of ",x

print x,fun(x),n
print x-1,fun(x-1),n
 
print time.time()-ras
