#Odd period Square Roots problem 64
import math


def find(n):
    A0=int(math.sqrt(n))
    return A0


def reversed(a1,a2,b1,n):
    a11=b1*a1
    b11=a1**2*n-a2**2
    a12=0
    theint=0
    c=b1*a2
    if a11>1:#reduce equation
        b11=b11/a11
        c=c/a11
        a11=1
     
    theint=int((float(a1)*math.sqrt(n)+float(c))/float(b11))#pulling out the integer part
    a12=theint*b11-c
     
    return a11,a12,b11,theint
""" 
n=26
print find(n)  
a,b,c,theint=reversed(1,find(n),1,n)
print a,b,c,theint

q,w,e,r=reversed(a,b,c,n)
print q,w,e,r
p,o,i,u=reversed(q,w,e,n)
print p,o,i,u
q,w,e,r=reversed(p,o,i,n)
print q,w,e,r
p,o,i,u=reversed(q,w,e,n)
print p,o,i,u
q,w,e,r=reversed(p,o,i,n)
print q,w,e,r
p,o,i,u=reversed(q,w,e,n)
print p,o,i,u
q,w,e,r=reversed(p,o,i,n)
print q,w,e,r
""" 
def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) / 2
    for x in range(1, max_len):
        cat=True
        for y in range(x,max_len,x):
           
          
          if seq[0:x] != seq[y:y+x]  :
              cat=False
              break
            
        if cat:
            return x

numOdds=0
numEvens=0
for n in range(1,10001):
    if math.sqrt(n)==int(math.sqrt(n)):
        continue
    
   
    a,b,c,theint=reversed(1,find(n),1,n)
   
    cage=[theint]
    
    for i in range(1,1000):
         
        q,w,e,aint=reversed(a,b,c,n)
        cage.append(aint)
        a,b,c=q,w,e
    
    #cage should now contain a 1000 iterations of sequence
    
    x=guess_seq_len(cage)
     
    if x:
        
      if x%2==0:
          numEvens+=1
          #print n,cage[:50],x,"Even"
      else:
          numOdds+=1
          #print n,cage[:50],x,"Odd"
    else:
        print "Crashed at ",n
     
print numOdds
print numEvens


    
    
    
