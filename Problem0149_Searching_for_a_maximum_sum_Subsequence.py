"""
Searching for a maximum-sum subsequence.
Problem 149
Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).

2	5	3	2
9	6	5	1
3	2	7	3
1	8	4	  8
Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":

For 1  k  55, sk = [100003  200003k + 300007k3] (modulo 1000000)  500000.
For 56  k  4000000, sk = [sk24 + sk55 + 1000000] (modulo 1000000)  500000.

Thus, s10 = 393027 and s100 = 86613.

The terms of s are then arranged in a 20002000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).


Answer:
52852124
Completed on Mon, 20 May 2013, 11:54

"""

grid=[[0 for r in xrange(2000)] for x in xrange(2000)]
grid

s=[0]*4000001
k=0
while k<4000000:
    k=k+1
    if  k<=55:
        s[k]=((100003-200003*k+300007*k**3)%1000000)-500000
    else:
        s[k]=((s[k-24]+s[k-55]+1000000)%1000000)-500000
        
for i in xrange(k):
    x=i/2000
    y=i%2000
    grid[x][y]=s[i]
print "Finished Setup"    
maximum=0
#Horizontal cases((( y vertical x horizontal

for y in xrange(2000):
    s=0
     
    for x in xrange(2000):
        s =max(s +grid[x][y],0)
 
 
        if s>maximum:
                maximum=s
                print "NEW maximum..",maximum

print "Finished Horizontals.. the new maximum is:", maximum
#Vertcal cases


for x in xrange(2000):
    s=0
     
    for y in xrange(2000):
        s=max (s +grid[x][y],0)
     
        if s>maximum:
                maximum=s



print "Finished Verticals.. the new maximum is:", maximum
#Diagonal Cases


for k in xrange(2000):
    x=k
   
    s=0
    y=0
    cat=True
    srange=1
    while cat:
            s=max(s+grid[x][y],0)
            if s>maximum:
                maximum=s
            srange+=1
            x+=1
            y+=1
            if x>1999 or y>1999:
                cat=False
  

print "Finished Regular Diagonals.. the new maximum is:", maximum
# Reverse Diagonal



for k in xrange(1999,-1,-1):
    y=k
    
    s=0
    x=0
    cat=True
    srange=1
    while cat:
            s=max(s +grid[x][y],0)
            if s>maximum:
                maximum=s
            srange+=1
            x+=1
            y-=1
            if x>1999 or y<0:
                cat=False
 



print "Finished Reversed Diagonals.. the new maximum is:", maximum









               
    
