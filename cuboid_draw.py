from maya.cmds import  *
import math
def cube(x1,y1,z1,x2,y2,z2,a):
    
    polyCube(n="p")
    select("p.vtx[0]")
    move(x1,y1,z2)
    select("p.vtx[1]")
    move(x2,y1,z2)    
    select("p.vtx[2]")
    move(x1,y2,z2)
    select("p.vtx[3]")
    move(x2,y2,z2)
    select("p.vtx[4]")
    move(x1,y2,z1)    
    select("p.vtx[5]")
    move(x2,y2,z1)   
    select("p.vtx[6]")
    move(x1,y1,z1)
    select("p.vtx[7]")
    move(x2,y1,z1) 
    select("p")
    rename(a)
    
    
n=[[398L, 43L, 2065L, 399, 91L, 2101L],\
[127L, 208L, 2000, 235L, 399, 2265L],\
[397L, 278L, 2325L, 399, 339L, 2399],\
[266L, 278L, 2325L, 396L, 339L, 2399],\
[257L, 186L, 2380L, 265L, 399, 2399]]
count=97
for i in n:
    g=[r/100. for r in i]
    
    cube(g[0],g[1],g[2],g[3],g[4],g[5],chr(count))
    count+=1