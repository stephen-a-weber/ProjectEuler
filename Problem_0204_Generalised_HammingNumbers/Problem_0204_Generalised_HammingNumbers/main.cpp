/*
 Generalised Hamming Numbers
 Problem 204
 A Hamming number is a positive number which has no prime factor larger than 5.
 So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
 There are 1105 Hamming numbers not exceeding 108.
 
 We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
 Hence the Hamming numbers are the generalised Hamming numbers of type 5.
 
 How many generalised Hamming numbers of type 100 are there which don't exceed 109?
 
 
 Answer:
 2944730
 Completed on Tue, 19 Mar 2013, 00:28

 */
 
#include <vector>
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;
int main(int argc, const char * argv[])
{    
    time_t start=clock();
     
    const uint64_t n=1000000000;
    int x=100;
    //bitset<n> sieve;
    vector<bool> sieve(n,true);
    vector<bool> Formula(n,true);
    //sieve.set();
    
     
 
    for (uint64_t i=2;i<n;i++){
        
        if (i<=x) {
        
                  if (sieve[i]==true) {
             
            
                  
            
            for (uint64_t j=i*i ;j<n;j+=i) {
                                
                sieve[j]=false;
            }
            
        }
        }
        else {
            
            
            if (sieve[i]==true) {
                
                
                
                
                for (uint64_t j=i ;j<n;j+=i) {
                
                    
                    sieve[j]=false;
                    Formula[j]=false;
                }
                
            }

            
            
            
            
            
        }
        
    }
        uint64_t count=1;
    
    for (int u=1; u<Formula.size();u++){
        if (Formula[u]) {
            count+=1;
           // cout<<u<<endl;
        }
    
        
    }
        
   
     cout<<"The number of generalized Hamming Numbers(100)  is "<<count<<endl;
    time_t end=clock()-start;
    cout<<"This took "<<((float)end)/CLOCKS_PER_SEC<<endl;
    // insert code here...
    
    return 0;
}

