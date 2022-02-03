//
//  main.cpp
//  euler07
//
//  Created by Stephen Weber on 1/22/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//
/*
 10001st prime
 Problem 7
 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 
 What is the 10 001st prime number?
 
 
 Answer:
 104743
 Completed on Tue, 22 Jan 2013, 20:07
 */

#include <vector>
#include <iostream>
#include <ctime>
using namespace std;
int main(int argc, const char * argv[])
{
    time_t start=clock();
    const int n=1000000;
    vector<bool> sieve(n,true);
    
    
    int count=1;
    for (int i=4;i<n;i+=2) {
        sieve[i]=false;
        //sieve prime 2 multiples
    }
    
    for (int i=3;i<n;i+=2){
        if (sieve[i]==1) {
            count+=1;
            
            if (count==10001){
                cout<<"The 10001st prime is "<<i<<endl;
                time_t end=clock()-start;
                cout<<"THIS TOOK "<<((float) end)/CLOCKS_PER_SEC<<endl;
                break;
            }
            
            for (int j=2*i;j<n;j+=i) {
                
                sieve[j]=false;
            }
            
        }
        
    }
    
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

