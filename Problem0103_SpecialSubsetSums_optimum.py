"""
Special subset sums: optimum
Problem 103
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B)  S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B)  S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to problems 105 and 106.
"""
year=[20,31,38,39,40,42,45]
 
num=7

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
polution=[]
 
def initialcheck( sets,n):
    for i in range(len(sets)):
            
            aaa=[]
             
            for a in sets[i]:
                aaa.append(n[a-1])
            
            polution.append(sum(aaa))
                
       
    
def check1(subsets,n):
    
    for i in range(len(subsets)-1):
        for j in range(i+1,len(subsets)):
            
            if polution[i]==polution[j]:
                return False
    return True
            
            
def passport(n,m):
    a=list(n)
    b=list(m)
    
    while len(a)>0:
         
        hb=b.pop(0)
        ha=a.pop(0)
        
        if ha>hb:
            
            return True
   
    return False

def check2(frog,n):
    for a,b in frog:
      
        s1=[]
        s2=[]
        for e in a:
            
            s1.append(n[e-1])
        for e in b:
            s2.append(n[e-1])
        if s1==s2:
            return False
    return True
            



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
#print len(frog)
initialcheck(sets,year)
print check2(frog,year)
print check1(sets,year)


 
          
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
