"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?



"""
total=0
n=1
a=1
cat=True
import time
r=time.time()
while cat:
    j=len(str(a**n))
    if j==n:
        total+=1
         
        print  a,"**",n," has ",j," length"
        a=a+1 
       
    if j<n:
        a=a+1
    if j>n:
        n=n+1
        a=1
        
        #print "Trying n of ",n," FAILED...."
    
    
    if n>100:
        cat=False
        print total
    
