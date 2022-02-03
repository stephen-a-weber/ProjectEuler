"""
Primes with runs
Problem 111
Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d	M(4, d)	N(4, d)	S(4, d)
0	2	13	67061
1	3	9	22275
2	3	1	2221
3	3	12	46214
4	3	2	8888
5	3	1	5557
6	3	1	6661
7	3	9	57863
8	3	1	8887
9	3	7	48073
For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).


Answer:
612407567715
Completed on Wed, 20 Mar 2013, 06:27

"""


import random



        
 
def is_Prime(n):
    #Miller-Rabin test for prime
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
 
    for i in range(5):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  
 

s=0#sum S(10,d)
n=9# number of digits for maximum
storage={}
for d in range(0,10):
    storage[d]=0
 
b=0
can=[]
golf=0
total=0
for d in range(0,1):
        golf=0
        total=0
        tree=False
        for k in range(1,10):#all but d
            b=k
            for kk in range(1,10):
                b+=kk*10**9
             
                #print b
                 
               
                total+=1                  
                if is_Prime(b):
                    can.append(b)
                    #print "YEES"
                    #print b
                    tree=True
                    golf+=1
                b=k
 
        s+=sum(can)           
        storage[d]+=sum(can)
        can=[]
        if tree:
            print "success for zero"
        else:
            print "failure for current ",d
        print "Found these number of primes for ",d, " :",golf

print total






for d in [1,3,4,5,6,7,9]:
    tree=False
    golf=0
    for i in range(0,10):
        b=0
        p=[r for r in range(0,10) if r !=d]
        for k in p:#all but d
            b+=k*10**(i)
             
         
            for j in range(0,10):
               
               if i!=j:
                
                  b+=d*10**j
                  
              
            if b>999999999:
                 
                if is_Prime(b):
                    can.append(b)
                    #print "YEES"
                    tree=True
                    golf+=1
            b=0
    s+=sum(can)
    storage[d]+=sum(can)
    can=[]
    if tree:
       print "success for ",d
    else:
       print "failure for current ",d
    print "Found these number of primes for ",d, " :",golf


    
for d in [ 2,8]:
    tree=False
    golf=0
    p=[r for r in range(0,10) if r !=d]
    print p
    b=0
    for i in range(0,9):
     
  
        
        for ii in range(i+1,10):
                 
                b=0
                for k in p:#all but d
                    b=k*(10**(i ))
                     
                    for kk in p:
                        b+=kk*10**(ii)
                     
  
                        for j in range(0,10):
                           
                           if i!=j and ii!=j:
                            
                              b+=d*(10**j)
                       
                              
                          
                        if b>999999999:
                            #print b 
                            if is_Prime(b):
                                can.append(b)
                                #print "YEES"
                                tree=True
                                golf+=1
                        b=k*(10**(i ))
    storage[d]+=sum(can)
    s+=sum(can)
    can=[]
    if tree:
       print "success for ",d
    else:
       print "failure for current ",d
    print "Found these number of primes for ",d, " :",golf
    
x=0
for i  in range(10):
	x=x+storage[i]
print x
