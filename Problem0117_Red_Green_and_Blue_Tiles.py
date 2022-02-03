
"""
Red, green, and blue tiles
Problem 117
Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.

				
			
			
			
			
		
		
		
		
		
		
	
	
	
	
 
How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to problem 116.


Answer:
100808458960497
Completed on Tue, 12 Mar 2013, 05:02

"""
 
d={}
for n in  range(1,51):
    

  
    count=0
   
    storage=[0]
    while storage:
         
        index=storage.pop()
        
        if index>(n-1):
            count+=1
            
  
          
            
        else:
            f=n-index
            if f in d:
                count=count+d[f]
                
           
            else:
                    storage.append( index+1)
                    
                    for i in range(2,5):
                         if f >=i:
  
      
                            storage.append(index+i)                           
                    
    d[n]=count
print count    
    
    
 
 
 
