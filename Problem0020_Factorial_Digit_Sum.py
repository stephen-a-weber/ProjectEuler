"""
Factorial digit sum
Problem 20
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


Answer:
648
Completed on Thu, 24 Jan 2013, 03:29
"""
n=1
for i in range(1,101):
    n=n*i

f=str(n)
m=0
for i in f:
    m+=int(i)
print m
