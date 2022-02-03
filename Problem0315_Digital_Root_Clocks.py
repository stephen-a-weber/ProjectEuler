
"""
Digital root clocks
Problem 315

Sam and Max are asked to transform two digital clocks into two "digital root" clocks.
A digital root clock is a digital clock that calculates digital roots step by step.

When a clock is fed a number, it will show it and then it will start the calculation, showing all the intermediate values until it gets to the result.
For example, if the clock is fed the number 137, it will show: "137"  "11"  "2" and then it will go black, waiting for the next number.

Every digital number consists of some light segments: three horizontal (top, middle, bottom) and four vertical (top-left, top-right, bottom-left, bottom-right).
Number "1" is made of vertical top-right and bottom-right, number "4" is made by middle horizontal and vertical top-left, top-right and bottom-right. Number "8" lights them all.

The clocks consume energy only when segments are turned on/off.
To turn on a "2" will cost 5 transitions, while a "7" will cost only 4 transitions.

Sam and Max built two different clocks.

Sam's clock is fed e.g. number 137: the clock shows "137", then the panel is turned off, then the next number ("11") is turned on, then the panel is turned off again and finally the last number ("2") is turned on and, after some time, off.
For the example, with number 137, Sam's clock requires:
"137"	:	(2 + 5 + 4)  2 = 22 transitions ("137" on/off).
"11"	:	(2 + 2)  2 = 8 transitions ("11" on/off).
"2"	:	(5)  2 = 10 transitions ("2" on/off).
For a grand total of 40 transitions.
Max's clock works differently. Instead of turning off the whole panel, it is smart enough to turn off only those segments that won't be needed for the next number.
For number 137, Max's clock requires:
"137"

:

2 + 5 + 4 = 11 transitions ("137" on)
7 transitions (to turn off the segments that are not needed for number "11").
"11"


:


0 transitions (number "11" is already turned on correctly)
3 transitions (to turn off the first "1" and the bottom part of the second "1"; 
the top part is common with number "2").
"2"

:

4 tansitions (to turn on the remaining segments in order to get a "2")
5 transitions (to turn off number "2").
For a grand total of 30 transitions.
Of course, Max's clock consumes less power than Sam's one.
The two clocks are fed all the prime numbers between A = 107 and B = 2107. 
Find the difference between the total number of transitions needed by Sam's clock and that needed by Max's one.


Answer:
13625242
Completed on Sun, 26 May 2013, 17:47

"""
import time
RAS=time.time()
MAX={}
BULBS=  [6,2,5,5,4,5,6,4,7,6]
#Sams typical clock can use BULBS for digit transforms
for n in xrange(0,10):
    MAX[n]=[]
    #   0,1,2,3,4,5,6,7,8,9
MAX[0]=[0,4,3,3,4,3,2,2,1,2]
MAX[1]=[4,0,5,3,2,5,6,2,5,4]
MAX[2]=[3,5,0,2,5,4,3,5,2,3]
MAX[3]=[3,3,2,0,3,2,3,3,2,1]
MAX[4]=[4,2,5,3,0,3,4,2,3,2]
MAX[5]=[3,5,4,2,3,0,1,3,2,1]
MAX[6]=[2,6,3,3,4,1,0,4,1,2]
MAX[7]=[2,2,5,3,2,3,4,0,3,2]
MAX[8]=[1,5,2,2,3,2,1,3,0,1]
MAX[9]=[2,4,3,1,2,1,2,2,1,0]
#MAX is what it takes for a good clock digit transform
n=1
n=20000000



primes=[]
primes.append(2)
sieve=[True]*n
for i in xrange(4,n,2):
    sieve[i]=False
for i in xrange(3,n,2):
      if sieve[i]==True:
          primes.append(i)
     
           
          for j in xrange(i*i,n,i):
             sieve[j]=False

print "Done With Prime Creation"
primes=[r for r in primes if r>=10**7 and r<=2*10**7]
 
def LIST(n):
    g=[]
    while n!=0:
        g.append(n%10)
        n=n/10
    return g
def DigitalRoots(T):
    g=[]
    while T>=10:
        P=LIST(T)
        g.append(P)
        T=sum(P)
    g.append(LIST(T))
    return g
        
 
 
Total=0
  
for o in xrange(len(primes)):

    prime=primes[o]
    Roots=DigitalRoots(prime)
    for  q in xrange(len(Roots)-1):
  
         seq=Roots[q]
         nextSeq=Roots[q+1]
          
         b=len(nextSeq)
         for i in xrange(b):
             Total+=BULBS[seq[i]]+BULBS[nextSeq[i]]-MAX[seq[i]][nextSeq[i]]
    

print Total
                
                     
print time.time()-RAS                    
"""
SamsTotal=0
MaxsTotal=0
primes=[1999993] 
for o in xrange(len(primes)):
    SamsTotal=0
    MaxsTotal=0
    prime=primes[o]
    Roots=DigitalRoots(prime)
    for i in xrange(len(Roots[0])):
        SamsTotal+=BULBS[Roots[0][i]]
    MaxsTotal=SamsTotal#FIRST PRIME TURNED ON
    for  q in xrange(len(Roots)-1):
        
             seq=Roots[q]
             nextSeq=Roots[q+1]
             a=len(seq)
             b=len(nextSeq)
             for i in xrange(a):
                 if i<b:
                    SamsTotal+=BULBS[seq[i]]+BULBS[nextSeq[i]]
                    MaxsTotal+=MAX[seq[i]][nextSeq[i]]
                    #Digits Transitioning
                 else:
                     SamsTotal+=BULBS[seq[i]]
                     MaxsTotal+=BULBS[seq[i]]
                     #Digits Replaced with nothing
    for i in xrange(len(Roots[-1])):
        SamsTotal+=BULBS[Roots[-1][i]]
        MaxsTotal+=BULBS[Roots[-1][i]]
        #last Digits off
                  
    Total+=SamsTotal-MaxsTotal

print SamsTotal
print MaxsTotal
                 
            
"""    
    

