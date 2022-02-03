/*
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
906609
Completed on Tue, 22 Jan 2013, 00:55

*/

#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

int main()
{
int bestNumber=0;
int product=0;
string number;
string reversedNumber;

for (int i=100;i<999;i++){
    for (int j =i;j<1000;j++) {

        product=i*j;
        ostringstream convert;
        convert << product;
        number=convert.str();
        reversedNumber=number;
        reverse(reversedNumber.begin(),reversedNumber.end());

        if (number==reversedNumber){
            if (product>bestNumber){
                bestNumber=product;
            }
        }


    }
}
cout<< "The Largest Palindrome made from two 3-digit numbers is "<<bestNumber<<endl;


    return 0;
}
