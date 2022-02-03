# -*- coding: utf-8 -*-
"""

Maximising a weighted product
Problem 190
Let Sm = (x1, x2, ... , xm) be the m-tuple of positive real numbers with x1 + x2 + ... + xm = m for which Pm = x1 * x22 * ... * xmm is maximised.

For example, it can be verified that [P10] = 4112 ([ ] is the integer part function).

Find Σ[Pm] for 2  m  15.


Answer:
371048281
Completed on Thu, 4 Jul 2013, 22:26


Lagrange Multiplier

constaints equal one so comparing equations is universal
a,b,c,d,e

b=2a
c=3a
d=4a...

a= n /  n*(n+1)/2

or a=2/(n+1)



total=0
for m in range(2,16):
    aa=(m)*(m+1)/2
    a=m*1.0/aa
    
    
    b=[a*r for r in range(1,m+1)]

    z=1
    for i in range(m):
        
        x=b[i]**(i+1)
        z*=x
        #print i,b[i],x

    print m,z
    total+=int(z)
print total
