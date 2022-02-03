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
    set<int> formula;
    typedef pair<int,int> pentagonal;
    int number=10000;
    
    for (int i =1;i<=number;i++){
        formula.insert(i*(3*i-1)/2);
        
    }
    set<int>::iterator it1;
    set<int>::iterator it2;
    
    
    for (it1=formula.begin();it1!=formula.end();it1++){
        
        for (it2=it1;it2!=formula.end();it2++){
            
            int y =*it2-*it1;
            int z =*it2+*it1;
            
            if (formula.find(y)!=formula.end()){
                
                if (formula.find(z)!=formula.end()){
                    
                    cout <<*it1<<"   "<<*it2<<endl;
                    cout<<*it2-*it1<<endl;
                }
            }
            
            
            
        }
        
        
        
        
    }
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

