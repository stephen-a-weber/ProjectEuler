"""
Power digit sum
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?


Answer:
1366
Completed on Thu, 24 Jan 2013, 00:49
"""
number=2**1000
d=sum([int(r) for r in str(number)])
print d
