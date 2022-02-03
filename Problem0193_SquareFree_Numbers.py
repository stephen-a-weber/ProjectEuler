"""
Squarefree Numbers
Problem 193
A positive integer n is called squarefree, if no square of a prime divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.

How many squarefree numbers are there below 250?


Answer:
684465067343069
Completed on Sun, 19 May 2013, 13:21

"""

import time
ras=time.time()
N=2**50
n=N 
squaredprime=int(n**.5)
n=squaredprime+1
primes=[]
 
primes.append(2)
sieve=[True]*n
for i in xrange(4,n,2):
    sieve[i]=False
for i in xrange(3,n,2):
      if sieve[i]==True:
          primes.append(i)
     
           
          for j in xrange(i*i,n,i):
             sieve[j]=False


n=N 
total=0
 
print "Finished Calculating primes" 
#item in cache::: Inclusion-Exclusion Algorithm

cache=[[1,1,-1]]
def recursion(lastprime,product,sign,total): 
 #   print "Recursion",lastprime,product,int(squaredprime/product)
    
   
     
    sign=-sign
    limit=int(squaredprime/product)
    
   
 #  newprimes=[r for r in primes if r>lastprime and r<=limit]
    for p in primes:
        if p>limit:
            return total
        if p<=lastprime:
            continue
    
     
     
         
        newproduct=p*product
        d= sign*int((n-1)/newproduct**2)
 #       print "...",p,"...",newproduct,"...",sign,"...",total
        total+=recursion(p,newproduct,sign,d)
    
    return total
e=recursion(1,1,-1,0)
print N,e,"values"
print N-1-e


print time.time()-ras






