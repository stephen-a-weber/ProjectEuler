"""
Intersections
Problem 165
A segment is uniquely defined by its two endpoints.
By considering two line segments in plane geometry there are three possibilities:
the segments have zero points, one point, or infinitely many points in common.

Moreover when two segments have exactly one point in common it might be the case that that common point is an endpoint of either one of the segments or of both. If a common point of two segments is not an endpoint of either of the segments it is an interior point of both segments.
We will call a common point T of two segments L1 and L2 a true intersection point of L1 and L2 if T is the only common point of L1 and L2 and T is an interior point of both segments.

Consider the three segments L1, L2, and L3:

L1: (27, 44) to (12, 32)
L2: (46, 53) to (17, 62)
L3: (46, 70) to (22, 40)

It can be verified that line segments L2 and L3 have a true intersection point. We note that as the one of the end points of L3: (22,40) lies on L1 this is not considered to be a true point of intersection. L1 and L2 have no common point. So among the three line segments, we find one true intersection point.

Now let us do the same for 5000 line segments. To this end, we generate 20000 numbers using the so-called "Blum Blum Shub" pseudo-random number generator.

s0 = 290797

sn+1 = snsn (modulo 50515093)

tn = sn (modulo 500)

To create each line segment, we use four consecutive numbers tn. That is, the first line segment is given by:

(t1, t2) to (t3, t4)

The first four numbers computed according to the above generator should be: 27, 144, 12 and 232. The first segment would thus be (27,144) to (12,232).

How many distinct true intersection points are found among the 5000 line segments?


Answer:
2868868
Completed on Mon, 13 May 2013, 10:01
"""

from fractions import Fraction
P={}

def blumblumshub():
    s=290797
    w=0
    while w<20000:
         
        w+=1
        s=(s*s)%50515093
        a= s%500
        w+=1
        s=(s*s)%50515093
        b=s%500
        w+=1
        s=(s*s)%50515093
        c=s%500
        w+=1
        s=(s*s)%50515093
        d=s%500
        a=Fraction(a)
        b=Fraction(b)
        c=Fraction(c)
        d=Fraction(d)
        yield tuple([a,b,c,d])

lines=[]        
for i in blumblumshub():
    a,b,c,d=i
    lines.append(tuple(i))
        
    if (c-a)!=0:
       m=Fraction( (d-b),(c-a))
       B=b-m*a
       P[i]=[False,m,B]
    else:
        P[i]=[True,(c)]
count=0#intersection
distinct=set()
for I in range(4999):
    if I%100==0:
        print I,count
    for J in range(I+1,5000):
        #vertical line
        i=lines[I]
        j=lines[J]
    
        if P[i][0]==True and P[j][0]==True:
             continue
        elif P[i][0]==True:#i line is vertical
            X=Fraction(P[i][1])#x value
           
    
            Y=Fraction(P[j][1]*X+P[j][2])#calculated y value to intersect vertical line
            q,w,e,r=j
            a,b,c,d=i
            at=[[a,b],[c,d],[q,w],[e,r]]
             
            if [X,Y] not in at:
                
                passing =False
                if e>q:
                    if X>q and X<e:
                        passing=True
                elif q>e:
                    if X<q and X>e:
                        passing=True
                elif q==e:
                    passing=False
                if passing:                       
                     #range of y values on vertical line
                    if d>b:
                        if Y>b and Y<d:
                            count+=1
                            distinct.add(tuple([X,Y]))
                            
                    elif b>d:
                        if Y>d and Y<b:
                            count+=1
                            distinct.add(tuple([X,Y]))
                    elif b==d:
                        if Y==b:
                            count+=1
                            distinct.add(tuple([X,Y]))#horizontal and vertical line
                        
                           
        elif P[j][0]==True:
            X=Fraction(P[j][1])#j vertical line
            
               
            Y=Fraction(P[i][1]*X+P[i][2])#calculated y value to intersect vertical line
            q,w,e,r=i
            a,b,c,d=j
            at=[[a,b],[c,d],[q,w],[e,r]]
             
            if [X,Y] not in at:           
                passing =False
                if e>q:
                    if X>q and X<e:
                        passing=True
                elif q>e:
                    if X<q and X>e:
                        passing=True
                elif q==e:
                    passing=False
                if passing:                       
                     #range of y values on vertical line
                    if d>b:
                        if Y>b and Y<d:
                            count+=1
                            distinct.add(tuple([X,Y]))
                           
                    elif b>d:
                        if Y>d and Y<b:
                            count+=1
                            distinct.add(tuple([X,Y]))
                    elif b==d:
                        if Y==b:
                            count+=1
                            distinct.add(tuple([X,Y]))#horizontal and vertical line
        
        else:
            p1,m1,b1=P[i]
            p2,m2,b2=P[j]
             
            if m1!=m2:
                a,b,c,d=i
                q,w,e,r=j
                X=Fraction((b2-b1),(m1-m2))
                Y=Fraction(m1*X+b1)               
                x1pass=False
                y1pass=False
                x2pass=False
                y2pass=False             
                if c>a:
                    if X >a and X<c:
                        x1pass=True
                elif c<a:
                    if X<a and X>c:
                        x1pass=True
                elif c==a:
                    print "No Way"
                if d>b:
                    if Y>b and Y<d:
                        y1pass=True
                elif d<b:
                    if Y<b and Y>d:
                        y1pass=True
                elif d==b and m1==0:
                        y1pass=True
                if e>q:
                    if X>q and X<e:
                        x2pass=True
                elif e<q:
                    if X<q and X>e:
                        x2pass=True
                elif e==q:
                    print "NO"
 
                if r>w:
                    if Y<r and Y>w:
                        y2pass=True
                elif r<w:
                    if Y>r and Y<w:
                        y2pass=True
                elif r==w and m2==0:
                    y2pass=True
                if x1pass==True and x2pass==True and y1pass==True and y2pass==True:
                    count+=1
                    at=[[a,b],[c,d],[q,w],[e,r]]
                     
                    if [X,Y] not in at:                    
                                    
                       distinct.add(tuple([X,Y]))
            else:
                pass
print count
print "the number of distinct points are:",len(distinct)
                        
                
                
                  
             
    
