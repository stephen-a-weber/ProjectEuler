#Diophantine equation project euler problem 66
"""
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 131802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 222 = 1
22 – 312 = 1
92 – 542 = 1
52 – 622 = 1
82 – 732 = 1

Hence, by considering minimal solutions in x for D  7, the largest x is obtained when D=5.

Find the value of D  1000 in minimal solutions of x for which the largest value of x is obtained.
"""


import time
import math
rrr=time.time()
def find(n):
    A0=int(math.sqrt(n))
    return A0


def reversed(a1,a2,b1,n):
    a11=b1*a1
    b11=a1**2*n-a2**2
    a12=0
    theint=0
    c=b1*a2
    if a11>1:#reduce equation
        b11=b11/a11
        c=c/a11
        a11=1
     
    theint=int((float(a1)*math.sqrt(n)+float(c))/float(b11))#pulling out the integer part
    a12=theint*b11-c
     
    return a11,a12,b11,theint

def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) / 2
    for x in range(1, max_len):
        cat=True
        for y in range(x,max_len,x):
           
          
          if seq[0:x] != seq[y:y+x]  :
              cat=False
              break
            
        if cat:
            return x


def cF(n):
    if math.sqrt(n)==int(math.sqrt(n)):
        print "break"
        return
    
   
    a,b,c,theint=reversed(1,find(n),1,n)
   
    cage=[theint]
    
    for i in range(1,1000):
         
        q,w,e,aint=reversed(a,b,c,n)
        cage.append(aint)
        a,b,c=q,w,e
    
    #cage should now contain a 1000 iterations of sequence
    
    x=guess_seq_len(cage)
    return n,find(n),cage[0:x]


def converge(d,num):
    r=[find(d)]
    a,b,cage=cF(d)
    num=num
    f=len(cage)
    b=num/f
    for i in range(b+1):
        for j in cage:
            r.append(j)
    r=r[:num]
    numerator=1
    denominator=r.pop()
    if num==1:
        hold=numerator
        numerator=denominator
        denominator=hold
    while r:
        t=r.pop()
        numerator=t*denominator+numerator
        if r:
            hold=numerator
            numerator=denominator
            denominator=hold
    return numerator,denominator
"""

n,d= converge(2,50)
print float(n)/float(d)
            
"""
story=[]
d=2
n=2
while (d<=1000) :
     
    x,y=converge(d,n)
    if (x*x-d*y*y==1):
        story.append(( x,d,y))
        d=d+1
        if int(math.sqrt(d))==float(math.sqrt(d)):
             
            d=d+1
        n=2
    else:
        n=n+1
print max(story)
         
print time.time()-rrr

