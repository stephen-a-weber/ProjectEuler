"""Combined Volume of Cuboids
Problem 212
An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) }, consists of all points (X,Y,Z) such that x0  X  x0+dx, y0  Y  y0+dy and z0  Z  z0+dz. The volume of the cuboid is the product, dx  dy  dz. The combined volume of a collection of cuboids is the volume of their union and will be less than the sum of the individual volumes if any cuboids overlap.

Let C1,...,C50000 be a collection of 50000 axis-aligned cuboids such that Cn has parameters

x0 = S6n-5 modulo 10000
y0 = S6n-4 modulo 10000
z0 = S6n-3 modulo 10000
dx = 1 + (S6n-2 modulo 399)
dy = 1 + (S6n-1 modulo 399)
dz = 1 + (S6n modulo 399)

where S1,...,S300000 come from the "Lagged Fibonacci Generator":

For 1  k  55, Sk = [100003 - 200003k + 300007k3]   (modulo 1000000)
For 56  k, Sk = [Sk-24 + Sk-55]   (modulo 1000000)

Thus, C1 has parameters {(7,53,183),(94,369,56)}, C2 has parameters {(2383,3563,5079),(42,212,344)}, and so on.

The combined volume of the first 100 cuboids, C1,...,C100, is 723581599.

What is the combined volume of all 50000 cuboids, C1,...,C50000 ?


Answer:
328968937309
Completed on Tue, 11 Jun 2013, 13:11

"""


from math import *
import itertools
import time
RAS=time.time()
import copy
###V is my BSP for the volume 52X52X52 200-cubed volumes for collision detection optimization
V={}
for x in xrange(52):
    V[x]={}
    for y in xrange(52):
        V[x][y]={}
        for z in xrange(52):
            V[x][y][z]=[]



#### n is Total number of cuboids in scene
n=50000


#### N is the storage for each cuboid min/max X,Y,Z,x,y,z
N=[[] for r in xrange(n+1)]

K=50000

####S and this loop create the randomness to pick placement and size of cuboids
S=[0]
for k in xrange(1,6*n+1):
    if k<=55:
        S.append((100003-200003*k+300007*k**3)%1000000)
    else:
        S.append((S[k-24]+S[k-55])%1000000)



### This loop of C creates all the cuboids from the random nonsense
### and finds all the boundaries 
qwerty=0
#CC=[0]
count=0
for C in xrange(1,n+1):
    #positions in space
    x0=S[6*C-5]%10000
    y0=S[6*C-4]%10000
    z0=S[6*C-3]%10000
    dx=1+(S[6*C-2]%399)
    dy=1+(S[6*C-1]%399)
    dz=1+(S[6*C]%399)
 #   CC.append([x0,y0,z0,dx,dy,dz])
    #volume cell of bounding box
    BoundX=set()
    BoundY=set()
    BoundZ=set()
    qwerty+=dx*dy*dz
    count+=1
    for x in range(x0/200,(x0+dx)/200+1):
        BoundX.add(x)
    for y in range(y0/200,(y0+dy)/200+1):
        BoundY.add(y)
    for z in range(z0/200,(z0+dz)/200+1):
        BoundZ.add(z)
#    BoundX=set( [ (x0/200), ((x0+dx)/200)])
#    BoundY=set( [ (y0/200), ((y0+dy)/200)])
#    BoundZ=set( [ (z0/200), ((z0+dz)/200)])
    Bound=[BoundX,BoundY,BoundZ]
    for x,y,z in itertools.product(*Bound):
        V[x][y][z].append(C)
    N[C]=[x0,y0,z0,x0+dx,y0+dy,z0+dz]#min,max
#maximum(10388,10387,10389) 52X52X52 volume BSP ->(0,51)
print "Volume:Number Cuboids",qwerty,":",count

### This function gets arguments of copies of all cubes in a voxel
### With the piece of any that are in multiple voxels...
### OUTPUT IS THE SUM OF ALL CUBES VOLUMES
### Any overlapping cubes are broken in half. And one
### step removes cubes that are inside another.
class block:
    minX=0
    minY=0
    minZ=0
    maxX=0
    maxY=0
    maxZ=0
 

def returnVolumeOfCell(cells):
    gorilla=0
    ape=0
    A=block()
    B=block()
    cat=True
    while cat:
        cat=False
        d=cells[:]
        #print "Looping"
