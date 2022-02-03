from maya.cmds import  *
import math
select(all=True)
delete()
circle(n="g",nr=[0,1,0],s=6,d=1)
planarSrf(n="hex",d=3,ko=0,rn=1,po=1,tol=.01)
rename("hex")
setAttr("nurbsTessellate1.uNumber",2)
setAttr("nurbsTessellate1.vNumber",2)
delete(ch=True)
delete("g") 
select("hex.e[7]",r=True)
delete()
select("hex.e[1]",r=True)
delete()
select("hex",r=True)
polyExtrudeFacet(thickness=.2)

polyBevel(offset=.03)
rot=math.pi/6 
length=3**.5#4*math.sin(math.pi/6)
radius=0 
k=1
r=1
y=.2
t=7
p=0
xx=0
zz=0
xxx=0
zzz=0 
lastone=0
face=0
select("hex",r=True)
duplicate()
 
root=0
for r in range (1,3):
    t=[math.pi/3*s for s in range(6)]
    xx=[math.cos(t[i])*length*r for i in range(6)]
    zz=[math.sin(t[i])*length*r for i in range(6)]
    
    if r==1:
              
        for i in range(6):
            select("hex",r=True)
            duplicate()
             
            move(xx[i],0,zz[i])
    else:
        middles=r
        for i in range(6):
            select("hex",r=True)
            duplicate()
             
            move(xx[i],0,zz[i])
            x=(xx[(i+1)%6]-xx[i]) /middles
            z=(zz[(i+1)%6]-zz[i]) /middles
            for m in range(1,middles):
                print r,middles
                select("hex",r=True)
                duplicate()
                  
                move(xx[i]+x*m,0,zz[i]+z*m)
                    