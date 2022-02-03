


"""
Triangle containment
Problem 102
Three distinct points are plotted at random on a Cartesian plane, for which -1000  x, y  1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""
import math
f=open("/Users/isadmin/Documents/pythonCode/triangles.txt")
triangle=[]
RadToDeg=180.0/math.pi
tri=f.readlines()
tri[0].split("\n")
for i in tri:
    g=i.split(",")
    h=[]
    for j in range(0,6,2):
        
        v=int(g[j])
        v1=int(g[j+1])
        v
        h.append([v,v1])
    triangle.append(h)
  
d=[]
OriginCentered=0
NotOrigined=0
for a,b,c in triangle:

  
 
  
  if a==[0,0] or b==[0,0] or c==[0,0]:
        print "no"
  line1_length=math.sqrt(a[0]**2+a[1]**2)
  line2_length=math.sqrt(b[0]**2+b[1]**2)
  line3_length=math.sqrt(c[0]**2+c[1]**2)
  dot12=a[0]*b[0]+a[1]*b[1]
  dot13=a[0]*c[0]+a[1]*c[1]
  dot23=b[0]*c[0]+b[1]*c[1]
  #print a, line1_length
  angle12=math.acos(dot12/float(line1_length*line2_length))#*RadToDeg
  angle13=math.acos(dot13/float(line1_length*line3_length))#*#RadToDeg
  angle23=math.acos(dot23/float(line2_length*line3_length))#RadToDeg
  #print angle12+angle13+angle23

  d.append(angle12)
  d.append(angle13)
  d.append(angle23)
  
  if abs(angle12)+abs(angle13)+abs(angle23) >=(-.0000000003+2*math.pi):
      #print [a,b,c]
      #print angle12,angle13,angle23
      OriginCentered+=1
  else:
      NotOrigined+=1

print OriginCentered
print NotOrigined
c=[e for e in d if e <180 and e>175]
 
