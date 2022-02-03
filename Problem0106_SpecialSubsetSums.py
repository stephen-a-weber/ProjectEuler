"""
Special subset sums: meta-testing
Problem 106
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B)  S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B)  S(C).
For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

NOTE: This problem is related to problems 103 and 105.
"""


num=12

n=range(1,num+1)
import itertools
p=set()
sets=[]
subsets={}
for i in range(1,num+1):
    subsets[i]=[]

for k in range(1,len(n)+1):
   for i in itertools.combinations(n,k):
        
       subsets[k].append(i)
       sets.append(i)
  
for a in range(2,num+1):
    for b in range(a,num+1):#a,b are the size of the subsets for each pair
        
         
 
        for ii in range(len(subsets[a]) ):
            i=subsets[a][ii]
            for jj in range(len(subsets[b])  ):
                j=subsets[b][jj]
                g=[i,j]
                g.sort()
               
                h=set(i)
                t=set(j)
                if len(i)==len(j):
                    if h.intersection(t)==set([]):
                       p.add(tuple(g))
                       
def passport(n,m):
    a=list(n)
    b=list(m)
    
    while len(a)>0:
         
        hb=b.pop(0)
        ha=a.pop(0)
        
        if ha>hb:
            
            return True
   
    return False                       
frog=[]                       
              
#print len(p)
for i in p:
    a,b=i
    cat=True
     
    cat=passport(a,b)
    if cat:
        frog.append(i)

 
for i in frog:
    #print i
    pass
print len(frog)


      
          
"""

1:1
1:2
1:3
1:4
1:5
1:6
1:7
1:8
1:9
1:10
1:11
2:2
2:3
2:4
2:5
2:6
2:7
2:8
2:9
2:10
3
"""
