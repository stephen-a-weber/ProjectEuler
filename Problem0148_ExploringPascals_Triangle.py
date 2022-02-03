import math
total=0
def c(n,k):
    return ((math.factorial(n))/((math.factorial(n-k)*math.factorial(k))))
number=0
x1=0
y1=0
x2=0
m=0
j=0
cat=False
mouse=False
dog=False
x3=0
y3=0
m3=0
b3=0
k3=0
j3=0
carrot=0
count=0
bunny=False
rabbit=False
bean=0
e=[0,0,0,0,0,0,0,0,0,0,0]
for n in xrange(0,10000):
    e[10]+=1
    for i in range(10,0,-1):
        
        if e[i]>=7:
            g=e[i]-7
            e[i]=g
            e[i-1]+=1
    if count!=0: 
       print "          ",count
    else:
        print
    count=0
    print e,n,":",
    for k in xrange(0,n+1):
        number+=1
        #print c(n,k),
        g=c(n,k)
        if g%49==0:
            rabbit==True
            bean+=1
        else:
            if rabbit:
                rabbit==False
                print bean,
                bean=0
            
        if g%7==0:
            count+=1
            bunny=True
            carrot+=1
             
        else :
         
            if bunny:
                bunny=False
                print carrot,
                carrot=0
             
    #predict number
    #
    if n%7==0:
        x1=6*(n/7)
        y1=n/7
        cat=True
    if n%(7**2)==0 and n!=0:
        
        mouse=True
        x2=6*(n/49)
        m=1
        j=x2
    if n%(7**3)==0 and n!=0:
        dog=True
        x3=6*(n/(7**3))
        b3=x3
        m3=1
        j3=x3
        k3+=1
    #
    if cat:
        x1-=y1
    if mouse:
        m+=1
        if m%8==0:
            m=1
            x2=x2-(n/49)
        j=x2*m
    if dog:
        m3+=1
        if m3%8==0:
            k3+=1
            m3=1 
            x3=b3*k3
        j3=x3*m3
        
    total+=count
    
print total,number-total
    
