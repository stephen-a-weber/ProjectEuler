#Arranged Probability Problem 100
"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""


from math import sqrt
import numpy as np
import scipy as sp
chain=1
def fr(b):
   return    (2+sqrt(8*b-4))/4.0
q=5.82842712474619
A=np.float64(2)
B=np.float64(0)
x=np.float64(0)
v=np.float64(0)
cat=True
while cat:
     
    B=2*A**2-2*A+1
    x=int((sqrt(B)+1.0)/2.0)
    if (x*2-1)**2==B:
        v=B/float(chain)
        
        chain=B
        print A,x#,"      ",v,"    ",B
      
      
        A=int(fr(B*v))
        
        
    else:
        A+=1
        #if A%(10**7)==0:
            #print A,x,x*1.0/A*(x-1)/(A-1)
 
    #    2+((4-8*(1-b))//4
           
            
         
        

 
