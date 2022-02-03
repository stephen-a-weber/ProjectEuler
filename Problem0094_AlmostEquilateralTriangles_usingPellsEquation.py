import math
import time
startT=time.time()
#
# In a triange with two sides of equal length a
# And the third  base side either a+1 or a-1
#
# Find the sum of the perimeters of all triangles with integer area
# Obviously integer perimeter with no perimeter larger then 1 billion.
#
# the height is sqrt((((  3*a**2 (+-) 2*a +1 )))))/2
# set this equal to y and solve for y**2
#
# Gives  ( (3*a (+-) 1)/2 )**2  - 3*y**2   =   1
#          
# let x =(3*a (+-) 1)/2
#
#
# Pells Equation comes up:  x**2 - 3*y**2 = 1

# Wikipedia solution from a base case
# base case solution is (2,1)
#
# Xk +Yk*(N)**.5  =  (X1 +Y1*(N)**.5)**k
#
# Xk+1 = X1*Xk + N*Y1*Yk
# Yk+1 = X1*Yk + Y1*Xk


#base case (2,1)    2**2 - 3 * 1**2 = 1    ----  4-3=1

X1=2
Y1=1
X=[X1]
Y=[Y1]

#N =3

N=3


for k in range(1,50):
    X.append(X1*X[k-1]+N*Y1*Y[k-1])
    Y.append(X1*Y[k-1]+Y1*X[k-1])
""" 
for i in range(len(X)):
    print X[i],Y[i]
""" 
# From above ... we are letting y equal the height....
# From above.....we can get the side of the triangle from x
# since  x =(3*a (+-) 1)/2

# The check is on the integral area.
# the two matching sides a can be (2*x  (-+) 1) )/ 3
# the base again is (+-) 1 from these two cases (2*x  (-+) 1) )/ 3 +-1
# Base = (2*x (+-) 4)/3
# we must divide this by 2 and multiply by height. The height is
# guaranteed to be an integer as that is what the pell equation solves for....
# the height again being just y
# so we have the two areas being (Y*(X (+-) 2)/3)
#and we can check if this is an integer if (X (+-) 2)%3==0
# NOTE THAT really small values can make AREA zero so a quick check
#for That  if X (+-2)==0
#perimeter   2*X (+-) 2 < 1 billion
total=0
limit=1000000000
for i in range(len(X)):
    areaCheck=X[i]+2
    if areaCheck%3==0:
        if 2*X[i]+2>limit:
            break
        total+=2*X[i]+2
    areaCheck=X[i]-2
    if areaCheck%3==0:
        if 2*X[i]-2>limit:
            break
        #IF Side==1 and BASE =Side-1=0.. Area =0
        if (2*X[i] -4)/3==0:
            continue
        
       
        total+=2*X[i]-2
print total
        

































print "time : ",time.time()-startT
