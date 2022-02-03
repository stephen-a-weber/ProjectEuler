"""
Singleton difference
Problem 136
Published on Friday, 29th December 2006, 10:00 am; Solved by 2570
The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. Given that n is a positive integer, the equation, x2  y2  z2 = n, has exactly one solution when n = 20:

132  102  72 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?


Answer:
2544559
Completed on Wed, 8 May 2013, 21:27
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
frog=set()
count=0
for b in xrange(1,12500001):
    if b%10000==0:
        print b
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
        if n>=50000000:
            break
        if q-2*b>0:
     
          if n not in frog:
            if n not in storage:
                storage[n]=[tuple([q,b])]
                
                count+=1
            else:
                
                if tuple([q,b]) not in storage[n]:
                    storage.pop(n)
                    frog.add(n)
                    count-=1
                    
                
        if qq-2*b>0:
          if n not in frog:
            if n not in storage:
                storage[n]=[tuple([qq,b])]
                count+=1
            else:
                if tuple([qq,b]) not in storage[n]:
                   frog.add(n)
                   storage.pop(n)
        
                   count-=1
#4946418        
#4946084
#2544559
 
print time.time()-ras
 
 
print len(storage)
 
