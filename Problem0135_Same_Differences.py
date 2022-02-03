"""

Same differences
Problem 135
Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the positive integer, n, for which the equation, x2  y2  z2 = n, has exactly two solutions is n = 27:

342  272  202 = 122  92  62 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?


Answer:
4989
Completed on Wed, 8 May 2013, 16:24
"""

"""
boiled down to square root needing to be an integer
of 4*x^2-N.

i used the difference between squares as 4x^2 is a square YEAH!!
basically n^2-(n-s)^2==== 2s*n-s^2
so the N will be of this and s varies until my n-s becomes negative (z) ???

so it ran fast and my limit for b was at the moment was tested to fit
when it stopped adding values..

lets see now. ok here is why 250000

on the very last gothrough while loop I expct it to invalidate because
the term is greater then 1000000 and at that first go the value of s=1

so 2*s*y-s*s ==> 2*s*2*b -s*s ==> 4*b-1 =1000000
b is approximately a quarter million


"""
import time
ras=time.time()
storage={}
for b in xrange(250000,0,-1):
    
    x=4*b*b
    y=2*b
    s=1
    z=y
    while z>0:
        n=2*s*y-s*s
        z=z-1
    
        s+=1
        q=3*b+z
        qq=3*b-z
        if n>=1000000:
            break
        if q-2*b>0:
            if n not in storage:
                storage[n]=set()
            storage[n].add(tuple([q,b]))
        if qq-2*b>0:
            if n not in storage:
                storage[n]=set()
            storage[n].add(tuple([qq,b]))
        
                        
 
print time.time()-ras
r=0
for i in storage:
    if i<1000000:
        if len(storage[i])==10:
            r+=1
print r
