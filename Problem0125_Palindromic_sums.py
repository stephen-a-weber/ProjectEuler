"""Palindromic sums
Problem 125
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.


Answer:
2906969179
Completed on Sat, 16 Mar 2013, 01:45

"""


import time
ras=time.time()
 
 
cattle=set()# made this a set as there are duplicates.. 
#7073 is roughly for two integers to square and be less then 10^8
for j in range(1,7071):
 x=j**2
 for i in range(j+1,7073):
   x+=i**2
  
   if x<100000000 :
       g=str(x)
       if g==g[::-1]:
        
           cattle.add(x)
 
 
print sum(cattle)
print "time,",time.time()-ras
 
 
 
