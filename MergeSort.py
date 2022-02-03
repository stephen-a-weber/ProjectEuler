

def sort_this(n):
    m=len(n)
    if m==1 or m==0:
        return n

    h=m/2
    a=sort_this(n[:h])
   
    b=sort_this(n[h:])
    
    ai=0
    bi=0
    c=[]
    for i in range(m):
        
        if a[ai]>b[bi]:
            c.append(a[ai])
            ai+=1
            if ai==len(a):
                
                for x in range(bi,len(b)):
                    c.append(b[x])
                return c
        else:
            c.append(b[bi])
            bi+=1
        
 
            if bi==len(b):
                     
                    for x in range(ai,len(a)):
                         c.append(a[x])
                    return c
    return c
            
    


f=[1,4,2,3,5]
