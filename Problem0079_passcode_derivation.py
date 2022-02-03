 
 
 
"""
for i in a:
    j=str(i)
     
    for e in j:
         
        if int(e) not in pat:
             
            pat[int(e)]=0
        pat[int(e)]+=1        
z=0
for i in pat:
    print i,pat[i]
    z+=pat[i]
print z/3.0
"""
def checktruth(prisoner,prisonTerm):
     for i in code:
          if not individualcode(i,prisoner,prisonTerm):
               return False
          
     return True


import copy

def individualcode(code,prisoner,prisonTerm):
     a,b,c=[r for r in str(code)]
     
     for x in range(0,prisonTerm-2):
               for y in range(x+1,prisonTerm-1):
                         for z in range(y+1,prisonTerm):
                                  if ( prisoner[x]==a) and \
                                     ( prisoner[y]==b) and \
                                     ( prisoner[z]==c) :
                                          """
                                          print code,": ",
                                          for i in range(len(prisoner)):
                                               
                                               if i ==x or i==y or i==z:
                                                    print "(",prisoner[i],")",
                                               else:
                                                    print prisoner[i],
                                          print
                                          print
                                          """
                                          return True
     return False
                                        
 
finished=False 
numbers=['0','1','2','3','6','7','8','9']
#code=[319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]
code=[129, 389, 769, 790, 160, 289, 290, 680, 689, 690, 180, 316, 318, 319, 710, 716, 162, 718, 719, 720, 728, 729, 731, 890, 736, 362, 620, 368, 168, 629, 760, 762, 380]

 
for prisonTerm in range(8,9):
     #print "starting ",prisonTerm
     a=[' ']*prisonTerm
     jail=[[a,[319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]]]
     while jail:
        prisoner,heist=jail.pop()
        #print "_________________Adding to___________________"
        #print prisoner
        #print "_____________________________________________"
        #print heist
        #print
        #print "---------------------------------------------"
        if  heist==[]:
                gore=checktruth(prisoner,prisonTerm)
                
                if gore:
                     frog=""
                     for i in prisoner:
                          frog+=i
                     print "The winning code number is : ",frog
                     finished=True
 
            
        else:
                g=copy.deepcopy(heist)
                each=g.pop()
                #print "Filling in with ",each
                #print "________________________________"
                a,b,c=[r for r in str(each)]
                for x in range(0,prisonTerm-2):
                    for y in range(x+1,prisonTerm-1):
                        for z in range(y+1,prisonTerm):
                             if (prisoner[x]==' ' or prisoner[x]==a) and \
                                (prisoner[y]==' ' or prisoner[y]==b) and \
                                (prisoner[z]==' ' or prisoner[z]==c) :
                                 hero=[r for r in prisoner]
                                 hero[x]=a
                                 hero[y]=b
                                 hero[z]=c
                                 #print hero
  
                                 jail.append([hero,g])
                             
        if finished:
             break;

