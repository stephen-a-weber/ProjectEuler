import math
"""
http://projecteuler.net/problem=158

 Exploring strings for which only one character comes lexicographically after its neighbour to the left.
Problem 158
Taking three different letters from the 26 letters of the alphabet, character strings of length three can be formed.
Examples are 'abc', 'hat' and 'zyx'.
When we study these three examples we see that for 'abc' two characters come lexicographically after its neighbour to the left.
For 'hat' there is exactly one character that comes lexicographically after its neighbour to the left. For 'zyx' there are zero characters that come lexicographically after its neighbour to the left.
In all there are 10400 strings of length 3 for which exactly one character comes lexicographically after its neighbour to the left.

We now consider strings of n  26 different characters from the alphabet.
For every n, p(n) is the number of strings of length n for which exactly one character comes lexicographically after its neighbour to the left.

What is the maximum value of p(n)?


Answer:
409511334375
Completed on Sun, 14 Apr 2013, 12:12


"""
letters=26
alphabet=[r for r in range(1,letters+1)]



#Creating a dictionary object for our solutions
# we need a storage place for n to vary from two letters to n letters
# Then we fill the easy one
# The two letter one with perfect lexigraphical letters
# Obviously using numbers instead of the alphabet

lexstorage={}
for i in range(2,letters+1):     
    lexstorage[i]={}


for a in range(1,letters+1):
    for b in range(1,letters+1):
        if a==b:
            continue     
        if a<b:
            lexstorage[2][tuple([a,b])]=1
            for i in range(3,letters+1):
              lexstorage[i][tuple([a,b])]=0



 

for letter1,letter2 in  lexstorage[2]:

    #For each of our Two letter combinations that are perfect lexographic pairs
    # which we created above.
    # LEFT and  RIGHT sets are created for any other letters that could be added on that side
    # such that they areNot lexographically ordered with  letter one or two
    LEFT  = set([ r for r in alphabet   if r > letter1 and r != letter2 ])   
    RIGHT = set([ r for r in alphabet   if r < letter2 and r != letter1 ])

    # Any letters between letter one and two will be in both sets
    # These will be called the Subset
    Subset=LEFT.intersection(RIGHT)    
    S=len(Subset)
     
    A=len(LEFT)-S
    B=len(RIGHT)-S
    Total=A+B

    # From here we will count the sets and get a variable
    # Total --> which are the sums of the first sets without the subset
    # S     --> which is the number of terms in the subset




    # This is the bit about whatifs
    # we have N from 2 to the number of letters
    # we have to add up all the combinations of the left and right terms
    # and the subset terms
    # but sometimes we have more subset terms then needed blah blah blah
    SubsetRange=0
    SubsetStartRange=0
    for length in range(3,letters+1):  #<-- Here is the MAIN loop which we then call "number" for # of terms
        number=length-2
        if number<S+1:
            SubsetRange=number+1
        else:
            SubsetRange=S+1
            
        
        if Total<number:
            SubsetStartRange=number-Total
        else:
            SubsetStartRange=0
  



       
        for subsUsed in range(SubsetStartRange,SubsetRange):#[0,S]
            # The subset group can be picked in some combination from
            # possibly zero to all.
            # The first line counts the possible combinations
            # Then since this is the subset group they can go either to the
            # left or right side and this is a 2 to the power of N choices
            subCombinations=math.factorial(S)/math.factorial(S-subsUsed)/math.factorial(subsUsed)
            subCombinations*=2**subsUsed
             
            # This next variable is the number  of other letters needed after choosing the subset ones
            num=number-subsUsed

            # Since both list of letters on the right or left side are chosen initially to
            # not add to the lexigraphical order , it really doesn't matter if we find the sub number on
            # the left and find the combinations of those and add them to the combinations on the right
            # That works out as equal to just totalling both sides and chosing from among this total
            # the number of letters we need.
            RegularsUsed=math.factorial(Total)/math.factorial(Total-num)/math.factorial(num)
 
            # Multiple all our possible combinations together
            Possibles=subCombinations*RegularsUsed

            # Add this in to our storage as we continue through the loop
            lexstorage[length][tuple([letter1,letter2])]+=Possibles
  
                 
                 

            

# output
for w in range (2,letters+1):
    
    d=0
    for i in lexstorage[w]:
        d+=lexstorage[w][i]   
    print "total for a length of ,",w,":",d 
     
"""
This outputs:

total for a length of , 2 : 325
total for a length of , 3 : 10400
total for a length of , 4 : 164450
total for a length of , 5 : 1710280
total for a length of , 6 : 13123110
total for a length of , 7 : 78936000
total for a length of , 8 : 385881925
total for a length of , 9 : 1568524100
total for a length of , 10 : 5380787555
total for a length of , 11 : 15730461760
total for a length of , 12 : 39432389100
total for a length of , 13 : 85056106800
total for a length of , 14 : 158086891300
total for a length of , 15 : 253047192320
total for a length of , 16 : 348019565465
total for a length of , 17 : 409484775700
total for a length of , 18 : 409511334375
total for a length of , 19 : 344863490400
total for a length of , 20 : 241408817650
total for a length of , 21 : 137949211400
total for a length of , 22 : 62704500950
total for a length of , 23 : 21810318400
total for a length of , 24 : 5452587075
total for a length of , 25 : 872414556
total for a length of , 26 : 67108837


These are the number of combinations of n letters (from a set of 26)
which have exactly one lexigraphic higher letter to its right.
The answer is a "word" with 18 letters for the highest number .
"""
