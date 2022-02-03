"""
Hilbert's New Hotel
Problem 359
An infinite number of people (numbered 1, 2, 3, etc.) are lined up to get a room at Hilbert's newest infinite hotel. The hotel contains an infinite number of floors (numbered 1, 2, 3, etc.), and each floor contains an infinite number of rooms (numbered 1, 2, 3, etc.).

Initially the hotel is empty. Hilbert declares a rule on how the nth person is assigned a room: person n gets the first vacant room in the lowest numbered floor satisfying either of the following:

the floor is empty
the floor is not empty, and if the latest person taking a room in that floor is person m, then m + n is a perfect square
Person 1 gets room 1 in floor 1 since floor 1 is empty. 
Person 2 does not get room 2 in floor 1 since 1 + 2 = 3 is not a perfect square. 
Person 2 instead gets room 1 in floor 2 since floor 2 is empty. 
Person 3 gets room 2 in floor 1 since 1 + 3 = 4 is a perfect square.

Eventually, every person in the line gets a room in the hotel.

Define P(f, r) to be n if person n occupies room r in floor f, and 0 if no person occupies the room. Here are a few examples: 
P(1, 1) = 1 
P(1, 2) = 3 
P(2, 1) = 2 
P(10, 20) = 440 
P(25, 75) = 4863 
P(99, 100) = 19454

Find the sum of all P(f, r) for all positive f and r such that f × r = 71328803586048 and give the last 8 digits as your answer.


Answer:
40632119
Completed on Sat, 18 Jun 2016, 07:28


 10=>>>2 ,5 which leads 
 11=> prime so we need 11! to get the number 11 to divide into
 let prime be N
 then we can have N(N-1) before we get to 11**2 (121) 11,22,33,44

12 

 
"""
import math
import time
import copy
r=time.time()
n=8445#75 second to get 10**8
squares=[i*i for i in range(1,8445639)]

factors=[{} for x in range(n+1)]                    
sieve=[True]* n
primes=[2]


for i in range(4,n,2):
   
    sieve[i]=False
for i in range(3,n,2):
    if sieve[i]==True:
        primes.append(i)        
        for j in range(i*i,n,i):
            sieve[j]=False
"""5 
floor=1
n=1
N=[1]
k=1
while k<len(squares):
    B=squares[k]-n
    if B>n:
        N.append(B)
        n=B
    else:
        N.append(0)
    k+=1

"""
 
hotel={}
latest=0
for n in range(1,100):
    floor=1
    cat=True
    while cat:
        if floor not in hotel:
            hotel[floor]=[n]
            cat=False
        else:
            latest=hotel[floor][-1]
            k=latest+n
            if int(k**.5)==k**.5:
                hotel[floor].append(n)
                cat=False
            else:
                floor+=1
        
for i in hotel:
    
        print(i,hotel[i])


