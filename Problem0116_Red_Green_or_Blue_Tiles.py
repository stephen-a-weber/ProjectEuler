"""Red, green or blue tiles
Problem 116
A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

			
			
			
			
		
		
		
 
If green tiles are chosen there are three ways.

		
		
		
 
And if blue tiles are chosen there are two ways.

	
	
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

NOTE: This is related to problem 117.


Answer:
20492570929
Completed on Tue, 12 Mar 2013, 04:19

"""

totalcount=0
for m in range(2,5): 
    d={}
    for n in range(1,51):
     
     
        count=0
         
        storage=[0]
        while storage:
             
            begin=storage.pop()
            if begin>(n-m):
                count+=1
                if count%10000000==0:
                   print n,count,len(storage)
                
            else:
                f=n-begin
                if f in d:
                    count=count+d[f]
                else:
                        storage.append(begin+1)
                        
                            
                        storage.append(begin+m)
        d[n]=count
        
    totalcount+=count-1
     
print totalcount

 
