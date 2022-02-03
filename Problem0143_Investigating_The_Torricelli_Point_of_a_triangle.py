"""
Investigating the Torricelli point of a triangle
Problem 143
Let ABC be a triangle with all interior angles being less than 120 degrees. Let X be any point inside the triangle and let XA = p, XB = q, and XC = r.

Fermat challenged Torricelli to find the position of X such that p + q + r was minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and AMC are constructed on each side of triangle ABC, the circumscribed circles of AOB, BNC, and AMC will intersect at a single point, T, inside the triangle. Moreover he proved that T, called the Torricelli/Fermat point, minimises p + q + r. Even more remarkable, it can be shown that when the sum is minimised, AN = BM = CO = p + q + r and that AN, BM and CO also intersect at T.


If the sum is minimised and a, b, c, p, q and r are all positive integers we shall call triangle ABC a Torricelli triangle. For example, a = 399, b = 455, c = 511 is an example of a Torricelli triangle, with p + q + r = 784.

Find the sum of all distinct values of p + q + r  120000 for Torricelli triangles.


Answer:
30758397
Completed on Thu, 23 May 2013, 14:00
"""


N=120000
 
import fractions
cat=set()
frog={}
count=0
for m in range(2,347):
    for n in range(1,m):
        if fractions.gcd(m,n)==1 and (m-n)%3!=0:
            a=(m*m-n*n)
            b=(2*m*n+n*n)
             
            count+=1
            k=a+b 
             
            K=N/k
            for e in range(1,K+1):
                dinosaur=[e*a,e*b]
                dinosaur.sort()
                p=dinosaur[0]
                r=dinosaur[1]
                if p not in frog:
                    frog[p]=[r]
                else:
                    frog[p].append(r)
                if r not in frog:
                    frog[r]=[p]
                else:
                    frog[r].append(p)
                        

  
print "DONE SEtting up THE POSSIBLES"
canister=set()
for i in frog:
    for j in frog[i]:
        for k in frog[i]:
            if j==k:
                continue
            if k in frog[j]:
                
                prisoner=[i,j,k]
                if sum(prisoner)<=N:
                    prisoner.sort()
                    canister.add(tuple(prisoner))


print len(canister)
print "sum..."
#total=0
dog=[]
for i in canister:
    dog.append(sum(i))
cat=set(dog)
print sum(cat)
#print total

        
    
