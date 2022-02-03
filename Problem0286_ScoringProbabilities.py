
import sys
"""Scoring probabilities
Problem 286
Barbara is a mathematician and a basketball player. She has found that the probability of scoring a point when shooting from a distance x is exactly (1 - x/q), where q is a real constant greater than 50.

During each practice run, she takes shots from distances x = 1, x = 2, ..., x = 50 and, according to her records, she has precisely a 2 % chance to score a total of exactly 20 points.

Find q and give your answer rounded to 10 decimal places.


Answer:
52.6494571953
Completed on Mon, 16 Nov 2015, 19:08
"""
"""
The exact probability is called it turns out Poisson Bernouilli Distribution

just with p1 p2 p3 p4 ... instead of one p

but it is the combinations of possibilities equalling the called
for probability
so since we aren't using variables we can calculate all the probs for
any q
then there is creating a function to find this.

with 1 element

0-f1
1-p1

with 2 elements

0-f1f2                       implies take each row and multiply by fn
1-p1f2 p2f1                  then take each row multiply by pn and put in next row
2-p1p2

with 3 elements
ABOVES FOR 2         BECOMES
0-f1f2                0-f1f2f3
                      1-f1f2p3
1-p1f2 p2f1           1-p1f2f3   p2f1f3
                      2-p1f2p3   p2f1p3
2-p1p2                2-p1p2f3
                      3-p1p2p3
with 3 elements
0-f1f2f3                         no passes
1-f1f2p3 p1f2f3 p2f1f3          each has one pass
2-p1f2p3 p2f1p3 p1p2f3          each with two passes
3-p1p2p3                        all three passes

"""



k=20
q=52.6
def Probability(q):
    PBD=[0]*51
    PBD[0]=[1]
    F=[x/q for x in range(0,51)]
    P=[1-x for x in F]

    C=[0]*k       

    for n in range(1,51):
        A=PBD[n-1]
        C=[0]*(len(A)+1)
        for i in range(len(A)):
            C[i]+=A[i]*F[n]
            C[i+1]+=A[i]*P[n]
        PBD[n]=C
    return PBD
        
        
"""    
for qq in range(5264945719530910,5264945719530921,1):
    q=qq/100000000000000.
    PBD=Probability(q)
    
   
    print(q,PBD[50][20]) 
#52.6494571953
"""
lo=52.
old=1000.
hi=99.
while True:
    q=(lo+hi)/2
    x=Probability(q)
    y=x[50][20]
    print(q,y)
    if y<.02:
        hi=q
    if y>.02:
        lo=q
    if q==old:
        sys.exit()
    old=q
    
    
        
    
    
    
    
    








            
   
