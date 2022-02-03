"""
Fibonacci golden nuggets
Problem 137
Consider the infinite polynomial series AF(x) = xF1 + x2F2 + x3F3 + ..., where Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is, Fk = Fk1 + Fk2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of x for which AF(x) is a positive integer.

Surprisingly AF(1/2)	 = 	(1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3 + (1/2)5.5 + ...
 	 = 	1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
 	 = 	2
The corresponding values of x for the first five natural numbers are shown below.

x	AF(x)
21	1
1/2	2
(132)/3	3
(895)/8	4
(343)/5	5
We shall call AF(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.


Answer:
1120149658760
Completed on Tue, 16 Apr 2013, 20:05

"""
 
"""
2
15
104
714
4895
33552
229970
1576239
10803704
74049690
507544127
3478759200
23843770274
163427632719
1120149658760
7677619978602
52623190191455
360684711361584
"""
x=2
y=2 
golden=0
while True:
    m=5*x*x+2*x+1
    if (int(m**.5)**2)==m:
        print x
        if x<=3478759200:
          x=int(x*6.85)
        else:
            x=int(x*6.8541019)
        
    
    x+=1
    
# Found the closed form solution is A(x)=x/(1-x-x**2)
# found the radical was 5m**2+2m+1 and
# just incremented till it was a perfect square
# Jumping the next increment logrythmically
# and then back to linear.
#

g=34**.5-3
g=g/5
 
a= g
b= 1-g-g**2
print a,b,a/b
print a%b
print   a%b<10**-16
 
h=2**.5-1
print h
print .5
j=(13**.5-2)/3
print j
k=(89**.5-5)/8
print k
print g

