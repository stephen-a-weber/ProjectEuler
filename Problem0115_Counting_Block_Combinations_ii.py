"""
Counting block combinations II
Problem 115
NOTE: This is a more difficult version of problem 114.

A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first exceeds one million.


Answer:
168
Completed on Tue, 12 Mar 2013, 04:00

"""
d={}
m=50
for n in range(50,6651):
 
 
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
                    for i in range(m,f+1):
                   
                        
                        storage.append(begin+i+1)
    d[n]=count
    if count>1000000:
        print n,m,count
        break
 
print count
