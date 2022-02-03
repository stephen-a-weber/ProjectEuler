//
//  main.cpp
//  pentagon_numbers_euler_44
//
//  Created by Isadmin on 1/27/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//

#include <iostream>
#include <set>
#include <utility>
using namespace std;
int main(int argc, const char * argv[])
{
    set<uint64_t> triangle;
    set<uint64_t> pentagon;
    set<uint64_t> hexagon;
        uint64_t number=1000000;
    
    for (uint64_t i =1;i<=number;i++){
        pentagon.insert(i*(3*i-1)/2);
        triangle.insert(i*(i+1)/2);
        hexagon.insert(i*(2*i-1));
        
    }
    set<uint64_t>::iterator it1;
   
    
    
    for (it1=triangle.begin();it1!=triangle.end();it1++){
        
        
            
            if (pentagon.find(*it1)!=pentagon.end()){
                
                if (hexagon.find(*it1)!=hexagon.end()){
                    
                    cout <<*it1 <<endl;
                   
                }
           
            
            
            
        }
        
        
        
        
    }
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

