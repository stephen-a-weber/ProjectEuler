import time
ras=time.time()
n=5000
primes=[]
  
primes.append(2)
sieve=[True]*n
 
for i in xrange(4,n,2):
    sieve[i]=False
  
for i in xrange(3,n,2):
  
    if sieve[i]==True:
        primes.append(i)
        for j in xrange(i,n,i):
            sieve[j]=False
  



def solution(n):

    coins=primes
    
    remainder=n
    coins.reverse()
    solutions=set()
    bag=[[n,[]]]
    while bag:
      remainder,check=bag.pop()
       
      for i in coins:
          h= remainder-i 
          if h<n and h>1:
               
              letter=check+[i]
              if h in capture:
                  for i in capture[h]:
                      d=letter+list(i)
                      d.sort()
                      solutions.add(tuple(d))
              else:
                 bag.append([h,letter])
          elif h==0:
              d=check+[i]
              d.sort()
              solutions.add(tuple(d))
               
          
    
    return solutions


        
capture={}    

 
pie=0
n=2

 
while pie<5001:
    n=n+1
    s=solution(n)
    pie=len(s)
    capture[n]=s
    
 

 
print n
print time.time()-ras
