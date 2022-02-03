"""
Digit power sum
Problem 119
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.


Answer:
248155780267521
Completed on Sun, 17 Mar 2013, 16:42

"""

best={}
for i in range(2,181):
    best[i]=i
e=1
exp=1
while e<31:
    
    for sumN in best:
        best[sumN]*=sumN
        c=best[sumN]
        d=0
        while c:
            d+=c%10
            c/=10
        if d==sumN:
            print e,best[sumN]
            e=e+1
            
            
        
        
    
    
    
