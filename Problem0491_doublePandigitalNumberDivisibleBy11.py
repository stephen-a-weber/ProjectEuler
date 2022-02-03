"""
Double pandigital number divisible by 11
Problem 491
We call a positive integer double pandigital if it uses all the digits 0 to 9 exactly twice (with no leading zero). For example, 40561817703823564929 is one such number.

How many double pandigital numbers are divisible by 11?


Answer:
194505988824000
Completed on Fri, 30 Oct 2015, 19:54
"""
import itertools
count=0

digits=[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
choices=[]
positives=[]
negatives=[]

def frank(n):
    fran=[]
    fran=[r for r in digits]
    for i in n:
        fran.remove(i)
    return fran
    
for positives in itertools.combinations(digits,10):
    count+=1
    negatives=frank(positives)
    a=sum(positives)
    b=sum(negatives)
    positives=list(positives)
    positives.sort()
    negatives.sort()
    c=a-b
    if c//11==c/11:
        
        choices.append([tuple(positives),tuple(negatives)])


print(count,len(choices))

index=0
while index<len(choices):
    if choices.count(choices[index])>1:
        g=choices.pop(index)
    else:
        index+=1



import math
def FAC(n):
    return math.factorial(n)


def numberpositives(n):
    f=set(n)
    frog={}
    for i in f:
        frog[i]=n.count(i)

    if 0 not in f:
        initial=FAC(10)
        for i in f:
            initial/=FAC(frog[i])
        
    else:
        if frog[0]==1:
            initial=9*FAC(9)
            for i in f:
                initial/=FAC(frog[i])
        if frog[0]==2:
            initial=8*FAC(9)
            for i in f:
                initial/=FAC(frog[i])
    return initial

def numbernegatives(n):
    f=set(n)
    frog={}
    for i in f:
        frog[i]=n.count(i)
    initial=FAC(10)
    for i in f:
        initial/=FAC(frog[i])
    return initial

 
permpositive=0
permnegative=0
total=0
print ("number of choices ", len(choices))


for a,b in choices:
    permpositive =numberpositives(a)
    permnegative =numbernegatives(b)
    total+=permpositive*permnegative
print ("The permutations of these choices gives an answer of ",total)





    
    
