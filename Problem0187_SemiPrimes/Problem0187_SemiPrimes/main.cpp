/*
 Semiprimes
 Problem 187
 A composite is a number containing at least two prime factors. For example, 15 = 3  5; 9 = 3  3; 12 = 2  2  3.
 
 There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
 
 How many composite integers, n  108, have precisely two, not necessarily distinct, prime factors?
 
 
 Answer:
 17427258
 Completed on Sun, 17 Mar 2013, 21:49

 */

#include <iostream>
#include <set>
#include <vector>
#include <ctime>
#include <map>
using namespace std;


int main(int argc, const char * argv[])
{  
 
clock_t r=clock();
 
 
uint64_t n =100000000;
set<uint64_t> nonprimes;
vector<uint64_t> primes;
vector <bool> sieve(n ,true);
primes.push_back(2);
for (uint64_t i =4;i <=n ;i+=2) {
    sieve[i]=false;
    
}
for (uint64_t i =3;i<=n ;i++) {
    
    if (sieve[i]==true) {
        
            primes.push_back(i);
       
        for (uint64_t j=i*i;j<=n ;j+=i){
            
            sieve[j]=false;
        }
    }
    
}
    cout<<"Primes finished"<<endl;
    uint64_t please=0;
    uint64_t m=0;
    uint64_t i =primes.size();
    for (uint64_t j=0;j<i;j++){
        
        please=100000000/primes[j];
        
        for(uint64_t k =j;k<i;k++){
            
            if(primes[k]<=please){
                m=m+1;
            }
            else {
                break;
            }
            
        }
    }
    cout<<m<<endl;
 


clock_t s =clock()-r;
cout<<"this took "<<((float) s)/CLOCKS_PER_SEC<<endl;

// insert code here...
std::cout << "Hello, World!\n";
return 0;
}

