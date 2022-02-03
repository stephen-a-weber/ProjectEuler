"""Connectedness of a network.
Problem 186
Published on Friday, 14th March 2008, 10:00 pm; Solved by 1412
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
import copy

pm=524287

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
     
phone={}
babyLFG()
a=0
b=0
 

call=0
ss=0
while True:
   
    call+=1
    rosary=False
    ss+=2
    a=LFG(ss-1)
    b=LFG(ss)
    if a==b:
        call-=1
    else:
         
        if a not in phone:
            phone[a]=set([a,b])
        
        else:
            
            phone[a].add(b)
            
          
        if b not in phone:
            phone[b]=set([b,a])
        else:
            phone[b].add(a)
        if a==pm or b==pm:
            break
        
        
friends=set([a,b])
print friends
print len(phone),len(friends)

def recursion(i):
    global phone
    global friends
    global pm
    storage=set()
    container=[]
   
    
    for a in phone[i]:

            
            phone[pm].add(a)
            friends.add(pm)
            
            container.append(a)
            storage.add(a)
    while container:
            j=container.pop()
        
            for b in phone[j]:
                if b not in storage:
                    phone[pm].add(b)
                    friends.add(b)
                    container.append(b)
                    storage.add(b)



while len(friends)<990000:
    candy=False
    if len(phone)%1000==0:
        print len(phone),len(friends),call
    call+=1
    rosary=False
    ss+=2
    a=LFG(ss-1)
    b=LFG(ss)
    if a==b:
        call-=1
    else:
        #print a,b
        if a in friends and b in friends:
            continue
        elif a not in friends and b not in friends:
            if a not in phone:
                phone[a]=set([a,b])
            
            else:
                
                phone[a].add(b)
            
            if b not in phone:
                phone[b]=set([b,a])
            else:
                phone[b].add(a)
        elif a not in friends:
            phone[pm].add(a)
            friends.add(a)
            if a not in phone:
                phone[a]=set([a,b])
 
            else:
                recursion(a)
        elif b not in friends:
            phone[pm].add(b)
            friends.add(b)
            if b not in phone:
                phone[b]=set([a,b])
 
            else:
                recursion(b)
                #call 2329876 2329810 2329739
                #friends 990056
    if call>2328700 or len(friends)==988321 or len(friends)>989800:
        candy=True
        print "...",len(phone),len(friends),call
        
    while candy:
            candy=False
            deer=copy.deepcopy(friends)
            for i in deer:
                for j in phone[i]:
                    if j not in friends:
                        friends.add(j)
                        candy=True
       
                
                
  
        
        
         
 
 

            
