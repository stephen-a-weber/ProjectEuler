"""
Prime triplets
Problem 196
Build a triangle from all positive integers in the following way:

 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
. . .

Each positive integer has up to eight neighbours in the triangle.

A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.

For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
Then S(8)=60 and S(9)=37.

You are given that S(10000)=950007619.

Find  S(5678027) + S(7208785).


Answer:
322303240771079935
Completed on Fri, 5 Apr 2013, 18:44

"""

import time
ras=time.time()
import random

import itertools

        
 
def is_Prime(n):
    #Miller-Rabin test for prime
    if n==1:
        return False
    if n==2:
        return True
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
 
    for i in range(10):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True
g={}
d={}
a=set()
#row=5678027#THE ANSWER IS : 79697256800321526
#row=7208785#THE ANSWER IS : 242605983970758409


#row=10000

total=0
#63480541604260474+201630334826257720
p1row=row-1
p2row=row-2
n1row=row+1
n2row=row+2
n3row=row+3
    
 
digit=row*(row-1)/2+1#first digit of row in question
 
p1digit=p1row*(p1row-1)/2+1
p2digit=p2row*(p2row-1)/2+1
n1digit=n1row*(n1row-1)/2+1
n2digit=n2row*(n2row-1)/2+1
n3digit=n3row*(n3row-1)/2+1
h=0
 
if digit%2==0:
    h=1
else :
    h=0
print "two"
 
for i in xrange(digit+h,n1digit,2):#main row primes
    if is_Prime(i):
         
        a.add(i)
 
     
up1=digit-p1digit
up2=p1digit-p2digit
down1=n1digit-digit
down2=n2digit-n1digit
 
 
print "three"
print time.time()-ras
for i in  a:
    count=1
    highest=[]
    lowest=[]
    for x in xrange(i-up1-1,i-up1+2):
        if x <p1digit or x>digit-1:
            continue
        if is_Prime(x):
            count+=1
            for y in xrange(x-up2-1,x-up2+2):
                if y<p2digit or y>p1digit-1:
                    continue
                if is_Prime(y):
                    count+=1
            if x==i-up1-1 and is_Prime(i-2) and i-2>=digit:
                count+=1
            if x==i-up1+1 and is_Prime(i+2)and i+2<=n1digit-1:
                count+=1
    #Now downlooking
    for x in xrange(i+down1-1,i+down1+2):
        if x<n1digit or x>n2digit-1:
            continue
        if is_Prime(x):
            count+=1
            for y in xrange(x+down2-1,x+down2+2):
                if y<n2digit or y>n3digit-1:
                    continue
                if is_Prime(y):
                    count+=1
                if x==i+down1-1 and is_Prime(i-2) and i-2>=digit:
                    count+=1
                if x==i+down1+1 and is_Prime(i+2) and i+2<=n1digit-1:
                    count+=1
    if count>=3:
        total+=i
print "THE ANSWER IS :",total
print time.time()-ras
