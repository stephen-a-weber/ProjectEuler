"""
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


Answer:
4179871
Completed on Thu, 24 Jan 2013, 20:48
"""



import time
RAS=time.time()

theset=[]
    
n=28124
 
 
primes=[2]
sieve=[True]*n
 
total=[set([1]) for r in range(n)] 
 
 
  
 
for i in xrange(3,n,2):    
    if sieve[i]:        
        primes.append(i)
        if n>i*i:          
            for j in xrange(i*i,n,i):               
                sieve[j]=False
 

for i in primes:
    for j in range(i,n,i):
        for x in range(j+j,n,j):
            total[x].add(j)
         
            
            
 
 

total=[sum(r) for r in total]
nonAbundant=[r for r in range(1,n) if total[r]>r]


c=set()
for a in nonAbundant:
    for b in nonAbundant:
        if a+b<n:
            c.add(a+b)
        else:
            continue
total=0
for x in range(1,n):
    if x not in c:
        total+=x

print "The answer is ",total
print "This took ",time.time()-RAS," seconds"
