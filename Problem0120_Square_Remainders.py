
"""
Square remainders
Problem 120
Let r be the remainder when (a1)n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728  42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3  a  1000, find  rmax.


Answer:
333082500
Completed on Fri, 15 Mar 2013, 22:19
"""



def fun(a):
    d=set()
    f=len(d)
    n=1
    g=f+1
    while g>f:
        f=len(d)
        for i in range(n,n+f+1):
            d.add(((a-1)**i+(a+1)**i)%a**2)
            #print d,f,g
        g=len(d)
        n+=f
    return max(d)
            
frog=0        
for a in range(3,1001):
    frog+=fun(a)
print frog

