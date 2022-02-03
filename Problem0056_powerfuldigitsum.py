total=0
number=0
for a in range(0,100):
    for b in range(0,100):
        c= str(a**b)
        f=[int(r) for r in c]
        d=sum(f)
        if d>total:
            total=d
            number=c
print total
        
        
