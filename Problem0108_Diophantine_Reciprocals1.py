"""
Diophantine reciprocals I
Problem 108
In the following equation x, y, and n are positive integers.

1

x
+	
1

y
=	
1

n
For n = 4 there are exactly three distinct solutions:

1

5
+	
1

20
=	
1

4
1

6
+	
1

12
=	
1

4
1

8
+	
1

8
=	
1

4
What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of problem 110; it is strongly advised that you solve this one first.
"""


primes=[2, 3, 5, 7, 11, 13, 17]
import itertools
divisors=[2,2,1,1,1,1,0,0,0,0,0,0,0,0]

def divide():
    total=1
    for i in divisors:
        total*=(2*i+1)
    return total

def  number():
    total=1
    for i in range(0,7):
        total*=primes[i]**divisors[i]
    return total

  
        
x=10000000000000000000000000000000

for i in range(2,25):
 
 print "startng :",i    
 for j in itertools.product(range(i),repeat=7):
            divisors=j
            num=number()
            if divide()>1999:
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
    



    
