"""
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


Answer:
171
Completed on Thu, 24 Jan 2013, 03:27

"""


dayOftheWeek=[]
tomorrowsDate=[]
todaysDate=[]
leapYear=[]
count=0
todaysDate.append((1,1,1900))
tomorrowsDate.append((1,2,1900))
dayOftheWeek.append(0)
leapYear.append(False)

def testSun(unit):
   global count
 
   if dayOftheWeek[unit]==6 :
       
        a,b,c =todaysDate[unit]
      
        if b==1:
            if c>1900:
              count+=1
   return
a=0
b=0
c=0

year=1900
unit=0
while c<2001:
    testSun(unit)
   
    x =dayOftheWeek[unit]
    x=(x+1)%7
    dayOftheWeek.append(x)
    a,b,c=tomorrowsDate[unit]
    todaysDate.append((a,b,c))
    
     
    b=b+1
    if (a==1):
       if  b>31:
               b=1
               a=2
    elif (a==2):
        if leapYear[unit]:
            if b>29:
                b=1
                a=3
        else:
            if b>28:
                b=1
                a=3

    elif (a==3):
        if  b>31:
            b=1
            a=4

    elif (a==4):
        if b>30:
            b=1
            a=5

    elif (a==5):
        if  b>31:
            b=1
            a=6

    elif (a==6):
        if b>30:
            b=1
            a=7

    elif (a==7):
        if  b>31:
            b=1
            a=8

    elif (a==8):
        if  b>31:
            b=1
            a=9

    elif (a==9):
        if b>30:
            b=1
            a=10

    elif (a==10):
        if  b>31:
            b=1
            a=11

    elif (a==11):
        if b>30:
            b=1
            a=12

    elif (a==12):
        if  b>31:
            b=1
            a=1
            c=c+1
    unit+=1
    if (c%100==0):
  
        if c%400==0:
            leapYear.append(True)
        else:
            leapYear.append(False)
    elif (c%4==0):
        leapYear.append(True)
    else:
        leapYear.append(False)
    tomorrowsDate.append((a,b,c))
    
            
        
         
        
print count   
    
