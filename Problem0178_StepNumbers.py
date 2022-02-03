"""
Step Numbers
Problem 178
Consider the number 45656. 
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.
How many pandigital step numbers less than 1040 are there?

Answer:
126461847755
Completed on Sat, 11 May 2013, 17:42
"""

barrel={}

cell=range(0,10)
storage=[]
count=0
for i in range(1,10):
   v=cell[:]
   v.remove(i)
   g=[i,False,tuple(v)]
   barrel[tuple(g)]=1
   storage.append([i,v,1])#val,pand,digits,count

def pan(n):
    for i in range(0,10):
        if n[i]==0:
            return False
    return True
for digits in range(1,40):
         
        container=[]
        while storage:
            a, d,e=storage.pop()
             
           
             
            if a==0:
                g, m=a,d[:]
                 
                g=1
                                     
                if 1 in m:
                    m.remove(1)
                container.append([g, m,e])
       
            elif a==9:
                g, m=a, d[:]
                                 
                g=8
                if 8 in m:
                    m.remove(8)

                container.append([g, m,e])
       
            else:
                g, m=a, d[:]
                 
                 
                g=g+1
                if g in m:
                    m.remove(g)
                
                container.append([g, m,e])
                
                g,m=a, d[:]
                 
                g=g-1
                if g in m:
                    m.remove(g)
       
                container.append([g,m,e])
    
        barrel={}
        for i in container:
           
            a,d,e=i
            g=tuple([a,tuple(d)])
            if g not in barrel:
                barrel[g]=e
                
   
            else:
                     
                  barrel[g]+=e

        for i in barrel:
            a,c=i
            d=barrel[i]
            storage.append([a,list(c),d])
        for i in barrel:
            a,b=i
            if b==tuple([]):
               count+=barrel[i]
        print digits,count
         
 
print count
            
        
            
        
            
    
    
    