def checking(p):
    total=0
    nn=int(math.log(n,p))
    holda=[p]
    holdb=[n//p]
    for y in range(2,nn+1):
        P=p**y
        holda.append(P)
    garden=[0]*(n+1)
    pointer=1
    value=2
     
        
        
        
def facting():
    choices={}
    whatisn=[]
    m=2
    choices[2]=i
    while m<n+1:
        m+=1
        d=factor(m)
        for i in d:
            if i not in choices:
                choices[i]=i
            else:
                choices[i]*=i
        

def hilbert(F,R):
    if F//2==F/2:
        #even floor
        return (F*int(F/2)+ R*(R-1)//2 + int(R/2)*2*F)
    else:
        if F==1:
            return (R*(R+1)//2)
        else:
            return (F+1)*int(F/2)+ int((R-1)/2)*(F-1)*2+ R*(R-1)//2
        
    
#answer=7631697331548232565040632119
    
#last eight digits =40632119
#facts=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
                
nn=71328803586048
possibles=[]
for i in range(28):
    for j in range(13):
        p=(2**i)*(3**j)
        r=nn//p
        if p*r!=nn:
            print("stop")
        possibles.append((p,r))
        possibles.append((r,p))

p=list(set(possibles))

total=0
for F,R in p:
    total+=hilbert(F,R)
print(total)
    
        
    
        
"""
floor room 1

1..0x+1
2..1x
3..1x+1
4..2x
5..2x+2
6..3x
7..3x+3
8..4x
9..4x+4
10.5x
11.5x+x
12.6x
hotel[100][0]=5000 TRUE!!!


1+2 3 4 5 6
R(R+1)/2=


odd floors
room 1  = (F+1  )*int(F/2)    
room 2 += 1
room 3 += 2*(F-1)+2
room 4 += 3
room 5 += 2*(F-1)+4
room 6 += 5
room 7 += 2*(F-1)+6
room 8 += 7
room 9 += 2*(F-1)+8

room R==(F+1)*int(F/2)+ int(R/2)*(F-1)*2+ R*(R-1)/2

eg F11 R13
12*5  + 6*20 +13*6
60+120+78
180+78
258 TRUE!


even floors
room 1  = (F)*(F//2)
room 2 += (2*F+1)
room 3 += 2
room 4 += (2*F+3)
room 5 += 4
room 6 += (2*F+5)
room 7 += 6

room R == F*int(F/2)+ R*(R-1)/2 + int(R/2)*2*F

eg F10 R13
121/2=50 13*6=78 12*10=120
  50  +78+132=
  78
 120
 ---
 248

[4900, 4901, 5099, 5102, 5302, 5307, 5509, 5516, 5720,
5729, 5935, 5946, 6154, 6167, 6377, 6392, 6604, 6621,
6835, 6854, 7070, 7091, 7309, 7332, 7552, 7577, 7799,
7826, 8050, 8079, 8305, 8336, 8564, 8597, 8827, 8862,
9094, 9131, 9365, 9404, 9640, 9681, 9919, 9962, 10202,
10247, 10489, 10536, 10780, 10829, 11075, 11126, 11374,
11427, 11677, 11732, 11984, 12041, 12295, 12354, 12610,
12671, 12929, 12992, 13252, 13317, 13579, 13646, 13910,
13979, 14245, 14316, 14584, 14657, 14927, 15002, 15274,
15351, 15625, 15704, 15980, 16061, 16339, 16422, 16702,
16787, 17069, 17156, 17440, 17529, 17815, 17906, 18194,
18287, 18577, 18672, 18964, 19061, 19355, 19454]

room R==(F+1)*int(F/2)+ int((R-1)/2)*(F-1)*2+ R*(R-1)//2
      == 4900         + R//2 * 196

4900 4901 5099 5102 5302 5307 5509 5516 5720
5729 5935 5946 6154 6167 6377 6392 6604 6621
6835 6854 7070 7091 7309 7332 7552 7577 7799
7826 8050 8079 8305 8336 8564 8597 8827 8862
9094 9131 9365 9404 9640 9681 9919 9962 10202
10247 10489 10536 10780 10829 11075 11126 11374
11427 11677 11732 11984 12041 12295 12354 12610
12671 12929 12992 13252 13317 13579 13646 13910
13979 14245 14316 14584 14657 14927 15002 15274
15351 15625 15704 15980 16061 16339 16422 16702
16787 17069 17156 17440 17529 17815 17906 18194
18287 18577 18672 18964 19061 19355 19454






4900 5097 5099 5298 5302 5503 5509 5712 5720
5925 5935 6142 6154 6363 6377 6588 6604 6817
6835 7050 7070 7287 7309 7528 7552 7773 7799
8022 8050 8275 8305 8532 8564 8793 8827 9058
9094 9327 9365 9600 9640 9877 9919 10158 10202
10443 10489 10732 10780 11025 11075 11322 11374
11623 11677 11928 11984 12237 12295 12550 12610
12867 12929 13188 13252 13513 13579 13842 13910
14175 14245 14512 14584 14853 14927 15198 15274
15547 15625 15900 15980 16257 16339 16618 16702
16983 17069 17352 17440 17725 17815 18102 18194
18483 18577 18868 18964 19257 19355 19650





hotelFloor 34
real
[578, 647, 649, 720, 724, 797, 803, 878, 886, 963, 973, 1052, 1064, 1145, 1159, 1242, 1258, 1343, 1361, 1448, 1468, 1557, 1579, 1670, 1694, 1787, 1813, 1908, 1936]

calculated
[578, 647, 649, 720, 724, 797, 803, 878, 886, 963, 973, 1052, 1064, 1145, 1159, 1242, 1258, 1343, 1361, 1448, 1468, 1557, 1579, 1670, 1694, 1787, 1813, 1908, 1936]
"""





def factor(x):
    d=[]
    for i in primes:
        while x%i==0:
            d.append(i)
            x/=i
        if x==1:
            return d
    d.append(x)
    return d

 