##        for i in d:
##            print i
        ee=len(d)
        for a in range(ee):
            if cat ==True:
                break
            for b in range(ee):
                if a==b:
                    continue
                ape=0
                A.minX,A.minY,A.minZ,A.maxX,A.maxY,A.maxZ=d[a]
                B.minX,B.minY,B.minZ,B.maxX,B.maxY,B.maxZ=d[b]
                q,w,e,r,t,y=d[a]
                gorilla=(r-q)*(t-w)*(y-e)
                #misses
                if (A.minX>=B.maxX and A.maxX>B.maxX) or (A.maxX<=B.minX and A.minX<B.minX) or\
                   (A.minY>=B.maxY and A.maxY>B.maxY) or (A.maxY<=B.minY and A.minY<B.minY) or\
                   (A.minZ>=B.maxZ and A.maxZ>B.maxZ) or (A.maxZ<=B.minZ and A.minZ<B.minZ):
                    continue
                   
                #completely bigger:
                if A.minX<=B.minX and A.maxX>=B.maxX and\
                   A.minY<=B.minY and A.maxY>=B.maxY and\
                   A.minZ<=B.minZ and A.maxZ>=B.maxZ:
                    cells.remove(d[b])
                    cat=True
##                    print "REMOVING ONE******",B
##                    print "Due to ***********",A
                    break
                     
                #A Cutting A in three because Ax in middle of Bx
                if A.minX<B.minX and A.minX<B.maxX and A.maxX>B.minX and A.maxX>B.maxX:
                    D=[A.minX,A.minY,A.minZ,B.minX,A.maxY,A.maxZ]
                    C=[B.minX,A.minY,A.minZ,B.maxX,A.maxY,A.maxZ]
                    E=[B.maxX,A.minY,A.minZ,A.maxX,A.maxY,A.maxZ]
                    cells.remove(d[a])
                    cells.append(D)
                    cells.append(C)
                    cells.append(E)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=E
                    ape+=(r-q)*(t-w)*(y-e)
                    if gorilla!=ape:
                        print "A"
                    cat=True
                    break

                #A Cutting A in three because Ay in middle of By
                if A.minY<B.minY and A.minY<B.maxY and A.maxY>B.minY and A.maxY>B.maxY:
                    D=[A.minX,A.minY,A.minZ,A.maxX,B.minY,A.maxZ]
                    C=[A.minX,B.minY,A.minZ,A.maxX,B.maxY,A.maxZ]
                    E=[A.minX,B.maxY,A.minZ,A.maxX,A.maxY,A.maxZ]
                    cells.remove(d[a])
                    cells.append(D)
                    cells.append(C)
                    cells.append(E)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=E
                    ape+=(r-q)*(t-w)*(y-e)
                    if gorilla!=ape:
                        print "B"
                    cat=True
                    break
                #A Cutting A in three because Az in middle of Bz
                if A.minZ<B.minZ and A.minZ<B.maxZ and A.maxZ>B.minZ and A.maxZ>B.maxZ:
                    D=[A.minX,A.minY,A.minZ,A.maxX,A.maxY,B.minZ]
                    C=[A.minX,A.minY,B.minZ,A.maxX,A.maxY,B.maxZ]
                    E=[A.minX,A.minY,B.maxZ,A.maxX,A.maxY,A.maxZ]
                    cells.remove(d[a])
                    cells.append(D)
                    cells.append(C)
                    cells.append(E)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=E
                    ape+=(r-q)*(t-w)*(y-e)
                    if gorilla!=ape:
                        print d[a],d[b]
                        print D
                        print C
                        print E
                        print "______________________________"
                    cat=True
                    break
                    
                #A Cutting A in half in X if AxMin inside B-X
                if A.minX>=B.minX and A.minX<B.maxX and A.maxX>B.maxX:
                    D=[B.maxX,A.minY,A.minZ,A.maxX,A.maxY,A.maxZ]
                    C=[A.minX,A.minY,A.minZ,B.maxX,A.maxY,A.maxZ]
                    cells.remove(d[a])
                    cells.append(C)
                    cells.append(D)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
 
                    if gorilla!=ape:
                        print "D"
                    cat=True
