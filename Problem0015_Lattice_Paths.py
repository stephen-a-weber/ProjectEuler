"""
attice paths
Problem 15
Starting in the top left corner of a 22 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 2020 grid?


Answer:
137846528820
Completed on Thu, 24 Jan 2013, 00:36
"""
import heapq  
knot=20 +1

graph={}
  
for x in range(0,knot):
    
    for y in range(0,knot):
       
        graph[(x,y)]=[ 0,[]]# value,neighbors
        m=x-1
        if m>=0:
            graph[(x,y)][1].append((m,y))
        n=y-1
        if n>=0:
            graph[(x,y)][1].append((x,n))
         
         
graph[( 0,0)][0]=1
children={}
 
for x in range(0,knot):
    
    for y in range(0,knot):
       
        children[(x,y)]=[  []]# value,neighbors
        m=x+1
        if m<knot:
            children[(x,y)][0].append((m,y))
        n=y+1
        if n<knot:
            children[(x,y)][0].append((x,n))
         
  
start=True 
heap=set()   
complete=set()

complete.add((0,0))
heap=set()
for i in complete:
        for d in children[i][0]:
            if d not in complete:
                heap.add(d)
 
while heap:
   
  
    while heap:
          
             pick=heap.pop();
             parents=graph[pick][1]
             tell=True             
             for p in parents:
                  
                 if p  not in complete:
                     tell=False
                        
             if tell:
                 
                 v=graph[pick][0]
                 for p in parents:
                     v+=graph[p][0]
                     
                  
                 graph[pick][0]=v
                  
                 complete.add(pick)
                  
             
                
    heap=set()
    for i in complete:
        for d in children[i][0]:
            if d not in complete:
                heap.add(d)
                  
                  
             
        
        
                     
         
print graph[(knot-1,knot-1)][0]       
