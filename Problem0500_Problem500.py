"""
Problem 500!!!
Problem 500
The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.

Find the smallest number with 2500500 divisors.
Give your answer modulo 500500507.


Answer:
35407281
Completed on Tue, 27 Oct 2015, 05:25

"""
import sys
import math
import time
import copy
import itertools

def lastprime(n):
    cat=False
    while not cat:
        try:
            if n<2:
                print ("opps")
                sys.exit()
            if n in primes:
                return n
            else:
                n=n-1
        except:
            n=n-1
            print(n)
            

r=time.time()
n=7376508
sieve=[True]* n
primes=[2]
toad=[r for r in range(n)]
frog=[0]*100

for i in range(4,n,2):
    sieve[i]=False
    
 


for i in range(3,n,2):

    if sieve[i]==True:
        primes.append(i)
         
    
        
        
         
        for j in range(i*i,n,i):
            sieve[j]=False
#524288 is 2**19
# so exponent of 15 is maximum to keep the first prime of TWO below whatever
#number near the end of the 500500th prime.
#o(n)= π (alpha+1)
# since the number of  divisors are powers of two .. alpha must be in the
#sequence (1,3,7,15,31..)

# so the first prime goes up in exponent from one to 15 . a difference
# of 14. So 500499 (based from zero) primes minus 14 of the end primes
# leaves us with 500485 as last prime.
# 2**14 *...

# nope
# primes at end used together. what is one less then the power of two
# that gives an exponent that is more then that left
# we start with 500500 primes
# the sequence has one at 2**262143
#the next in the sequence would be 2**524287 which is greater
# then 500500
#so the next number is 500500-262142=238358
"""
0 1
1 3
2 7
3 15
4 31
5 63
6 127
7 255
8 511
9 1023
10 2047
11 4095
12 8191
13 16383
14 32767
15 65535
16 131071
17 262143
18 524287
19 1048575
"""
# 
# for the exponent of the next prime 3. we can fill 131071
# spots or remove them from our 238358 - 131070 = 107288 left

# for the exponent of the next prime 5. we can fill 65535
# 107288 - 65534 = 41754

# next prime 7. using 32767. 41754-32766 = 8988
#
# prime 11. using 8191.  8988-8190 = 798

# prime 13. using 511. 798 -510 = 288

# prime 17. using 255. 288-254 = 34

# prime 19. using 31. 34 - 30 = 4

# prime 23. using 3. 4-2 = 2

# prime 29 and prime 31 to the power of one.

# so the exponents listed above charted
"""
2 ** 262143     (alpha+1) must be a power of 2 for divisors

2**18 =262144 
"""

a=primes[-1]
larger=[r for r in primes]
for i in primes:
    for j in range(1,25):
       
        g=i**(2**j)
        if g<a:
            larger.append(g)
        else:
            break
        

larger.sort()
print("done here...")
answer=1
for i in range(500500):
    answer*=larger[i]
    answer%=500500507
print("the answer is ",answer)

#ok finally the solution argument goes like this
# we know that there must be 500500 terms in the answer
# with each term being on or off as a piece in a divisor
# so p1*p2*p3*p4...*pn  all to power 1. this adds to 500500
# for the first 500500 primes
# but anyprime raised to the power of 2**k adds a lower choice
#then some of the higher primes . Think about it like
# a byte in computer terms. Each power of 2 adds another
#bit to the byte. 2^1   2^2   2^4   2^8
# we then already have 2^3 = on divisors of 2^1 and 2^2
# or 2^7 = divisors of 2^1 2^2 2^4  4+2+1=7
# so take least numbers of the first 500500 primes
# with each one raised to incremental powers of 2

#all numbers are of the form p1^a1  * p2^a2 * p3^a3
# this gives least number .
#the trick i missed above is seeing that the number of
#terms to get 2^500500 divisors is to still keep
#500500 terms. And look at it like each one is either
# part of a particular divisor or is not. on or off.
