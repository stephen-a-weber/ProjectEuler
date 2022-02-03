"""
Investigating a Prime Pattern
Problem 146
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?


Answer:
676333270
Completed on Thu, 4 Apr 2013, 14:03
"""

import time
ras=time.time()
import random
import itertools
 
 
def isPrime(n):
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
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True
def check(p):
    
    if isPrime(p+1):
        #print p,"P+1"
      
        
            
            if isPrime(p+3):

         
         
                        if isPrime(p+7):
                                    
                                                if isPrime(p+9):
                                                    
                                                    if isPrime(p+13):
                                                         
                                                            if not isPrime(p+21):
                                                                 if isPrime(p+27):
                                                                   return True
                                                                 else:
                                                                   return False
                                                            else:
                                                                return False
                                                        
                                                             
                                                    
                                                    else:
                                                        return False
                                                else:
                                                    return False
                                     
                        else:
                            return False
                        
            else:
                return False
            
         
    else:
        return False



        
count=0
sumIntegers=0
storage=[]
for i in range(10,150000000,10):
  if ((i%7==3 or i%7==4) and not(i%3==0)):
    
    p=i*i
     
     
    if check(p):
        print i,time.time()-ras
        count+=1
        sumIntegers+=i
        storage.append(i)

 
print sumIntegers
print time.time()-ras
