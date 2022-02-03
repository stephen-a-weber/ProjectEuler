"""
Perfect Square Collection
Problem 142
Find the smallest x + y + z with integers x  y  z  0 such that x + y, x  y, x + z, x  z, y + z, y  z are all perfect squares.


Answer:
1006193
Completed on Fri, 10 May 2013, 11:29


using pythagorean triplets with c^2 <1000000
"""

total=10000000
kitten=False
import pickle
ff=open("/Users/isadmin/Desktop/Triplets.python","r+b")
T=pickle.load(ff)
count=0
print "going through 878..."
for c,a,b in T:
    count+=1
    if count%10==0:
        print count
  
    ac=a+c

    for x in range(ac+1,1000000):
        n=2*x
        #two tests one for a one for b
        if (int((n-c)**.5)**2)==(n-c):

            #for a
            if (int((n-a)**.5)**2)==(n-a):
                if(int((n-a-c)**.5)**2)==(n-a-c):
                   top=3*x-a-c
                   if top<total:
                       total=top
                       print x,x-a,x-c," THIS IS THE ANSWER TOTAL =",3*x-a-c
                       print "(((",c,b,a,2*x,n,")))"
                   else:
                       print "Found a value BUT..",x,x-a,x-c,3*x-a-c
                    
                  

            #for b
            if (int((n-b)**.5)**2)==(n-b):
                if(int((n-b-c)**.5)**2)==(n-b-c):
                   top=3*x-b-c
                   if top<total:
                       total=top
                       print x,x-b,x-c," THIS IS THE ANSWER TOTAL =",3*x-b-c
                       print "(((",c,b,a,2*x,n,")))"
                   else:
                       print "Found a value BUT..",x,x-b,x-c,3*x-b-c
                   
   
                
