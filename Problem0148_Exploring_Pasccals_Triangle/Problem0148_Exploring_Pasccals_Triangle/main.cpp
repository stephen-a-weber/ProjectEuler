/*
 Exploring Pascal's triangle.
 Problem 148
 We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:
 
 1
 1	 	 1
 1	 	 2	 	 1
 1	 	 3	 	 3	 	 1
 1	 	 4	 	 6	 	 4	 	 1
 1	 	 5	 	10	 	10	 	 5	 	 1
 1	 	 6	 	15	 	20	 	15	 	 6	 	 1
 However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.
 
 Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.
 
 
 Answer:
 2129970655314432
 Completed on Wed, 15 May 2013, 16:28

 */
//
//  main.cpp
//  Problem0148_Exploring_Pasccals_Triangle
//
//  Created by Isadmin on 5/15/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
int main(int argc, const char * argv[])
{   vector<int>aa={1,7,49,343,2401,16807,117649,823543,5764801,40353607,282475249};
    uint64_t count=0;
    uint64_t total=0;
    uint64_t dist=0;
    uint64_t carry=1;
    uint64_t N=0;
    uint64_t a=0;
    uint64_t r=0;
    uint64_t n=0;
    uint64_t t=0;
    uint64_t Final=1000000000;
    while (N<Final-1){
        if (N%10000000==0) {
            cout<<N<<endl;
        }
        N+=1;
        carry=1;
        count=0;
        dist=N;
        for (int i=10;i>0;i=i-1){
            a=aa[i];
            r=dist%a;
            n=(dist-r)/a;
            t=a-1-r;
            count+=carry*n*t;
            carry*=(n+1);
            dist=r;
        
            
        }
        total+=count;
    }
    
    uint64_t b=0;
    b=Final*(Final+1)/2;
    b=b-total;
    cout<<"THE ANSWER IS "<<b<<endl;
    
    
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

