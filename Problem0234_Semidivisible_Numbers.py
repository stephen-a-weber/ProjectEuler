"""
Semidivisible numbers
Problem 234
For an integer n  4, we define the lower prime square root of n, denoted by lps(n), as the largest prime  n and the upper prime square root of n, ups(n), as the smallest prime  n.

So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37.
Let us call an integer n  4 semidivisible, if one of lps(n) and ups(n) divides n, but not both.

The sum of the semidivisible numbers not exceeding 15 is 30, the numbers are 8, 10 and 12.
15 is not semidivisible because it is a multiple of both lps(15) = 3 and ups(15) = 5.
As a further example, the sum of the 92 semidivisible numbers up to 1000 is 34825.

What is the sum of all semidivisible numbers not exceeding 999966663333 ?


Answer:
1259187438574927161
Completed on Sat, 11 May 2013, 19:11

"""
import time
ras=time.time()
n=1000004
T=999966663333 
primes=[]
primes.append(2)
sieve=[True]*n
for i in xrange(4,n,2):
    sieve[i]=False
for i in xrange(3,n,2):
      if sieve[i]==True:
          primes.append(i)
     
           
          for j in xrange(i*i,n,i):
             sieve[j]=False


sumtotal=0

 
print "Going through 78499 primes.."
r=len(primes)
for L in range(0,r-1):
##    if L%1000==0:
##        print L,int(time.time()-ras)
##        ras=time.time()
    low=primes[L]
    high=primes[L+1]
    minimum=low**2
    maximum=high**2
    p=high-low
     
    k=minimum+low 
    lowcage=set()
    while k<maximum:
        if k<T: 
           lowcage.add(k)
        k=k+low
  
    k=maximum-high
    highcage=set()
    while k>minimum:
        if k<T: 
           highcage.add(k)
        k=k-high
    d=lowcage.symmetric_difference(highcage)
    sumtotal+=sum(d)
     
##    print low,high,":",minimum,maximum
##    print range(minimum+1,maximum)
##    print lowcage
##    print highcage
##    print">>>>>",d
##    print
    
    
    
    
 
print sumtotal

print time.time()-ras
