"""
Connectedness of a network.
Problem 186
Here are the records from a busy telephone system with one million users:

RecNr	Caller	Called
1	200007	100053
2	600183	500439
3	600863	701497
...	...	...
The telephone number of the caller and the called number in record n are Caller(n) = S2n-1 and Called(n) = S2n where S1,2,3,... come from the "Lagged Fibonacci Generator":

For 1  k  55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)
For 56  k, Sk = [Sk-24 + Sk-55] (modulo 1000000)

If Caller(n) = Called(n) then the user is assumed to have misdialled and the call fails; otherwise the call is successful.

From the start of the records, we say that any pair of users X and Y are friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z; and so on for longer chains.

The Prime Minister's phone number is 524287. After how many successful calls, not counting misdials, will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?


Answer:
2325629
Completed on Fri, 24 May 2013, 20:10

"""

pm=524287
#data structure, [group,next,last,size] linkedlist..

phone=[[r,-1,r,1] for r in xrange(1000000)]
Sk=[0]*56
def babyLFG():
    global Sk
    for k in xrange(1,56):        
        Sk[k]=((100003-200003*k+300007*k**3)%1000000)
    return
def LFG(k):
    global Sk
    if k>=1 and k<=55:
        return Sk[k]
    else:
        h=(Sk[k-24]+Sk[k-55])%1000000
        Sk.append(h)
        return h
     
 
babyLFG()
a=0
b=0
#data structure, [group,next,last,size] linkedlist..
GROUP=0
NEXT=1
LAST=2
SIZE=3
call=0
ss=0
 
def CliqueMerge(A,B):
    
    global phone   
     
    if phone[A][GROUP]>phone[B][GROUP]:#size
        phone[A][SIZE]+=phone[B][SIZE]#size transfer to one group
        phone[phone[A][LAST]][NEXT]=B #updated the next phone on last item in group

        phone[A][LAST]=phone[B][LAST]#moving pointer to last of the added items
        number=B
        while number!=-1:
            phone[number][GROUP]=A #update added members group id
            number=phone[number][NEXT]
            #the king group will never lose it's original
            # -1 assignment for next...
    else:
        phone[B][SIZE]+=phone[A][SIZE]#size transfer to one group
        phone[phone[B][LAST]][NEXT]=A #updated the next phone on last item in group

        phone[B][LAST]=phone[A][LAST]#moving pointer to last of the added items
        number=A
        while number!=-1:
            phone[number][GROUP]=B #update added members group id
            number=phone[number][NEXT]
            #the king group will never lose it's original
            # -1 assignment for next...

            
   
#data structure, [group,next,last,size] linkedlist..

while phone[phone[pm][GROUP]][SIZE]<990000:
    
    if call%10000==0:
      phone[phone[pm][GROUP]][SIZE],call
    call+=1
    
    ss+=2
    a=LFG(ss-1)
    b=LFG(ss)
    if a==b:
        call-=1
    else:
        #print a,b
        A=phone[a][GROUP]#group
        B=phone[b][GROUP]
        if A!=B:
            CliqueMerge(A,B)
 
  
#data structure, [group,next,last,size] linkedlist..   
print "THE ANSWER IS ",call         
 
 

            
