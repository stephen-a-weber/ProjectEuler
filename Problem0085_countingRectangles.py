#Counting Rectangles
"""
By counting carefully it can be seen that
a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly
two million rectangles, find the area of the grid with the nearest solution.
"""
def cat(m,n):
    total=0

    for a in range(0,m):
        for b in range(0,n):
            total+=(m-a)*(n-b)
    
    return total


print "1,2.....",cat(1,2)
print "3,1.....",cat(3,1)
print "2,3.....",cat(2,3)

 
for n in range(20,90):
    
   for m in range(20,90):
       kitty=cat(n,m)
        
       if abs(kitty-2000000)<10000:
           print n,m,"....",kitty,
           print abs(kitty-2000000)
