/*
 Large repunit factors
 Problem 132
 A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.
 
 For example, R(10) = 1111111111 = 11412719091, and the sum of these prime factors is 9414.
 
 Find the sum of the first forty prime factors of R(109).
 
 
 Answer:
 843296
 Completed on Sat, 6 Apr 2013, 21:06
 
 */

//
//  main.cpp
//  Problem0132_Large_Repunit_Factors
//
//  Created by Isadmin on 4/6/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//
#include <cmath>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

bool divide(uint64_t n,int R){
    int place=1;
    int value=0;
    set <int> shop;
    //cout<<"trial "<<shop.size()<< "  "<<n<<endl;
    while(place<=R){
                value=value*10+1;
        value=value%n;
        if (value==0) {
            if(R%(shop.size()+1)==0){
                return true;
            }
            else{return false;}

        }
       if (shop.size()>100000){return false;}
                if (shop.count(value)==1){return false;}
        shop.insert(value);
        place+=1;
        
        
        
    }//end while
    if (value==0){
        return true;
        
    }
    else {
    return false;
    }
}


int main(int argc, const char * argv[])
{
     
     
    uint64_t n =162252;
    // set<uint64_t> nonprimes;
    vector<uint64_t> primes;
    vector <bool> sieve(n ,true);
    
    
    for (uint64_t i =3;i<=n ;i=i+2) {
        
        if (sieve[i]==true and i!=5) {
            
            primes.push_back(i);
            
            for (uint64_t j=i*i;j<=n ;j+=i){
                
                sieve[j]=false;
            }
        }
        
    }
    cout<<"Primes finished"<<endl;
    int qwerty=pow(10,9);
    int count=35;
    uint64_t total=398135;
    vector<uint64_t>::iterator pt;
    
    for (pt=primes.begin();pt!=primes.end();++pt){
       // if ((*pt)<60102){continue;}
         
         
        if (divide((*pt),qwerty) ) {
            count+=1;
            cout<<count<<"   "<<(*pt)<<endl;
            
            total+=(*pt);
            bool poll=true;
            int mmm=1;
            while (poll){
                mmm+=1;
            uint64_t k=pow((*pt),mmm);
            if (divide(k,qwerty) ) {
                count+=1;
                cout<<count<<"   "<<(*pt)<<"   OPPS MORE"<<endl;
                
                total+=(*pt);
            }
            else {
                cout<<"_____________________"<<total<<endl;
                poll=false;
            }
            }
            if (count==40){
                cout<<"THE WINNING NUMBER IS "<<total<<endl;
                break;
            }
             
        }
        
    }//end for

    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

