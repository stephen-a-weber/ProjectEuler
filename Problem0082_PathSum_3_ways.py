f=open("C:\Users\sweber\Desktop\matrix.txt")
matrix=[]
import copy
 
c=0
for i in range(80):

    a= f.readline()
    b=a.split(',')
    b=[int(r) for r in b]
    if max(b)>c:
        c=max(b)
    matrix.append(b)
    box=set()
    
#print "highest element ",c
""" 
matrix=[[131,	673	,234,	103,	18],\
 [201,	96,	342,	965,	150],\
[630,	803,	746,	422,	111],\
[537,	699,	497,	121,	956],\
[805,	732,	524,	37,	331]]
"""
for i in matrix:
    #print i
    pass
rowRange=80
import time
rtime=time.time()
total=[]
for First in range(0,rowRange):
        print First,"    ", time.time()-rtime
        Q=[]
        dist={}
        distance=[]
        for i in range(rowRange):
            for j in range(rowRange):
                dist[(i,j)]=123456789
                distance.append((123456789,i,j))       
                Q.append((i,j))
        distance.remove((dist[First,0],First,0))
        distance.append((matrix[First][0],First,0))
        dist[(First,0)]=matrix[First][0]
         
        while Q:
            distance.sort(reverse=True)
            a,x,y=distance.pop()
            #print a,x,y,".."
            #print "++++++++++++"
            #print x,y
            #print "--------"
             
            Q.remove((x,y))
            if a==123456789:
                print" no"
                break
            #make neighbors of x,y :
            neighbors=[]
            if x+1<rowRange:
                neighbors.append((x+1,y))
            if x-1>=0:
                neighbors.append((x-1,y))
            if y+1<rowRange:
                neighbors.append((x,y+1))
            for eachX,eachY in neighbors:

                alt=a+matrix[eachX][eachY]
                if alt<dist[(eachX,eachY)]:
                    #print eachX,eachY,alt,dist[(eachX,eachY)]
                    distance.remove((dist[(eachX,eachY)],eachX,eachY))
                    
                    dist[(eachX,eachY)]=alt
                    distance.append((alt,eachX,eachY))
        catch=[]
        for i in range(rowRange):
            catch.append(dist[(i,rowRange-1)])
        total.append(min(catch))
print min(total)
"""
                    
print   
for i in range(5):
    print
    for j in range(5):
        print dist[(i,j)],"   ",
"""
print time.time()-rtime
