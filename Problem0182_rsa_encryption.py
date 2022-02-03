# -*- coding: utf-8 -*-
"""
RSA encryption
Problem 182
The RSA encryption is based on the following procedure:

Generate two distinct primes p and q.
Compute n=pq and φ=(p-1)(q-1).
Find an integer e, 1eφ, such that gcd(e,φ)=1.

A message in this system is a number in the interval [0,n-1].
A text to be encrypted is then somehow converted to messages (numbers in the interval [0,n-1]).
To encrypt the text, for each message, m, c=me mod n is calculated.

To decrypt the text, the following procedure is needed: calculate d such that ed=1 mod φ, then for each encrypted message, c, calculate m=cd mod n.

There exist values of e and m such that me mod n=m.
We call messages m for which me mod n=m unconcealed messages.

An issue when choosing e is that there should not be too many unconcealed messages. 
For instance, let p=19 and q=37.
Then n=19*37=703 and φ=18*36=648.
If we choose e=181, then, although gcd(181,648)=1 it turns out that all possible messages
m (0mn-1) are unconcealed when calculating me mod n.
For any valid choice of e there exist some unconcealed messages.
It's important that the number of unconcealed messages is at a minimum.

Choose p=1009 and q=3643.
Find the sum of all values of e, 1eφ(1009,3643) and gcd(e,φ)=1, so that the number of unconcealed messages for this value of e is at a minimum.


Answer:
399788195976
Completed on Wed, 1 May 2013, 18:07
"""
import fractions
def mod_exp(a, b, q):
    """return a**b % q"""
    val = 1
    mult = a
    while b > 0:
        odd = b & 1 # bitwise and
        if odd == 1:
            val = (val * mult) % q
            b -= 1
        if b == 0:
            break
        mult = (mult * mult) % q
        b = b >> 1 # bitwise divide by 2
    return val

def modular_exponent(base, exponent, mod):
    """\
    Modular exponentiation through binary decomposition.
 
    We use the same technique as for the binary exponentiation above in
    order to find the modulo of our very large exponent and an arbitrary
    integer mod.
    """
    exponent = bin(exponent)[2:][::-1]
 
    x = 1
    power = base % mod
    for i in range(0, len(exponent)):
        if exponent[i] == '1':
            x = (x * power) % mod
        power = (power ** 2) % mod
    return x
import time
ras =time.time()
"""
for i in range(10000):
    modular_exponent(1777,367,1885)
print time.time()-ras
ras =time.time()
for i in range(10000):
    pow(1777,367,1885)
print time.time()-ras
for i in range(10000):
    mod_exp(1777,367,1885)
print time.time()-ras
"""
phi=1008*3642
p=1009
q=3643
 
n=p*q
storage={}
f=[]
for e in xrange(2,phi):
     
    if fractions.gcd(e,phi)==1:
       storage[e]=0
       f.append(e)
print "starting"
 
 
for e in f:
       
            
   total=(1 + fractions.gcd(e-1, p-1))*(1 + fractions.gcd(e-1, q-1))
   storage[e]=total
print "done check"
g=100000000000000000000000000000000
bestE=0
for i in storage:
 
    if storage[i]<g:
        g=storage[i]
        bestE=i

print bestE
best=storage[bestE]
frog=0
for i in storage:
    if storage[i]==best:
        frog+=i

print "THe Answer is ",frog
