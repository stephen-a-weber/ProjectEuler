
 
 #################
for B in xrange(1,6):
    yrange=B
   # print
    
    
    for m in xrange(1,yrange+1):
        print (B,m),"::::::::"
        
        x=B
        y=m
        cat=True
         
        while cat:
            k=x*(x-1)/2+y
            print (x,y),
            
           
            y=y+1 
            if y>x-yrange+m:
                y=m
                x=x+1
                print
              
            
            if x>5:
                cat=False
      
            

 
