#POSITIONING LATITUDE AND LONGITUDE

LAT=40.057179 #North
LONG=-76.5572  #West

DLAT=30.269#hurricane Jose 9/17//2017
DLONG=-71.873#157.2444086955905 84.746877243562

 
DLAT=38.897546#white house
DLONG=-77.036552#-162.15108279307788 89.39138798192285
 
DLAT=40.703189#new york
DLONG=-73.999334#70.83161598083399 88.97365513039136


 
DLAT=37.778932#San Francisco
DLONG=-122.265440#-78.63638081043024 72.3779437906609

 
DLAT=48.850193#Paris,France
DLONG=2.329309#52.54136047140143 62.78406827588084


 
DLAT=39.038518#North Korea
DLONG=125.898282#-17.446190373784646 40.85765597509988


 
DLAT=55.731944#Moscow
DLONG=37.196667#33.504434516829036 55.49607631885093

 
 
DLAT=19.829842#Hawaii
DLONG=-155.407989#-81.21793086674347 55.474496676607195

DLAT= 51.753352 # Oxford
DLONG=-1.257642  #  50.13646873790762 64.36513117315309 

 
DLAT=57.535947#Scotland
DLONG=-5.044693#43.51030429567791 66.15962632792008

 
DLAT=-31.839488#South Africa
DLONG=22.834712#110.57172713576301 31.768832360887497


 
DLAT=-87.548043#Antartica
DLONG=75.718124#178.4600325861348 23.891189259136958

 
DLAT=-25.147571#Antartica
DLONG=130.579547#178.4600325861348 23.891189259136958
 
DLAT=18.261#Puerto Rico
DLONG=-66.182#154.66998521044047 78.21886319315445


##DLAT=41
##DLONG=-76.5572  #due nouth 0,89.5 Correct

##DLAT=39
##DLONG=-76.5572  #due south -180,89.5 Correct
##
##DLAT=40.057179
##DLONG=-76 # due west 90,90
## 
##
##DLAT=40.057179
##DLONG=-77 # due east -90,90
## 
##DLAT=0  #equator
##DLONG=-76.5572  #due south -180,70 Correct
##
##DLAT=-40 # below equator
##DLONG=-76.5572  #due south -180,50 Correct
##
##DLAT=-90  #south pole
##DLONG=-76.5572  #due south -180,25 Correct
##
##
##DLAT=-40.057179  #opposite coord
##DLONG=-76.5572+180  #  26.5,0 Correct
##
##DLAT= 51.753352 # Oxford
##DLONG=-1.257642  #  50.13646873790762 64.36513117315309 
##
##DLAT= 51.760455 # Headington
##DLONG=-1.198849  #  50.11311915725531 64.34898377486036
##
##
##DLAT= 51.895349 # Bicester
##DLONG=-1.15201  # 49.937376699086656 64.35649743485946
##
##
##DLAT= 51.585869 # Wallingford
##DLONG=-1.119064  # 50.30502111894978 64.29783411095032
##
##DLAT= 51.495398 # London
##DLONG=-0.132775  # 50.160568319961556 63.99302953775101
####LAT= 51.753352 # Oxford
####LONG=-1.257642  #  50.13646873790762 64.36513117315309 
####DLAT=40.057179 #North
####DLONG=-76.5572  #West
##
## 

from math import pi
from math import cos
from math import sin
from math import acos
from math import atan


def norm(a ):
    d= sum([e*e for e in a]) 
    d=d**.5
    return d
     
def cross(b,a):
    d = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return d   

def multV(vector,god):
    d=[sum(a*b for a,b in zip(vector,god[t])) for t in range(3)]
    return d
    
lat=LAT*pi/180
long=LONG*pi/180

dlat=DLAT*pi/180
dlong=DLONG*pi/180

here=[cos(lat)*cos(long),cos(lat)*sin(long),sin(lat)] #spherical coordinates
dest=[cos(dlat)*cos(dlong),cos(dlat)*sin(dlong),sin(dlat)] #spherical coordinates

vector=[x - y for x, y in zip(here,dest)]

c=[e for e in here]
normal=norm(c)
c=[r/normal for r in c]

p=[0,0,1/sin(lat)]
a=[x - y for x,y in zip(p,here)]
normal=norm(a)
a=[r/normal for r in a]

b=cross(c,a)

 
god=[[x for x in a],[y for y in b],[z for z in c]]#Jacobian transformation matrix

 

vector = multV(vector,god)

normal=norm(vector)
vector=[r/normal for r in vector]

vertical=acos(vector[2])
vertical=vertical*180/pi
 
north=atan(vector[1]/vector[0])
north= north*180/pi-180




if vector[0]<0:
    north+=180
if north>180:
    north-=360
if north<-180:
    north+=360

print(north,vertical)
 
#Python3 program for finding 
