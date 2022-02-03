//
//  main.cpp
//  Problem0211_Divisor_Square_sum
//
//  Created by Isadmin on 5/21/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//
#include <iostream>
#include <unordered_set>
#include <vector>
#include <ctime>
#include <cmath>
#include<utility>
using namespace std;
 
    
uint64_t div(uint64_t n){
    
     
    uint64_t m=pow(n,.5)+1;
    unordered_set<uint64_t> v;
    for (uint64_t i =1;i<m;i++){
        if(n%i==0){
            v.insert(i);
            uint64_t a=n/i;
            v.insert(a);
        }
    }
    uint64_t t=0;
    unordered_set<uint64_t>::iterator S;
    for (S=v.begin();S!=v.end();++S){
        t+=(*S)*(*S);
        
    }
    return t;
    
}
 
 
int main(int argc, const char * argv[]){
    
    clock_t r=clock();
    
    clock_t s =clock()-r;
    cout<<"this took "<<((float) s)/CLOCKS_PER_SEC<<endl;
    uint64_t N=64000000;
    uint64_t total=0;
    
    for(uint64_t i=1;i<N+1;i++){
        
        uint64_t m=div(i);
        if(i%100000==0){
            cout<<i<<" ................ ";
            clock_t s =clock()-r;
            cout<<"this took "<<((float) s)/CLOCKS_PER_SEC<<endl;
            r=clock();
        }
        uint64_t b= pow(m,.5);
        if(pow(int(b),2)==m){
            total+=i;
            cout<<i<<"...."<<total<<endl;
        }
    }
    cout<<"Final answer is :"<<total<<endl;
 
    
    
      // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

