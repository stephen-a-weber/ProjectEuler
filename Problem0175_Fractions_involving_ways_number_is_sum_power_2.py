"""
Fractions involving the number of different ways a number can be expressed as a sum of powers of 2.
Problem 175
Define f(0)=1 and f(n) to be the number of ways to write n as a sum of powers of 2 where no power occurs more than twice. 

For example, f(10)=5 since there are five different ways to express 10:
10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1

It can be shown that for every fraction p/q (p0, q0) there exists at least one integer n such that
f(n)/f(n-1)=p/q.

For instance, the smallest n for which f(n)/f(n-1)=13/17 is 241.
The binary expansion of 241 is 11110001.
Reading this binary number from the most significant bit to the least significant bit there are 4 one's, 3 zeroes and 1 one. We shall call the string 4,3,1 the Shortened Binary Expansion of 241.

Find the Shortened Binary Expansion of the smallest n for which
f(n)/f(n-1)=123456789/987654321.

Give your answer as comma separated integers, without any whitespaces.

Answer:
1,13717420,8
Completed on Thu, 13 Jun 2013, 14:26


my solution was by hand...

       i/j

     |      |

    i        i+j
   ---      -----
   i+j         j

so our fraction needs to be divided by 9 to get
a gcd of 1 since the hyperbinary tree 
(The hyperbinary sequence and the Calkin-Wilf tree)
needs coprimes to count all rationals.

Anyway it starts as 13717421
                    --------
                    109739369
this is a left leaf
8 times in a row
and then we are at a fraction of 13717421
                                 --------
                                     1
which nicely is 13717420 right leafs
from 1/1

now the binary representations just march down the tree
we start with '1'
and we need the 13717420 '0'
and then 8 '1'
which takes us down the tree the way we went up.
"""

f=13#123456789#/98765432
d=17#98765432
g={}
g[0]=1

n=0
cat=True

while cat:
     
     
    g[2*n+1]=g[n]
    g[2*n+2]=g[n]+g[n+1]
    #print g[2*n+1],1.0/g[2*n],
    if   g[2*n+1]==f and g[2*n ]==d:
        print
        print 2*n+1
        cat=False
 
    n=n+1
