//
//  main.cpp
//  Problem0006_Sum_Squre_Difference
//
//  Created by Stephen Weber on 3/5/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//
/*
 Sum square difference
 Problem 6
 The sum of the squares of the first ten natural numbers is,
 
 12 + 22 + ... + 102 = 385
 The square of the sum of the first ten natural numbers is,
 
 (1 + 2 + ... + 10)2 = 552 = 3025
 Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
 
 Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 
 
 Answer:
 25164150
 Completed on Tue, 22 Jan 2013, 03:51
 
 
 
*/
#include <math.h>
#include <iostream>
using namespace std;
int main(int argc, const char * argv[])
{
    
    int sumOfSquares=0;
    int squareOfSum =0;
    
    for (int i =1;i<101;i++){
        int u=pow(i,2);
        sumOfSquares+=u;
        squareOfSum+=i;
    }
    squareOfSum=pow(squareOfSum,2);
    
    
    int Difference = squareOfSum-sumOfSquares;
    
    cout<<"THE ANSWER IS "<<Difference<<endl;
    
    
    
    return 0;
}

