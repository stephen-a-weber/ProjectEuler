 
import time
ras=time.time()
n=10000000
primes=[]
phi=[1]*n
for i in xrange(2,n):
   phi[i]*=i 
primes.append(2)
sieve=[True]*n
phi[2]*=(1-1/2.0)
for i in xrange(4,n,2):
    sieve[i]=False
    phi[i]*=.5
for i in xrange(3,n,2):
  
    if sieve[i]==True:
        primes.append(i)
        for j in xrange(i,n,i):
            sieve[j]=False
            phi[j]*=(1-1/float(i))

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
frogs=[1]*n
gulls=[]
for i in xrange(2,n):
     
   frogs[i]=[int(r) for r in str(int(phi[i]))]
   frogs[i].sort()
   bird=[int(r) for r in str(i)]
   bird.sort()
   if bird==frogs[i]:
        gulls.append(i)
   

highn=0
highnphi=10000

for i in gulls:
    k=i/float(phi[i])
    if k<highnphi:
        highnphi=k
        highn=i
    

print highn," with a value of ",highnphi

rr=time.time()
print rr-ras
 
 

