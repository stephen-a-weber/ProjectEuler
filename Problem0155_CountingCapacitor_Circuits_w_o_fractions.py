"""
Counting Capacitor Circuits.
Problem 155
An electric circuit uses exclusively identical capacitors of the same value C. 
The capacitors can be connected in series or in parallel to form sub-units, which can then be connected in series or in parallel with other capacitors or other sub-units to form larger sub-units, and so on up to a final circuit.

Using this simple procedure and up to n identical capacitors, we can make circuits having a range of different total capacitances. For example, using up to n=3 capacitors of 60 F each, we can obtain the following 7 distinct total capacitance values:


If we denote by D(n) the number of distinct total capacitance values we can obtain when using up to n equal-valued capacitors and the simple procedure described above, we have: D(1)=1, D(2)=3, D(3)=7 ...

Find D(18).

Reminder : When connecting capacitors C1, C2 etc in parallel, the total capacitance is CT = C1 + C2 +..., 
whereas when connecting them in series, the overall capacitance is given by: 


Answer:
3857447
Completed on Thu, 13 Jun 2013, 18:18
"""
import time
RAS=time.time()
cap={}
for c in range(1,19):
    cap[c]=set()
cap[1].add(60.)
 
 
 
total=set()
 
for num in xrange(1,19):
    e=num//2+1
    for D in xrange(1,e):
        d=num-D
        
        
        for a in cap[d]:
            for b in cap[D]:
                #print d,D
                new= (a*b)*1.0/(a+b) 
                 
                    
                     
                cap[num].add(new)
                
                new=a+b 
                 
                
                cap[num].add(new)
    cp=[r for r in cap[num]]
    for p in cp:
        x=round(p,9)
        if x not in total:
            total.add(x)
        else:
            cap[num].remove(p)
           
   
   
         
     
         
             
    
  
 
    print    num,len(cap[num])
 

 
                           
 
    
print "TOTAL NOW", len(total)
print "Time:",time.time()-RAS
