"""
The generating function is

-(3x^2+x)/(1-x-x**2)
and
http://www.alpertron.com.ar/QUAD.HTM
"""

 
A=[]

X=0
Y=-1
 
A.append(X)
count=1
while count<30:

    Xnew=-9*X-4*Y-14
    Ynew=-20*X-9*Y-28
    A.append(Xnew)
   
    X=Xnew
    Y=Ynew
    count+=1    
X=0
Y=1
 
A.append(X)
count=1
while count<30:

    Xnew=-9*X-4*Y-14
    Ynew=-20*X-9*Y-28
    A.append(Xnew)
   
    X=Xnew
    Y=Ynew
    count+=1    
X=-3
Y=-2
 
A.append(X)
count=1
while count<30:

    Xnew=-9*X-4*Y-14
    Ynew=-20*X-9*Y-28
    A.append(Xnew)
   
    X=Xnew
    Y=Ynew
    count+=1    
X=-3
Y=2
 
A.append(X)
count=1
while count<30:

    Xnew=-9*X-4*Y-14
    Ynew=-20*X-9*Y-28
    A.append(Xnew)
   
    X=Xnew
    Y=Ynew
    count+=1    
X=-4
Y=-5
 
A.append(X)
count=1
while count<30:

    Xnew=-9*X-4*Y-14
    Ynew=-20*X-9*Y-28
    A.append(Xnew)
   
    X=Xnew
    Y=Ynew
    count+=1    
X=-4
Y=5
 
A.append(X)
count=1
while count<30:

    Xnew=-9*X-4*Y-14
    Ynew=-20*X-9*Y-28
    A.append(Xnew)
   
    X=Xnew
    Y=Ynew
    count+=1    
X=2
Y=-7
 
A.append(X)
count=1
while count<30:

    Xnew=-9*X-4*Y-14
    Ynew=-20*X-9*Y-28
    A.append(Xnew)
   
    X=Xnew
    Y=Ynew
    count+=1    
X=2
Y=-7
 
A.append(X)
count=1
while count<30:

    Xnew=-9*X-4*Y-14
    Ynew=-20*X-9*Y-28
    A.append(Xnew)
   
    X=Xnew
    Y=Ynew
    count+=1    
B=[r for r in A if r>0]
B=list(set(B))
B.sort()
B=B[:30]
print B
print sum(B)
