"""
Investigating multiple reflections of a laser beam.
Problem 144
In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam. The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100

The section corresponding to 0.01  x  +0.01 at the top is missing, allowing the light to enter and exit through the hole.


The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection "angle of incidence equals angle of reflection." That is, both the incident and reflected beams make the same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between the laser beam and the wall of the white cell; the blue line shows the line tangent to the ellipse at the point of incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = 4x/y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?


Answer:
354
Completed on Mon, 20 May 2013, 10:48
"""


import pickle
#from fractions import Fraction
#Initial Incidence ray
X=0.0
Y=10.1
x=1.4
y=-9.6
Mi=(y-Y)/(x-X)
Bi=y-Mi*x
 
#Initial Surface
M=-4*x/y
B=10.1-M*x
storage=[tuple([x,y])] 
rays=0
point=0
cat= True
 
while cat:
    print "...",x,y
    if rays%100==0:
        print "rays at",rays
    rays+=1
    M=-4*x/y
    B=y-M*x
  
    vertical=False
    #working on next ray hoping it escapes
    if abs(M)==1 and Mi==0:
         
        vertical=True
        #hope it is last ray to leave...
    elif abs(M)==1 and Mi!=0:
        Mr=1.0/Mi
        Br=y-x*Mr
    else:
        Mr=(2*M-Mi*(1-M*M))/(1-M*M+2*M*Mi)
        Br=y-Mr*x
    if not vertical:
        X,Y=storage[point]
        point+=1
        
        mess=(4*Mr*Mr*Br*Br-4*(4+Mr*Mr)*(Br*Br-100))**.5
        mess2=2*(4+Mr*Mr)
        xx1=(-2*Mr*Br-mess)/mess2
        a,b= (-2*Mr*Br+mess)/mess2,Mr*(-2*Mr*Br+mess)/mess2+Br
        c,d= (-2*Mr*Br-mess)/mess2,Mr*(-2*Mr*Br-mess)/mess2+Br
        print "________________________________"
        print X,Y
        print "............."
        print a,b
        print c,d
         
        if round(X,9)==round(a,9) and round(Y,9)== round(b,9):
            x=c 
            y=d
        elif round(X,9)==round(c,9) and round(Y,9)==round(d,9):
            x=a
            y=b
        else:
            print "OPPS"
            
        if xx1==X:
            x=(-2*Mr*Br+mess)/mess2
           
       
        Mi=Mr
        Bi=Br
        storage.append(tuple([x,y]))
    else:
        print "opps"
    print "THe code chooses one with x of",x
    print "_______________________________"


    if (x<=.01 and x>=-.01) and (y>8):
        cat=False


print rays
ff=open("C:/Users/sweber/Desktop/rays.python","w+b")
pickle.dump(rays,ff)
ff.close()

        
