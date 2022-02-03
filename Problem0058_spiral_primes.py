#Spiral Primes (problem 58)

"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?"
"""
import time
r=time.time()
n=1000000000
primes=set()
primes.add(2)
sieve=[True]*n
for i in xrange(4,n,2):
    sieve[i]=False
for i in xrange(3,n,2):
    if sieve[i]==True:
        primes.add(i)
        for j in xrange(i*i,n,i):
            sieve[j]=False

total=100
print "Time to make primes ",time.time()-r 
start=0
numberPrimes=0
numberNotPrimes=0
while total>=.1:
   start=start+1
   #print (2*start+1)**2-6*start,(2*start+1)**2-4*start,(2*start+1)**2-2*start,(2*start+1)**2 ,
   road=(2*start+1)**2
   if road>n:
        print "ending ",total
        total=.001
   else:
    if road-6*start in primes:
        numberPrimes+=1
    else:
        numberNotPrimes+=1
    if road-4*start in primes:
        numberPrimes+=1
    else:
        numberNotPrimes+=1
    if road-2*start in primes:
        numberPrimes+=1
    else:
        numberNotPrimes+=1
    if road        in primes:
        numberPrimes+=1
    else:
        numberNotPrimes+=1

    total=float(numberPrimes)/(float(numberNotPrimes)+float(numberPrimes)+1)
    #print "layer ->",start,"      percentage",numberPrimes," / ",numberNotPrimes+numberPrimes+1,"  ",total
    #print  start,"   ",total
     

print (2*start+1) ,start  
print time.time()-r






    

    

    
