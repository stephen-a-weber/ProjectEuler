"""
Pandigital Fibonacci ends
Problem 104
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""
import time
ras=time.time()
def pandigital(n):
    f=set(range(1,10))
   
    
    g=set([int(r) for r in n])
    
    if f.difference(g)==set([]):
        return True
    return False


 
 
k=3
a=[1]*3
s=2
cat=True
dog=True
while cat:
    b=(s-2)%3
    e=(s-1)%3
    a[s]=a[b]+a[e]
    Fib=str(a[s])
    #print k,Fib
    if k%20000==0:
        print k,Fib[:9],Fib[-9:]
        print time.time()-ras
        print "---"
         
            
             
 
    if len(Fib)>9:
        begin= Fib[:9]
        end= Fib[-9:]
         
        if pandigital(begin) and pandigital(end):
             
           
                print "SOLUTION:___________________________________________________"
                print "************************************************************"
                
                print k
                
                cat=False
         
            
 
    s+=1
    s=s%3
    k=k+1
     
    
print "time", time.time() -ras
