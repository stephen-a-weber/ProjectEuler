#Problem0206_Concealed_Squares.py
"""
Concealed Square
Problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.


Answer:
1389019170
Completed on Fri, 15 Mar 2013, 20:11

"""
import time
ras=time.time()

x=1020304050607080900
#print x**.5
#y=1929394959697989990
#print y**.5
low= 1010101030#10#.1
high=1389026570#620#3#.11
#edited as 900 comes from x30^2 or x70^2
answer=0
i=low
frog=True #for alternating steps to keep last two places 30 or 70
while i<high:
    
 
     
    g=i*i
    #print "trying ",i,"--",g
    y=x
    cat=False
    while (y>0):
      digitA=y%10
      #print digitA
      digitB=g%10
      if digitA!=digitB:
         break
      y=y/100
      
      g=g/100
      if y==0:
         cat=True
         answer=i*i
    if cat:
        print answer
        break
    if frog:
        i+=40
        frog=False
    else:
        i+=60
        frog=True
    
    
         
     
print time.time()-ras 
