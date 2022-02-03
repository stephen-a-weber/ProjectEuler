from math import factorial
"""
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


Answer:
2783915460
Completed on Thu, 24 Jan 2013, 20:53

"""
# the right n-1 digits of digits are rotated a factorial amount of time
# this changes the nth digit to that many cycles increased
# from the choices left in digits
#
# For example 9!=362880
# 9!*2 =725760 <1000000
# so the left most digit cycles from 0..1..2 and
# final=[2] with digits being [0,1,3,4,5,6,7,8,9] to the right
# and so on
final=[]
digits=[0,1,2,3,4,5,6,7,8,9]
#The millionth is after 999999 moves
total=999999
pos=0

while pos<10:
    temp=factorial(len(digits)-1)
    cycles=total/temp   
    total=total-cycles*temp
    f=digits[cycles]   
    digits.remove(f)
    final.append(f)
    pos+=1
final+=digits
print "".join([str(r) for r in final])
    
        
    
