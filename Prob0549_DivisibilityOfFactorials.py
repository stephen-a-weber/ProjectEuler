"""
Divisibility of factorials
Problem 549
The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
So s(10)=5 and s(25)=10.
Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
S(100)=2012.

Find S(108).


Answer:
476001479068717
Completed on Sat, 21 May 2016, 10:31


"""
import time
import math
import sys
import pickle
rrr=time.time()
n=10**8
exponent={}
cage=[0 for x in range(n+1)]
D=0
single=False
total=0
findall={}
f=open("/Users/lisa/Python/primes.p","rb")
primes=pickle.load(f)
print ("primes loaded in ",time.time()-rrr)

if n!=10**8: 
    xxx=0
    for i in range(len(primes)):
        if primes[i] >n:
            break
        xxx=i+1
    primes=primes[:xxx]
     
    print(primes[-1]) 
"""           
                    
sieve=[True]* n
primes=[2]


for i in range(4,n,2):
   
    sieve[i]=False
for i in range(3,n,2):
    if sieve[i]==True:
        primes.append(i)        
        for j in range(i*i,n,i):
            sieve[j]=False
 
"""

#creation of findall. max exponent of prime <n
for i in range(len(primes)):
    exp=math.floor(math.log(n,primes[i]))
    findall[primes[i]]=exp
 
print (time.time()-rrr," seconds to find max counts")




def fasterFactors(p,n):
 #   r=time.time()
    count=0
    while n>1:
        n//=p
        count+=n
 #   print(time.time()-r)
    return count
#returns count of prime factors from 1-n

def loop(n,p,x):
        # finds maximum power of p less then n        
        ex = findall[p]
        k=p**ex
        while fasterFactors(p,k)>x:
            ex-=1
            k=p**ex
        return k

def maximumNumber(p,x):
    if x==1:
        return p
    # find number with x factors of prime p   
    k=loop(p*x,p,x)        
    place=k
    while x>0:
        guess=fasterFactors(p,k)
        
        x-=guess
        if x>p:
            k=loop(p*x,p,x)

            place+=k
        elif x>0:
            place+=x*p
            x=0
    return place


#creation of final answer ..cage
#first loop places all the distinct primes
#and their strict powers throughout N
 

for p in primes:
    x=findall[p]
    
    P=p
    pp=P    
    for y in range(1,x+1):
        theNum=maximumNumber(p,y)
        cage[P]=theNum
        P*=p
    
 
#then each prime and some factor reaches other numbers
# this next loop through checks for the highest
#cage value that then fits both factors
 

 

for p in primes:
     
    D=cage[p]#this always equals p
     
    for X in range(2,n+1):#this is any other factor
        x=X*p
        if x>n:
            break
        if D>cage[x]:
            cage[x]=D
        if cage[X]>cage[x]:
            cage[x]=cage[X]
  


total+=sum(cage)
    
    
print("the answer is ",total)

print(time.time()-rrr)
 
 
"""

the answer is  476001479068717
358.47135400772095 seconds + primes
"""
 
 
