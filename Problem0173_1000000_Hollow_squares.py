"""
Using up to one million tiles how many different "hollow" square laminae can be formed?
Problem 173
We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry. For example, using exactly thirty-two square tiles we can form two different square laminae:


With one-hundred tiles, and not necessarily using all of the tiles at one time, it is possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?


Answer:
1572729
Completed on Mon, 18 Mar 2013, 01:07

"""
n=1000000

count=0
a=1
b=a+2

c=b*b-a*a

while c<=n:
    
  
    while c<=n:
        count+=1
        #print a,b
        b=b+2
        c=b*b-a*a
    a+=1
    b=a+2
    c=b*b-a*a

print count
