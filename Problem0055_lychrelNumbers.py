
finals=[]

def Pal(number):
    length=len(number)/2
    
    if  number[::-1][:length]==number[:length]:
        return True
    else:
        return False

def adding(number):
    return str(int(number)+int(number[::-1]))


for i in range(1,10000):


    palindrome=str(i)
    for j in range(0,51):
     
        palindrome=adding(palindrome)
        if Pal(palindrome):
            break
        
  

        if j==50:
            finals.append(str(i))

print len(finals)
            

  

        
