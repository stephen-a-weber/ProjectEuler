# -*- coding: utf-8 -*-
"""
	

Maximum product of parts
Problem 183
Let N be a positive integer and let N be split into k equal parts, r = N/k, so that N = r + r + ... + r.
Let P be the product of these parts, P = r  r  ...  r = rk.

For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.

Let M(N) = Pmax for a given value of N.

It turns out that the maximum for N = 11 is found by splitting eleven into four equal parts which leads to Pmax = (11/4)4; that is, M(11) = 14641/256 = 57.19140625, which is a terminating decimal.

However, for N = 8 the maximum is achieved by splitting it into three equal parts, so M(8) = 512/27, which is a non-terminating decimal.

Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.

For example, ΣD(N) for 5  N  100 is 2438.

Find ΣD(N) for 5  N  10000.


Answer:
48861552
Completed on Fri, 10 May 2013, 16:50
"""

import time
ras=time.time()
rass=time.time()
total=14
green=True
great=0
trulygreat=1
hy=1
for n in range(5,10001):
    if n%101==0:
        print n,great,trulygreat,"   ",total,"time:",time.time()-ras
        ras=time.time()
        hy=trulygreat
        trulygreat=0
    if n<100:
        hy=1
    d=0
    qa=0
    qb=0
       
    theEnd=int(n*hy+1)
    if theEnd>n+1:
        theEnd=n+1
    for k in range(great,theEnd ):
        a=n**k
        b=k**k
        h=1
         
        h=a/b
        #print n,":",k," =",a*1.0/b,d
        if h>d:
            d=h
            great=k
            qa=a
            qb=b
    
 
    c=qb
    #print n,":",d
    while c%2==0:
        c/=2
    while c%5==0:
        c/=5
    if qa%c==0 :
        total-=n
        green=True
    else:
        total+=n
        green=False
    if n==8:
        print "ppp",great,green
    if n==11:
        print "jjj",great,green 
    #print n,total#great, great*1.0/n
    if great*1.0/n>trulygreat:
        trulygreat=great*1.0/n
##    if n<100 :
##        hy=1
## 
##    elif n>=100 :
##         hy=.39
  
        
print total        
        
print "total time=",time.time()-rass
