"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
6857
Completed on Mon, 21 Jan 2013, 23:53
"""
import time
ras=time.time()

class prime_factors:
    def __init__(self,n):
        self.primes=[2]
        self.sieve=[True]*7000
        self.make_primes(7000)
        self.factor(n)
                         
    def factor(self,n):
        solution=0
        primeIterator=0
        while n!=1:
            solution=self.primes[primeIterator]
            if n%solution==0:
                n/=solution
            else:
                primeIterator+=1
            if primeIterator==len(self.primes):
                print "Need a Greater Prime List"
                return
        print "The Answer is ",solution
    def make_primes(self,n):
        for i in range(4,n,2):
            self.sieve[i]=False
        for i in range(3,n,2):
            if self.sieve[i]==True:
                self.primes.append(i)
                for j in range(i*i,n,i):
                    self.sieve[j]=False
 

 
cat=prime_factors(600851475143)

print "Time Took :",time.time()-ras
 
 
 
