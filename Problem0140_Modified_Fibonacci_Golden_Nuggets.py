"""
Modified Fibonacci golden nuggets
Problem 140
Consider the infinite polynomial series AG(x) = xG1 + x2G2 + x3G3 + ..., where Gk is the kth term of the second order recurrence relation Gk = Gk1 + Gk2, G1 = 1 and G2 = 4; that is, 1, 4, 5, 9, 14, 23, ... .

For this problem we shall be concerned with values of x for which AG(x) is a positive integer.

The corresponding values of x for the first five natural numbers are shown below.

x	AG(x)
(51)/4	1
2/5	2
(222)/6	3
(1375)/14	4
1/2	5
We shall call AG(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 20th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.


Answer:
5673835352990
Completed on Thu, 9 May 2013, 16:26

"""

import time
ras=time.time()
r=[]
count=0
lasty=1
bear=True
y=2
total=0
while True:

        d=176+20*y*y
    
        
        if int(d**.5)**2==d:
            e=d**.5
            f=int(16+e)
             
            if f>0:
                if f%10==0:
                    r.append(f/10-3)
                    count+=1
                    total+=f/10-3
                    print count,": ", f/10-3,total,bear,y,y*1.0/lasty,"time:",time.time()-ras
                    ras=time.time()
                    lasty=y
                    if count>=4 and count<10:
                        if bear:
                            y=int(y*3.5)
                            bear=False
                        else:
                            y=int(y*1.9)
                            bear=True
                    elif count>=10 and count<14:
                        if bear:
                            y=int(y*3.535)
                            bear=False
                        else:
                            y=int(y*1.9387)
                            bear=True
                    elif count>=14:
                        if bear:
                            y=int(y*3.5353221)
                            bear=False
                        else:
                            y=int(y*1.9387489)
                            bear=True
        y=y+1
        
       
           
              
print count
print len(r)
