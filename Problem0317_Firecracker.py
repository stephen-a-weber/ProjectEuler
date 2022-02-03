"""
Firecracker
Problem 317
A firecracker explodes at a height of 100 m above level ground. It breaks into a large number of very small fragments, which move in every direction; all of them have the same initial velocity of 20 m/s.

We assume that the fragments move without air resistance, in a uniform gravitational field with g=9.81 m/s2.

Find the volume (in m3) of the region through which the fragments move before reaching the ground. Give your answer rounded to four decimal places.


Answer:
1856532.8455
Completed on Fri, 19 Apr 2013, 17:26

 

All things in the sky follow a parabolic path .

so fitting

y=a*x**2 + b

it is pretty easy to find the 45 degree law.

Then the maximum height of the explosion can be found as v**2/(2*g)
and the maximum distance of the explosion is v**2/g

solving these x0 and y0 for a and b

we have y= (-g/(2*v**2))*x**2 + v**2/(2*g)

the integral for a f(x,y) equation is  PI * integral ( f(x)**2 dx)

and we need to increase our y value by 100.

and find the limits as that 100+ymax to zero

rewritting this as f(y)---- it is a squre root that the integral squares...

pi*integral (((    2*v**2)/g  *     [  v**2/2*g  - y +100 ]   ))

"""

v=20
g=9.81
d_max=v*v/g
h_max=(v**2)/(2*g) 
a= (2*v**2)/g
b= (h_max)+100

import math

"""
pi [[[   a *b *y  - a*y**2/2   ]]]  
"""
y=h_max +100

total=math.pi*(a*b*y-a/2*y**2)
print total


"""
with just d_max and h_max

the answer is

"""
 
h_max=(v**2)/(2*g) +100
d_max=v*v/g
 
print math.pi*d_max*h_max**2
