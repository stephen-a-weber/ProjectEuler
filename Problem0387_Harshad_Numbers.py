"""
Harshad Numbers
Problem 387
A Harshad or Niven number is a number that is divisible by the sum of its digits. 
201 is a Harshad number because it is divisible by 3 (the sum of its digits.) 
When we truncate the last digit from 201, we get 20, which is a Harshad number. 
When we truncate the last digit from 20, we get 2, which is also a Harshad number. 
Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a right truncatable Harshad number.

Also: 
201/3=67 which is prime. 
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime. 
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable. 
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 1014.


Answer:
696067597313468
Completed on Sun, 19 May 2013, 19:08

"""

import random

import itertools

        
 
def is_Prime(n):
    if n==2:
        return True
    if n==0 or n==1 or n%2==0:
        return False
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
Ptotal=0
storage=range(1,10)
for t in range(12):
   container=[]
   while storage:
       a=storage.pop()

       
       for i in range(0,10):
           b=a*10+i
     
           total=i
           x=a
           for k in range(0,t+2):
               total+=x%10
               x/=10
           #print a,b,total
            
 
           if b%total==0:
               container.append(b)
               aP=b/total
               
               
               if is_Prime(aP):#strong harsgad number
 #                  print b,":",
                   for ii in range(1,10,2):
                       c=b*10+ii
                       if is_Prime(c):
 #                         print c ,
                          Ptotal+=c
 #                  print
                   pass
                          
       
                   
        
   storage=container[:]
   container=[]
print Ptotal             
               
           
           






       
   
