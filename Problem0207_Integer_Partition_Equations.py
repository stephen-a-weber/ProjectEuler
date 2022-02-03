"""Integer partition equations
Problem 207
For some positive integers k, there exists an integer partition of the form   4t = 2t + k,
where 4t, 2t, and k are all positive integers and t is a real number.

The first two such partitions are 41 = 21 + 2 and 41.5849625... = 21.5849625... + 6.

Partitions where t is also an integer are called perfect.
For any m  1 let P(m) be the proportion of such partitions that are perfect with k  m.
Thus P(6) = 1/2.

In the following table are listed some values of P(m)

   P(5) = 1/1
   P(10) = 1/2
   P(15) = 2/3
   P(20) = 1/2
   P(25) = 1/2
   P(30) = 2/5
   ...
   P(180) = 1/4
   P(185) = 3/13

Find the smallest m for which P(m)  1/12345


Answer:
44043947822
Completed on Fri, 24 May 2013, 13:17

"""
#removing printing possibilities and just streamlining to answer
Ints=0
Total=0
kk=1
power=4
right=1
while True:
    kk=kk+2
    if kk==(power)-1:
        Ints+=1
        right=Ints*12345
        power*=2 
    Total+=1
    if right<Total:       
        break
print "The answer is ",(kk*kk-1)/4

###########################
#otherwise




import math
from fractions import Fraction
Ints=0
Total=0
aaa=0
bbb=0
k=0
kk=1
while True:
    kk=kk+2
    k=(kk*kk-1)/4
    K=(1+(1+4*k)**.5)/2
    t=math.log(K,2)
    a=4**t
    b=2**t
   
    #print k,t,a,b,
    Total+=1
    if int(t)==t:
        Ints+=1
        #print  True,
    else:
        pass
        #print False,
    aaa= Fraction(Ints,Total)
    
    bbb=k
    #print aaa
    if aaa<Fraction(1,12345):
        print "Over"
        break
        
      
print float(aaa),"<",1.0/12345
print "The answer is ",bbb
  
