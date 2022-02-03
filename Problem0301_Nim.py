# -*- coding: utf-8 -*-
"""
Nim
Problem 301
Nim is a game played with heaps of stones, where two players take it in turn to remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as follows:
- At the start of the game there are three heaps of stones.
- On his turn the player removes any positive number of stones from any single heap.
- The first player unable to move (because no stones remain) loses.

If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2 and n3 then there is a simple function X(n1,n2,n3) — that you may look up or attempt to deduce for yourself — that returns:

zero if, with perfect strategy, the player about to move will eventually lose; or
non-zero if, with perfect strategy, the player about to move will eventually win.
For example X(1,2,3) = 0 because, no matter what the current player does, his opponent can respond with a move that leaves two heaps of equal size, at which point every move by the current player can be mirrored by his opponent until no stones remain; so the current player loses. To illustrate:
- current player moves to (1,2,1)
- opponent moves to (1,0,1)
- current player moves to (0,0,1)
- opponent moves to (0,0,0), and so wins.

For how many positive integers n  230 does X(n,2n,3n) = 0 ?


Answer:
2178309
Completed on Mon, 17 Jun 2013, 11:21
"""


cat=False
for n in range(1,1000):
    a=(n^(2*n)^(3*n))
    if a ==0:
        cat=True
        print n,
        if n%4==0:
            print "this value is n/4       ", n/4,"    ::::",
    elif cat==True:
        cat=False
        print
     
     
for n in range(1,1000):
    a=(n^(2*n)^(3*n))
    if a ==0:
         
        print n,
        
print "_________________________________________"
print "Noticed that n varies by two or three zeros in a row"
print " BUT the next n is a multiple from 1 of the terms that were zero"
year=2 
frog=[]
c=0
count=0
n=1
while n<=1073741824:
    if n%1000000==0:
        print n
    a=(n^(2*n)^(3*n))
    if a==0:
        year+=1
        #print n,
        frog.append(n)
        n+=1
        count+=1
    else:
        n=frog[c]*4
        c+=1
