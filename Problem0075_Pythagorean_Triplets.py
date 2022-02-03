theend=1500000
 
import math
import time
ras=time.time()
 
digits={} 

anger=[[3,4,5]]
n=1
m=2
k=1
zz=0
a1=0
b1=0
c1=0
a2=0
b2=0
c2=0
a3=0
b3=0
c3=0

while  anger:
    a,b,c=anger.pop()
    x=a+b+c
    k=1
    while k*x<theend:
      if k*x not in digits:
            digits[k*x]=[]
      digits[k*x].append([a*k,b*k,k*c])
      k=k+1
    a1=a-2*b+2*c
    b1=2*a-b+2*c
    c1=2*a-2*b+3*c
    if  (a1+b1+c1<theend) :
          anger.append([a1,b1,c1])
    a2=a+2*b+2*c
    b2=2*a+b+2*c
    c2=2*a+2*b+3*c
    if (a2+b2+c2<theend):
           anger.append([a2,b2,c2])
    a3=-a+2*b+2*c
    b3=-2*a+b+2*c
    c3=-2*a+2*b+3*c
   
    if (a3+b3+c3<theend):
       anger.append([a3,b3,c3])

zzz=0

print time.time()-ras
for i in digits:

    if len(digits[i])==1:
        zzz+=1
print zzz
