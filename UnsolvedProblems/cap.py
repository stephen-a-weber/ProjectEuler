import copy
cap={}
cap=set([60])
storage=[60]

n=2

for loop in range(1,n):
    d=list(cap)
    d.append(60)
    cat=True
    ff=len(cap)
    while ff==len(cap):
        ff=len(cap)
        for a in d:
            for b in d:
                c=a+b
                cap.add(c)
                e=1.0/(1.0/a+1.0/b)
                cap.add(e)
        
            
print len(cap)
