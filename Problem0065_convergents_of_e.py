#Convergents of e problem 65
import copy
r=[2]
k=1
m=1
final=100
for x in range(final):
    k=2*m
    r.append(1)
    r.append(k)
    r.append(1)
    m=m+1
r=[r[d] for d in range(final)]

print r
print "length of r",len(r) 
n=1 
d=r.pop()
#print d,"-----"
#print "n/d  " ,n,"/",d
 
if final==1:
      a=n
      n=d
      d=a
      #print "n/d  " ,n,"/",d
 
while r:
    t=r.pop()
    #print t,"-----"
    n=t*d+n
    if r: 
      a=n
      n=d
      d=a
    #print "n/d  " ,n,"/",d
 
 
print ">>>>>>>>>>>>>>"
 
print
print float(n)/float(d)
v=[int(r) for r in str(n)]
print "sum of digits is ",sum(v)
