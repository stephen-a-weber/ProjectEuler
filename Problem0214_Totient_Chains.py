


 
import time
ras=time.time()
n=40000000
primes=set()
phi=[1]*n
for i in xrange(2,n):
   phi[i]*=i 
primes.add(2)
sieve=[True]*n
phi[2]*=(1-1/2.0)
for i in xrange(4,n,2):
    sieve[i]=False
    phi[i]*=.5
for i in xrange(3,n,2):
  
    if sieve[i]==True:
        primes.add(i)
        for j in xrange(i,n,i):
            sieve[j]=False
            phi[j]*= (1-1/float(i))
phi=[int(r) for r in phi] 
g=0
print "Finished Primes"
import copy 
sieve=[]
totient={}
 
for num in xrange(1,n):
    if num%100000==0:
      print "40000000:",num
 
    tot=phi[num]
    if tot not in totient:
       totient[tot]=[num]
    else:
       totient[tot].append(num)
storage=[3,4,6]
container=[]
x=2
value=2
phi=[] 
print "Now moving totients to container"
for n in xrange(3,25):
    print "n=34:",n
    for i in storage:
        if i in totient:
            for a in totient[i]:
                container.append(a)
                #print "totient",i,"   number",a

    storage=copy.deepcopy(container)
    container=[]
print "Last bit..."
storage=[r for r in storage if r%2!=0 and r%3!=0 and r%5!=0]
print "Calculated Storage possibilities done"

 
 
frog=0
for i in storage:
    if i in primes:
        frog+=i
print frog

print "thats answer",time.time()-ras       
 

