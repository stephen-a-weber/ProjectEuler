
"""
Number Rotations
Problem 168
Consider the number 142857. We can right-rotate this number by moving the last digit (7) to the front of it, giving us 714285.
It can be verified that 714285=5142857.
This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.

Find the last 5 digits of the sum of all integers n, 10  n  10100, that have this property.


Answer:
59206
Completed on Fri, 14 Jun 2013, 23:23

"""
sad=[]
total=0 
for x in range(2,10):
    for y in  range(1,10):
        name=[]
      
        a=x*y
        carry=a/10
        digit=a%10
        name.append(digit)
        place=1
        
      
        while place<99:
      
            if digit==y and carry ==0 and name[-2]!=0:
                frog= name[:]
                frog.reverse()
                dog= [str(r) for r in frog]
                if dog[0]==0:
                    print"_"
                cat="".join(dog)
                parrot="".join(dog[1:])+"".join(dog[0])
                bird=int(parrot)
                sad.append(bird)
                total+=bird
                #print x,"".join(dog[1:])+"".join(dog[0]),"=",cat
                #happy.add(tuple(name))
                sad.append(name)
            a=x*digit+carry
             
            carry=a/10
  
            digit=a%10
            place+=1
            name.append(digit)
             
for i in range(1,10):
    d=str(i)
    for t in range(2,101):
        d+=str(i)
        e=int(d)
        total+=e
print total%100000
    
                
#print len(happy)               
