# -*- coding: utf-8 -*-
"""
Pythagorean tiles
Problem 139
Let (a, b, c) represent the three sides of a right angle triangle with integral length sides. It is possible to place four such triangles together to form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.


However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred million, how many Pythagorean triangles would allow such a tiling to take place?


Answer:
10057761
Completed on Thu, 9 May 2013, 11:52
"""
count=0
import fractions
import time
T=set()
ras=time.time()
nset=[r for r in range(1,10000)]
def mset(n):
    begin=n+1
 #   mset=[r for r in range(begin,10000) if fractions.gcd(r,n)==1]
    frog=set()
    v=2
    k=n
    while k>=v:
        if k%v==0:
            frog.add(v)
            k=k/v
        v+=1
    mset=[r for r in range(begin,10001)]
    for i in frog:
         
        
        camp=[r for r in mset if r%i!=0]
        mset=camp[:]
    return mset
 
Fa=100000000000000000000000
 
X1=0
Y1=0
Z1=0
for n in nset:
    j=mset(n)
    if n==2:
        print"one done"
    if n%1000==0:
        print n
    for m in j:
     
     
     if (m-n)%2==1:
            a=((m**2-n**2)) 
            b=(2*m*n) 
            c=((m**2+n**2)) 
            if c>1000000:
                break
            for k in xrange(1,1000000):
                aa=(k*a)**2
                bb=(k*b)**2
                cc=(k*c)**2
                if cc<1000000:
                    T.add(tuple([cc,aa,bb]))
                    
                
                else:
                    break
                
print count            
print time.time()-ras 
