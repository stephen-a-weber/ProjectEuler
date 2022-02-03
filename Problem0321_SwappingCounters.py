"""
Swapping Counters
Problem 321
A horizontal row comprising of 2n + 1 squares has n red counters placed at one end and n blue counters at the other end, being separated by a single empty square in the centre. For example, when n = 3.

p321_swapping_counters_1.gif
A counter can move from one square to the next (slide) or can jump over another counter (hop) as long as the square next to that counter is unoccupied.

p321_swapping_counters_2.gif
Let M(n) represent the minimum number of moves/actions to completely reverse the positions of the coloured counters; that is, move all the red counters to the right and all the blue counters to the left.

It can be verified M(3) = 15, which also happens to be a triangle number.

If we create a sequence based on the values of n for which M(n) is a triangle number then the first five terms would be: 
1, 3, 10, 22, and 63, and their sum would be 99.

Find the sum of the first forty terms of this sequence.


Answer:
2470433131948040
Completed on Thu, 19 Nov 2015, 19:52
"""
from decimal import Decimal
t=[1,3,10,22,63]
count=6
n=64
g=63
tail=True
while count<=40:
    f=(n**2+2*n)
    b=1+8*f
    c=Decimal(b).sqrt()
    
    if c==c.to_integral_value() and c%2==1:
        
        
        t.append(n)
        x=n/g
        print(count,n,x)
        g=n
        count+=1
        if tail==True:
            n*=2.78361162489
            n=int(n)
            tail=False
        else:
            n*=2.09383632135
            tail=True
            n=int(n)
        
                
        
     
    
    n+=1



print (sum(t))