##                    print "SPLITTING __",A
##                    print "INTO        ",C
##                    print "AND         ",D
##                    print "DUE TO ___________",B
                 
                    break
                #A Cutting A in half in X if AxMax inside B-X
                if A.maxX>B.minX and A.maxX<=B.maxX and A.minX<B.minX:
                    D=[A.minX,A.minY,A.minZ,B.minX,A.maxY,A.maxZ]
                    C=[B.minX,A.minY,A.minZ,A.maxX,A.maxY,A.maxZ]
                    cells.remove(d[a])
                    cells.append(C)
                    cells.append(D)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
 
                    if gorilla!=ape:
                        print "E"
                    cat=True
                    break
                #A Cutting A in half in Y if AyMin inside B-Y
                if A.minY>=B.minY and A.minY<B.maxY and A.maxY>B.maxY:
                    D=[A.minX,B.maxY,A.minZ,A.maxX,A.maxY,A.maxZ]
                    C=[A.minX,A.minY,A.minZ,A.maxX,B.maxY,A.maxZ]
                    cells.remove(d[a])
                    cells.append(C)
                    cells.append(D)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
 
                    if gorilla!=ape:
                        print "F"
                    cat=True
                    break
                #A Cutting A in half in Y if AyMax inside B-Y
                if A.maxY>B.minY and A.maxY<=B.maxY and A.minY<B.minY:
                    D=[A.minX,A.minY,A.minZ,A.maxX,B.minY,A.maxZ]
                    C=[A.minX,B.minY,A.minZ,A.maxX,A.maxY,A.maxZ]
                    cells.remove(d[a])
                    cells.append(C)
                    cells.append(D)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
 
                    if gorilla!=ape:
                        print "G"
                    cat=True
                    break
                #A Cutting A in half in Z if AzMin inside B-Z
                if A.minZ>=B.minZ and A.minZ<B.maxZ and A.maxZ>B.maxZ:
                    D=[A.minX,A.minY,B.maxZ,A.maxX,A.maxY,A.maxZ]
                    C=[A.minX,A.minY,A.minZ,A.maxX,A.maxY,B.maxZ]
                    cells.remove(d[a])
                    cells.append(C)
                    cells.append(D)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
 
                    if gorilla!=ape:
                        print "H"
                    cat=True
                    break
                #A Cutting A in half in Z in AzMax inside B-Z
                if A.maxZ>B.minZ and A.maxZ<=B.maxZ and A.minZ<B.minZ:
                    D=[A.minX,A.minY,A.minZ,A.maxX,A.maxY,B.minZ]
                    C=[A.minX,A.minY,B.minZ,A.maxX,A.maxY,A.maxZ]
                    cells.remove(d[a])
                    cells.append(C)
                    cells.append(D)
                    q,w,e,r,t,y=D
                    ape+=(r-q)*(t-w)*(y-e)
                    q,w,e,r,t,y=C
                    ape+=(r-q)*(t-w)*(y-e)
 
                    if gorilla!=ape:
                        print "I"
                    cat=True
                    break
 
    Total=0
    for x1,y1,z1,x2,y2,z2 in cells:
        Total+=(x2-x1)*(y2-y1)*(z2-z1)
  #  print Total
    return Total
                
                

CompleteTotal=0 
#check each Cell Volume
for Xx in xrange(0,52):#this reaches x=10200 and dx will be 200 more
    print "Countdown to 51,.,,",Xx
    for Yy in xrange(0,52):#ditto for y
        
        for Zz in xrange(0,52):
            cuboids= V[Xx][Yy][Zz]
            x=200*Xx
            y=200*Yy
            z=200*Zz
            cells=[]
            for a in cuboids:
                
                
                    A=[max(N[a][0],x),max(N[a][1],y),max(N[a][2],z),min(N[a][3],x+200),min(N[a][4],y+200),min(N[a][5],z+200)]
                    cells.append(A)
            
          #  print "Trying voxel:",Xx,Yy,Zz," IT started with ",len(cells)," boxes"
            
            CompleteTotal+=returnVolumeOfCell(cells)
            
            
                    
                      

              


 
print "Running time:",time.time()-RAS
#initial setup runs about 1.2 seconds         
#Matching up each possible box to each box each cell about 10.3 seconds
print "Non overlapping Volume",CompleteTotal
"""
[398L, 43L, 2065L, 399, 91L, 2101L]A
[266L, 278L, 2325L, 399, 339L, 2399]B
[257L, 186L, 2380L, 396L, 399, 2399]C
[127L, 208L, 2000, 235L, 399, 2265L]D
Looping
[398L, 43L, 2065L, 399, 91L, 2101L]A
[257L, 186L, 2380L, 396L, 399, 2399]C
[127L, 208L, 2000, 235L, 399, 2265L]D
[397L, 278L, 2325L, 399, 339L, 2399]   B Divided because of C x:   E
[266L, 278L, 2325L, 396L, 339L, 2399]  B Divided because of C x:  F
Looping
[398L, 43L, 2065L, 399, 91L, 2101L]A
[127L, 208L, 2000, 235L, 399, 2265L]D
[397L, 278L, 2325L, 399, 339L, 2399]E
[266L, 278L, 2325L, 396L, 339L, 2399]F
[257L, 186L, 2380L, 265L, 399, 2399] Huh C part
[266L, 186L, 2380L, 396L, 399, 2399]C


 

"""
 
#SEEMS TO WORK WELL
def B(x0,y0,z0,x1,y1,z1):

    BoundX=set()
    BoundY=set()
    BoundZ=set()
    for x in range(x0/200,(x1)/200+1):
        BoundX.add(x)
    for y in range(y0/200,(y1)/200+1):
        BoundY.add(y)
    for z in range(z0/200,(z1)/200+1):
        BoundZ.add(z)
    Bound=[BoundX,BoundY,BoundZ]
    for x,y,z in itertools.product(*Bound):
        print (x,y,z)
    print [x0,y0,z0,x1,y1,z1]
