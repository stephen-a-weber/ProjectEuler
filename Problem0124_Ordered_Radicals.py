"""
Ordered radicals
Problem 124
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23  32  7, so rad(504) = 2  3  7 = 42.

If we calculate rad(n) for 1  n  10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

Unsorted
 	
Sorted

n

rad(n)


n

rad(n)

k
1
1
 	
1
1
1
2
2
 	
2
2
2
3
3
 	
4
2
3
4
2
 	
8
2
4
5
5
 	
3
3
5
6
6
 	
9
3
6
7
7
 	
5
5
7
8
2
 	
6
6
8
9
3
 	
7
7
9
10
10
 	
10
10
10
Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1  n  100000, find E(10000).


Answer:
21417
Completed on Fri, 15 Mar 2013, 21:18

"""
n=100001
 
 
primes=[2]
sieve=[True]*n
numbers={}
for i in xrange(1,n):
    numbers[i]=[]
    numbers[1].append(1)
numbers[2].append(2) 
for i in xrange(4,n,2):
    numbers[i].append(2) 
    sieve[i]=False
for i in xrange(3,n,2):
     
    if sieve[i]:
        numbers[i].append(i)
        primes.append(i)
        for j in xrange(i+i,n,i):
            sieve[j]=False
            numbers[j].append(i)
rad=[] 
for i in range(1,n):
    x=1
    for j in numbers[i]:
        x*=j
    numbers[i]=x
    rad.append(tuple([numbers[i],i]))

    
    
rad.sort()
print rad[9999][1]
 
