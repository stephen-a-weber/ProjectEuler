/*
 Consecutive positive divisors
 Problem 179
 Find the number of integers 1  n  107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
 
 
 Answer:
 986262
 Completed on Sat, 16 Mar 2013, 02:51
*/
#include <iostream>
#include <vector>
#include <map>
#include <utility>
using namespace std;

int main(int argc, const char * argv[])
{
    map <int,vector <int> > numbers;
    pair <int, vector <int> > go;
  
    int n=10000000;
    vector <int> handle;
    handle.push_back(1);
    
    for (int i =1;i<n;i++){
        numbers[i]= handle;
        
    }
    
    for (int i=2;i<n;i++){
        
        numbers[i].push_back(i);
        for (int j=i+i;j<n;j+=i){
            
            numbers[j].push_back(i);
            
            
        }
        
        
    }
    int x=0;
    for (int i=2;i<n-1;i++){
        
        if ( numbers[i].size()==numbers[i+1].size()){
            
            x=x+1;
        }
        
    }
    cout<<"The answer is "<<x<<endl;
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

