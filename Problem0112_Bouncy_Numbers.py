n=100

"""
Bouncy numbers
Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.


Answer:
1587000
Completed on Sun, 10 Mar 2013, 04:11

"""

def check(n):
    f=str(n)
    d=int(f[0])
    start=True
    flag_increase=False
    flag_decrease=False
    for i in range(1,len(f)):
         
        if flag_increase:
            if int(f[i])>=d:
                if i<len(f)-1:
                    d=int(f[i])
                else:
                    return 1
            else:
                return 0
        if flag_decrease:
            if int(f[i])<=d:
                if i<len(f)-1:
                    d=int(f[i])
                else:
                    return -1
            else :
                return 0
        if start:
            start=False
            if int(f[i])>d:
                flag_increase=True
                d=int(f[i])
                if i==len(f)-1:
                    return 1
            elif int(f[i])<d:
                flag_decrease=True
                d=int(f[i])
                if i ==len(f)-1:
                    return -1
            elif int(f[i])==d:
                start=True
            if i ==len(f)-1:
                
                return -45

           
total=99 
proportions=0
n=99
b=0
while not(proportions==.99):

     n+=1
     if check(n)==0:
         b=b+1
     total+=1
     proportions=float(b)/total
     
print n,proportions                
"""
count=0
for i in range(100,1000):
    if check(i)==0:
        count+=1
print count
"""
