import time
ras=time.time()
 
 
import math
import itertools
 
def mul(r):
    a=1
    for i in r:
        a*=i
    return a
def adding(r):
    a=0
    for i in r:
        a+=i
    return a


def factor(n):
      factors =[[n]]
      for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
          factors.append([x,n//x])
          for i in factor(n//x):
              factors.append([x,i])
    
      dog=set()
      for i in factors:
          cat=[]
          for a in i:
              if type(a) is list:
                  for b in a:
                      cat.append(b)
                   
              else:
                  cat.append(a)
          cat.sort()
          dog.add(tuple(cat))
      
      dog=[list(r) for r in dog]           
      return sorted(dog)



pony=[]
 
def stallion():
    for n in range(2,14000):
         f=factor(n)
         for each in f:
             pony.append(each)
    pony.sort(key=mul)
                 
stallion() 
print "TIME to start ",time.time()-ras
goat=[]
k=2

where=0 
for k in range(2,12001):
        
        if k%1000==0:
            print "we are at ",k,
            print "TIME: ",time.time()-ras
       
        for a in range(where,len(pony)):
            p=pony[a]
            
            cost=k-len(p)+adding(p)
            if cost==mul(p):
                goat.append(cost)
                where=where-1000
                if where<0:
                    where=0
                break
 
print "there should be 12001 2,12000 elements:"
print "there are ",len(goat)
g=list(set(goat))

print  
print "this sums to ,",sum(g)
print

 
print
print "TOTAL TIME ",time.time()-ras
