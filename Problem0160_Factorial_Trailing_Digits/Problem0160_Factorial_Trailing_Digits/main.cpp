//
//  main.cpp
//  Problem0160_Factorial_Trailing_Digits
//
//  Created by Isadmin on 6/3/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//

#include <iostream>
#include <cmath>
using namespace std;
int main(int argc, const char * argv[])
{
    uint64_t total=1;
    uint64_t  f=1000000000000;
    uint64_t g=0;
    uint64_t c=0;
      
    for (uint64_t t=1;t<=f;t++){
        g=t;
        while (g%5==0) {
            c+=1;
            g/=5;}
        while (c>0){
            if (g%2==0){
                g/=2;
                c=c-1;
            }
            else{break;}
        }
        total*=g;
       
        total=total%1000000;
        if (t%100000000==0){
            cout<<t<<"  "<<total%100000 <<"  c:  "<<c<<endl;
        }
    }
    cout<<"the answer is "<<total%100000<<"  c:  "<<c<<endl;
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
/*
 999800000000  93536
 999900000000  45152
 1000000000000  96768
 the answer is80896768
 Hello, World!
*/
