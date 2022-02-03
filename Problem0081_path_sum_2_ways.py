f=open("C:\Users\sweber\Desktop\matrix.txt")
matrix=[]
for i in range(80):

    a= f.readline()
    b=a.split(',')
    b=[int(r) for r in b]
   
    matrix.append(b)

box=set()
box.add((78,79))
box.add((79,78))

while box:
    emptybox=[]
    while box:
        emptybox.append(box.pop())

    for x,y in emptybox:
        #find solutions
        a=0
        b=0
        
        if x+1>79 and y+1>79:
            print x,y, "have no forward, WTF we eliminated this case.."

        if x+1>79 and y+1<80:
            
            matrix[x][y]+=matrix[x][y+1]

        if x+1<80 and y+1>79:
            matrix[x][y]+=matrix[x+1][y]

        if x+1<80 and y+1<80:
            a=matrix[x+1][y]
            b=matrix[x][y+1]
            if a<b:
                matrix[x][y]+=matrix[x+1][y]
            else:
                matrix[x][y]+=matrix[x][y+1]



        #add next set to box
        if x-1>=0:
            box.add((x-1,y))
        if y-1>=0:
            box.add((x,y-1))

print matrix[0][0]
            
        
