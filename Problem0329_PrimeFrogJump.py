"""
Prime Frog
Problem 329
Susan has a prime frog.
Her frog is jumping around over 500 squares numbered 1 to 500. He can only jump one square to the left or to the right, with equal probability, and he cannot jump outside the range [1;500].
(if it lands at either end, it automatically jumps to the only available square on the next move.)

When he is on a square with a prime number on it, he croaks 'P' (PRIME) with probability 2/3 or 'N' (NOT PRIME) with probability 1/3 just before jumping to the next square.
When he is on a square with a number on it that is not a prime he croaks 'P' with probability 1/3 or 'N' with probability 2/3 just before jumping to the next square.

Given that the frog's starting position is random with the same probability for every square, and given that she listens to his first 15 croaks, what is the probability that she hears the sequence PPPPNNPPPNPPNPN?

Give your answer as a fraction p/q in reduced form.

Answer:
199740353/29386561536000
Completed on Wed, 11 Nov 2015, 05:54"""

import time
 
from fractions import Fraction
rrr=time.time()
n=501


board=["P"]* n
board[1]="N"
board[0]="N"
board[2]="P"
for i in range(4,n,2):
    board[i]="N"
for i in range(3,n,2):    
    if board[i]=="P":
        
        for j in range(i*i,n,i):
            board[j]="N"


heard="PPPPNNPPPNPPNPN"
 
dictseq={}
def prob(position,seq):
    global dictseq
    temp=0
    squareProb=0
    if seq=="":
        return 1
    

    
    if (position,seq)in dictseq:
        return dictseq[(position,seq)]
       
    if seq[0]==board[position]:
        squareProb=Fraction(2,3)
    else:
        squareProb=Fraction(1,3)
        
    if position==1 :
        temp= squareProb*prob(2,seq[1:])
    
    elif position==500 :
        temp= squareProb*prob(499,seq[1:])
    else :  
        temp= squareProb*Fraction(1,2)*(prob(position+1,seq[1:])+prob(position-1,seq[1:]))

        
    dictseq[(position,seq)]=temp
    return temp
probability=0                                              
for position in range(1,501):
    
    probability+=prob(position,heard)
    

print(probability/500)
print (time.time()-rrr)
    


"""
72599658529994479407104527942207128254604194111450217117275252373322604173581
/9776386633518291972807336862896691263402147840000000000000000000000000000000000000000000000000000000

"""      
#199740353/29386561536000
    
    
