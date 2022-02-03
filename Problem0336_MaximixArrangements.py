"""
Maximix Arrangements
Problem 336
A train is used to transport four carriages in the order: ABCD. However, sometimes when the train arrives to collect the carriages they are not in the correct order. 
To rearrange the carriages they are all shunted on to a large rotating turntable. After the carriages are uncoupled at a specific point the train moves off the turntable pulling the carriages still attached with it. The remaining carriages are rotated 180 degrees. All of the carriages are then rejoined and this process is repeated as often as necessary in order to obtain the least number of uses of the turntable.
Some arrangements, such as ADCB, can be solved easily: the carriages are separated between A and D, and after DCB are rotated the correct order has been achieved.

However, Simple Simon, the train driver, is not known for his efficiency, so he always solves the problem by initially getting carriage A in the correct place, then carriage B, and so on.

Using four carriages, the worst possible arrangements for Simon, which we shall call maximix arrangements, are DACB and DBAC; each requiring him five rotations (although, using the most efficient approach, they could be solved using just three rotations). The process he uses for DACB is shown below.

p336_maximix.gif
It can be verified that there are 24 maximix arrangements for six carriages, of which the tenth lexicographic maximix arrangement is DFAECB.

Find the 2011th lexicographic maximix arrangement for eleven carriages.


Answer:
CAGBIHEFJDK
Completed on Fri, 17 Jun 2016, 08:15
"""


n=11
storage={}
for i in range(0,n-1):
    storage[i]=[]
a=["A","B","C","D","E","F","G","H","I","J","K"]#[r for r in range(1,n+1)]
storage[i-1]=[a[:i-1]+[a[-2],a[-3],a[-1]]]
#starting at bottom three
hold=[]
end=[]
print(a)
i-=1
while i>0:
 #   print (i,"==",len(storage[i]))
    hold=[]
    while storage[i]:
        item=storage[i].pop()
  #      print(item)
        saved=item[:i-1]
 #       print(saved)
        ending=item[i-1:]
 #       print(ending)
        ending.reverse()
 #       print(ending)
      
        k=n-i
        for y in range(1,k):
            gend=ending[y :]
            gend.reverse()
            g=ending[0:y]+gend
            storage[i-1].append(saved+g)
           # print(saved,ending[0:y+1],gend)
 #           print(saved+g,".........")
 #       print("________")
    i-=1
    
ground=[i for i in storage[0]]
ground.sort()
print ("".join(ground[2010]))
    



#'CAGBIHEFJDK'
     
    



"""

ABCDEF
ABCEDF
ABFDEC

-ABFCED-ADECFB-
ADBFCE-ECFBDA-
EADBFC
ECADBF
ECFADB
ECFBAD

A 
 
BAC
BCA
ACB
ABC

 
ABCD
-->
ACBD
DBCA

--DBAC
--DACB





ABCDEF
.ABCEDF
..ABFDEC

-ABFCED-ADECFB-
ADBFCE-ECFBDA-
EADBFC
ECADBF
ECFADB
ECFBAD


ADEBFC-CFBEDA-
CADEBF
CFADEB
CFBADE
CFBEAD


ADECBF-FBCEDA-
FADECB
FBADEC
FBCADE
FBCEAD



-ABFDCE-AECDFB-

AEBFDC-CDFBEA-
CAEBFD
CDAEBF
CDFAEB
CDFBAE


AECBFD-DFBCEA-
DAECBF
DFAECB
DFBAEC
DFBCAE


AECDBF-FBDCEA-
FAECDB
FBAECD
FBDAEC
FBDCAE

"""
