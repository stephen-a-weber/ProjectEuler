"""
Efficient exponentiation
Problem 122
The most naive way of computing n15 requires fourteen multiplications:

n  n  ...  n = n15

But using a "binary" method you can compute it in six multiplications:

n  n = n2
n2  n2 = n4
n4  n4 = n8
n8  n4 = n12
n12  n2 = n14
n14  n = n15

However it is yet possible to compute it in only five multiplications:

n  n = n2
n2  n = n3
n3  n3 = n6
n6  n6 = n12
n12  n3 = n15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1  k  200, find  m(k).


Answer:
1582
Completed on Tue, 19 Mar 2013, 06:13

"""
base={}
chili={}
for i in range(1,201):
    base[i]=[]
    chili[i]=1000000
base[1]=[]
base[2]=[2]
total=200
 
"""
base[2]=[2]
base[3]=[2,3]
base[4]=[2,4]
base[5]=[2,4,5]
base[6]=[2,3,6]
"""
chicken=[ [2],  [2,3]]
while chicken:
     
    j=chicken.pop()
    
    turn=j[-1]
    iop=len(j)
    if iop<chili[turn]:
        chili[turn]=iop
        base[turn]=j
        chicken.sort(reverse=True,key=len)
        #print turn,len(chicken)
    if iop==chili[turn] :
     
     
   
        if turn<200:
            chicken.append(j+[turn+1])

            for each in range(0,iop):
                k=j[each]
                m=k+turn
                if m<=total:
                  chicken.append(j+[m])
                  
             
s=0
for i in range(1,201):
    s+=len(base[i])
print s
   
  
