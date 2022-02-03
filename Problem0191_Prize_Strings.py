"""
Prize Strings
Problem 191
A particular school offers cash rewards to children with good attendance and punctuality. If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?


Answer:
1918080160
Completed on Mon, 18 Mar 2013, 23:01

"""



#first pass would be [(0,0,1),(1,0,1),(0,1,1)]
grainery=[(0,0,1)]
#second pass should be=[(0,0,2),(1,0,1),(0,1,3), (2,0,1), (1,1,1)]
#(a,b,c)  a is absents b is tardy c is last two numbers
 
 
days=30
storage=[]
for i in range( days ):
    new={}
    storage=[]
    print grainery
    for a,b,c in grainery:
        if a<2:
            choice=tuple([a+1,b])
            if choice not in new:
                new[choice]=c
            else:
                new[choice]+=c
        #print "1",new
        if b<1:
            choice=tuple([0,b+1])
            if choice not in new:
                new[choice]=c
            else:
                new[choice]+=c
        #print "2",new
         
        choice=tuple([0,b])
        if choice not in new:
                new[choice]=c 
        else:
                new[choice]+=c 
        #print "3",new
    for j in new:
        a,b=j
      
        storage.append(tuple([a,b,new[j]]))
    grainery=storage

s=0
for a,b,c in grainery:
    s=s+c
print s
    
