"""
5-smooth totients
Problem 516
5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers.
Let S(L) be the sum of the numbers n not exceeding L such that Euler's totient function φ(n) is a Hamming number.
S(100)=3728.

Find S(1012). Give your answer modulo 232.


Answer:
939087315
Completed on Sun, 1 Nov 2015, 09:53

"""

import sys
import math

import random


n=100000
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
      
frog=[]
for i in primes[3:]:
    k=i-1
    while k//2==k/2:
        k=k/2
    while k//3==k/3:
        k=k/3
    while k//5==k/5:
        k=k/5
    if k==1:
        frog.append(i)
toad=set(frog)
for i in frog:
    for j in frog:
        if i!=j:
            toad.add(i*j)

frog=list(toad)
frog2=[r for r in frog]
for i in frog:
    frog2.append(i*3)
    frog2.append(i*5)

frog3=[r for r in frog]
for i in frog:
    frog3.append(i*2)
    frog3.append(i*5)
frog5=[r for r in frog]
for i in frog:
    frog5.append(i*2)
    frog5.append(i*3)
 
def is_Prime(n):
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
        
    if n==2 or n==3 or n==5 or n==7:
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
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  

    
    
def n2(maxm):
    b=int(math.log(maxm,2))
    a=1
    numbers=0
    for i in range(1,b+1):
        k=2**i
        numbers+=k
        for m in frog2:
            if k*m<maxm:
                numbers+=k*m
            
    return numbers
def n3(maxm):
    b=int(math.log(maxm,3))
    a=1
    numbers=0
    for i in range(1,b+1):
        k=3**i
        numbers+=k
        for m in frog3:
            if k*m<maxm:
                numbers+=k*m
    return numbers
def n5(maxm):
    b=int(math.log(maxm,5))
    a=1
    numbers=0
    for i in range(1,b+1):
        k=5**i
       
        numbers+=k
        for m in frog5:
            if k*m<maxm:
                numbers+=k*m
    return numbers
def add2(maxm,n):
    return int(math.log(maxm,2)-math.log(n,2))
def add3(maxm,n):
    return int(math.log(maxm,3)-math.log(n,3))
def add5(maxm,n):
    return int(math.log(maxm,5)-math.log(n,5))

maxm=10**12

crash=[1]

b=int(math.log(maxm,2))
for i in range(1,b+1):
    a=2**i
    crash.append(a)
    
bb=int(math.log(maxm,3))
for i in range(1,bb+1):
    a=3**i
    crash.append(a)
    
bb=int(math.log(maxm,5))
for i in range(1,bb+1):
    a=5**i
    crash.append(a)

       
#nn23
a=2*3
f2=add2(maxm,a)
for i in range(f2+1):   
    for j in range(add3(maxm,a*2**i)+1):
        k=(a*(2**i)*(3**j))
        crash.append(k)

#nn25
a=2*5
f2=add2(maxm,a)
for i in range(f2+1):   
    for j in range(add5(maxm,a*2**i)+1):
        k=(a*(2**i)*(5**j))
        crash.append(k)


#nn23
a=3*5
f3=add3(maxm,a)
for i in range(f3+1):   
    for j in range(add5(maxm,a*3**i)+1):
        k=(a*(3**i)*(5**j))
        crash.append(k)

#nn235
a=2*3*5
f2=add2(maxm,a)
for x in range(f2+1):
    for y in range(add3(maxm,a*2**x)+1):
        for z in range(add5(maxm,a*(2**x)*(3**y))+1):
            k=(a*(2**x)*(3**y)*(5**z))
            crash.append(k)
print(len(crash))
crash.sort()
burn=[]
for i in crash:
    if is_Prime(i+1):
        if i+1<=maxm:
           burn.append(i+1)
print (len(burn))
burn.remove(2)
burn.remove(3)
burn.remove(5)

import copy
pr=copy.deepcopy(burn)
p=1
for i in range(len(burn)):
    p=p*i
    if p>maxm:
        break
d=i
print("going for ",d)



y=len(pr)
hold=copy.deepcopy(pr)
tear=[7, 11, 13, 17, 19, 31, 37, 41, 61]
pea=burn.index(61)
cry=burn[pea+1:]
i=1
cell=copy.deepcopy(burn)
rr=len(burn)

for i in range(rr-1):
        
        for j in range(i+1,rr):
            s=burn[i]*burn[j]
            if s<=maxm:
                cell.append(s)
            else:               
                break

for i in range(rr-2): 
        for j in range(i+1,rr-1):
                ss=burn[i]*burn[j]
                if ss>maxm:
                    break
                for k in range(j+1,rr):
                        s=ss*burn[k]
                        if s<=maxm:
                            cell.append(s)
                        else:
                           
                            break

for i in range(rr-3):
        for j in range(i+1,rr-2):
                ss=burn[i]*burn[j]
                if ss>maxm:
                    break
                for k in range(j+1,rr-1):
                        sss=ss*burn[k]
                        if sss>maxm:
                            break
                        for l in range(k+1,rr):
                            s=sss*burn[l]
                            if s<=maxm:
                                cell.append(s)
                            else:
                                break

