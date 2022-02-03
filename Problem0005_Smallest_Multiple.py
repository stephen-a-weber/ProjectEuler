"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


Answer:
232792560
Completed on Tue, 22 Jan 2013, 03:07
"""
 
 
class prime_factors:
    def __init__(self):
        self.primes=[2]
        self.sieve=[True]*7000
        self.make_primes(7000)
         
                         
   
    def make_primes(self,n):
        for i in range(4,n,2):
            self.sieve[i]=False
        for i in range(3,n,2):
            if self.sieve[i]==True:
                self.primes.append(i)
                for j in range(i*i,n,i):
                    self.sieve[j]=False

 
a=prime_factors()
def factor(n):
    x=int(n**.5)+1
    factors=list()
    for i in a.primes:
        while n%i==0:
            factors.append(i)
            n=n/i
     
    return factors
 
 
gullet=[]
hat=[]
for i in range(1,21):
     g=factor(i)
     hat=[]
     
     for i in g:
         if i not in gullet:
             hat.append(i)
         else:
             hat.append(i)
             gullet.remove(i)
     for i in hat:
         gullet.append(i)
   
t=1
for i in gullet:
    t*=i

print "The answer is ", t
