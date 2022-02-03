from maya.cmds import *
select(all=True)
delete()
polyPlane(name="cell",sx=1,sy=1)
move(0,0,0)
setAttr("lambert1.color",.6,.1,.2,type="double3")
duplicate()
rename("cello") 

def create(steps):
    d=["Fa"]
    for _ in range(steps):
        f=d[-1]      
        f=f.replace("a","aR_FR")      
        f=f.replace("b","LF+Lb")
        f=f.replace("_","b")
        f=f.replace("+","a")
       
        d=[f]
    return d
d=create(5)
x=0
z=0
count=1
facing=1
for i in d[0]:
       
        count+=1
        if i=="F":
            if facing==1:
                
                z=z+1
            elif facing==0:
                x=x-1
            elif facing==2:
                x=x+1
            else:
                z=z-1
            select("cello",r=True)
            duplicate()
            rename("cell"+str(count))
            move(x,0,z)
            select("cell",add=True)
            polyUnite(ch=1,mergeUVSets=1)
            rename("cell")
            delete(all=True,constructionHistory=True)
        elif i=="R":
            facing+=1
            facing=facing%4
        elif i=="L":
            facing-=1
            facing=facing%4
        else:
            continue
            
