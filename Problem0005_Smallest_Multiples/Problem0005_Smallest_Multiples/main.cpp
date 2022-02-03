//
//  main.cpp
//  Problem0005_Smallest_Multiples
//
//  Created by Stephen Weber on 3/5/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//
/*
 Smallest multiple
 Problem 5
 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 
 What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 
 
 Answer:
 232792560
 Completed on Tue, 22 Jan 2013, 03:07

*/


#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <math.h>
using namespace std;
int main(int argc, const char * argv[])
{
    typedef vector<int> facts;
    facts::iterator III;
    map <int, vector<int> > factors;
    map <int, int >::iterator IT;
    map <int, int> terms;
    map <int, vector<int> >::iterator mit;
    long maxNumber=0;
    
    
    for (int n=2; n<21;n++){
         factors[n]=facts();
        int value =n;
        
        for (int y =2;y<n+1;y++){
            
            while (value%y==0) {
                value/=y;
                factors[n].push_back(y);
            }
        }
    }
    /*
    
    for (long n=2;n<21;n++){
        
        cout<<n<<" : ";
        for (III=factors[n].begin();III!=factors[n].end();III++) {
            cout <<"  "<<(*III);
        }
        cout<<endl;
    }
   */
    
    for (int i =2;i<21;i++){
        maxNumber=0;
        for (int j =2;j<21;j++){
            
             vector <int > frog=factors[j];
               
              long baby;
            
               baby=count(frog.begin(),frog.end(),i);
                
            if (baby>maxNumber){
                maxNumber=baby;
            }
            
        }
        terms[i]=maxNumber;
        
            
        }
        
     
    
    int total=1;
    for (int t=2;t<21;t++){
        total=total* pow(t,terms[t]);
         
    }
        
         
        
    cout<<"THE ANSWER IS "<<total<<endl<<endl<<endl;
    
    
     
    cout<<endl<<endl<<endl;
    // insert code here...
    
    return 0;
}

