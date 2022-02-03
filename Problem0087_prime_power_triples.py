import time
ras=time.time()
n=7100
primes=[]
import math
print math.sqrt(50000000)
primes.append(2)
sieve=[True]*n
 
for i in xrange(4,n,2):
    sieve[i]=False
  
for i in xrange(3,n,2):
  
    if sieve[i]==True:
        primes.append(i)
        for j in xrange(i,n,i):
            sieve[j]=False
numbers=set() 
cubes=[]
squares=[]
fourths=[]
print "number of fourths ",len(fourths)
for i in primes:
    cubes.append(i*i*i)
    squares.append(i*i)
    fourths.append(i*i*i*i)
for i in fourths:
    print "we are at ",i
    if i>50000000:
        break
    for j in cubes:
        for k in squares:
            f=i+j+k
            if f <50000000:
                numbers.add(f)
                
            
print len(numbers)


print
print time.time()-ras
