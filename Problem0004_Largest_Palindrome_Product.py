"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
906609
Completed on Tue, 22 Jan 2013, 00:55

"""
bestNumber=0
for threeDigitNumber1 in range(100,999):
    for threeDigitNumber2 in range(threeDigitNumber1,1000):
        product = threeDigitNumber1 * threeDigitNumber2
        
        check=str(product)
        if check==check[::-1]:
             
            if product>bestNumber:
                bestNumber=product
                 
print "The Largest Palindrome made from two 3-digit numbers ",bestNumber
