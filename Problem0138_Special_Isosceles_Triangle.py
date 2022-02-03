"""
Special isosceles triangles
Problem 138
Consider the isosceles triangle with base length, b = 16, and legs, L = 17.


By using the Pythagorean theorem it can be seen that the height of the triangle, h = (172  82) = 15, which is one less than the base length.

With b = 272 and L = 305, we get h = 273, which is one more than the base length, and this is the second smallest isosceles triangle with the property that h = b  1.

Find  L for the twelve smallest isosceles triangles for which h = b  1 and b, L are positive integers.


Answer:
1118049290473932
Completed on Wed, 10 Apr 2013, 05:12

"""
total=0
m=4
n=0
mfactor=4.2
lastm=0
nfactor=.23
def check(i):
    global m
    global n
    global mfactor
    global lastm
    global nfactor
    global total
    if abs(2*i[0]-i[1])==1:
         
        if lastm!=0:
            mfactor=m*1.0/lastm
            nfactor=n*1.0/m
        lastm=m
        total+=i[2]
        m=int(m*mfactor)
        print i,total,nfactor,mfactor
     
 
        
def parameterSpace():
    global m
    global n
    global nfactor
    while True:
        n+=1
        if n==m:
            m+=1
            n=int(m*nfactor)
            
        
        yield n,m

def CreateTriplets(a,b,c):
    k=1
    e=0
    f=0
    g=0
    for k in range(2,100000):
         
            e,f,g=k*a,k*b,k*c
            d=[e,f,g]
            d.sort()
            check(d)
 #           Triplets.append([e,f,g])
            
             
     
for n,m in parameterSpace():
     if (m-n)%2==1:
            a=(m**2-n**2)
            b=2*m*n
            c=(m**2+n**2)
            d=[a,b,c]
            q=True
            if b<a:
                q=False
            
            d.sort()
            check(d)

 #           CreateTriplets(a,b,c)
                
"""                
                 
for i in Triplets:
    i.sort()

Triplets.sort()

""" 
