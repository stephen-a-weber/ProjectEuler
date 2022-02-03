"""Exploring the number of different ways a number can be expressed as a sum of powers of 2.
Problem 169
Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(1025)?


Answer:
178653872807
Completed on Tue, 11 Jun 2013, 18:21
"""


X=bin(10**25)[2:]
print X
F=[ int(i) for i in X]
F.reverse()


c=0
nc=1
for x in range(len(F)-1):
    i=F[x]
    a=nc+c
    if i==0:
        c=a
    else:
        nc=a
 
print nc+c
