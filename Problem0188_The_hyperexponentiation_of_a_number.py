"""
The hyperexponentiation of a number
Problem 188
The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b or ba, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 327 = 7625597484987 and 3↑↑4 is roughly 103.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.


Answer:
95962097
Completed on Wed, 20 Mar 2013, 21:18
"""

a=1777

def powerUp(n):
    limit=10**8
    result=1
    for i in range(n):
        result=result*1777
        result=result%limit
    return result

phi=2**6*5**7
digit=10**8
b=(1777**1777)%phi

n=2

while n<8:

    c=powerUp(b)
    c=c%digit
    b=c%phi
    n=n+1
    print n,c

print c
