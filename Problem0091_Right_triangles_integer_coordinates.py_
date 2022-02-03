import itertools
import math
import time
ras=time.time()
square=50
square+=1
total=0
points= [(x,y) for x in range(0,square) for y in range(0,square)]
points.remove((0,0))
  
for i in itertools.combinations(points,2):

    b=[r for r in i]
  
    b.append((0,0))
    
    f=[]
    
    for j in itertools.combinations(b,2):
         
        a,c=j
        x1,y1=a
        x2,y2=c
        f.append((x1-x2)**2+(y1-y2)**2)
    f.sort()
    if (f[0]+f[1])==f[2] and f[0]!=0 and f[1]!=0 and f[2]!=0:
             
            total+=1

print "The number of right triangles :",total
print "TIME :",time.time()-ras           


#Integer Lengthed right triangles in oblique mode in grid with origin as one vertex

"""
import math
import itertools
deer={}
intP=[[3,4,5],[5,12,13],[6,8,10],[7,24,25],[8,15,17],[9,12,15],[9,40,41],[10,24,26],[12,16,20],[12,35,37],[14,48,50],[15,20,25],[15,36,39],[16,30,34],[18,24,30],[20,48,52],[20,21,29],[21,28,35],[24,32,40],[24,45,51],[27,36,45],[28,45,53],[30,40,50],[33,44,55],[36,48,60],[40,42,58]]
deer[(0,0)]={}
point=[]

for a,b,c in intP:
    point.append((a,b))
    point.append((b,a))
    deer[(0,0)][(a,b)]=c
    deer[(0,0)][(b,a)]=c
print "here"   
for i in range(len(point)):
  
        deer[point[i]]={}
         
for a,b in point:
    for c,d in point:
        f=math.sqrt((a-c)*(a-c)+(b-d)*(b-d))
        if f==int(f) and f!=0:
        
                   deer[(a,b)][(c,d)]=f
                   deer[(c,d)][(a,b)]=f
                     
print "done"             
r=deer.keys()
r.remove((0,0))
total=0
for i in itertools.combinations(r,2):
    q,w=i
    a,b=q
    c,d=w
    if (c,d) in deer[(a,b)]:
        x=deer[(0,0)][(a,b)]
        y=deer[(0,0)][(c,d)]
        z=deer[(a,b)][(c,d)]
    
        if (x**2+y**2)==z**2 or (x**2+z**2)==y**2 or (y**2+z**2)==x**2:
             total+=1
             print a,b,"   ",c,d
"""