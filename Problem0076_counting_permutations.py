def solution(n):

    coins=range(1,n)
    number=len(coins)
    
    memory={0:[1]*(number+1)}

    for a in xrange(1,n+1):

        memory[a]=[1]*(number+1)
       

        for c in xrange(1,number+1):
            if c >(n-2):
                memory[a][c]=memory[a][c-1]
         
            else:
                if a-coins[c]>=0:
                    memory[a][c]=memory[a][c-1] + memory[a-coins[c]][c]
                else:
                      memory[a][c]=memory[a][c-1]
   
    for i in memory:
        print i,memory[i] 
    return memory[a][number]

print solution(5)
