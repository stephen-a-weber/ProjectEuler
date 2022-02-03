"""A Modified Collatz sequence
Problem 277
A modified Collatz sequence of integers is obtained from a starting value a1 in the following way:

an+1 = an/3 if an is divisible by 3. We shall denote this as a large downward step, "D".

an+1 = (4an + 2)/3 if an divided by 3 gives a remainder of 1. We shall denote this as an upward step, "U".

an+1 = (2an - 1)/3 if an divided by 3 gives a remainder of 2. We shall denote this as a small downward step, "d".

The sequence terminates when some an = 1.

Given any integer, we can list out the sequence of steps.
For instance if a1=231, then the sequence {an}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps "DdDddUUdDD".

Of course, there are other sequences that begin with that same sequence "DdDddUUdDD....".
For instance, if a1=1004064, then the sequence is DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
In fact, 1004064 is the smallest possible a1  106 that begins with the sequence DdDddUUdDD.

What is the smallest a1  1015 that begins with the sequence "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?


Answer:
1125977393124310
Completed on Mon, 17 Jun 2013, 13:23
"""
#m= "dDDUDDdDUUDUUdDUUDDDdUDUDUdDD"
m="UDDDUdddDDUDDddDdDddDDUDDdUUDd"
#m="DdDddUUdDD"
#m="UDDDUdddDDUDDddDdDddDDUDDdUUDddDDUDDdDUUDUUdDUUDDDdUDUDUdDD"
b=[r for r in m]
b.reverse()
a="".join(b)
#print m
#print a
man=0
"""
917713 29 60065266169871
1966289 30 96521732651065
6160593 30 302412864745714
10354897 30 508303996840363
14549201 30 714195128935012
18743505 30 920086261029661
22937809 30 1125977393124310
27132113 30 1331868525218959
31326417 30 1537759657313608
35520721 30 1743650789408257

1000000000000000    10**15
508303996840363
714195128935012
920086261029661
1125977393124310   GREATER THAN 10**15
1331868525218959
1537759657313608
1743650789408257 
for z in xrange(1,200000000):#[1966289]:
   r=0
   c=z
   for i in a:
        if i=="D":
            c=c*3
            #print c," pass D"
            r+=1
        elif i=="U":
            if (c*3-2)%4!=0:
                #print c,(c*3-2),"............"
                break
               
                 
                
            c=(c*3-2)  /4
            #print c," pass U"
            r+=1
        elif i=="d":
            if (c*3+1)%2!=0:
                 #print c,c*3+1,"__________"
                 break
                
                 
            c=(c*3 +1)/2
            #print c, " pass d"
            r+=1
   if man<r or r==29:
       man=r
       print z,r,c
 
""" 
n=1125977393124310
c=n
cat=""
while c!=1:#966289:
    f=c%3
    if f==0:
        c=c/3
        cat+="D"
    elif f==1:
        c=(4*c+2)/3
        cat+="U"
    else :
        c=(2*c-1)/3
        cat+="d"
     
print cat
print m
