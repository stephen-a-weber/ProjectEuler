//
//  main.cpp
//  prime pair sets euler 60
//
//  Created by Stephen Weber on 1/30/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//
#include <set>
#include <vector>
#include <ctime>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>
#include <list>
 

using namespace std;
int main(int argc, const char * argv[])
{  clock_t r=clock();
    uint64_t n =100000000;
    
    set<uint64_t> primes;
    set<uint64_t>::iterator check1;
    set<uint64_t>::iterator check2;
    primes.insert(2);
    vector<bool> sieve(n,true);
    
    for (uint64_t i =4;i<n;i+=2){
        sieve[i]=false;
    }
    for (uint64_t i=3;i<n;i+=2) {
        if (sieve[i]==true) {
        primes.insert(i);
        for (uint64_t j=i*i;j<n;j+=i){
            sieve[j]=false;
        }
    }
    }
    clock_t dddd=clock()-r;
    cout<<"Primes :::THIS TOOK "<<((float)dddd)/CLOCKS_PER_SEC<<endl;

    map<uint64_t,set<uint64_t> > waste;
    
    set<uint64_t>::iterator it1;
    set<uint64_t>::iterator it2;
    
    for (it1=primes.begin();it1!=primes.end();it1++) {
        set<uint64_t> help;
        for (it2=primes.begin();it2!=primes.end();it2++) {
            if (*it1 !=*it2) {
                ostringstream a1;
                a1 << *it1;
                ostringstream a2;
                a2 << *it2;
                string aa  =a1.str()+a2.str();
                string bb = a2.str()+a1.str();
                 
                uint64_t zx=atoi(aa.c_str() );
                uint64_t xz=atoi( bb.c_str());
                //cout<<*it1<<"   "<<*it2<<"  "<<aa<<"   "<<bb<<"  "<<zx<<"  "<<xz<<endl;

                if (zx>n or xz>n) {
                    break;
                }
                check1=primes.find(zx);
                check2=primes.find(xz);
                bool cat=( check1!=primes.end());
                bool dog =(check2!=primes.end());
                if ( cat and dog) {
                     
                   // cout<<zx<<"  "<<cat<<"       "<<xz<<"   "<<dog<<endl;
                    if (primes.find(1)!=primes.end()){
                        cout<<"hamburger"<<endl;
                    }
                   // cout<<primes.size()<<endl;
                      help.insert(*it2);
                    
                   
                    
                }
                
            }
        }
        if (help.size()>4){
        waste[*it1]=help;
        }
    }
    
    cout<<waste.size()<<endl;
    map<uint64_t,set<uint64_t>> choices;
    map<uint64_t,set<uint64_t>>::iterator it;
    for (it=waste.begin();it!=waste.end();it++) {
        set<uint64_t>::iterator setit;
        set<uint64_t> hell;
        hell=it->second;
        vector<uint64_t> quasar;
        for (setit=hell.begin();setit!=hell.end();setit++) {
            if (waste.find(*setit)==waste.end()){
                quasar.push_back(*setit);
                             }
            
                             }
        vector<uint64_t>::iterator vit;
        for (vit=quasar.begin();vit!=quasar.end();vit++){
            hell.erase(*vit);
        }
        if (hell.size()>4) {
        choices[it->first]=hell;
        
        }
        
    }
   
    list<set <uint64_t> > koke;
    list<set <uint64_t> > babel;
    list<set <uint64_t> > camel;
    list<set <uint64_t> > fox;
    
    for (it=choices.begin();it!=choices.end();it++){
        
        for (it1=choices[it->first].begin();it1!=choices[it->first].end();it1++) {
            set<uint64_t> horse;
            horse.insert(it->first);
            horse.insert(*it1);
             
            koke.push_back(horse);
        }
    }
    uint64_t kokeNum[2];
    while (!koke.empty()) {
      //  cout<< "KOKE "<<"   "<<koke.size()<<endl;
        set<uint64_t> horse;
        
        set<uint64_t>::iterator horseIT;
         
        int h=0;
         
        horse=koke.back();
        koke.pop_back();
        for (horseIT=horse.begin();horseIT!=horse.end();horseIT++){
            kokeNum[h]=*horseIT;
          //  cout <<kokeNum[h]<<"  ";
            h+=1;
           // cout<<endl;
        }
        for (it1=choices[kokeNum[0]].begin();it1!=choices[kokeNum[0]].end();it1++) {
         
            if  (  choices[kokeNum[1]].find(*it1) !=choices[kokeNum[1]].end() ) {
                set<uint64_t> horse;
                for (int i =0;i<2;i++){
                    horse.insert(kokeNum[i]);
              //      cout<<kokeNum[i]<<"  ";
                                    }
                horse.insert(*it1);
              //  cout<<*it1<<endl;
                babel.push_back(horse);
                
            }
               
            
        }
        
        
    }
 uint64_t babelNum[3];
    
    while (!babel.empty()) {
       //  cout<< "babel "<<"   "<<babel.size()<<endl;
        
        set<uint64_t> horse;
        set<uint64_t>::iterator horseIT;
        
        
        int h=0;
        
        horse=babel.back();
        babel.pop_back();
        for (horseIT=horse.begin();horseIT!=horse.end();horseIT++){
            babelNum[h]=*horseIT;
          //   cout<<babelNum[h]<<" ";
            h+=1;
          //  cout<<endl;
        }
        for (it1=choices[babelNum[0]].begin();it1!=choices[babelNum[0]].end();it1++) {
            
            if  (  choices[babelNum[1]].find(*it1) !=choices[babelNum[1]].end()  and
                  choices[babelNum[2]].find(*it1) !=choices[babelNum[2]].end()  
                   
                 ) {
                //cout<<"Kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"<<endl;
                set<uint64_t> horse;
                for (int i =0;i<3;i++){
                    horse.insert(babelNum[i]);
     //               cout<<babelNum[i]<<"  ";
                }
                horse.insert(*it1);
               // cout<<*it1<<endl;
                camel.push_back(horse);
                          }
            
            
        }

        
        
        
        
        
        
        
        
        
        
    }
    
 
     uint64_t camelNum[4];
    
    while (!camel.empty()){
        
     //    cout<< "camel "<<"   "<<camel.size()<<endl;
        
        
        set<uint64_t> horse;
        set<uint64_t>::iterator horseIT;
        
        int h=0;
        
        horse=camel.back();
        camel.pop_back();
        for (horseIT=horse.begin();horseIT!=horse.end();horseIT++){
            camelNum[h]=*horseIT;
        //    cout<<camelNum[h]<<endl;
            h+=1;
            
        }
        for (it1=choices[camelNum[0]].begin();it1!=choices[camelNum[0]].end();it1++) {
            
            if  (  choices[camelNum[1]].find(*it1) !=choices[camelNum[1]].end()  and
                 choices[camelNum[2]].find(*it1) !=choices[camelNum[2]].end()   and
                 choices[camelNum[3]].find(*it1) !=choices[camelNum[3]].end()
                 ) {
                set<uint64_t> horse;
                cout<<"Kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"<<endl;
                for (int i =0;i<4;i++){
                    horse.insert(camelNum[i]);
                    cout<< camelNum[i]<<"   ";
                }
                horse.insert(*it1);
                cout<<*it1<<"   "<<endl;
                cout<<endl<<endl;
                fox.push_back(horse);
                
            }
            
            
        }
        
      
        
        
    } 
    
    cout<<" THE FINAL SIZE IS "<<fox.size()<<endl;
   
    
    /*
   
    set<uint64_t> great;
    set<uint64_t>::iterator it4;
        for (int i =0;i<n;i++){
            if (waste.find(i)!=waste.end()){
                great=waste[i];
           cout<<i<<"::::::";
            for(it4=great.begin();it4!=great.end();it4++){
             cout<<"  "<<*it4;
            
                    }
        cout<<endl;
            }
        }
    great.clear();
    cout<<endl<<endl<<endl;
    
    for (int i =0;i<n;i++){
        if (choices.find(i)!=choices.end()){
            great=choices[i];
            cout<<i<<"::::::";
            for(it4=great.begin();it4!=great.end();it4++){
                cout<<"  "<<*it4;
                
            }
            cout<<endl;
        }
    }
    */
  
    clock_t dd=clock()-r;
    cout<<"THIS TOOK "<<((float)dd)/CLOCKS_PER_SEC<<endl;
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

