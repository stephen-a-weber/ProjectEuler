"""
Sum of a square and a cube
Problem 348
Many numbers can be expressed as the sum of a square and a cube. Some of them in more than one way.

Consider the palindromic numbers that can be expressed as the sum of a square and a cube, both greater than 1, in exactly 4 different ways.
For example, 5229225 is a palindromic number and it can be expressed in exactly 4 different ways:

22852 + 203
22232 + 663
18102 + 1253
11972 + 1563

Find the sum of the five smallest such palindromic numbers.


Answer:
1004195061
Completed on Thu, 20 Jun 2013, 14:00

"""
import time
RAS=time.time()
def test(n):
    n=str(n)

    a=len(n)

    for i in range(a):
        if n[i]!=n[-(i+1)]:
            return False
    return True
def t(n):
    g=0
    k=n
    while k!=0:
        k/=10
        g+=1
    
    for i in range(g/2 ):
        bottom=(n%(10**(i+1)))/(10**(i))
        top=(n/(10**(g-i-1 )))%(10)
         
        if top!=bottom:
            return False
    return True

def X(n):
    v=str(n)
    if v==v[::-1]:
        return True
    return False
the={}
a=0
b=0
f=0
limit=800000000
for s in xrange(1,30000):
    if s%1000==0:
        print s
        print time.time()-RAS
        RAS=time.time()
    a=s*s
    if a>limit:
            break
    for c in xrange(1,1000):
         
         
        f=a+c*c*c
        if f>limit:
            break
        if X(f):
            
            if f not in the:
                the[f]=1
            else:
                the[f]+=1
        
      

print time.time()-RAS 
d=[]
for i in the:
    if the[i]==4:
        d.append(i)
d.sort()
print "Answer ",sum(d[:5])
