import time
import math

rtime=time.time()

pentagonal = lambda k: k*(3*k-1)/2
k= map(pentagonal,range(-200,201))
k.remove(0)

print len(k) 
k.sort()
p={}
p[0]=1
 
n=0
sign=1
cat=True
while cat:
    n=n+1
    sign=1
    answer=0
    for k in range(1,100000):
        f=pentagonal(k)
        
        if n-f>-1:
  
            answer+=sign*p[n-f]
        else:
            break
        f=pentagonal(-k)
        if n-f>-1:
            answer+=sign*p[n-f]
        else:
            break
        sign=-sign
        
    p[n]=answer
    if answer%1000000==0:
        print n
        print
        print answer
        cat=False
            
 print
 print
 









print time.time()-rtime
