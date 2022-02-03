
"""
Consecutive positive divisors
Problem 179
Find the number of integers 1  n  107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.


Answer:
986262
Completed on Sat, 16 Mar 2013, 02:51
"""



# This makes a diictionary of numbers with
#the values being a list of the numbers divisors

#compare n,n+1 to see if len(divisors)  equal

import time
ras=time.time()
n=10000000
 
 
 
numbers={}
for i in xrange(1,n):
    numbers[i]=[1]
 
  
     
for i in xrange(2,n):
    numbers[i].append(i) 
     
  
      
    for j in xrange(i+i,n,i):
            
       
            numbers[j].append(i)

x=0
for i in range(2,n-1):
    if len(numbers[i])==len(numbers[i+1]):
        x=x+1


print "time .",time.time()-ras
