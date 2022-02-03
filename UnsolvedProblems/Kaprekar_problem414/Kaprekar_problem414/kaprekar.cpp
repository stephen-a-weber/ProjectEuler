//
//  kaprekar.cpp
//  Kaprekar_problem414
//
//  Created by Stephen Weber on 2/11/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//

#include "kaprekar.h"

kaprekar::kaprekar()
{
    
    vector<uint64_t> CB(0,5);
    vector<uint64_t> number(0,5);
    vector<uint64_t> check(0,5);
    vector<uint64_t> rnumber(0,5);
    vector<uint64_t> diff(0,5);
    vector<uint64_t>last(0,5);
    SBofI=0;
    SUMofB=0;
    cbValue=false;
    init();
    
}

kaprekar::~kaprekar()
{
    
    
}


void kaprekar::init(){
    
 
CB={0,0,0,0,0};
number= {0,0,0,0,0};
check={0,0,0,0,0};
rnumber={0,0,0,0,0};
diff={0,0,0,0,0};
last={0,0,0,0,0};
}
 



void kaprekar::fill_number(uint64_t i, int base)
{
    //cout<<i<<endl;
    uint64_t m4=i/pow(base,4);
   //cout<<m4<<" should be zero"<<endl;
    number[0]=m4;
    i-=m4*pow(base,4);
    
    uint64_t m3=i/pow(base,3);
         number[1]=m3;
    i-=m3*pow(base,3);
    
    uint64_t m2=i/pow(base,2);
    number[2]=m2;
    i-=m2*pow(base,2);
    
    uint64_t m1=i/base;
    number[3]=m1;
    i-=m1*base;
    
    number[4]=i;
   // Print(number);
   // cout<<"_______________"<<endl;
    }
    

void kaprekar::reverse_number()
{
    
    for (int i=0;i<5;i++){
        
        rnumber[4-i]=check[i];
    }
    
    
}


void kaprekar::subtract_number(int base)
{
  //  Print(diff);
    
    
    for (int i=4;i>-1;i=i-1){
 
        
        if (rnumber[i]<=check[i]) {
            diff[i]=check[i]-rnumber[i];
            
        }
        else{
                
                 if (check[i-1]>0) {
                     check[i-1]-=1;
                     diff[i]=check[i]+base -rnumber[i];
                      }
                 else {
                     
                       if  ( check[i-2]>0) {
                
            
                           check[i-2]-=1;
                           check[i-1]+=base-1;
                           diff[i]=check[i]+base-rnumber[i];
                            
                       }
                       else {
                           if (check[i-3]>-0) {
                             
                               check[i-3]-=1;
                               check[i-2]+=base-1;
                               check[i-1]+=base-1;
                               diff[i]=check[i]+base-rnumber[i];
                                 
                           }
                    
                           else {
                               check[i-4]-=1;
                               check[i-3]+=base-1;
                               check[i-2]+=base-1;
                               check[i-1]+=base-1;
                               diff[i]=check[i]+base-rnumber[i];
                                
                           }
                       }
                 }
        }
                        
        
    }
    
  //  Print(diff);
  //  cout<<endl;
    
}

void kaprekar::Copy(vector<uint64_t> &a, vector<uint64_t> &b)
{
    for (int i=0;i<5;i++) {
        
        b[i]=a[i];
    }
    
}


bool kaprekar::Equal(vector<uint64_t> &a, vector<uint64_t> &b)
{
    for (int i =0;i<5;i++){
        if (a[i]!=b[i]){
            return false;
        }
        
    }
    return true;
    
}


void kaprekar::loop_through_bases()
{   
    
    for (int k=15;k<16;k++)
    {
        base=6*k+3;
        int total=pow(base,5);
        fill(CB.begin(),CB.end(),0);
        cbValue=false;
        
        for(uint64_t i =1;i<total;i++)
        {
            //cout<<"we are at "<<i<<endl;
            SBofI=0;
            fill_number(i,base);
            Copy(number,check);
            Copy(check,diff);
            fill(last.begin(),last.end(),0);
            if (Equal(number,CB)) {
                continue; //gives a zero value when i is CB
                
            }
            if (count(check.begin(),check.end(),check[0])==5) {
                cout<<"Found all digits the same"<<endl;
                continue; // gives a zero value when all digits are same
            }
            check_loop();// All the checks
            SUMofB+=SBofI;
            
            
        }
    }
    
    
    
}



void kaprekar::Print(vector<uint64_t> &h)
{
    for (it=h.begin();it!=h.end();it++) {
        
        cout<<"   "<<*it;
    }
    cout<<endl;
    return;
    
    
}



void kaprekar::check_loop()
{   while (true)
{
    //cout<<"Are we breaking yet?"<<endl;
    //Print(check);
    //cout<<"should change too"<<endl;
    Copy(diff,check);
    //Print (check);
    sort(check.begin(),check.end(),greater<int>());
    //cout<<"Should sort"<<endl;
    //Print(check);
    //cout<<"Don't forget to reverse.."<<endl;
    reverse_number();
    //Print(rnumber);
    subtract_number(base);
    //Print(diff);
    //cout<<"CHECKCHECKCHEKCHCKEC"<<endl<<endl;
    SBofI+=1;
    if (cbValue and Equal(diff,CB)) {
            break;
    
        }
    if (not Equal(diff,last)) {
            last=diff;
        //cout<<"JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ"<<endl;
        }
    else {
        //cout<<"AAAAAAAAAAAAAAAAA___________________AAAA_________________AAAAA"<<endl;
            if (cbValue==false) {
                SBofI-=1;
                //Print(check);
                //Print(CB);
                Copy(diff,CB);
                //cout<<"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"<<endl;
                //Print(check);
                Print(CB);
                
                //cout<<endl<<endl<<endl<<endl<<endl;
                cbValue=true;
                break;
            }
        }
        
    }
    
    
    
}
    
    
    
    
void kaprekar::run()
{
    loop_through_bases();
    cout<<"The answer is "<<SUMofB;
    cout<<endl<<endl;
}
 
 

