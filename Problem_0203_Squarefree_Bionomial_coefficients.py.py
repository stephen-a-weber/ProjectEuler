"""
Squarefree Binomial Coefficients
Problem 203
The binomial coefficients nCk can be arranged in triangular form, Pascal's triangle, like this:

1	
1		1	
1		2		1	
1		3		3		1	
1		4		6		4		1	
1		5		10		10		5		1	
1		6		15		20		15		6		1	
1		7		21		35		35		21		7		1
.........
It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n. Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.


Answer:
34029210557338
Completed on Mon, 18 Mar 2013, 00:07

"""
import time
ras=time.time()

rows=51
rows=rows-1    
#pascals storage problem
p={}
p[0]=[1,1]
for x in range(1,rows):
    f=len(p[x-1])-1
    p[x]=[1]
    for i in range(f):
        
      p[x].append(p[x-1][i]+p[x-1][i+1])
    p[x].append(1)
    
baby=set()   
for i in range(rows):
             print p[i]
             d=set(p[i])
             baby=baby.union(d)
import copy
print len(baby),"this is the length of the baby"
print baby
son=copy.deepcopy(baby)
n=6961284
prime=[]
  
numbers={}
 
prime.append(2)
for i in baby:
    if i%4==0:
        son.remove(i)
baby=copy.deepcopy(son)
print max(baby),"  max"
sieve=[True]*n
 
for i in xrange(4,n,2):
    sieve[i]=False
   
  
for i in xrange(3,n,2):
  
    if sieve[i]==True:
        prime.append(i)
        for w in baby:
            r=i*i
            if w%r==0:
                son.remove(w)
        baby=copy.deepcopy(son)
        
                
        for j in xrange(i*i,n,i):
            sieve[j]=False
      
print "Size ",len(baby)
print "Sum  ",sum(baby)
 
