"""
250250
Problem 250
Find the number of non-empty subsets of {11, 22, 33,..., 250250250250}, the sum of whose elements is divisible by 250. Enter the rightmost 16 digits as your answer.


Answer:
1425480602091519
Completed on Tue, 25 Jun 2013, 12:35
"""



freq=[0]*250
for i in range(1,250251):
    freq[pow(i,i,250)]+=1

t=[0]*250
t[0]=1
tx=[]
for i in range(250):
  
    for j in range(freq[i]):
        tx=[0]*250
        for k in range(250):
            
            tx[k]= (t[k]+t[k-i])%10**16
        t=tx
 
        
