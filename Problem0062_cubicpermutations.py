#Cubic Permutations problem 62
"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
digits={0:[]}
import sys
for n in range(1,20000):
    f=n**3
    g=len(str(f))
    if g not in digits:
        digits[g]=set()
        k=g-1
         
        j=[r for r in digits[k]]
        p=[]
         
        for i in j:
            kk=[int(r) for r in str(i)]
            kk.sort()
            p.append(kk)
        for i in p:
            h=p.count(i)
            if h==5:
                print "the range has ",k," digits"
                 
                #sys.exit()
                m=[]
                for ll in j:
                    kk=[int(r) for r in str(ll)]
                    for a in i:
                        if a in kk:
                            kk.remove(a)
                    if len(kk)==0:
                        m.append(ll)
                print "These are the cubic numbers ",m
                print "They sum to  ",sum(m)
                
        
    digits[g].add(f)

