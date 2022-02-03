# -*- coding: utf-8 -*-
"""
Binary Circles
Problem 265
2N binary digits can be placed in a circle so that all the N-digit clockwise subsequences are distinct.

For N=3, two such circular arrangements are possible, ignoring rotations:


For the first arrangement, the 3-digit subsequences, in clockwise order, are:
000, 001, 010, 101, 011, 111, 110 and 100.

Each circular arrangement can be encoded as a number by concatenating the binary digits starting with the subsequence of all zeros as the most significant bits and proceeding clockwise. The two arrangements for N=3 are thus represented as 23 and 29:

00010111 2 = 23
00011101 2 = 29
Calling S(N) the sum of the unique numeric representations, we can see that S(3) = 23 + 29 = 52.

Find S(5).


Answer:
209110240768
Completed on Tue, 21 May 2013, 12:41
"""

import itertools
x=0
check=set()
for i in itertools.product([0,1],repeat=5):
    check.add(i)
    x=x+1
 
import copy
total=0
cell=tuple([0,0,0,0,0])
a=[]
a.append(cell)
angle=set() 
storage=[[cell,a]]
 
count=0
while storage:
    count+=1
   
    current,group=storage.pop()
     
    if count%1000==0:
        print len(storage),total
    if len(group)==32:
        if list(current)==[1,0,0,0,0]:
           total+=1
        x=tuple(group)
        angle.add(x)
  
    else:
        d=list(current)[1:]
        e=d+[1]
        e=tuple(e)
        if e not in group:
            frog=copy.deepcopy(group)
            frog.append(e)
            storage.append([e,frog])
        e=d+[0]
        e=tuple(e)
        if e not in group:
            frog=copy.deepcopy(group)
            frog.append(e)
            storage.append([e,frog])            
print "Final total",total
print "Unique ones",len(angle)

TotalSum=0
BinarySum=0
for i in angle:
    BinarySum=0
    j=[0,0,0,0,0]
    k=list(i)
    for p in range(1,28):
        j.append(k[p][4])
    t=[str(r) for r in j]
    u="".join(t)
    TotalSum+=int(u,2)
         
    

print TotalSum   
    
