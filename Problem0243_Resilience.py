# -*- coding: utf-8 -*-
"""
Resilience
Problem 243
A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .


Answer:
892371480
Completed on Thu, 11 Apr 2013, 18:01

"""




x=0.163588195559            
maxim=88 
import time
ras=time.time()
n=100
primes=[2] 
 
 
sieve=[True]*n
 
for i in xrange(4,n,2):
    sieve[i]=False
    
for i in xrange(3,n,2):
  
    if sieve[i]==True:
         
        primes.append(i)
        for j in xrange( i,n,i):
            sieve[j]=False

def resilience(n):
    g=n
    total=[]
    for i in primes:
        while n%i==0:
            n=n/i
            total.append(i)
        if n==1:
            break
    if n!=1:
       print "MORE PRIMES"
    
    totient=1
    while total:
       for a in total:
          f=total.count(a)
          b=(a**f)*(1.0-1.0/a)
          #print a,f,b,"INSIDE ",totient
          totient*=b
          for _ in range(f):
             total.remove(a)
          break
    return totient/(g-1.0)


#2730656728800
#156165009000
#53542288800
#26771144400            
#26771144400
#22086194130
#13385572200
#892371480


maximum=999
r=tuple([2])
house={}
house[2]=1
storage=set( )
storage.add(r)

top=892371480

while storage:
    r=storage.pop()

 
     
    m=1
    for i in r:
        m*=i
    if m<top:#22086194130:#26771144400:#53542288800:#156165009000:#2730656728800:
        
    
        gr=resilience(m)
        if gr<maximum:
            maximum=gr
            if gr<x:

                if m<top:
                    print gr,x,m
                    top=m
                else:
                    break
            else:    
              print gr ,x,m
        h=max(r)
        p=primes[primes.index(h)+1]
        for i in primes:
          if i<=p:
             f=list(r)
             f.append(i)
             storage.add(tuple(f))
          else:
                break

            
    
