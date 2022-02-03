"""
Composites with prime repunit property
Problem 130
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

You are given that for all primes, p  5, that p  1 is divisible by A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n  1 is divisible by A(n).


Answer:
149253
Completed on Sun, 7 Apr 2013, 20:34


"""

#
# R(k)= (10^k-1)/9 in general
#

#
# R(k)=0 mod p
# (10^k-1)/9 = 0 mod p
# (10^k-1)   = 0 mod 9*P
#
# or  10^k   = 1 mod 9*P
#
#
n=1000000
lastPrime=0
primes=[2]
 
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




crate=[]
import time
ras=time.time()
maxim=0
these=[]
n=7
cat=True
while cat:
  if n%5==0 :
        n=n+2
  A=2
  dog=True
  while dog:
      
     if pow(10,A,9*n)==1:
        #print"...","       number of repunits:",A,"  divisible by:",n
        dog=False
        if ((n-1)%A==0):
            if n not in primes:
                
               crate.append(n)
               print len(crate),n
        if len(crate)==25:
            print "THE ANSWER IS ",sum(crate)
            cat=False
            break
     else:
         A+=1
     
  
  if A>maxim :
      maxim=A
      #print "repunits are at a maximum of  ",maxim
  if A>1000000:
       
           break
  n+=2


print "the least divisor is ",n
print
print "This took ",time.time()-ras
