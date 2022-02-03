"""Flea Circus
Problem 213
A 3030 grid of squares contains 900 fleas, initially one flea per square.
When a bell is rung, each flea jumps to an adjacent square at random (usually 4 possibilities, except for fleas on the edge of the grid or at the corners).

What is the expected number of unoccupied squares after 50 rings of the bell? Give your answer rounded to six decimal places.


Answer:
330.721154
Completed on Mon, 25 Mar 2013, 20:09

"""


storage=[dict() for r in range( 51)]
answer={}
for i in range(0,30):
    for j in range(0,30):
     
        answer[(i,j)]=1




 

def move(p):
        container=[] 
        x,y=p      
        
        g=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for xx,yy in g:        
                
                   
                   
            if xx<0 or yy<0 or xx>29 or yy>29:
                        continue
                    
            else :
                        container.append((xx,yy))
        return container

#print move((0,0))
#print move((29,0))
#print move((0,29))
#print move((29,29))
#print move((0,29))
for ii in range(0,30):
    for jj in range(0,30):
        storage=[dict() for r in range( 51)]

        for i in range(0,30):
            for j in range(0,30):
                storage[0][(i,j)]=0

        storage[0][(ii,jj)]=1
 
        day=0
        while True:
            #print day
            if day==50:
                break

            for i in storage[day]:
                x,y=i
                container=move(i)
                h=len(container)
                for each in container:
                    xx,yy=each
                    if each in storage[day+1]:
                        storage[day+1][each]+=storage[day][i]*1.0/h
                    else:
                        storage[day+1][each]=storage[day][i]*1.0/h
            day+=1

        for i in storage[50]:
            g=1-storage[50][i]
            answer[i]*=g
            

s=0
for i in answer:
    s+=answer[i]
print s
            
