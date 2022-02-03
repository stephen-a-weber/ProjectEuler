"""
Numbers for which no three consecutive digits have a sum greater than a given value.
Problem 164
How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?


Answer:
378158756814587
Completed on Tue, 19 Mar 2013, 07:40

"""

digits=2
num=20
total=0
storage=[]
den=[]
grate={}
for i in range(0,10):
    for j in range(0,10):
      if i+j<10:
        g=tuple([i,j])
        #print g
         
        storage.append(tuple([g,1]))

      
while digits< num:
  
    den=[]
    grate={}
    
    if digits<num-1:
        for a,b in storage:
            g=sum(a)
             
            x=10-g
            for y in range(x):
                
                g=tuple([y,a[0]])
                
                if g in grate:
                    grate[g]+=b
                else:
                    grate[g]=b

        for y in grate:
            den.append(tuple([y,grate[y]]))
        storage=den
        
    else:
        for a,b in storage:
            g=sum(a)
        
            x=10-g
            for y in range(1,x):
                g=tuple([y,a[0]])
                
                if g in grate:
                    grate[g]+=b
                else:
                    grate[g]=b
        s=0
        for y in grate:
             den.append(tuple([y,grate[y]]))
             s+=grate[y]
        storage=den
        print s
  
    digits+=1


            
                
 
    
    
