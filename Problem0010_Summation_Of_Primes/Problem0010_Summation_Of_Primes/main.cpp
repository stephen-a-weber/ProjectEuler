//
//  main.cpp
//  euler10
//
//  Created by Stephen Weber on 1/22/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//
/*
 Summation of primes
 Problem 10
 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 
 Find the sum of all the primes below two million.
 
 
 Answer:
 142913828922
 Completed on Tue, 22 Jan 2013, 22:11
 
 */
#include <bitset>
#include <vector>
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;
int main(int argc, const char * argv[])
{
    time_t start=clock();
    const uint64_t n=2000000;
    
    //bitset<n> sieve;
    vector<bool> sieve(n,true);
    //sieve.set();
    
    uint64_t count=2;
    for (int i=4;i<n;i+=2) {
        sieve[i]=false;
        //sieve.set(i,0);
        //sieve prime 2 multiples
    }
    
    for (uint64_t i=3;i<n;i+=2){
        if (sieve[i]==1) {
            count+=i;
            
            
            
            for (uint64_t j=i*i;j<n;j+=i) {
                
                sieve[j]=false;
            }
            
        }
        
    }
    cout<<"The sum of the primes below "<<n<<" is "<<count<<endl;
    time_t end=clock()-start;
    cout<<"This took "<<((float)end)/CLOCKS_PER_SEC<<endl;
    // insert code here...
    
    return 0;
}

