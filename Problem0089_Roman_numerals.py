#roman numerl

f=open("/Users/isadmin/Documents/pythonCode/roman.txt")
d=f.readlines() 

frog={}
frog["I"]=1
frog["V"]=5
frog["X"]=10
frog["L"]=50
frog["C"]=100
frog["D"]=500
frog["M"]=1000
toad={}
toad[1]="I"
toad[5]="V"
toad[10]="X"
toad[50]="L"
toad[100]="C"
toad[500]="D"
toad[1000]="M"


def  digitize(n):
    f=[]
    a= [r for r in n]
   
    for i in range(len(a)):
   
        f.append(frog[a[i]])
    return f
def romanize(n):
    g=""
    for i in n:
        g+=toad[i]
    return g

def totalize(n):
    Game=[]
   
    count=0
    index=0
    item=n[index]
    newitem=False
    while index<len(n):
        if   newitem:
            newitem=False
            count=0
            item=n[index]
        else:
            count+=1
            #print item,index,count
            if index+count>=len(n):
                Game.append(item*(count))
                break
            elif n[index+count]>item:
                Game.append(n[index+count]-item*(count))
                index=index+count+1
                newitem=True
            elif n[index+count]<item:
                Game.append(item*(count))
                index=index+count 
                newitem=True          
    return Game

def makeRoman(x):
    n=int(x)
    roman=""
    M=n/1000
    for i in range(M):
        roman+="M"
    n=n-1000*M
    if n>=900:
        roman+="CM"
        n=n-900
    if n>=500:
        roman+="D"
        n=n-500
    if n>=400:
        roman+="CD"
        n=n-400
    C=n/100
    for i in range(C):
        roman+="C"
    n=n-100*C
    if n>=90:
        roman+="XC"
        n=n-90
    if n>=50:
        roman+="L"
        n=n-50
    if n>=40:
        roman+="XL"
        n=n-40
    X=n/10
    for i in range(X):
        roman+="X"
    n=n-X*10
    if n>=9:
        roman+="IX"
        n=n-9
    if n>=5:
        roman+="V"
        n=n-5
    if n>=4:
        roman+="IV"
        n=n-4
    for i in range(n):
        roman+="I"
        
    return roman

    
                
            
golf=[]
disney=[]



 
 
total=0      
for i in range(1000):
  
    
   ee=d[i].replace("\n","")
    
   p=digitize(ee)
   
   ff= totalize(p)
   ff=sum(ff)
   s=makeRoman(ff)
  
  
   if len(d[i])-1>len(s):
       golf.append(i)
       #print d[i] ,len(d[i])-1
       #print s,len(s)
       
       #print":::::::::::::::::::::"
       total+= (len(ee)-len(s))
print total
print



 
love=[t for t in d]
apple=0
for i in d:
    apple+=len(i)
 
cherry=0
 
for a in range(1000):
    i=d[a]
    flower=len(i)
    i=i.replace("VIIII","IX")
    i=i.replace("IIII","IV")
    i=i.replace("LXXXX","XC") 
    i=i.replace("XXXX","XL")
    i=i.replace("DCCCC","CM") 
    i=i.replace("CCCC","CD")
 
    doll=len(i)
  
    if flower!=doll:
       disney.append(a)
       cherry+=(flower-doll)
       #print i,flower,doll
print cherry

 
    
            
