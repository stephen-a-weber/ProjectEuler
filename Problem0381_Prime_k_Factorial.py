"""
Factorial trailing digits
Problem 160
For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so f(9)=36288
10! = 3628800 so f(10)=36288
20! = 2432902008176640000 so f(20)=17664

Find f(1,000,000,000,000)


Answer:
16576
Completed on Wed, 5 Jun 2013, 06:08

"""
import math

def primes(n):
    #primes to n
    primes=[2]
    sieve=[True]*n
    for i in xrange(4,n,2):
        sieve[i]=False
    for i in xrange(3,n,2):
        if sieve[i]==True:
            primes.append(i)
            for j in xrange(i*i,n,i):
      
                sieve[j]=False
    return primes
b=primes(10**8)
print "done with primes"
b.remove(2)
b.remove(3)
t=1
c=0
can=0
total=0
""" 
for x in b:
    k=1
    total=0
    while k<6:
        d=pow(math.factorial(x-k),1,x)
##        if k==3:
##            print x,x-k,"  ",d%x
##        if k==3:
##            print d%x,
####        if k==5:
##            print x,x-k,"          ",d%x
        total+=d
        k+=1
    total=total%x
    can+=total
    print x,total,can
    
#(p-1)!   p-1
#(p-2)!   1
#(p-3)!   (p-1)/2
#(p-4)!   (p.
w=len(b)
for i in xrange(w):
    print (b[i]-1)/2,
print
print "1",
four=1
run=1
w=len(b)
for i in xrange(w):
    B=b[i]
    if B==5:
        continue
    run+=b[i-1]
    print B,run%b[i],run
    four+=run%b[i]
"""        
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
can=0
w=len(b)
print "there are ", w," primes"
for x in xrange(w):
    i=b[x]
    if x%10000==0:
        print"At ",x
    total=0
    v=(i-1)/2
    total+=i+v
    #thats three
    x=v*modinv((i-3),i)%i
    #print i, x
    y=x*modinv((i-4),i)%i
    #print i,y
    total+=x+y
    total=total%i
    can+=total
print can,"."
