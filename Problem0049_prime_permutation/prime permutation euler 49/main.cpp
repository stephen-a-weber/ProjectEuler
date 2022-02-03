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
{ int a=0;
    int b=0;
    
    cin>>a>>b;
    cout<<a+b<<endl;
    return 0;
}
    clock_t r;
    r=clock();
    uint64_t onum=2;
    uint64_t number=10000;
    set<uint64_t> nonprimes;
    set<uint64_t> primes;
    vector <bool> sieve(number,true);
    //primes.insert(2);
    for (uint64_t i =4;i <=number;i+=2) {
        sieve[i]=false;
        
    }
    for (uint64_t i =3;i<=number;i++) {
        
        if (sieve[i]==true) {
            if (i>999){
            primes.insert(i);
            }
            for (uint64_t j=i*i;j<=number;j+=i){
                
                sieve[j]=false;
            }
        }
        
    }
    set<uint64_t>::iterator  it;
    
    
   
    
    
    clock_t s;
    s=clock()-r;
    cout<<"this took "<<((float) s)/CLOCKS_PER_SEC<<endl;
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

