"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


Answer:
21124
Completed on Thu, 24 Jan 2013, 01:22

"""


a=[1]*999
a[1]="one"
a[2]="two"
a[3]="three"
a[4]="four"
a[5]="five"
a[6]="six"
a[7]="seven"
a[8]="eight"
a[9]="nine"
a[10]="ten"
a[11]="eleven"
a[12]="twelve"
a[13]="thirteen"
a[14]="fourteen"
a[15]="fifteen"
a[16]="sixteen"
a[17]="seventeen"
a[18]="eighteen"
a[19]="nineteen"
a[20]="twenty"
a[30]="thirty"
a[40]="forty"
a[50]="fifty"
a[60]="sixty"
a[70]="seventy"
a[80]="eighty"
a[90]="ninety"
a[100]="hundred"

total=0
one_nine=0
b=[1,2,3,4,5,6,7,8,9]
 
for i in b:
    
    one_nine+=len(a[i]) 
   
 
 
c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

print c
for i in c:
    total+=len(a[i])

#20-----[20,20,1,20,2,20,3,20,4,20,5,20,6,20,7,20,8,20,9]
#total+=10*len(a[20])
#total+=one_nine
 
 
for i in range(2,10):
    total+= 10*len(a[i*10])
    total+=one_nine
    
#total good to 1-99 so save for hundreds as doubleDigits
doubleDigits=total
 
hundred1=len(a[1])+len(a[100])
hundred2=len(a[2])+len(a[100])
hundred3=len(a[3])+len(a[100])
hundred4=len(a[4])+len(a[100])
hundred5=len(a[5])+len(a[100])
hundred6=len(a[6])+len(a[100])
hundred7=len(a[7])+len(a[100])
hundred8=len(a[8])+len(a[100])
hundred9=len(a[9])+len(a[100])
#100-199
total+=hundred1
total+=(hundred1+3)*99 #the three is for "and"
total+=doubleDigits
#200-299
total+=hundred2
total+=(hundred2+3)*99
total+=doubleDigits
#300-399
total+=hundred3
total+=(hundred3+3)*99
total+=doubleDigits
#400-499
total+=hundred4
total+=(hundred4+3)*99
total+=doubleDigits
#500-599
total+=hundred5
total+=(hundred5+3)*99
total+=doubleDigits
#600-699
total+=hundred6
total+=(hundred6+3)*99
total+=doubleDigits
#700-799
total+=hundred7
total+=(hundred7+3)*99
total+=doubleDigits
#800-899
total+=hundred8
total+=(hundred8+3)*99
total+=doubleDigits
#900-999
total+=hundred9
total+=(hundred9+3)*99
total+=doubleDigits

#1000
total+=len(a[1])+len("thousand")
print total
 
 
