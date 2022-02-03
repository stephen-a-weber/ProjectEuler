# -*- coding: utf-8 -*-
"""
Criss Cross
Problem 166
A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.

It can be seen that in the grid

6 3 3 0
5 0 4 3
0 7 1 4
1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, each column, and both diagonals have the same sum?


Answer:
7130034
Completed on Sun, 25 Aug 2013, 13:38

"""


import itertools

t={}
p={}
k={}
m={}
for r in range(0,37):
    t[r]=[]# given 0 of 4
    p[r]={}# given 2 of 4
    m[r]={}# find choices given 3 of 4
    k[r]=set()#all 4 of sum r full permutations
    
            
             
            
     

for r in itertools.combinations_with_replacement(range(0,10),4):
    y=sum(r)
    t[y].append(r)
    for z in itertools.permutations(r):
        k[y].add(z)




for x in xrange(0,37):
    for y in xrange(len(t[x])):
        for r in itertools.permutations(t[x][y],2):
            e=list(t[x][y])
            e.remove(r[0])
            e.remove(r[1])
            if r not in p[x]:
                p[x][r]=set()
            for rr in itertools.permutations(e,2):
                p[x][r].add(rr)


for x in xrange(0,37):
    for y in xrange(len(t[x])):
        for r in itertools.permutations(t[x][y],3):
            e=list(t[x][y])
            e.remove(r[0])
            e.remove(r[1])
            e.remove(r[2])
             
            
            m[x][r]=e[0]
            
#     0 1 2 3
#   a
#   b
#   c
#   d

# Took seven minutes initially. Added the center four equal sum and some optimizing with
#that took it to 45 secs
# 
            
count=0
"""
def item1(r,b,c):
    global count
    x0=(b[0],c[0])
    
    if x0 not in p[r]:
        return  
    x1=(b[1],c[1])
    if x1 not in p[r]:
        return  
    for ad0 in p[r][x0]:
         
    
        for ad1 in p[r][x1]:
     
            c1b2d0=(c[1],b[2],ad0[1])
            if c1b2d0 not in m[r]:
                continue
             
            a0b1c2=(ad0[0],b[1],c[2])
            if a0b1c2 not in m[r]:
                continue
            a3=m[r][c1b2d0]
            d3=m[r][a0b1c2]
            
            if (a3,d3) not in p[r]:
                continue
            if (b[3],c[3]) not in p[r][(a3,d3)]:
                continue
  #          a01234=(ad0[0],ad1[0],a3)
            if (ad0[0],ad1[0],a3) not in m[r]:
                continue
            if (ad0[1],ad1[1],d3) not in m[r]:
                continue
            if (b[2],c[2]) not in p[r]:
                continue
            if (m[r][ad0[0],ad1[0],a3],m[r][ad0[1],ad1[1],d3]) not in p[r][(b[2],c[2])]:
                continue
            count+=1
            
            
    
                     
    
    return True
"""
def item1(r,b,c):
    global count
   
    for a0,d0 in p[r][(b[0],c[0])]:
         
    
        for a1,d1 in p[r][(b[1],c[1])]:
     
            c1b2d0=(c[1],b[2],d0)
            if c1b2d0 not in m[r]:
                continue
             
            a0b1c2=(a0,b[1],c[2])
            if a0b1c2 not in m[r]:
                continue
            a3=m[r][c1b2d0]
            d3=m[r][a0b1c2]
            
 
   
            if (a0,a1,a3) not in m[r]:
                continue
            if (d0,d1,d3) not in m[r]:
                continue

 
            count+=1
            
            

                    
    
    return True


    
    
import time
RAS=time.time()
 
for r in xrange(0,37):
    print r, 
     
  
    for b in k[r]:
        for c in k[r]:
            if b[1]+b[2]+c[1]+c[2]==r:
                item1(r,b,c)
 
print
                
print "total=",count
print time.time()-RAS               
