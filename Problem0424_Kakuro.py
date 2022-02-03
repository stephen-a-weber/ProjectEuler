import copy
fi=open("/Users/isadmin/Downloads/kakuro200.txt","rb")
e=fi.readline()
r=e.split(',')

import itertools
rrr=range(1,10)
rb={}
for i in range(1,7):
    rb[i]={}
     
        
    for j in itertools.combinations(rrr,i):
        k=sum(j)
        if k not in rb[i]:
            rb[i][k]=set([j])
        else:
            rb[i][k].add(j)
"""
for i in rb:
	for j in rb[i]:
		print i,j, rb[i][j]
"""

def checkComplete (alpha,value):#winning hand check
    global words
    chicken=True
    for i in words:
        if len(i[0])==1:
            sumtotal=0
            for j in i[1]:
                sumtotal+=value[j]
            if alpha[i[0][0]]!=sumtotal:
                chicken=False
                break
            
        elif len(i[0])==2:
            sumtotal=0
            for j in i[1]:
                sumtotal+=value[j]
            if (alpha[i[0][0]]*10+alpha[i[0][1]])!=sumtotal:
                chicken=False
                break
        else:
            print "ERROR CHECK"
            
    if chicken:
        return True
    else:
        return False

def addwordtostorage(alpha,value,word,qwerty):
    global storage
    global rb
    letters,positions=word
##    print alpha
##    print value
##    print word
##    print qwerty
##         
##    print"_______"
    empties=[]
    fulls=set()
    letts=set()
    for i in positions:
        if value[i]==999:
            empties.append(i)
        else:
            fulls.add(i)
            letts.add(value[i])
    numNeeded=len(empties)
##    if numNeeded==0:
##     
##        storage.append([qwerty,alpha,value])
##        return
    possibles=set(range(1,10)).difference(letts)
    if len(letters)==1:
        
 
        if alpha[letters[0]]!=-1:
            #print"A"
            #one sum 
            total=alpha[letters[0]]
            totalS=total-sum(letts)
            if totalS not in rb[numNeeded]:
                return
            cars=rb[numNeeded][totalS]
            for driven in cars:
                drive=set(driven)
                if drive.issubset(possibles):
                    for y in itertools.permutations(drive):
                        aaa=copy.deepcopy(alpha)
                        vvv=copy.deepcopy(value)
                        for x in range(len(y)):
                            vvv[empties[x]]=y[x]
                            #print aaa,
                            #print vvv
                            if checkword(aaa,vvv,word):
                                storage.append([qwerty,aaa,vvv])
                        
                        
        else:
            #all possible sums
            #print"B"
            al=set(alpha)
            al.remove(-1)
            numberTotalsPossible=set(range(1,10)).difference(al)
            for total in numberTotalsPossible:
                totalS=total-sum(letts)
                if totalS not in rb[numNeeded]:
                        continue
                cars=rb[numNeeded][totalS]
                for driven in cars:
                    drive=set(driven)
                    if drive.issubset(possibles):
                        for y in itertools.permutations(drive):
                            aaa=copy.deepcopy(alpha)
                            vvv=copy.deepcopy(value)
                            for x in range(len(y)):
                                vvv[empties[x]]=y[x]
                                aaa[letters[0]]=total
                                #print aaa,vvv
                                if checkword(aaa,vvv,word):
                                    storage.append([qwerty,aaa,vvv])
                                 
                                


            
        pass
    if len(letters)==2:
        
        L1=alpha[letters[0]]
        L2=alpha[letters[1]]
        if L1!=-1 and L2!=-1:#we know the sum with both letters
            #print"C"
            total=L1*10+L2
            totalS=total-sum(letts)

            #print numNeeded,total,sum(letts),letts
            if totalS not in rb[numNeeded]:
                        return
            cars=rb[numNeeded][totalS]
            for driven in cars:
                drive=set(driven)
                if drive.issubset(possibles):
                    for y in itertools.permutations(drive):
                        aaa=copy.deepcopy(alpha)
                        vvv=copy.deepcopy(value)
                        for x in range(len(y)):
                            vvv[empties[x]]=y[x]
                            if checkword(aaa,vvv,word):
                                storage.append([qwerty,aaa,vvv])
                
        elif L1!=-1 and L2==-1:
            #print"D"
            al=set(alpha)
            al.remove(-1)
            numberTotalsPossible=set(range(1,10)).difference(al)
            NumberTP=[L1*10+r for r in numberTotalsPossible]
            for total in NumberTP:
                totalS=total-sum(letts)
                if totalS not in rb[numNeeded]:
                     
                    continue
                cars=rb[numNeeded][totalS]
                for driven in cars:
                    drive=set(driven)
                    if drive.issubset(possibles):
                        for y in itertools.permutations(drive):
                            aaa=copy.deepcopy(alpha)
                            vvv=copy.deepcopy(value)
                            for x in range(len(y)):
                                vvv[empties[x]]=y[x]
                                aaa[letters[1]]=total-L1*10
                                if checkword(aaa,vvv,word):
                                    storage.append([qwerty,aaa,vvv])
                                 





            
             
        elif L1==-1 and L2!=-1:
            #print"E"
            al=set(alpha)
            al.remove(-1)
            numberTotalsPossible=set(range(1,10)).difference(al)
            NumberTP=[r*10+L2 for r in numberTotalsPossible]
            for total in NumberTP:
                totalS=total-sum(letts)
                if totalS not in rb[numNeeded]:
                    continue
                cars=rb[numNeeded][totalS]
                for driven in cars:
                    drive=set(driven)
                    if drive.issubset(possibles):
                        for y in itertools.permutations(drive):
                            aaa=copy.deepcopy(alpha)
                            vvv=copy.deepcopy(value)
                            for x in range(len(y)):
                                vvv[empties[x]]=y[x]
                                aaa[letters[0]]=(total-L2)/10
                                if checkword(aaa,vvv,word):
                                    storage.append([qwerty,aaa,vvv])
                                 





            
            
        elif L1==-1 and L2==-1:
            #print"F"
            al=set(alpha)
            al.remove(-1)
            numberTotalsPossible=set(range(1,10)).difference(al)
            for W in numberTotalsPossible:
                
            
                NumberTP=[r*10+W for r in numberTotalsPossible if r != W]
                
                for total in NumberTP:
                    totalS=total-sum(letts)
                    if totalS not in rb[numNeeded]:
                        continue
                    #print numNeeded,total,sum(letts),letts
                    cars=rb[numNeeded][totalS]
                    for driven in cars:
                        drive=set(driven)
                        if drive.issubset(possibles):
                            for y in itertools.permutations(drive):
                                aaa=copy.deepcopy(alpha)
                                vvv=copy.deepcopy(value)
                                for x in range(len(y)):
                                    vvv[empties[x]]=y[x]
                                     
                                    aaa[letters[0]]=(total-W)/10
                                    aaa[letters[1]]=W
                                    if checkword(aaa,vvv,word):
                                        storage.append([qwerty,aaa,vvv])



            
            
        else:
            print"This is broken"
        #need variable total== total for two letters
            
        
        

