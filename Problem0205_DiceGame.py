"""
Dice Game
Problem 205
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg


Answer:
0.5731441
Completed on Fri, 15 Mar 2013, 17:42
"""


Peter=[]
P={}

for aa1 in range(1,5):
    for aa2 in range(1,5):
        for aa3 in range(1,5):
            for aa4 in range(1,5):
                for aa5 in range(1,5):
                    for aa6 in range(1,5):
                        for aa7 in range(1,5):
                            for aa8 in range(1,5):
                                for aa9 in range(1,5):
                                    a=(aa1+aa2+aa3+aa4+aa5+aa6+aa7+aa8+aa9)
                                    Peter.append(a)
                                    if a not in P:
                                        P[a]=1
                                    else:
                                        P[a]+=1
                                        
Colin=[]
C={}
for bb1 in range(1,7):
    for bb2 in range(1,7):
        for bb3 in range(1,7):
            for bb4 in range(1,7):
                for bb5 in range(1,7):
                    for bb6 in range(1,7):
                        b=(bb1+bb2+bb3+bb4+bb5+bb6)
                        Colin.append(b)
                        if b not in C:
                            C[b]=1
                        else:
                            C[b]+=1

#same= Colin.intersection(Peter)
PTotal=262144
CTotal=46656
 
pete=0
col=0
tie=0
for i in P:
    for j in C:
        if i==j:
            tie+=1*P[i]*C[j]
        elif i>j:
            pete+=1*P[i]*C[j]
        else:
            col+=1*P[i]*C[j]
 
ttt=len(Peter)*len(Colin)
a=tie*1.0/ttt
b=col*1.0/ttt
c=pete*1.0/ttt
print a+b+c
print  a,b,c

#http://mathworld.wolfram.com/Dice.html 

        


                                

                        
