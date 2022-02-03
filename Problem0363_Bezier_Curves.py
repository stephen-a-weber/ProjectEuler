# -*- coding: utf-8 -*-
"""
Bézier Curves
Problem 363
A cubic Bézier curve is defined by four points: P0, P1, P2 and P3.
The curve is constructed as follows:
On the segments P0P1, P1P2 and P2P3 the points Q0,Q1 and Q2 are drawn such that P0Q0/P0P1=P1Q1/P1P2=P2Q2/P2P3=t (t in [0,1]).
On the segments Q0Q1 and Q1Q2 the points R0 and R1 are drawn such that Q0R0/Q0Q1=Q1R1/Q1Q2=t for the same value of t.
On the segment R0R1 the point B is drawn such that R0B/R0R1=t for the same value of t.
The Bézier curve defined by the points P0, P1, P2, P3 is the locus of B as Q0 takes all possible positions on the segment P0P1. (Please note that for all points the value of t is the same.) 

In the applet to the right you can drag the points P0, P1, P2 and P3 to see what the Bézier curve (green curve) defined by those points looks like. You can also drag the point Q0 along the segment P0P1.

From the construction it is clear that the Bézier curve will be tangent to the segments P0P1 in P0 and P2P3 in P3.




A cubic Bézier curve with P0=(1,0), P1=(1,v), P2=(v,1) and P3=(0,1) is used to approximate a quarter circle.
The value v0 is chosen such that the area enclosed by the lines OP0, OP3 and the curve is equal to π/4 (the area of the quarter circle).

By how many percent does the length of the curve differ from the length of the quarter circle?
That is, if L is the length of the curve, calculate 100*(L-π/2)/(π/2).
Give your answer rounded to 10 digits behind the decimal point.


Answer:
0.0000372091
Completed on Sat, 1 Jun 2013, 08:04

"""


import turtle
import math
import time
from bigfloat import *
Context(precision=40)
RAS=time.time()
AbscissaeValues=[ -0.1488743389816312157059030596428783610463,0.1488743389816312157059030596428783610463,-0.4333953941292472133994806426926515996456,0.4333953941292472133994806426926515996456,-0.6794095682990244355892173189204186201096,0.6794095682990244355892173189204186201096,-0.8650633666889845363456856830453034490347,0.8650633666889845363456856830453034490347,-0.9739065285171717434309357486199587583542,0.9739065285171717434309357486199587583542]
WeightValues=[ 0.2955242247147528700246255084493895992637,0.2955242247147528700246255084493895992637,0.2692667193099963496294435572053771466017,0.2692667193099963496294435572053771466017,0.2190863625159820415877476307286997325718,0.2190863625159820415877476307286997325718,0.1494513491505805868886369580650352872908,0.1494513491505805868886369580650352872908,0.0666713443086881379917585377370414789766,0.0666713443086881379917585377370414789766]
#above is n=10


#AbscissaeValues= [-0.5773502691896257310588680411456152796745,0.5773502691896257310588680411456152796745]
#WeightValues=[ 1.0000000000000000000000000000000000000000,1.0000000000000000000000000000000000000000]
#above is n=2

