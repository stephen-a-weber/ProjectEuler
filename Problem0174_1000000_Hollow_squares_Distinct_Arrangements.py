"""
 Counting the number of "hollow" square laminae that can form one, two, three, ... distinct arrangements.
Problem 174
We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a 1x1 hole in the middle. However, using thirty-two tiles it is possible to form two distinct laminae.


If t represents the number of tiles used, we shall say that t = 8 is type L(1) and t = 32 is type L(2).

Let N(n) be the number of t  1000000 such that t is type L(n); for example, N(15) = 832.

What is  N(n) for 1  n  10?


Answer:
209566
Completed on Mon, 18 Mar 2013, 17:26


"""
n=1000000
go={}
 
b=int((n+4)/4.0)
end=0 
for i in range(b,2,-1):
    e=i*i
    if i%2==0:
        end=2
    else:
        end=1
        
    for j in range(i-2,end-1,-2):
        #print i,j,
        p=e-j**2
        #print p
        if p>n:
             
            #print "breaking"
            break
                   
         
        if p not in go:
            go[p]=1
        else:
            go[p]+=1


s=0
t=0
for i in go:
    if go[i]>=1 and go[i]<=10:
        s=s+1
    if go[i]==15:
        t=t+1

print "15 gives ",t
print "Hopefully the answer is then ",s
