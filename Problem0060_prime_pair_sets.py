"""
Prime pair sets
Problem 60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


Answer:
26033
Completed on Thu, 31 Jan 2013, 03:51

"""


import time
import random
ras=time.time()
n=10000
lastPrime=0
primes=[]
#primes.append(2)
sieve=[True]*n
for i in xrange(4,n,2):
    sieve[i]=False
for i in xrange(3,n,2):
      if sieve[i]==True:
          primes.append(i)
          lastPrime=i
          if i*i<n:
           for j in xrange(i*i,n,i):
             sieve[j]=False
print "PRIMES DONE" ,time.time()-ras
waste={}
 
import random
 
 


def concat(a ,b):
    c=1
    while True:
        if b/(10**c)==0:
            break
        else:
            c=c+1
    return a*10**c+b

        
 
def is_Prime(n):
    #Miller-Rabin test for prime
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
  
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(5):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  
        
        
    
for i in primes:
    gin=set()
    for j in primes:
        if i is not j:
             
            
                if is_Prime(concat(i,j)) and is_Prime(concat(i,j)) :
                     
                        
                    gin.add(j)
    if len(gin)>4:
        waste[i]=gin

storage=set()
 
 
 
for i in waste:
   
 
    
    for j in waste[i]:
        s=i+j
        p=[i,j]
        p.sort()
        p=tuple(p)
        storage.add(tuple((s,p))) 
print "STARTING MAIN LOOP",time.time()-ras
print "STORAGE IS at",len(storage)
bestlen=0
while storage:
    weight,path=storage.pop() 
    #print weight,path
    #print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    holding=set()
    coin =True
    if len(path)>bestlen:
        bestlen=len(path)
    if len(path)==5:
        print path
        print weight
        print "SOLUTION___________________________________________"
        break
    for each in path:
        #print each,"-->",waste[each]
        if coin:
          holding=waste[each]
          coin=False
        holding=holding.intersection(waste[each])
    #print holding
    for i in holding:
        if i not in path:
         
            h=  list(path)+[i]
            h.sort()
            h=tuple(h)
            w=weight+i
            storage.add(tuple([w,h]))
    
        
    
print "THE LONGEST CHAIN OF PRIMES IS ",bestlen    

print "Time to completion :",time.time()-ras