##AbscissaeValues=[-0.0640568928626056299791002857091370970011,0.0640568928626056299791002857091370970011,-0.1911188674736163106704367464772076345980,0.1911188674736163106704367464772076345980,-0.3150426796961633968408023065421730279922,0.3150426796961633968408023065421730279922,-0.4337935076260451272567308933503227308393,0.4337935076260451272567308933503227308393,-0.5454214713888395626995020393223967403173,0.5454214713888395626995020393223967403173,-0.6480936519369755455244330732966773211956,0.6480936519369755455244330732966773211956,-0.7401241915785543579175964623573236167431,0.7401241915785543579175964623573236167431,-0.8200019859739029470802051946520805358887,0.8200019859739029470802051946520805358887,-0.8864155270044010714869386902137193828821,0.8864155270044010714869386902137193828821,-0.9382745520027327978951348086411599069834,0.9382745520027327978951348086411599069834,-0.9747285559713094738043537290650419890881,0.9747285559713094738043537290650419890881,-0.9951872199970213106468008845695294439793,0.9951872199970213106468008845695294439793]
##WeightValues=[  0.1279381953467521593204025975865079089999,0.1279381953467521593204025975865079089999,0.1258374563468283025002847352880053222179,0.1258374563468283025002847352880053222179,0.1216704729278033914052770114722079597414,0.1216704729278033914052770114722079597414,0.1155056680537255991980671865348995197564,0.1155056680537255991980671865348995197564,0.1074442701159656343712356374453520402312,0.1074442701159656343712356374453520402312,0.0976186521041138843823858906034729443491,0.0976186521041138843823858906034729443491,0.0861901615319532743431096832864568568766,0.0861901615319532743431096832864568568766,0.0733464814110802998392557583429152145982,0.0733464814110802998392557583429152145982,0.0592985849154367833380163688161701429635,0.0592985849154367833380163688161701429635,0.0442774388174198077483545432642131345347,0.0442774388174198077483545432642131345347,0.0285313886289336633705904233693217975087,0.0285313886289336633705904233693217975087,0.0123412297999872001830201639904771582223,0.0123412297999872001830201639904771582223]
###above is n=24
##
WeightValues=[0.0486909570091397, 0.0486909570091397, 0.0485754674415034, 0.0485754674415034, 0.048344762234803, 0.048344762234803, 0.0479993885964583, 0.0479993885964583, 0.0475401657148303, 0.0475401657148303, 0.04696818281621, 0.04696818281621, 0.0462847965813144, 0.0462847965813144, 0.0454916279274181, 0.0454916279274181, 0.0445905581637566, 0.0445905581637566, 0.0435837245293235, 0.0435837245293235, 0.0424735151236536, 0.0424735151236536, 0.0412625632426235, 0.0412625632426235, 0.0399537411327203, 0.0399537411327203, 0.0385501531786156, 0.0385501531786156, 0.03705512854024, 0.03705512854024, 0.0354722132568824, 0.0354722132568824, 0.0338051618371416, 0.0338051618371416, 0.0320579283548516, 0.0320579283548516, 0.0302346570724025, 0.0302346570724025, 0.0283396726142595, 0.0283396726142595, 0.0263774697150547, 0.0263774697150547, 0.0243527025687109, 0.0243527025687109, 0.0222701738083833, 0.0222701738083833, 0.0201348231535302, 0.0201348231535302, 0.0179517157756973, 0.0179517157756973, 0.0157260304760247, 0.0157260304760247, 0.0134630478967186, 0.0134630478967186, 0.0111681394601311, 0.0111681394601311, 0.0088467598263639, 0.0088467598263639, 0.0065044579689784, 0.0065044579689784, 0.0041470332605625, 0.0041470332605625, 0.0017832807216964, 0.0017832807216964]
AbscissaeValues =[-0.0243502926634244, 0.0243502926634244, -0.072993121787799, 0.072993121787799, -0.1214628192961206, 0.1214628192961206, -0.1696444204239928, 0.1696444204239928, -0.2174236437400071, 0.2174236437400071, -0.2646871622087674, 0.2646871622087674, -0.311322871990211, 0.311322871990211, -0.3572201583376681, 0.3572201583376681, -0.4022701579639916, 0.4022701579639916, -0.4463660172534641, 0.4463660172534641, -0.489403145707053, 0.489403145707053, -0.5312794640198946, 0.5312794640198946, -0.571895646202634, 0.571895646202634, -0.6111553551723933, 0.6111553551723933, -0.6489654712546573, 0.6489654712546573, -0.6852363130542333, 0.6852363130542333, -0.7198818501716109, 0.7198818501716109, -0.7528199072605319, 0.7528199072605319, -0.7839723589433414, 0.7839723589433414, -0.8132653151227975, 0.8132653151227975, -0.8406292962525803, 0.8406292962525803, -0.8659993981540928, 0.8659993981540928, -0.8893154459951141, 0.8893154459951141, -0.9105221370785028, 0.9105221370785028, -0.9295691721319396, 0.9295691721319396, -0.9464113748584028, 0.9464113748584028, -0.9610087996520538, 0.9610087996520538, -0.973326827789911, 0.973326827789911, -0.983336253884626, 0.983336253884626, -0.9910133714767443, 0.9910133714767443, -0.9963401167719553, 0.9963401167719553, -0.9993050417357722, 0.9993050417357722]
#above is n=64



print len(WeightValues)

d=1


class point:
    x=BigFloat(0)
    y=BigFloat(0)
    def __init__(self,x=0,y=0):
        self.x=x 
        self.y=y
v=BigFloat(.551778477804 )         
#v=BigFloat(0.5522847498307936)#Find Magic Number c=2**,5ish middle circle 45degrees       
P0=point(1,0)
P1=point(1,v)
P2=point(v,1)
P3=point(0,1)
 
def arcIntegral(k):
    t=BigFloat(k)
    global P0,P1,P2,P3
  
    xpart=3*(1-t)*(1-t)*( P1.x-P0.x) + 6*(1-t)*t*( P2.x- P1.x)+ 3* t*t*( P3.x - P2.x)
    ypart=3*(1-t)*(1-t)*( P1.y-P0.y) + 6*(1-t)*t*( P2.y- P1.y)+ 3* t*t*( P3.y - P2.y)
    together= xpart*xpart+ypart*ypart
    integral= together**.5
    return integral
def areaIntegral(m):
    global P0,P1,P2,P3
    k=BigFloat(m)
    t=k
    global v
     
    xpart=3*(1-t)*(1-t)*( 1-1) + 6*(1-t)*t*( v- 1)+ 3* t*t*( 0 - v)
    Y=0*(1-k)*(1-k)*(1-k)+3*v*(1-k)*(1-k)*k+3*1*(1-k)*k*k+1*k*k*k
    return -Y*xpart
def arcLength(v):
    global AbscissaeValues
    global WeightValues
    N=len(AbscissaeValues)
  
    #  P0(1,0)   P1(1,v)    P2(v,1)    P3(0,1)
    global P0,P1,P2,P3
    global area
    area=BigFloat(0)
    sumarea=BigFloat(0)
    arcL=BigFloat(0) 
    z=1.0/2
    sumarc=BigFloat(0)
    for n in range(N):
        corrected=z*AbscissaeValues[n]+z
        sumarc+=WeightValues[n]*arcIntegral(corrected)
        sumarea+=WeightValues[n]*areaIntegral(corrected)
    arcL+=z*sumarc
    area+=z*sumarea
    print v,area,BigFloat(math.pi/4)
    a=BigFloat(math.pi/2)
    b=arcL-a
    c=div(b,a)
    c=c*100
    
    print "Calculated ArcLength:           ",arcL
    print "ABSOLUTE ArcLength pi/2         ",d*math.pi/2
    print "Percentage of this wanted =     ",c
    print "AREA== pi/4                     ",math.pi/4
    print "calculated area                 "  ,area
   
 
    return 
 
 
arcLength(v)
""" 
print "TIME:",time.time()-RAS 
r=.551778477804
f=[]
while r<=.551778477805:
    f.append(r)
    r+=.0000000000001
    
for v in f:
    arcLength(v)
 
"""