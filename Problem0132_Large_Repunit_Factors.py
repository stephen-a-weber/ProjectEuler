"""
Large repunit factors
Problem 132
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.

For example, R(10) = 1111111111 = 11412719091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(109).


Answer:
843296
Completed on Sat, 6 Apr 2013, 21:06

"""
#finished with c++ and a value limit of 100000 to get them all
#
# R(k)= (10^k-1)/9 in general
#
# down below it is important to see that R(10^9) is NOT
# divisible by the prime 3.
# 3 goes into repunits...037037037
# so only a k value that is divisible b three will leave
# an R(k) divisible by three
#
# R(k)=0 mod p
# (10^k-1)/9 = 0 mod p
# from above P will never be 3 so the 9 part will never be part
# of the perfect division OR (10^k-1) must be evenly divisible by P
#
# so  10^k-1 = 0 mod P
# or  10^k   = 1 mod P
#
# 



def divide(n,R):
    
    place=1
    value=0
    shop=[]
    while place<=R:
        value=value*10+1
  
        value=value%n
        
        if value==0:
            if R%(len(shop)+1)==0:
                print "________________",len(shop),"____"
                return True
            else:
                return False
        if value in shop:
            return False
        #if len(shop)>13000:
 #         return False
        shop.append(value)
         
        place+=1
        
    if value==0:
            return True
    return False
  
 

import time
import random
ras=time.time()
n=1000000
lastPrime=0
primes=[]
 
sieve=[True]*n
for i in xrange(4,n,2):
    sieve[i]=False
for i in xrange(3,n,2):
      if sieve[i]==True:
          
          primes.append(i)
          lastPrime=i
          if i*i<n:
           for j in xrange(i*i,n,i):
             sieve[j]=False





primes.remove(5)
primes.remove(3)

these=[]
for i in primes:
    if pow(10,10**9,i)==1:
        print i
        these.append(i)
        if len(these)==40:
            break

print "the answer",sum(these)
 """
             
print "PRIMES DONE" ,time.time()-ras
primes.remove(5)
xxx=[11, 17, 41, 73, 101, 137, 251, 257, 271, 353, 401,\
     449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, \
     5051, 9091, 10753, 15361, 16001, 19841, 21001, 21401, \
     24001, 25601, 27961,37501,40961,43201,60101,62501,69857,76001,\
     76801,160001]

qwerty=10**9

c=[]
c=[r for r in primes if r >76000]
count=0
total=0
for i in c:
    print i
    level=1
    if divide(i,qwerty):

     
     count+=1
     print count,i
     total+=i
     xxx.append(i)
     
     if divide(i*i,qwerty):
         count+=1
         print count,i*i,"OPPS"
         total+=1
     if count==40:
         break
    
     
     while divide(i**level,qwerty):
        count+=1
  
        total+=i
        level+=1
        if count==40:
            print "THE ANSWER IS ",total
            break
     """

 
