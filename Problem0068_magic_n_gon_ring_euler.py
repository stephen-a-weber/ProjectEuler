import itertools
"""
frog={}
for j in range(25):
   frog[j]=[]
   for i in itertools.combinations(range(1,11),3):
     
  
        if sum(i)==j:
           frog[j].append(i)
           #gives range of 11 to 22 with at least 5 possibiliities
"""

total=[]

for j in range(11,23):
    
   sump=[]
   for i in range(1,10):
       sump.append([10,i])

   # this takes care of two of the ten spaces to here
   #print j,len(sump),
   sump3=[]
   while sump:
       trial=sump.pop()
       value=sum(trial)
        
       k=j-value
       if k>0 and k<10 and k not in trial:
  
           trial.append(k)
           sump3.append(trial)
   # this takes care of three of the ten spaces to here
   #print len(sump3),
   sump4=[]
   while sump3:
       trial=sump3.pop()
       for i in range(1,10):
           if i not in trial:
               goat=[r for r in trial]
               goat.append(i)
               sump4.append(goat)
   # this takes care of four of the ten spaces to here
   #print len(sump4),
   sump5=[]
   while sump4:
       trial=sump4.pop()
       value=trial[2]+trial[3]
       k=j-value
       if k>0 and k<10 and k not in trial:
           trial.append(k)
           sump5.append(trial)
   # this takes care of five of the ten spaces to here
   #print len(sump5),
   sump6=[]
   while sump5:
       trial=sump5.pop()
       for i in range(1,10):
           if i not in trial:
               goat=[r for r in trial]
               goat.append(i)
               sump6.append(goat)

   # this takes care of six of the ten spaces to here
   #print len(sump6),
   sump7=[]
   while sump6:
       trial=sump6.pop()
       value=trial[4]+trial[5]
       k=j-value
       if k>0 and k<10 and k not in trial:
           trial.append(k)
           sump7.append(trial)
   # this takes care of seven of the ten spaces to here
   #print len(sump7),
   sump8=[]
   while sump7:
       trial=sump7.pop()
       for i in range(1,10):
           if i not in trial:
               goat=[r for r in trial]
               goat.append(i)
               sump8.append(goat)
   # this takes care of 8 of the ten spaces
   #print len(sump8),
   sump9=[]
   while sump8:
       trial=sump8.pop()
       value=trial[6]+trial[7]
       k=j-value
       if k>0 and k<10 and k not in trial and (k+trial[1])<j:
           trial.append(k)
           sump9.append(trial)
   # this is almost complete
   #print len(sump9),
   sump10=[]
   while sump9:
       trial= sump9.pop()
       for i in range(1,10):
           if i not in trial:
               if (i+trial[8]+trial[1])==j:
                   goat=[r for r in trial]
                   goat.append(i)
                   sump10.append(goat)
   #print len(sump10)
   for i in sump10:
       total.append(i)
print sump10
catch=[]
for i in total:
    a=[]
   
    b=[0,3,5,7,9]
    for j in b:
        a.append(i[j])
    c=min(a)
    frog=[]
    v=[]
    h=i.index(c)
    for p in range(5):
        if h==0:
            v=[0,1,2]
        if h==3:
            v=[3,2,4]
        if h==5:
            v=[5,4,6]
        if h==7:
            v=[7,6,8]
        if h==9:
            v=[9,8,1]
        for u in v:
            frog.append(i[u])
        h=(h+1)%5
  
    catch.append( frog)

print max(catch)




   
