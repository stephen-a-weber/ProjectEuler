# -*- coding: utf-8 -*-
"""
Fibonacci Words
Problem 230
For any two strings of digits, A and B, we define FA,B to be the sequence (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of the previous two.

Further, we define DA,B(n) to be the nth digit in the first term of FA,B that contains at least n digits.

Example:

Let A=1415926535, B=8979323846. We wish to find DA,B(35), say.

The first few terms of FA,B are:
1415926535
8979323846
14159265358979323846
897932384614159265358979323846
14159265358979323846897932384614159265358979323846
Then DA,B(35) is the 35th digit in the fifth term, which is 9.

Now we use for A the first 100 digits of π behind the decimal point:

14159265358979323846264338327950288419716939937510 
58209749445923078164062862089986280348253421170679

and for B the next hundred digits:

82148086513282306647093844609550582231725359408128 
48111745028410270193852110555964462294895493038196 .

Find n = 0,1,...,17   10n DA,B((127+19n)7n) .


Answer:
850481152593119296
Completed on Thu, 16 May 2013, 08:34

"""
#0:B[27]
#1:B[22]
#2:B[85] note not zero based

#4:B[3]
#5:B[54]
pa="14159265358979323846264338327950288419716939937510\
58209749445923078164062862089986280348253421170679"
pb="82148086513282306647093844609550582231725359408128\
48111745028410270193852110555964462294895493038196"
 
total=0
n=0
 
F=[0]*79
Y=[0]*18
X=[0]*18
F=[0,1]
o=[0,1,1]
r=2
for Fibonacci in range(0,75):
    a=r-1
    b=r-2
    F.append(F[a]+F[b])
    #print r,F[r]
    r+=1
F=[100*r for r in F]    
for i in range(0,18):
    y= (127+19*i)*7**i
    Y[i]=y
    x=0
    
    c=0
    while y>c:
        x=x+1
        c= F[x]
       
    X[i]=x                
    print i,y,"    ",x,c


 
for u in range(10):
    print u,F[u]
 
f=["A","B","AB"]
r=2
for i in range(5):
    d=(r-2)%3
    w=(r-1)%3
    f[r]=f[d]+f[w]

    r=(r+1)%3
    #print i+1,len(f[r])*100,f[r]
b=0    
n=0
num=0

for i in range(0,18):

    n=X[i]
    num=Y[i]
##    print
##    print i,n,num,F[n]
##    print"___________________"
    while n>2:
        b=n-2
        while num<F[b]:
            b=b-2
##        print "subtracting",num,"-",F[b],"=",
        num=num-F[b]
##        print num
         
        
        n=b+1
        #print "Now n is ",n
        if num<100 and n>2:
            while n>2:
                n=n-2
        
   
            
    if n==1:
        print i,": A[",num,"]",pa[num-1]
        total+=(10**i)*int(pa[num-1])
    elif n==2:
        print i,": B[",num,"]",pb[num-1]
        total+=(10**i)*int(pb[num-1])
    else:
        print"error at",i
        break
print total








     
    
    
