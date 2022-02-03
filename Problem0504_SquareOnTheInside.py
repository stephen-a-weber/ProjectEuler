"""
Square on the Inside
Problem 504
Let ABCD be a quadrilateral whose vertices are lattice points lying on the coordinate axes as follows:

A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a, b, c, d ≤ m and a, b, c, d, m are integers.

It can be shown that for m = 4 there are exactly 256 valid ways to construct ABCD. Of these 256 quadrilaterals, 42 of them strictly contain a square number of lattice points.

How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?


Answer:
694687
Completed on Sun, 1 Nov 2015, 19:28

"""

import itertools

def factor(n):
    f={}
    for i in range(1,101):
        f[i]=set([1])
    for i in range(2,101):
        j=i
        while j<=n:
            f[j].add(i)
            j+=i
    return f

F=factor(100)
def hypotenuseVertices(A,B):
    #gcf-1
    a=F[A]
    b=F[B]
    c=max(a&b)
    return c-1
    
#boundary lines hypotenuse are found by
#greatest common
#factor of the two edges minus one
#since we are given edge lengths
#each length is plus one for number of vertices
#the two perpendicular edges are sharing a
#vertex.
#so with side A,B and hypotenuse C
# the boundary points are (A+1) points
# (B+1) points
# gcf(A,B)-1  = C without end points
# total
# A+B+gcf(A,B)

#Picks Theorem

#Area of triangle =
#Boundary vertices
#+ Interior vertices
#-1

#or (A-1)*(B-1) is interior points of the quad
# subtract hypotenuse points and divide by two
M=100
square=[r**2 for r in range(1,202)]
T={}
for x in range(1,M+1):
    for y in range(1,M+1):
        interiorVertices=int(((x-1)*(y-1)-hypotenuseVertices(x,y))/2)
        T[(x,y)]=interiorVertices
count=0
print("TO ",M)
for a in range(1,M+1):
    print("Now at ",a)
    for b in range(1,M+1):
        for c in range(1,M+1):
            for d in range(1,M+1):
                points=a+b+c+d-3+T[(a,b)]+T[(a,d)]+T[(b,c)]+T[(c,d)]
                if points in square:
                    count+=1
                
print (count)           
            
