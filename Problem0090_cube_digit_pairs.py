import itertools
a=0
flock=[]
thei=[]

for i in itertools.combinations(range(0,10),6):
    thei.append(i)
    
for a in range(len(thei)-1):     
     for b in range(a,len(thei)):
          i=thei[a]
          j=thei[b]
          
  
    
          level1=False
          level2=False
          level3=False
          level4=False
          level5=False
          level6=False
          level7=False
          level8=False
          level9=False
          if (0 in i and 1 in j) or (0 in j and 1 in i):
              #print "level1"
              level1=True

              if level1:
                  if (0 in i and 4 in j) or (0 in j and 4 in i):
                      #print "level2"
                      level2=True
                  if level2:


                      
                      if ((0 in i and 9 in j) or (0 in j and 9 in i)) :
                          level3=True
                          #print "level3"
                      if ((6 in i and 0 in j) or (6 in j and 0 in i)):
                          level3=True

                          #print "level3"
                      if level3:


                                  
                          if ((1 in i and 6 in j) or (1 in j and 6 in i)) :
                              level4=True
                              #print "level4"
                          if  ((1 in i and 9 in j) or (1 in j and 9 in i)):
                              level4=True

                              #print "level4"


                          if level4:
                              
                              if (2 in i and 5 in j) or (2 in j and 5 in i):
                                  level5=True
                                  #print "level5"

                              if level5:
                                  

                                          
                                  if ((3 in i and 6 in j) or (3 in j and 6 in i)) :
                                      level6=True
                                  if  ((3 in i and 9 in j) or (3 in j and 9 in i)):
                                      level6=True

                                      #print "level6"
                                      
                                  if level6:


                                      
                                      if ((4 in i and 9 in j) or (4 in j and 9 in i)) :
                                          level7=True
                                      if ((4 in i and 6 in j) or (4 in j and 6 in i)):
                                          level7=True

                                          #print "level7"
                                      if level7:


                                          
                                          if ((6 in i and 4 in j) or (6 in j and 4 in i)) :
                                              level8 =True
                                          if  ((9 in i and 4 in j) or (9 in j and 4 in i)):
                                              level8=True

                                              #print "level8"
                                          if level8:


                                              
                                              if (8 in i and 1 in j) or (8 in j and 1 in i):
                                                  flock.append([i,j])
                                                  #print "no"

print len(flock)
