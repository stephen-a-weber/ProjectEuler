
/*
 Prime generating integers
 Problem 357
 Consider the divisors of 30: 1,2,3,5,6,10,15,30.
 It can be seen that for every divisor d of 30, d+30/d is prime.
 
 Find the sum of all positive integers n not exceeding 100 000 000
 such that for every divisor d of n, d+n/d is prime.
 
 
 Answer:
 1739023853137
 Completed on Thu, 23 May 2013, 18:22

 */

//
//  main.cpp
//  Problem_0357_Prime_Generating_Integers
//
//  Created by Isadmin on 5/23/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//

 
//
#include <iostream>
#include <unordered_set>
#include <vector>
#include <ctime>
#include <cmath>
#include<utility>
using namespace std;
uint64_t n=100000002;
vector<uint64_t> primes;
vector<uint64_t>::iterator pit;
vector <bool> sieve(n ,true);

bool div(uint64_t n){
    if (sieve[n]){
        return false;
    }
    
    uint64_t m=pow(n,.5)+1;
    
    for (uint64_t i =1;i<m;i++){
        if(n%i==0){
            
            uint64_t a=n/i;
            uint64_t b=a+i;
            if (not sieve[b]){
                return false;
            }
        }
    }
    
    return true;
    
}


int main(int argc, const char * argv[]){
    clock_t r=clock();
    primes.push_back(2);
    for (uint64_t i =4;i<=n ;i=i+2) {
        sieve[i]=false;}
    for (uint64_t i =3;i<=n ;i=i+2) {
        
        if (sieve[i]==true) {
            
            primes.push_back(i);
            
            for (uint64_t j=i*i;j<=n ;j+=i){
                
                sieve[j]=false;
            }
        }
        
    }
    
    cout<<div(30)<<" . "<<div(25)<<endl;
    clock_t s =clock()-r;
    cout<<"this took "<<((float) s)/CLOCKS_PER_SEC<<endl;
    uint64_t N=100000000;
    uint64_t total=3;
    
    for(uint64_t i=1;i<N+1;i++){
        
        uint64_t m=div(i);
        if(i%100000==0){
            cout<<i<<" ........";
            clock_t s =clock()-r;
            cout<<"this took "<<((float) s)/CLOCKS_PER_SEC<<endl;
            r=clock();
        }
        
        if(div(i)==true){
            total+=i;
            
        }
    }
    cout<<"Final answer is :"<<total<<endl;
    
    
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

