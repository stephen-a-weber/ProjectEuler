
# q1+ q = p
# q + p = p1
#
# | q q1 |
# | p p1 |
#
#stored as q,p,q1,p1
#    | * q1 |  >>>   | * q1 |     | q1 p1 |    | p1 q1 |
#    | * p1 |  >>>   | p1 * |     | *  *  |    | *   * |

storage=[[1,2,1,3]] #calculated starting with first two odd GCD=1 ->1,3          
box=0
Fibs=[]
while True:
    c=storage.pop(0)
    #first add next three fibonacci boxes
    q,p,q1,p1=c
     
    FB1=[p1-q1,p1,q1,2*p1-q1]
    FB2=[q1,p1+q1,p1,p1+2*q1]
    FB3=[p1,q1+p1,q1,q1+2*p1]
    storage.append(FB1)
    storage.append(FB2)
    storage.append(FB3)
    a=[2*q*p,q1*p1,q*p1+q1*p]
    a.sort()
    if a[2]>100000000:
        break
    if a in Fibs:
        print "duplicate"
    else:
        Fibs.append(a)
    
    
    
