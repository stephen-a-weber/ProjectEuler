# -*- coding: utf-8 -*-
"""
Alexandrian Integers
Problem 221
We shall call a positive integer A an "Alexandrian integer", if there exist integers p, q, r such that:

A = p · q · r    and  	
1
A
=	
1
p
+	
1
q
+	
1
r
For example, 630 is an Alexandrian integer (p = 5, q = 7, r = 18). In fact, 630 is the 6th Alexandrian integer, the first 6 Alexandrian integers being: 6, 42, 120, 156, 420 and 630.

Find the 150000th Alexandrian integer.


Answer:
1884161251122450
Completed on Tue, 7 May 2013, 19:50
"""
"""
Basically I saw the two patterns
1) that n, n+1, n*n+n+1

2) that given p>q>r  the limits can be gained by incrementing r
                     q (skipping the given of n+1 goes to a max limit approx 2r
                     then given a r and q we use the original equation for a check if a p
                     is valid.
                     


"""


count=0
storage=set()
import time
def tri():
    global storage
    global count
    count=0
    p=2
    q=1
    r=1
    ras=time.time()
    
    while True:
        
         
        
            
          for q in range(r+2,2*r+1):
              if (1+q*r)%(q-r)==0:
                p=(1+q*r)/(q-r)
            
  
  
       
          
                t=p*q*r
                storage.add(t)
                count+=1
                if count%1000==0:
                    s=list(storage)
                    s.sort()
                    s=s[:150000]
                    print count,s[149999],":time",round(time.time()-ras)
                    ras=time.time()
                    storage=set(s)
                      
          r=r+1
      
         
     
         
      

def two():
    global storage
    global count
    for p in range(1,150001):
        t=p*(p+1)+1
        t*=p*(p+1)
        storage.add(t)
    print len(storage)

two()
tri()        
        
