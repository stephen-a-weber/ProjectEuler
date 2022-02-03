//
//  main.cpp
//  Lychrel numbers euler 55
//
//  Created by Stephen Weber on 1/29/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
 

using namespace std;

  
bool Pal(string palindrome){
     
    uint64_t length=   palindrome.size();
    string reversed="";
    string forward="";
     
    
    uint64_t yes=length/2;
    
    for(uint64_t i=0;i<yes;i++){
        forward+=palindrome[i];
    }
    for(uint64_t i=length-1;i>=length-yes;i--){
        reversed+=palindrome[i];
    }
    if (forward==reversed){
        return true;
    }
    else {return false;}
    
    
};
int maxlength=0;
string adding(string number){
    string theString;
    uint64_t what=std::atoi(number.c_str());
     
    uint64_t length=number.size();
    if (length>maxlength) {
        maxlength=length;
        cout<<maxlength<<endl;
    }
    string reversed;
    for (uint64_t i=0;i<length;i++){
        reversed+=number[length-i-1];
    }
    
    uint64_t where=atoi(reversed.c_str());
    uint64_t when =what+where;
    
    theString=to_string(when);
    
     
    return theString;
}



int main(int argc, const char * argv[])
{
    vector<string> finals;
    uint64_t range=10000;
    for (uint64_t i =2;i<range;i++) {
        string palindrome=to_string(i);
        for (uint64_t j=0;j<51;j++) {
            
            if (Pal(palindrome)){
                 
                break;
            }
            else {
                
                palindrome=adding(palindrome);
            }
             
            if (j==50) {
                finals.push_back(palindrome); 
            }
            
            
        }
        
        
    }
    
    cout<<"The number is at "<<finals.size() <<endl;
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

