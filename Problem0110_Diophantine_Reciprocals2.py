"""Diophantine reciprocals II
Problem 110
In the following equation x, y, and n are positive integers.

1

x
+	
1

y
=	
1

n
It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million?

NOTE: This problem is a much more difficult version of problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.
"""



primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
import itertools
divisors=[2,2,1,1,1,1,0,0,0,0,0,0,0,0]

def divide():
    total=1
    for i in divisors:
        total*=(2*i+1)
    return total

def  number():
    total=1
    for i in range(0,14):
        total*=primes[i]**divisors[i]
    return total

  
        
x=10000000000000000000000000000000

d=range(7)
 
     
for j in itertools.product(d,repeat=19):
            divisors=list(j)
            divisors.reverse()
            num=number()
            if divide()>7999999:
                if num<x:
                    x=num
                    print x,"   ",divisors
        
            """    
            print divisors
            print "the num is ",num
            print "This gives a total number of divisors of ",divide()
            """ 
            
            """
614889782588491410
87562704385856700
97291893762063000
42075585224372700
162616451002305300
63892555340714100
38783845967735803935
8013191315647893375
97291893762063000
9350130049860600
            if divide()>1000:
                print divisors
                print "WINNER",num
            """
    



    
