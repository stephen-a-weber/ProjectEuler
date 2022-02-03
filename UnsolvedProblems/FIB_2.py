import time
ras=time.time()
def pandigital(n):
    f=set(range(1,10))
    g=[int(r) for r in n]
    if f.difference(g)==0:
        return True
    return False
k=3
a=[1]*3
s=2
cat=True
FIB0=""
FIB1=""
while cat:
    b=(s-2)%3
    e=(s-1)%3
    
    a[s]=a[b]+a[e]
     
    Fib=str(a[s])
    
     
    if k==107:
        FIB0=Fib
    if k==108:
        FIB1=Fib
        cat =False
        break
         
    s+=1
    s=s%3
    k=k+1    
frog=True
greatBegin=Fib[:11]
greatEnd=Fib[-11:]
gB=[1]*3
gE=[1]*3
gB[0]=int( FIB0[:11])
gB[1]=int( FIB1[:11])
gE[0]=int(FIB0[-11:])
gE[1]=int(FIB1[-11:])
#print gB[0],gB[1],gE[0],gE[1]
#print greatBegin, greatEnd
     
while frog:
        b=(s-2)%3
        e=(s-1)%3
        gB[s]=gB[b]+gB[e]
        gE[s]=gE[b]+gE[e]
        k=k+1
 

        
        GBbegin=int(str(gB[s])[:9])
        
        
         
        GEend=int(str(gE[s])[-9:])
        
        if k%20000==0:
              
                print k,GBbegin,GEend
                print time.time()-ras
                print "___"
               
        if pandigital(str(GBbegin)) and pandigital(str(GEend)):
                print "SOLUTION:___________________________________________________"
                print "************************************************************"
                
                print k
        
        s+=1
        s=s%3
             
           
        
print  time.time() -ras
