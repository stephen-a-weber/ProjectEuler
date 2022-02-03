"""

Logged in as stephen_weber
Tue, 21 Jun 2016, 18:49
RSS Feedsecure_icon
Previous
Next
Bitwise-OR operations on random integers
Problem 323
Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
(i.e. 0 ≤ yi < 232, every value equally likely).

For the sequence xi the following recursion is given:

x0 = 0 and
xi = xi-1| yi-1, for i > 0. ( | is the bitwise-OR operator)
It can be seen that eventually there will be an index N such that xi = 232 -1 (a bit-pattern of all ones) for all i ≥ N.

Find the expected value of N. 
Give your answer rounded to 10 digits after the decimal point.


Answer:
6.3551758451
Completed on Tue, 21 Jun 2016, 18:30

import math
count=0
for i in range(0,33):
    print(i,"--> ",round(math.factorial(32)/math.factorial(i)/math.factorial(32-i)))
    count+=round(math.factorial(32)/math.factorial(i)/math.factorial(32-i))
print(count,2**32)



the first turn has 1/(2**32)== 1/4294967296 of success

the second turn 
0 -->  1         there is 1 success                 
1 -->  32        there are two successes
2 -->  496       there is 4 successes
3 -->  4960      2**3 successes
4 -->  35960
5 -->  201376
6 -->  906192
7 -->  3365856
8 -->  10518300
9 -->  28048800
10 -->  64512240
11 -->  129024480
12 -->  225792840
13 -->  347373600
14 -->  471435600
15 -->  565722720
16 -->  601080390
17 -->  565722720
18 -->  471435600
19 -->  347373600
20 -->  225792840
21 -->  129024480
22 -->  64512240
23 -->  28048800
24 -->  10518300
25 -->  3365856
26 -->  906192
27 -->  201376
28 -->  35960
29 -->  4960
30 -->  496    etc
31 -->  32                2**31
32 -->  1                 2**32
4294967296 4294967296


 
 
"""
import math
import sys
 
import decimal  
prob=decimal.Decimal(0) 
#print(storage)
n=decimal.Decimal( 32) 
original=decimal.Decimal(1)
probability=decimal.Decimal(1)/(2**n)
index=decimal.Decimal(0)
newProbability=decimal.Decimal(1)
total=0
cat=True
sy=total
print(probability,".")
while cat:
     
     
    """
    success=0
    for i in range(len(storage)):
        success+=amounts[i]*(2**i)
        #print(i,amounts[i],"*",(2**i),"= ",amounts[i]*(2**i))
    newProbability=success/((2**2)**(index))
    prob=newProbability-probability
    #print(amounts) 
    total+=prob*index
    probability=newProbability
    """   
     
     
    #print(prob,k,total)
    """
    for i in range(len(amounts)):
        newAmounts[i]=storage[i]*(original)**i 
     
    amounts=[r for r in newAmounts]
  
    """
    y=1-(1-1/2**index)**n
    #E(x)=sum Prob(X>=index)
    #as (1-1/2**index)**n ==prob at X
    #https://en.wikipedia.org/wiki/Expected_value
    #Discrete distribution taking only non-negative integer values
  
    total+=y
   
   
    
    #print (success,((2**2)**(index)))
    if index%10000==0:
        print("converging too>> > > ",total)
    #print()
    #print(k) 
    index+=1
     
        
        
    

 
