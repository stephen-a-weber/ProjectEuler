import itertools
s =[""]*9
s[0]="aqbwced"
s[1]="(aqb)wced"
s[2]="((aqb)wc)ed"
s[3]="(aqb)w(ced)"
s[4]="aq(bwc)ed"
s[5]="(aq(bwc))ed"
s[6]="aq((bwc)ed)"
s[7]="aqbw(ced)"
s[8]="aq(bw(ced))"
operations=[('+', '*', '/'), ('/', '/', '*'), ('+', '-', '/'), ('-', '*', '+'), ('/', '+', '/'), ('/', '/', '+'), ('/', '*', '/'), ('-', '*', '*'), ('*', '/', '/'), ('-', '+', '-'), ('+', '+', '*'), ('*', '-', '+'), ('-', '/', '*'), ('+', '+', '+'), ('*', '-', '*'), ('+', '*', '+'), ('-', '+', '/'), ('+', '*', '*'), ('*', '/', '+'), ('-', '-', '/'), ('*', '+', '+'), ('-', '/', '-'), ('*', '+', '*'), ('/', '-', '+'), ('-', '+', '*'), ('+', '+', '/'), ('-', '-', '-'), ('*', '/', '-'), ('-', '+', '+'), ('-', '-', '*'), ('*', '-', '/'), ('/', '/', '-'), ('+', '+', '-'), ('-', '-', '+'), ('*', '+', '/'), ('/', '-', '-'), ('*', '/', '*'), ('/', '+', '-'), ('+', '/', '/'), ('-', '/', '+'), ('/', '+', '*'), ('/', '-', '/'), ('*', '*', '*'), ('/', '+', '+'), ('+', '/', '-'), ('+', '-', '*'), ('/', '/', '/'), ('-', '/', '/'), ('+', '/', '*'), ('+', '-', '+'), ('-', '*', '/'), ('/', '-', '*'), ('+', '/', '+'), ('/', '*', '+'), ('+', '*', '-'), ('*', '*', '-'), ('+', '-', '-'), ('*', '*', '+'), ('/', '*', '*'), ('-', '*', '-'), ('*', '+', '-'), ('*', '*', '/'), ('*', '-', '-'), ('/', '*', '-')]
total=0
clue=[]
count=0 
def function(a,b,c,d):
    answers=set()
    global count
    count+=1
    eee=[a,b,c,d]
    global total
    global clue
   
    for a,b,c,d in itertools.permutations(eee,4):
         
        for q,w,e in operations:   
  
       
            m=[r for r in s] 
         
            for i in m:
                 
                i=i.replace("a",str(float(a)))
                i=i.replace("b",str(float(b)))
                i=i.replace("c",str(float(c)))
                i=i.replace("d",str(float(d)))
                i=i.replace("q",q)
                i=i.replace("w",w)
                i=i.replace("e",e)
                 
                 
                try: 
                   v=eval(i)
                   if v==int(v) and v>0:
                      answers.add(v)
                except:
                          pass
    
    target=1
    while target in answers:
         
        target+=1
    target-=1
    print eee,target
    if target>total:
        total=target
        clue=eee
        print "Increased to ",clue,"  totalling ",total
         
   
                 
 

def run():
    a=1
    b=2
    c=5
    d=8
    function(a,b,c,d)
    while True:
        if d-c==1 and c-b==1 and b-a==1:
            d+=1
            a=1
            b=2
            c=4

        elif c-b==1 and b-a==1:
            c+=1
            b=2
            a=1
        elif b-a==1:
            b+=1
            a=1
        else:
            a=a+1
        function(a,b,c,d)
         

run()
