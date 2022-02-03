"""Tribonacci non-divisors
Problem 225
The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.

It can be shown that 27 does not divide any terms of this sequence.
In fact, 27 is the first odd number with this property.

Find the 124th odd number that does not divide any terms of the above sequence.


Answer:
2009
Completed on Fri, 24 May 2013, 15:27
"""
"""
The generating Function I have so far as
(1-x**2)/(1-x-x**2-x**3)
"""
 
c=[1,1,1]
x=3
print "1,1,1",
d=set()
for i in xrange(40000):
    f=x%3
    c[f]=c[(x-1)%3]+c[(x-2)%3]+c[(x-3)%3]
    #print c[f],
    x=x+1
    d.add(c[f])
 
frog=[]
p=3
popcorn=True
while popcorn:
    p=p+2
 
    candy=True
    for i in d:
      if i%p==0:
        candy=False
        break
    if candy:
            print p
            frog.append(p)
    if len(frog)==124:
        popcorn=False
        break