for i in range(rr-4):
        for j in range(i+1,rr-3):
                ss=burn[i]*burn[j]
                if ss>maxm:
                    break
                for k in range(j+1,rr-2):
                        sss=ss*burn[k]
                        if sss>maxm:
                            break
                        for l in range(k+1,rr-1):
                                t=sss*burn[l]
                                if t>maxm:
                                    break
                                for m in range(l+1,rr):
                                    s=t*burn[m]
                                    if s<=maxm:
                                        cell.append(s)
                                    else:       
                                        break


for i in range(rr-5):
    for j in range(i+1,rr-4):
        ss=burn[i]*burn[j]
        if ss>maxm:
            break
        for k in range(j+1,rr-3):
            sss=ss*burn[k]
            if sss>maxm:
                break
            for l in range(k+1,rr-2):
                t=sss*burn[l]
                if t>maxm:
                    break
                for m in range(l+1,rr-1):
                    tt=t*burn[m]
                    if tt>maxm:
                        break
                    for n in range(m+1,rr):
                        s=tt*burn[n]
                        if s<=maxm:
                            cell.append(s)
                        else:       
                            break

for i in range(rr-6):
    for j in range(i+1,rr-5):
        ss=burn[i]*burn[j]
        if ss>maxm:
            break
        for k in range(j+1,rr-4):
            sss=ss*burn[k]
            if sss>maxm:
                break
            for l in range(k+1,rr-3):
                t=sss*burn[l]
                if t>maxm:
                    break       
                for m in range(l+1,rr-2):
                    tt=t*burn[m]
                    if tt>maxm:
                        break
                    for n in range(m+1,rr-1):
                        ttt=tt*burn[n]
                        if ttt>maxm:
                            break
                        for b in range(n+1,rr):
                            s=ttt*burn[b]
                            if s<=maxm:
                                cell.append(s)
                            else:       
                                break

for i in range(rr-7):
    for j in range(i+1,rr-6):
        ss=burn[i]*burn[j]
        if ss>maxm:
            break
        for k in range(j+1,rr-5):
            sss=ss*burn[k]
            if sss>maxm:
                break
            for l in range(k+1,rr-4):
                t=sss*burn[l]
                if t>maxm:
                    break
                for m in range(l+1,rr-3):
                    tt=t*burn[m]
                    if tt>maxm:
                        break
                    for n in range(m+1,rr-2):
                        ttt=tt*burn[n]
                        if ttt>maxm:
                            break
                        for b in range(n+1,rr-1):
                            tttt=ttt*burn[b]
                            if tttt>maxm:
                                break
                            for v in range(b+1,rr):
                                s=tttt*burn[v]
                                if s<=maxm:
                                    cell.append(s)
                                else:       
                                    break

for i in range(rr-8):
    for j in range(i+1,rr-7):
        ss=burn[i]*burn[j]
        if ss>maxm:
            break
        for k in range(j+1,rr-6):
            sss=ss*burn[k]
            if sss>maxm:
                break
            for l in range(k+1,rr-5):
                t=sss*burn[l]
                if t>maxm:
                    break
                for m in range(l+1,rr-4):
                    tt=t*burn[m]
                    if tt>maxm:
                        break
                    for n in range(m+1,rr-3):
                        ttt=tt*burn[n]
                        if ttt>maxm:
                            break
                        for b in range(n+1,rr-2):
                            tttt=ttt*burn[b]
                            if tttt>maxm:
                                break
                            for v in range(b+1,rr-1):
                                zz=tttt*burn[v]
                                if zz>maxm:
                                    break
                                for c in range(v+1,rr):
                                    s=zz*burn[c]
                                    if s<=maxm:
                                        cell.append(s)
                                    else:       
                                        break


pr=cell


pr.sort()



   


print("found all the hammingprimes")
        
print("length =",len(pr))
crash.sort()
tree=[r for r in crash]
for r in pr:
    for s in crash:
        k=r*s
        if k<=maxm:
            tree.append(k)
        else:
            break


print("the answer is ",sum(tree)%(2**32))



def factor(n):
    m=[]
    index=0
    while n!=1:
        p=primes[index]
        if n//p==n/p:
            m.append(p)
            n//=p
            
        if n//p!=n/p:
            index+=1
    return m

def phi(n):
    b=factor(n)
    m=set(b)
    
    for i in m:
        n=n*(1-1/i)
    return int(n)

"""
frog=[]
h=maxm
for i in range(1,h+1):
    
    k=phi(i)
    j=k
    while j//2==j/2:
        j/=2
    while j//3==j/3:
        j/=3
    while j//5==j/5:
        j/=5
    if j==1:
        frog.append(i)

       

print ("for ",h," the answer is ",sum(frog))

"""
"""
or  500  the answer is  62625
>>> ================================ RESTART ================================
>>> 
for  1000  the answer is  203813
>>> ================================ RESTART ================================
>>> 
for  5000  the answer is  3054007
>>> 
"""
