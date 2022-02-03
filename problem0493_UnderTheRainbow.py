"""
Under The Rainbow
Problem 493
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
Urn=[]
U=range(1,8)
for _ in range(10):
    Urn+=U
import time
r=time.time()


#print len(Urn),Urn
"""



===

[7,10]

ex=1


==after one chosen must be

[6,10][1,9]                     1 color
                            





==after two chosen either

 [5,10][1,9][1,9]                2 colors
 [6,10][1,8]                    1  color

                               2/2  +1/2  =1.5


to three 
[6,10][1,7]                     
[5,10][1,9][1,8]

[4,10][1,9][1,9][1,9]
[5,10][1,8][1,9]
[5,10][1,9][1,8]


==after three chosen either
all same color
[6,10][1,7]           1 vweaion       1 color        
two one color 
[5,10][1,9][1,8]      3 versions     2 colors       
three different colors
[4,10][1,9][1,9][1,9] 1 version      3 colors       




We are looking at each count for any tuple in this list of tuples that
has at least one out of the Urn or if there isn't a ten in the mix.







class slist(list):
    @property
    def length(self):
        return len(self)
"""
import copy
count=1

Ex=0

altprison=dict()
altprison[((6,10),(1,9))]=[1,1]#dictionary of expectation value and color

prison=copy.deepcopy(altprison)
total=0
while count<21:
    numLeft=(70-count)*1.0
    rr=time.time()-r
    #print "finished in ", rr
    
    prison=copy.deepcopy(altprison)
     
    
    total=0
  
    
    for a in prison:
        dd=altprison[a]
        #print dd[0]*dd[1]
        total+=(dd[0]*dd[1]*1.0)
        #print a," ::: ",dd
    #print
    print "solution count ",count, "---",total
     
    altprison=dict()
    expect=0
     
    Ex=0
    while   len(prison)>0:
        can,answer=prison.popitem()
        #print"hi ",len(prison)
        #print can,"  ....  ",answer
        jails=copy.deepcopy(can)
        storage=list(can)
        garden=answer[0]
        #print "storage = ",storage
        #print "last ex ",garden
        # what is needed here or what is being coded here
        # is the expectation of a particular outcome
        # multiplied by that particular outcome's number of colors
         
        
             #expectation value for count
        while len(storage)>0:
            ja=copy.deepcopy(jails)
            jail=[]
            for i in ja:
                jail.append(i)
            
            choice=storage.pop()
     
            jail.remove(choice)
         
            a=choice[0]
            b=choice[1]
             
            
            grouped=a*b*1.0/numLeft*garden
             
         
            
            if b>0:
                c=b-1
                if a==1:
                    jail.append((1,c))
     
                    
                else:
                    jail.append((1,c))
                     
                    jail.append((a-1,b))
                colors=0
                Ex=0
                for q,w in jail:
                   
                    if w<>10:
                        colors+=1                   
                #print count," ... ",jail,
                jail.sort()
                frog=tuple(jail)
                if frog in altprison:
                    altprison[frog][0]+=grouped
                else:
                    altprison[frog]=[grouped,colors]
                #print altprison[frog][0]
            
        
            
    
    #print "Expectation for count ",count," is ",Ex
    count+=1
 
    
rr=time.time()-r
print "finished in ", rr       

  



  




