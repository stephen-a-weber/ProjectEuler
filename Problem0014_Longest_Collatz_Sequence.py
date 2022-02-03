
"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Answer:
837799
Completed on Wed, 23 Jan 2013, 07:51
"""


 
n=1
total=0
count=0
k=3
while n<1000001:
    n+=1
     

    k= n
    table=[k]
    while k!=1:
    
     if k%2==0:
        k/=2
        table.append(k)
     else:
        k=3*k+1
        table.append(k)
    if len(table)>total:
        total=len(table)
        count=n
        print n," has a cooatz length of ",len(table)
    
    
