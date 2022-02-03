"""
Prime pair connection
Problem 134
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2  p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find  S for every pair of consecutive primes with 5  p1  1000000.


Answer:
18613426663617118
Completed on Wed, 24 Apr 2013, 13:02


"""

import time
r=time.time()

 

def primes(n):
    #primes to n
    primes=[2]
    sieve=[True]*n
    for i in range(4,n,2):
        sieve[i]=False
    for i in range(3,n,2):
        if sieve[i]==True:
            primes.append(i)
            for j in range(i*i,n,i):
                sieve[j]=False
    return primes
 
def possibles():
  
    values={}
    for n in [1,3,5,7,9]:
  
        values[n]={}
        for j in range(0,10):
            k=(n*j)%10
            if k not in values[n]:
  
                
                values[n][k]=j
    return values
            
def flub(a,b):
    aa=len(str(a))
    bb=len(str(b))
    
    n=1
    x=(n*b)%10**aa
    
    
    while x!=a:
        n=n+2
        x=(n*b)%10**aa
        #print n,x,a,b,a*n
     
    #print x,":",b," * ",n,"==",a,"--->",b*n
    return b*n

def main():
    n=1000004
    p=primes(n)
    p.remove(2)
    p.remove(3)
    g=0
    
    f=len(p)
    value=possibles()
    """
    for i in value:
        for j in value[i]:
            print i,j,value[i][j]
    """
    """ #This was the absolute brute force flub() ;)
    for i in range(0,f-1):
        a=p[i]
        b=p[i+1]
        g+=flub(a,b)
        if i%100==0:
            
          print f,":",i,"GRANDTOTAL = ",g
    print f,":",i,"GRANDTOTAL = ",g
    """
    """
    My theory was that I created a dictionary of just the lowest ..welll
    all but five had only one from divisor quotient and the multiple for
    single digits (i.e. given 3 divided by 7 I wanted 9) this is value[][]

    i get each pair
    find the length of the first low value one
    find the last digit of each
    and the value that works I create that as my next higher digit in the answer
    multiply it by the higher prime subtract that from the lower prime(and later my carry value)
    with the caveat that if that subtraction is less then zero I add
    10**(length of low prime +1) like I carried a one over in subtraction


    I precalculated the last prime as 1000003
    """
    for prime in range(f-1):
        a=p[prime]
        b=p[prime+1]
        x=1
        while a/10**x!=0:
            x=x+1
        y=b%10
        answer=0
        h=a
        for i in range(x):
            z=h%10
             
            m=value[y][z]
            #print y,z,m,i
            answer+=m*10**(i)
            v=(m*b)%10**x
            if h-v<0:
                h+=10**(x+1)

            h=h-v
            h=h/10
        g+=b*answer
        if prime%10000==0:
           print f,":",a,b,answer,b*answer,"GRANDTOTAL = ",g
          
    print f,":",a,b,answer,b*answer,"GRANDTOTAL = ",g



main()
