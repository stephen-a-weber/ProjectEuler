/*
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
6857
Completed on Mon, 21 Jan 2013, 23:53
*/




#include <iostream>
#include <vector>
using namespace std;

void factor(uint64_t n,   vector<int> &primes){
uint64_t solution=0;
vector<int>::iterator vit;
vit=primes.begin();
 while (n!=1){
    solution=*vit;
    if (n%(*vit)==0) {
        n=n/(*vit);}
     // cout<<*vit<<endl;


    if (vit==primes.end()){
        cout<<"Need a greater Prime List"<<endl;
        return;
    }
    vit+=1;
 }
 cout<<"The Answer is "<<solution<<endl;
}

void make_primes(int total,  vector <int> &primes,   vector <bool> &sieve) {

   for (int i=4;i<total;i+=2){
    sieve[i]=false;
   }
   for (int i =3;i<total;i+=2){
    if (sieve[i]==true) {
//cout<<"prime "<<i<<endl;
        primes.push_back(i);
        for (int j=i*i;j<total;j+=i) {
            sieve[j]=false;
        }
    }
   }



                 }

int main()
{   int numberOfPrimes=7000;
uint64_t gear=600851475143;
cout<<"STARTING NUMBER IS "<<gear<<endl;
    vector<bool> sieve(numberOfPrimes,true);
    vector<int> primes( 1,2);

    make_primes(numberOfPrimes,primes,sieve);
    factor(600851475143,primes);



    return 0;
}
