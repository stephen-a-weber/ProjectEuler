player1win=0
player2win=0
games=[]
cards={}
cards['A']=14
cards['K']=13
cards['Q']=12
cards['J']=11
cards['T']=10
book=open( "/Users/sweber/Desktop/codeFolder/poker.txt")

#999
n=1000
for i in range(0,n):
    
    a =book.readline()
    
    g=a.split(" ")
    
     
    games.append(g)

def highCard(hand):
    total=0
    for i in range(0,5):
        if        hand[i][0]>total:
            total=hand[i][0]
    return True,total

def onePair(hand):
    highcard=0
    #returns zero for none
    g=[]
    h=set()
    for i in range(0,5):
        g.append(hand[i][0])
    for i in range(0,5):
        if g.count(g[i])==2:
            h.add(g[i])
    j=list(h)
    j.sort()
    if len(j)==1:
        
        return True,j
    else:
        return False,[0]
    
def twoPair(hand):
    highcard=0
     
    g=[]
    h=set()
    for i in range(0,5):
        g.append(hand[i][0])
    for i in range(0,5):
        if g.count(g[i])==2:
            h.add(g[i])
  
     
    j=list(h)
    j.sort()
     
    
    if len(j)==2:
      
        return True,[j[1],j[0]]
     
         
     
    else:
        return False,[0,0]
 


def threeKind(hand):
      
     
    g=[]
    h=set()
    for i in range(0,5):
        g.append(hand[i][0])
    for i in range(0,5):
        if g.count(g[i])==3:
            h.add(g[i])
     
     
    j=list(h)
    j.sort()
     
    
    if len(j)==1:
      
        return True,j
     
         
     
    else:
        return False,[0]
 

def straight(hand):
    g=[]
     
    for i in range(0,5):
        g.append(hand[i][0])
    h=set(g)
    if len(h)==5:
        g.sort()
        if g[0]+4==g[4]:
            return True,g[4]
        else:
            return False,0
    else:
        return False,0

def flush(hand):
    g=[]
    j=[] 
    for i in range(0,5):
        g.append(hand[i][1])
        j.append(hand[i][0])
    maxcard=max(j)
    h=set(g)
    if len(h)==1:
        return True,maxcard
    else:
        return False,0

def fullHouse(hand):
    g=[]
     
    for i in range(0,5):
        g.append(hand[i][0])
    h=set(g)
    if len(h)==2:
        threecard=False
        twocard=False
        maxcard=0
        mincard=0
        for i in h:
            if g.count(i)==3:
                threecard=True
                maxcard=i
            if g.count(i)==2:
                twocard=True
                mincard=i
        if threecard and twocard:
            return True,[maxcard,mincard]
        else:
            return False,0
    else:
        return False,0

def fourKind(hand):
    g=[]
    h=set()
    for i in range(0,5):
        g.append(hand[i][0])
    for i in range(0,5):
        if g.count(g[i])==4:
            h.add(g[i])
  
     
    j=list(h)
    j.sort()
     
    
    if len(j)==1:
      
        return True,j
     
         
     
    else:
        return False,[0]
    return False,0

def straightFlush(hand):
    work,answer=flush(hand)
    if work:
        otherwork,otheranswer=straight(hand)
        if otherwork:
            return True,otheranswer
        else:
            return False,0
    return False,0

def RoyalFlush(hand):
    work,answer=straightFlush(hand)
     
    if work:
        if answer==14:
            return True,answer
        else:
            return False,0
    else:
        return False,0


     

def checkcards(thePlayer):
    theLevel=0
    theAnswer=0
    for i in range(10,0,-1):
        if i==10:
            works,theAnswer=RoyalFlush(thePlayer)
            if works:
                theLevel=10
                break
        if i==9:
            works,theAnswer=straightFlush(thePlayer)
            if works:
                theLevel=9
                break
        if i==8:
            works,theAnswer=fourKind(thePlayer)
            if works:
                theLevel=8
                break
        if i==7:
            works,theAnswer=fullHouse(thePlayer)
            if works:
                theLevel=7
                break
        if i==6:
            works,theAnswer=flush(thePlayer)
            if works:
                theLevel=6
                break
        if i==5:
            works,theAnswer=straight(thePlayer)
            if works:
                theLevel=5
                break
        if i==4:
            works,theAnswer=threeKind(thePlayer)
            if works:
                theLevel=4
                break
        if i==3:
            works,theAnswer=twoPair(thePlayer)
            if works:
                theLevel=3
                 
                break
        if i==2:
            works,theAnswer=onePair(thePlayer)
            if works:
                theLevel=2
                break
        if i==1:
            works,theAnswer=highCard(thePlayer)
            if works:
                theLevel=1
                break
  
             
    return theAnswer,theLevel 


 

for i in range(0,n):
    a=games[i]
    b=[]
    for j in a:
        if j[0] in cards:
            b.append([cards[j[0]],j[1]])
        else:
            b.append([int(j[0]),j[1]])
    
    player1=b[:5]
    player2=b[5:]
    answer1,level1=checkcards(player1)
    answer2,level2=checkcards(player2)
     
  
    if level1>level2:
        player1win+=1
  
    elif level1<level2:
        player2win+=1
  
    if level1==level2:
        if answer1>answer2:
            player1win+=1
            
        else:
            player2win+=1
             
           ##note there is a clear winner

print player1win  
    
    
    
 
