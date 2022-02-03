
"""
Investigating the behaviour of a recursively defined sequence
Problem 197
Given is the function f(x) = 230.403243784-x2  10-9 (   is the floor-function),
the sequence un is defined by u0 = -1 and un+1 = f(un).

Find un + un+1 for n = 1012.
Give your answer with 9 digits after the decimal point.


Answer:
1.710637717
Completed on Mon, 20 May 2013, 19:35

"""
#Noticed that the value mod 10000 was always the same so answer
#is same as n=10000

def f(x):
    return (int(2**(30.403243784-x*x))*10**(-9))
a=10000
c=[-1,0]
x=0
z=0
zz=0

while x<a+1:
    if x%10000==0:
        
       print x,c[x%2]
    c[(x+1)%2]=f(c[x%2])
    x+=1
    if x==a:
        z=c[x%2]
        
        print "n Answer", z
    if x==a+1:
        zz=c[x%2]
        print "n+1 Answer",zz
print "Sum:",z+zz
        
