"""
abc-hits
Problem 127
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23  32  7, so rad(504) = 2  3  7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a  b
a + b = c
rad(abc)  c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5  27
5 + 27 = 32
rad(4320) = 30  32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c  1000, with c = 12523.

Find c for c  120000.


Answer:
18407904
Completed on Wed, 17 Apr 2013, 06:58

"""


import time
ras=time.time()

  
n=120000
rad={}
rad[1]=set([1])
sieve=[True]*(n)
primes=[2]
rad[2]=set([2])
for i in range(4,n,2):
    sieve[i]=False
    rad[i]=set([2])
for i in range(3,n,2):
    if sieve[i]:
        primes.append(i)
        rad[i]=set([i])
        for j in range(2*i,n,i):
            sieve[j]=False
            if j not in rad:
                rad[j]=set([i])
            else:
                rad[j].add(i)

rads={}
for i in rad:
    f=1
    for u in rad[i]:
        f*=u
    rads[i]=f
    
def radical(n):
    h=n
    j=set([])
    for i in primes:
        if h%i==0:
            h=h/i
            j.add(i)
            while h%i==0:
                h/=i
    return j
y=1
total=0
x=120000
for a in range(1,x-1):
    if a%1000==0:
        print "we are at " ,a,"taking this much time:", time.time()-ras
    for b in range(a+1,x):
        
        if rad[a].intersection(rad[b])!=set([]):
            continue
        else:
            c=a+b
            if c<x:
                if c in rad:
                    cr=rad[c]
                else:
                    cr=radical(c)
                if rad[a].intersection(cr)!=set([]):
                        continue
                else:
                    if rad[b].intersection(cr)!=set([]):
                            continue
                    else:
                        f=rads[a]*rads[b]
                        for i in cr:
                            f*=i
                        
                        if f<c:
                            #int y,":",a,b,c
                            y+=1
                            total+=c
print "The answer is :",total
                                
                    
     



        
