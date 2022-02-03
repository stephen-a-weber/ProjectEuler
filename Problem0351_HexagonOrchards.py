"""
Hexagonal orchards
Problem 351
A hexagonal orchard of order n is a triangular lattice made up of points within a regular hexagon with side n. The following is an example of a hexagonal orchard of order 5:


Highlighted in green are the points which are hidden from the center by a point closer to it. It can be seen that for a hexagonal orchard of order 5, 30 points are hidden from the center.

Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.

H(5) = 30. H(10) = 138. H(1 000) = 1177848.

Find H(100 000 000).


Answer:
11762187201804552
Completed on Tue, 3 Mar 2015, 16:07

"""
import time

reee=time.time()
 
 

n=100000000

d=[1]*(n+1) 

d[0]=0
d[1]=0
num=2
v=n/2
while num<=v:
    
    if num<2000:
        print num," time is ",time.time()-reee
    
    else:
        if num%100000==0:
           print num," time is ",time.time()-reee
 
    count=num*2
    while count<=n:
        d[count]+=(num-d[num])
        count+=num
     
    num+=1



print n,":==",sum(d)*6




        
