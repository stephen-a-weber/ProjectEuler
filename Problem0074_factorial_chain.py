import math
import time
rrrt=time.time()
digit={}

def summing(n):
     h=[math.factorial(int(r)) for r in str(n)]
     return sum(h)




def loop(h):
    f=len(h)
    for each in h:
        if each in digit:
            b=h.index(each)
            r=digit[each]
            for i in range(0,b):
                digit[h[i]]=b-i+r
            return digit[h[0]]

    #it is not saved currently
    for i in range(60):
        for j in range(1,60):
             
            if h[i:i+j]==h[i+j:i+2*j]:
                #print h[i:i+j],h[i+j:i+2*j]
                for a in range(i+j):
                    digit[h[a]]=i-a+j
                    #print "putting ",h[a],i-a+j,i,a,j
                return digit[h[0]]


def create(n):

    f=[n]
    x=n
    for i in range(120):
        x=summing(x)
        f.append(x)
        if x in digit:
            break
    return f


mm=0
for i in range(1000000):
   f=create(i)
   g=loop(f)
   if g==60:
       mm+=1



















print
print time.time()-rrrt
