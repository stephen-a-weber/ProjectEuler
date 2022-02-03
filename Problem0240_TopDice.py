"""
Top Dice
Problem 240
There are 1111 ways in which five 6-sided dice (sides numbered 1 to 6) can be rolled so that the top three sum to 15. Some examples are: 

D1,D2,D3,D4,D5 = 4,3,6,3,5 
D1,D2,D3,D4,D5 = 4,3,3,5,6 
D1,D2,D3,D4,D5 = 3,3,3,6,6 
D1,D2,D3,D4,D5 = 6,6,3,3,3 

In how many ways can twenty 12-sided dice (sides numbered 1 to 12) be rolled so that the top ten sum to 70?


Answer:
7448717393364181966
Completed on Sun, 25 Aug 2013, 16:58

"""

import itertools
dice={}
s=[]
for t in range(1,8):
    dice[t]=[]
for r in itertools.combinations_with_replacement(range(1,13),10):
 
    y=sum(r)
     
    if y==70:
        x=min(r)
        dice[x].append(r)
        s.append(r)

print "There are ",len(s),"sets of ten dice rolls that sum to 70"


spread={}
for y in range(2,9):
    print y
    spread[y-1]=set()
    x = range(1,y)
     
    grown=set()
    for r in itertools.combinations_with_replacement(x,10):
        spread[y-1].add(r)
      
 
tt=0    
count=0
print "highest minimum is [7 7 7 7 7 7 7]"
import math
n=math.factorial(20)
for x in range(1,8):
    print x,
    for a in dice[x]:
        for b in spread[x]:
            h=set().union(a,b)
             
            c=list(a)
            c.extend(b)
            total=n
            for i in h:
                g=c.count(i)
                total/=math.factorial(g)
            count+=total
            
print "..."            
print "the answer is ",count