def smallestword(alpha,value):
    global words
    m=1000
    qwerty=[]
    for i in range(len(words)):
         
        c=0
        for j in words[i][1]:
            if value[j]==999:
                c=c+1
        if c==0:
            qwerty.append(i)
        if c <m and c>0:
            m=c
            ch=i
    
    return ch,qwerty
        
        

def checkword(alpha,value,word):
    letters,positions=word
    t=0
    for f in positions:
        t+=value[f]
    alp=0
    if len(letters)==1:
        alp=alpha[letters[0]]
    else:
        alp=alpha[letters[0]]*10+alpha[letters[1]]
    if t==alp:
        return True
    else:
        
     
        return False
        




    

g=len(e)
a=0
p=int(e[0])
v={}
for c in range(p):
    v[c]=[0]*p
 
        

 
grid={}
count=0
choices=[]
words=[]
value={}
val=0
#print e
frog=False
while a<g-2:
     
    while e[a]!=",":
        a+=1
        if a==g:
            frog=True
            break
    a+=1
    #print a
    if frog:
        break
    count+=1
    nexta=0   
    col=(count-1)%p
    row=(count-1)/p
    if col==0:
        #print
        pass
     
  
    if e[a]=="X":
        grid[(row,col)]=0
        #print "X",
        v[row][col]=999
    if e[a]=="O":
        val=val+1
        value[val]=999
        grid[(row,col)]=[]
        #print "O",
        v[row][col]=val
    if e[a]>="A" and e[a]<="J":
        #print e[a],
        val+=1
        value[val]=999
        words.append([[ord(e[a])-65],[val]])#1,2 letters list 1 and list of sum
        v[row][col]=val
    if e[a]=="(":
        inside=""
  
        nexta=a+1
        v[row][col]=999
        while e[nexta]!=")":
            inside+=e[nexta]
            nexta+=1
        #print a,nexta
        carrot=False
        for i in range(a,nexta):
            if e[i]==",":
                #two
                carrot=True
                xxx=inside.split(",")
                 
                choices.append([[row,col],xxx[0]])
                choices.append([[row,col],xxx[1]])
                
                #print"Z",
        if not carrot:
                #one
                choices.append([[row,col],inside])
                #print"z",
        a=nexta
#print val,"..."

"""
for a in range(p):
    print
    for b in range(p):
        print v[a][b],
"""        
for i in choices:
    if len(i[1])==3:
        frog=[ord(i[1][1])-65,ord(i[1][2])-65]
    else:
        frog=[ord(i[1][1])-65]
   
    if i[1][0]=="v":
        x,y=i[0]
        x=x+1
        ccc=[]
        while v[x][y]!=999:
             
             
            if x==p:
                break
            ccc.append(v[x][y])
            x=x+1
            if x==p:
                break
        words.append([frog,ccc])
        
        
        

    elif i[1][0]=="h":
        x,y=i[0]
        y=y+1
        ccc=[]
        while v[x][y]!=999:
             
             
            if y==p:
                break
            ccc.append(v[x][y])
            y=y+1
            if y==p:
                break
        words.append([frog,ccc])
words.sort(key=len)
#print
#print words
alpha=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
storage=[]
golf=words[0]
theend=len(words)
addwordtostorage(alpha,value,words[0],[0] )

##for i in storage:
##    c,alpha,value=i
##    if   checkword(alpha,value,words[0]):
##        print "LOVELY"
##print "CCCCC"
## 
getty=[8,4,2,6,0,3,9,5,7,1]  
while storage:#[   [0,alpha,value]    ]
    qwerty,b,c=storage.pop(0)
    rat=False
    for i in qwerty:
        if not checkword(b,c,words[i]):
         
            rat=True
            break
    if not rat:
        
        if b==getty:
                print "now"
                print checkComplete(b,words,c)
                break
        if len(qwerty)==theend:
            print "JJJJJ______________________*****()()()()())("
             
                
            if checkComplete(b,words,c):
                print b,c
                break
        ch,qwerty=smallestword(b,c)
        k=qwerty+[ch]
        addwordtostorage(b,c,words[ch],k)
        #totalS=total-sum(letts)if len(storage)%100==0:
        if len(storage)%100==0:
           
           
          print k,len(storage)
       

