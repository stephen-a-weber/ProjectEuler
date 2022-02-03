"""
Paper sheets of standard sizes: an expected-value problem.
Problem 151
A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special colour-proofing paper of size A5.

Every Monday morning, the foreman opens a new envelope, containing a large sheet of the special paper with size A1.

He proceeds to cut it in half, thus getting two sheets of size A2. Then he cuts one of them in half to get two sheets of size A3 and so on until he obtains the A5-size sheet needed for the first batch of the week.

All the unused sheets are placed back in the envelope.


At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random. If it is of size A5, he uses it. If it is larger, he repeats the 'cut-in-half' procedure until he has what he needs and any remaining sheets are always placed back in the envelope.

Excluding the first and last batch of the week, find the expected number of times (during each week) that the foreman finds a single sheet of paper in the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx .


Answer:
0.464399
Completed on Sun, 24 Mar 2013, 17:37

"""


storage=[dict() for r in range(30)]
storage[0][(1,1,1,1)]=1

result=0

for day in range(0,28):
    print day
    for paper in storage[day]:
        total=sum(paper)
        p=list(paper)
        print paper,storage[day][paper]
        if total==1 and p[3]==0:
            result+=storage[day][paper]
  
        if total!=0:
             
          
              
            newpaper=p[:]
             
                
            if newpaper[0]:
                newpaper[0]-=1
                newpaper[1]+=1
                newpaper[1]+=1
                newpaper[2]+=1
                newP=tuple(newpaper)
                if newP in storage[day+1]:
                    storage[day+1][newP]+=p[0]*storage[day][paper]*1.0/total
                else:
                    storage[day+1][newP]=p[0]*storage[day][paper]*1.0/total            
            newpaper=p[:]
            if newpaper[1]:
                newpaper[1]-=1
                newpaper[2]+=1
                newpaper[3]+=1
                newP=tuple(newpaper)
                if newP in storage[day+1]:
                    storage[day+1][newP]+=p[1]*storage[day][paper]*1.0/total
                else:
                    storage[day+1][newP]=p[1]*storage[day][paper]*1.0/total            
            newpaper=p[:]
            if newpaper[2]:
                newpaper[2]-=1
                newpaper[3]+=1
                newP=tuple(newpaper)
                if newP in storage[day+1]:
                    storage[day+1][newP]+=p[2]*storage[day][paper]*1.0/total
                else:
                    storage[day+1][newP]=p[2]*storage[day][paper]*1.0/total
            newpaper=p[:]
            if newpaper[3]:
                newpaper[3]-=1
                newP=tuple(newpaper)
                if newP in storage[day+1]:
                    storage[day+1][newP]+=p[3]*storage[day][paper]*1.0/total
                else:
                    storage[day+1][newP]=p[3]*storage[day][paper]*1.0/total
     
print result
            

        
           



