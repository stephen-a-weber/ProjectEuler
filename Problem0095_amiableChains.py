import time
ras=time.time()
n=1000000
divisors={}

 
import math
for i in range(n):
  
    divisors[i]=[1]
for i in xrange(2,n,2):

       divisors[i].append(2)
    
for i in xrange(3,n):
  
   
      
        for j in xrange(i,n,i):
            divisors[j].append(i)


for i in range(n):
    f=sum(divisors[i])-i
    divisors[i]=f



pascal=[] 
maxcount=0
maxindex=0

for i in range(2,n):
    #print "INITIAL DIVISORS",divisors[i]
    s=[i]
    #print s[0]
    
    j=divisors[s[0]]
        #print "THIS IS NEXT ",j
    s.append(j)
    
    hare=1
    turtle=0
     
    count=1
    cat=True
    #if i ==12496:
       # print "YES  !!!"
    #print "DDD",s[hare],s[turtle]
    while s[hare]!=s[turtle]:
        #print s
        #print "Turtle,Hare  ",s[turtle],s[hare],count
        if cat:
            cat=False
        else:
            turtle+=1
            hare+=2
            #print s[-1]
            if s[-1]<n and s[-1]!=1:
               
               k=divisors[s[-1]]
               if k==1 or k>n:
                   count=0
                   break
               #print k
               s.append(k)
            else:
                count=0
                break
                #print "OOOOOOOOOOOOOOOOOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPSSSSSSSSSSSSSSSSSSSSSSSSSSS"
            #print s[-1]
            if s[-1]<n :
            
      
               k=divisors[s[-1]]
               if k==1 or k>n:
                   count=0
                   break
               #print k
               s.append(k)
            else:
                count=0
                break
                #print "OOOOOOOOOOOOOOOOOOOOOOOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPSSSSSSSSSSSSSSSSS"
            count+=1
    
     
    #print "OK THIS ONE THIS ONE THIS ONE IS ON THE WAY TO A CHAIN YEAH!!!"
    
    length=len(s)
    dog=False
    for gg in range(count):
        if s[length-gg-1]==s[0]:
            dog=True
    if dog:
     
        #print "the count is ",count
        #print "HERE IS ", s[turtle]
        #print "and     ", s[0]
     
        
        if maxcount<count:
            maxcount=count
            maxindex=i
            pascal=s
            #print "HEREEEEEEEE",maxcount,i
pascal.sort()
print pascal[0]
            
   
        
             
            



 

print time.time()-ras
