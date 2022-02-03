"""
Counting block combinations I
Problem 114
A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square. There are exactly seventeen ways of doing this.

						
				
				
				
				
				
		
			
			
			
			
		
		
		
	
	

 
How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), black (1), and red (4).


Answer:
16475640049
Completed on Mon, 11 Mar 2013, 10:36

"""
d={}
for n in range(1,51):
 
 
    count=0
     
    storage=[0]
    while storage:
         
        begin=storage.pop()
        if begin>(n-3):
            count+=1
            if count%10000000==0:
               print n,count,len(storage)
            
        else:
            f=n-begin
            if f in d:
                count=count+d[f]
            else:
                    storage.append(begin+1)
                    for i in range(3,f+1):
                   
                        
                        storage.append(begin+i+1)
    d[n]=count                
 
print count
