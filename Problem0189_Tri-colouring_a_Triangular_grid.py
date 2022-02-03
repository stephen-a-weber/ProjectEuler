"""
Tri-colouring a triangular grid
Problem 189
Consider the following configuration of 64 triangles:


We wish to colour the interior of each triangle with one of three colours: red, green or blue, so that no two neighbouring triangles have the same colour. Such a colouring shall be called valid. Here, two triangles are said to be neighbouring if they share an edge.
Note: if they only share a vertex, then they are not neighbours.

For example, here is a valid colouring of the above grid:


A colouring C' which is obtained from a colouring C by rotation or reflection is considered distinct from C unless the two are identical.

How many distinct valid colourings are there for the above configuration?


Answer:
10834893628237824
Completed on Tue, 9 Apr 2013, 19:14

"""


color=[1,2,3]
import itertools 
 
tri={}
row={}
for i in range(1,9):
    tri[i]={}
    row[i]=[]
tri[1][(1)]=1  #example
tri[1][(2)]=1
tri[1][(3)]=1
row[1]=[[[1],1],[[2],1],[[3],1]]
for n in range(2,9): #[2,8]
    #PART ONE     
     
    green=[]
  
    for possible,num in row[n-1]:
            d=[]
            for c in range(len(possible)):                
                col=possible[c]
                possibleColors=[r for r in color if r!=col]                           
                d.append(possibleColors)
            for i in itertools.product(*d):
                green.append([i,num])
 
     
    babycache={}
    for i,j in green:
        if i not in babycache:
            babycache[i]=j
        else:
            babycache[i]+=j
    cache=[]
    
    for i in babycache:
        cache.append(tuple([i,babycache[i]]))

    #print cache
    #PART TWO
    # 
    green=[]
    while cache:
        t,num=cache.pop()
            
        d=[]
        #firstTriangle
        possibleColors=[r for r in color if r!=t[0]]
        d.append(possibleColors)
        #middleTriangles
        for middle in range(1,len(t)):
            possibleColors=[r for r in color if r!=t[middle-1] and r!=t[middle]]           
            d.append(possibleColors)
        #lastTriangle
        possibleColors=[r for r in color if r!=t[-1]]
        d.append(possibleColors)
        for i in itertools.product(*d):
                green.append([i,num])
 
    
     
         
  
    for i,j in green:
       
        if i not in tri[n]:
            tri[n][i]=j
        else:
            tri[n][i]+=j
    row[n]=[]
    total=0
    for i in tri[n]:
        row[n].append(tuple([i,tri[n][i]]))
        total+=tri[n][i]
    print"The total for row ",n," is ",total
    #print row[n]
    
                                   
        
            





                
