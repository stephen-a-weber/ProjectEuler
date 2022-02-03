import math


def continuedFractionSqrt(N,a,b):#   (SQRT+a)/b ===> Integer + 1/X
    Integer= int((math.sqrt(N)+a)/b)
    #print Integer
                          # where X is next of form (SQRT+a2)/b2
    c= a - b*Integer
    #print "c",c
    a2 = -c 
    #print a2
                             # (SQRT+c)/b ===> 1/X
    b2 = (N-c**2)/b
    #print b2
    
    return a2,b2,Integer
     

def buildcontinuedFraction(N):

    if math.sqrt(N)!=int(math.sqrt(N)):
        sequence=[]
        a=0 #simple sqrts
        b=1
        for i in range(1,1000):
            
            a,b,integer=continuedFractionSqrt(N,a,b)
             
            sequence.append(integer)        
        return sequence
 
    
def depthOfContinuedFraction(seq,depth):
    theseq=seq 
    theseq=theseq[:depth]
    theseq.reverse()
    d=theseq[0]
    n=1
    #print n,"/",d
    for i in range(1,depth):
         
        a=d
        d=theseq[i]*d+n
        n=a
        #print n,"/",d
    c=n
    n=d
    d=c
    return  (n*10**180)/d
 
def find100digits(n):
     
        if math.sqrt(n)!=int(math.sqrt(n)):
            seq=buildcontinuedFraction(n)
            m=20
            a=depthOfContinuedFraction(seq,m)
            b=0
            cat=True
            while cat:
                m+=1
                b=depthOfContinuedFraction(seq,m)
                if a!=b:
                    a=b
                else:
                    cat=False
                    return a

 

def main():
    total=0
    count=0
    for n in range(2,1000):
        count+=1
        #print n,
        if count==100:
            break
        if math.sqrt(n)==int(math.sqrt(n)):
            continue
        print n,"    ",math.sqrt(n)
        a=find100digits(n)
        a=str(a)
        a=a[:100]
        print a
        print
        dog=0
        for i in range(len(a)):
            dog+=int(a[i])
         
        print "total = ",dog,"this is the ",count," one in the list"
        total+=dog
         
    print "THE ANSWER IS ",total


main()
