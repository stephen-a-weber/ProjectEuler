tree={}
for r in range (0,10):
    tree[r]={}
    for t in range (0,10):
        tree[r][t]=[]
for t in range (0,10):
   
    for s in range(0,10):
            d= (t*s)%10
     
            tree[d][t].append(s)
print tree

def r(m):
    n=m
    nn=0
    mm=0
    a=0
    possibles=set()
    length=1
    value=1
    storage=[0]
    while n!=0:
        g=[r for r in storage]
        storage=[]
        a=a*length
        
        for yy in g:
            a=n%10
            b=yy%(10**length)
            if b<=2:
                nn=b
                mm=0
            else:
                nn=12-b
                mm=10-b
            for u in range(nn,mm):
                
             for i in tree[u][b]:
              storage.append(yy+i*n)
            n=n%10
        length+=1




    return min(possibles)
