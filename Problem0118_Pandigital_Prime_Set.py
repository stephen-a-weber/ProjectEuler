"""
Pandigital prime sets
Problem 118
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?


Answer:
44680
Completed on Sun, 31 Mar 2013, 18:14

"""
import random
import itertools
 
def is_Prime(n):
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
        
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
  
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  
heaven=set()
golf=set() 
cat=set([str(r) for r in range(1,10)])
 
storage=list() 
 
for r in itertools.permutations(range(1,10)):
    storage.append([[],r])

print "Filled Cache"
while storage:
    a,b=storage.pop()
  
    if len(storage)%10000==0:
        print len(storage),len(heaven)
    if len(b)==0:
        golf.add(tuple(a))
        d=set()
        for i in a:
            for e in str(i):
                d.add(e)
        if d==cat:
            heaven.add(tuple(a))
        else:
            print "************",a
        
    else:
        length=len(b)-1
        c=0
    
        f=0
       
        while c<=length:
            f+=b[length-c]*10**c
     
            if is_Prime(f):
                v=[r for r in a]
                v.append(f)
                v.sort()
    
                e=b[:length-c]
                storage.append([v,e])
   
            c=c+1
        
 
print len(heaven)

    
 
