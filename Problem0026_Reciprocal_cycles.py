"""Reciprocal cycles
Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


Answer:
983
Completed on Thu, 24 Jan 2013, 21:45
"""
import time
RAS=time.time()
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

longest=0
def cycle_length(n):
    """
    repeated cycles
    """
    start=0
    checking=True
    end=len(n)
    space=1
    while checking:
        seq= guess_seq_len(n[start:])
        if not seq:
           start+=1
        else:
            checking=False
                    
                            
    return seq
            
            
longest=0
longestD=0

denominator=1
while denominator<1000:
    seq=[]
    numerator=1
    while len(seq)<5000:
         
         
        if numerator*1.0/denominator<1:
            seq.append(0)
            numerator*=10
        else:
            digit=int(numerator*1.0/denominator)
            seq.append(digit)
            numerator-=digit*denominator
   # print denominator 
    seqLength=cycle_length(seq)
    if seqLength>longest:
        longest=seqLength
        longestD=denominator
    denominator+=1
     
print "The answer is ",longestD, "with   a length of ",longest
        
print "THIS TOOK ",time.time()-RAS," seconds"   
        
        
    
