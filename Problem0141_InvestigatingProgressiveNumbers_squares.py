"""
Investigating progressive numbers, n, which are also square.
Problem 141
A positive integer, n, is divided by d and the quotient and remainder are q and r respectively. In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 1022, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (1012).


Answer:
878454337159
Completed on Thu, 2 May 2013, 20:19

"""
storage=set()
p=0
"""
R D Q-->  s ,  sa/b  , saa/bb

s is divisible by b for integer numbers

RDQ -->  s=pbb    pbb, pba , paa

pba*paa+pbb=N
p^2*b*a^3 is big term

"""
for a in range(2,10001):
            for b in range(1,a):
                p=1
                f=0
                while f<10**12:
                  f=(p**2)*b*(a**3)+p*(b**2)
                
    
                  h=int(f**.5)
                
                  if h*h==f and f<10**12:
                     
                    storage.add(f)
                    print a,b,p,f,sum(storage)
                  p+=1
