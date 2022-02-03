"""
Minimum of subsequences
Problem 375
Published on 10 March 2012 at 10:00 pm [Server Time]
Let Sn be an integer sequence produced with the following pseudo-random number generator:

S0	= 	290797 
Sn+1	= 	Sn2 mod 50515093
Let A(i, j) be the minimum of the numbers Si, Si+1, ... , Sj for i ≤ j.
Let M(N) = ΣA(i, j) for 1 ≤ i ≤ j ≤ N.
We can verify that M(10) = 432256955 and M(10 000) = 3264567774119.

Find M(2 000 000 000).
"""
#solution 7435327983715286168 


import time
import sys
RRRR=time.time()

# Problem is N=2000000000

#Sequence repeats with S[6308948]
# being the same as S[0]
# or 6308948 terms in the sequence

#The minimum of the sequence is 3
# This minimum is at S[2633996]
# this is 2633997 terms

 
def numberGen(x):
    home=[]
    S=290797
    S1=50515093
    result=S
    for v in range(1,x+1):
        result=pow(result,2,S1)
        home.append(result)
    return home



#First lets create a list with the
# sequence in total
# 6308948+2633997=8942946 full seq+ seq repeat to next minimum
# in a list S[8942945]

S=numberGen(8942945)

def totals(S):
    storage=[S]
    total=0
    while storage:
        T=storage.pop()
        L=len(T)
        m=min(T)
        
        P=T.index(m)+1
        
        total+=m*(L-P+1)*P
        
        if P!=1:
            
           A=T[:P-1]
          
           storage.append(A)
        if P!=L:
           B=T[P:]
           
           storage.append(B)
    return total



#Original Length of desired sequence       
remainingSeq=2000000000

#first part of seq to first minimum
H=S[:2633997]

#Shortening length by this first part
remainingSeq-=2633997

#totalling for this first part
totalAmount=totals(H)+3*(2633997)*(remainingSeq)

#Shortening Sequence down to the repeated minimum
S=S[2633997:]
 
Length=len(S)#6308948

#Finding the total for seq between the minimums
total=totals(S)
print total,"totals done"
print "Time ",time.time()-RRRR


while remainingSeq>=Length:
    remainingSeq-=Length
     
    totalAmount+=total+3*Length*remainingSeq



     
print totalAmount," total is this now."
print remainingSeq," is the length of remaining seq"



Y=S[:remainingSeq]

lastTotal=totals(Y)

print "result ",totalAmount+lastTotal
    
     
    
 
#solution 7435327983715286168   
 
    

    
    
    

 
sys.exit()

       
        
        
        

""" 
xxx=0
for i in range(1,R+1):

    L=K[i]
    count=0
    for j in range(i,R+1):
        if K[j]>L:
            xxx+=L
            
        else:
            L=K[j]
            xxx+=L
print xxx

#this code works for examples
"""
  
    

    
    

 
  
    
