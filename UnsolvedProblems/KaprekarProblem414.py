def base5(num):
   return ((num == 0) and  "0" ) or ( base5(num / 5).strip("0") + "01234"[num % 5])


#print base5(23)

CB=[0]*5
 
number=[0]*5
check=[0]*5
rnumber=[0]*5
diff=[0]*5
last=[0]*5
def fill_number(i,base):
     
    m4=i/base**4
    number[0]=m4
    i-=m4*base**4
    m3=i/base**3
    number[1]=m3
    i-=m3*base**3
    m2=i/base**2
    number[2]=m2
    i-=m2*base**2
    m1=i/base
    number[3]=m1
    i-=m1*base
    number[4]=i
    return 

def what_is_number(n,base):
    x=0
    for i in range(5):
        x=x+n[i]*base**(4-i)
    return x
  
def reverse_number():
      
     for i in range(5):
         rnumber[4-i]=check[i]

def subtract_number(base):
    a=0
    for i in range(4,-1,-1):
        
        if rnumber[i]<=check[i]:
           b=check[i]-rnumber[i]
           a+=b
           diff[i]=b
        else:
             
            if check[i-1]>0:
                check[i-1]-=1
                b=check[i]+base -rnumber[i]
                a+=b
                diff[i]=b
            elif check[i-2]>0:
                        check[i-2]-=1
                        check[i-1]+=base-1
                        b=check[i]+base-rnumber[i]
                        a+=b
                        diff[i]=b            
            elif check[i-3]>-0:
                        check[i-3]-=1
                        check[i-2]+=base-1
                        check[i-1]+=base-1
                        b=check[i]+base-rnumber[i]
                        a+=b
                        diff[i]=b
                      
            else:
                        check[i-4]-=1
                        check[i-3]+=base-1
                        check[i-2]+=base-1
                        check[i-1]+=base-1
                        b=check[i]+base-rnumber[i]
                        a+=b
                        diff[i]=b
                
    if a!=0:
        return True
    else:
        return False
        
def compare_Kaprekar():
    for i in range(5):
        if CB[i]!=diff[i]:
            return False
    return True

"""
a=10000
base=15
fill_number(a,base)
print a
print "original ",number

print "CHECKING ",number," = ",what_is_number(number,base)
check=number
check.sort(reverse=True)
print "CHECKING ",check," =",what_is_number(check,base)
print check
 
#fill_number(a,base)

reverse_number()
print rnumber
print "CHECKING ",rnumber," = ",what_is_number(rnumber,base)
print subtract_number(base)
print diff
print "CHECKING ",diff," = ",what_is_number(diff,base)



"""
bbb=1
for k in range(34,35):#k=301
    base=6*k+3
    SUMofB=0
    CB=[0]*5
    cbvalue=False
    for i in range(1,base**5):
        SBofI=0
        fill_number(i,base)
        check=[r for r in number]
        diff=check
        cat =True
        last=[0]*5
        if number==CB:
           continue
        while cat:
            check=diff
            #print "CHECKING ",number," = ",what_is_number(number,base) 
            check.sort(reverse=True)
            #print "CHECKING ",check," =",what_is_number(check,base)
            reverse_number()
            #print "CHECKING ",rnumber," = ",what_is_number(rnumber,base)
            #print check,rnumber,CB
            
            if subtract_number(base):
                SBofI+=1
                if cbvalue:
                    #print "Got a CB value",CB
                    if diff==CB:

                        break
                    
                     
                #print "CHECKING ",diff," = ",what_is_number(diff,base)
                #print check,rnumber,diff,SBofI
                #print"______________________________________"
                if diff!=last:
                   #print "Printing Last ",last
                   last=[r for r in diff]
                    
                else:
                     
                        
                    if cbvalue==False:
                        SBofI-=1
                        CB=check
                        #print "Setting CB Value", CB," iterations : ",SBofI
                        cbvalue=True
                         
                        break#found the CB value
                         
       
                
            else:#  identical digits??
                SBofI=0
                print "identical digits ",bbb
                bbb+=1
                break#leave while
             
                    
             
            
                 
  
             
        SUMofB+=SBofI

print SUMofB                   
      
        
        
