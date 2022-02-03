 
import time
r=time.time()
n=1000000
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

g=0

def green(n):
    g=n
    total=set()
    for i in primes:
        while n%i==0:
            n=n/i
            total.add(i)
        if n==1:
            break
    collie=g
    for i in total:
               collie*=(1-1.0/i)
    return collie
        
    

 
maxfrog=0
maxphi=0
for j in range(2,10001):
     g=green(j)
     lll=float(j)/g
     
     if lll>maxphi:
         maxphi=lll
         maxfrog=j

print "The max n/phi(n) ratio is produced by ",maxfrog, " and is ",maxphi
    
print "time at ",time.time()-r
