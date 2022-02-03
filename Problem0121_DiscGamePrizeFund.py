"""
Disc game prize fund
Problem 121
A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.


Answer:
2269
Completed on Mon, 18 Mar 2013, 21:42
"""


possible=[[1,0,0]]

import time
ras=time.time()
new={}
choices=[1,1]
#print possible
#print choices
#first round is either r or b in possible added r
for i in range(15):
    new={}
    print "Chugging at :" ,i+1,time.time()-ras
     
         
 
    for a,r,b in possible:
        choice=( r+1,b)
        #print "This to add:",choice
        if choice in new:
            new[choice]+=a*choices[0] 
        else:
            new[choice]=a*choices[0]
        choice=(r,b+1)
        #print "This to add:",choice
        if choice in new:
            new[choice]+=a*choices[1]
        else:
            new[choice]=a*choices[1]
        

                
                 
    #print "-----"
    #print new
    #print choices
    
    #print "---"
    possible=[]
    for x,y in new:
        possible.append(tuple([new[(x,y)],x,y]))
    #print possible       
    choices[0]+=1
 

win=0
loses=0
for a,r,b in possible:
    #print "red : ",r,"    blue: ",b,"     Combos of this: ",a
    if r>=b:
        loses+=a
    else:
        win+=a
                


print "wins  ",win
print "loses ",loses
print "total ",win+loses

total=win+loses

prize=int(total/win)
print "The max prize is ",prize
