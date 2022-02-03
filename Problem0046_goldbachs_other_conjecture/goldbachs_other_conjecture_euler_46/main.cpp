//
//  main.cpp
//  goldbachs_other_conjecture_euler_46
//
//  Created by Isadmin on 1/27/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//

#include <iostream>
#include <set>
#include <vector>
#include <ctime>
using namespace std;


int main(int argc, const char * argv[])
{
    clock_t r;
    r=clock();
    uint64_t onum=9;
    uint64_t number=10000;
    set<uint64_t> nonprimes;
    set<uint64_t> primes;
    vector <bool> sieve(number,true);
    primes.insert(2);
    for (uint64_t i =4;i <=number;i+=2) {
        sieve[i]=false;
    
    }
    for (uint64_t i =3;i<=number;i++) {
        
        if (sieve[i]==true) {
            primes.insert(i);
            for (uint64_t j=i*i;j<=number;j+=i){
                
                sieve[j]=false;
            }
        }
        
    }
    
    for (uint64_t i=9;i<=number;i+=2){
        
        if (primes.find(i)==primes.end()) {
            if (i>onum) {
                nonprimes.insert(i);}
            
        }
    }
    
   // nonprimes.insert(80);
    
    bool rabbit=true;
    
    set<uint64_t>::iterator it;
    set<uint64_t>::iterator pit;
     
    for (it=nonprimes.begin();it!=nonprimes.end();it++){
         bool cat=true;
        bool dog=true;
        for (pit=primes.begin();pit!=primes.end();pit++) {
            
            
            if (cat==false){break;}
            for (uint64_t i =1;i<=number;i++){
                
                uint64_t h;
                
                h=*pit+2*i*i;
                if ( h>*it) {break;}
                if (h==*it) {cat=false;dog=false;
                    if (*it==80){rabbit=false;}
                  //  cout<<*it<<"     "<<*pit<<" ---"<<i<<endl;
                    break;}
                
                
                
            }
            
                    }
        
        if (dog==true){
        
        cout <<*it<<endl;
        break;
        
        }
    }
    
    clock_t s;
    s=clock()-r;
    cout<<"this took "<<((float) s)/CLOCKS_PER_SEC<<endl;

    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

