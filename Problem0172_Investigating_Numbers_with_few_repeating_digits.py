#Problem0172_Investigating_numbers_with_few_repeat_digits.py
"""
Investigating numbers with few repeated digits.
Problem 172
How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?


Answer:
227485267000992000
Completed on Fri, 26 Apr 2013, 19:24
"""
total=0
digits=[0]*10
storage=[]
for i in range(1,10):
    f=digits[:]
    f[i]=1
    storage.append([f,1])

container={}

for index in range(17,0,-1):
    #print index
    container={}
    while storage:
         
        a,b  =storage.pop()
         
       
        for x in range(0,10):
            ad=list(a)
            if ad[x]<3 :
                ad[x]+=1
                z=tuple(ad)
                if z not in container:
                    container[z]=b
                else:
                    container[z]+=b
    for item in container:
        storage.append([item,container[item]])
for item in container:
    total+=container[item]
            
print total
