import time
r=time.time()


def poly(a,b,primes):
    #output number of primes of n+1 starting with n=0
    total=0
    cat= True
    n=0
    while cat:
        answer=n**2+a*n+b
  
        if answer in primes:
            total+=1
            n+=1
        else:
            cat=False
    return total

def prime(n):
    #primes to n
    primes=[2]
    sieve=[True]*n
    for i in range(4,n,2):
        sieve[i]=False
    for i in range(3,n,2):
        if sieve[i]==True:
            primes.append(i)
            for j in range(i*i,n,i):
                sieve[j]=False
    return primes


primes=prime(88000)
#1000-168 primes
aa=0
bb=0
total=0
 
for a in range(-999,1000):
    for b in range(-999,1000):
        cancer=poly(a,b,primes)
        if cancer>total:
            total=cancer
            aa=a
            bb=b
print aa,bb,total
  
    
print time.time()-r
