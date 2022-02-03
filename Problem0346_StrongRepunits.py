"""
Strong Repunits
Problem 346
The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6 
(i.e. 710 = 116 = 1112). In other words, 7 is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit. It can be verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}. 
Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 1012.

Answer:
336108797689259276
Completed on Sat, 1 Jun 2013, 17:50

"""
x=10**12
y=x**.5

total=set([1])#for one

n=2
while n<y:
    if n%100000==0:
        print n,len(total)
    b=n*n
    g=b+1+n
    while g<x:
        total.add(g)
        b*=n
        g+=b
    n=n+1
print sum(total)
    
    

