"""
Non-bouncy numbers
Problem 113
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.

How many numbers below a googol (10100) are not bouncy?


Answer:
51161058134250
Completed on Sun, 17 Mar 2013, 03:35

"""
#starting with one digit with an array of ten
#ones representing 0-9.

# The sum of this array is the number of possibilities
# Decending numbers start the next digit over with this total
# (( Z=[sum(x)] )) and we create their possibilites by continually
# subtracting the previous column over
#
# 9         1
# 8         1
# 7         1
# ...
# 0         1
#
# the total for 99-90 is sum of above
# 99-90     10
# 88-80     9
# 77-70     8  <-- subtracting 1 from previous column value

# the total for 99-00 is the sum of all ten or 55
# 999-900     55
# 888-800     55-10=45
# 777-700     45-9 =36
# 666-600     36-8 =28
#
# because of  leading zero we cumulatively add each of these totals
# two digits three digits to n digits
# also each digit column separately gets to represent a set of zeros
# so we subtract  one from this. each time
#
# Ascending works the same but only a running total is needed. and it
# only gets down to a single not counted zero once. It is remoned at the end.
#
# Finally all possible sets of digits can be the same number
# like 777 which is counted both as ascending and decending
# These are removed by subtracting nine times the number of digits
#
# 
ascending=[1]*10
descending=0
 
for digit in range(1,101):

    y=sum(ascending)
    z=[y]
    for i in range(9):
        z.append(z[-1]-ascending[i])
    ascending=z
     
    descending+=ascending[0]-1
    #print ascending,ascending[0]-1,decending,9*a
    

print ascending[0]-1+descending-9*digit

                 
    
