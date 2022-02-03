//
//  main.cpp
//  arrange_probability problem 100
//
//  Created by Isadmin on 2/20/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//
/*
 If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)(14/20) = 1/2.
 
 The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
 
 By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
*/
#include <cmath>
#include <iostream>
#include "/usr/local/Cellar/gmp/5.0.5/include/gmp.h"
using namespace  std;

// My first go with gmp !!!
// So ignore my convoluted method for my equations...
// way better solutions then python numpy

//Best solutioin is seeing it can be a pell equaiion
//diophantine equation....


int main(int argc, const char * argv[])
{//     1004670312710
    //uint64_t A=1000044557551;
    //uint64_t B=0;
   // uint64_t x=0;
    mpz_t A;
    mpz_t B;
    mpz_t C;
    mpz_t Q;
    mpz_t R;
    int count=1;
    unsigned long int g=2;
    unsigned long int eight=8;
    mpz_t ten;
    mpz_init(ten);
    mpz_set_ui(ten,10);
    mpz_t two;
    mpz_init(two);
    mpz_set_ui(two,2);
    mpz_t one;
    mpz_init(one);
    mpz_set_ui(one,1);
    mpz_init(Q);
    mpz_init(R);
    mpz_init(C);
    mpz_t D;
    mpz_init(D);
    mpz_init(A);
    mpz_init(B);
    mpz_set_ui(A,2);
    mpz_t Y;
    mpz_init(Y);
    mpz_t chain;
    mpz_init(chain);
    mpz_set_ui(chain,1);
    mpz_t v;
    mpz_init(v);
    mpz_t fr;
    mpz_init(fr);
    mpz_t four;
    mpz_init(four);
    mpz_set_ui(four,4);
    bool cat=true;
    while (cat) {
        
        mpz_set(Y,A);
         //gmp_printf ("%s  A is an mpz %Zd\n", "here", A);
         //gmp_printf ("%s Y is an mpz %Zd\n", "here",Y);
        mpz_pow_ui(Y,Y,g);
         //gmp_printf ("%s Y an mpz %Zd\n", "here", Y);
        mpz_mul(D,two,Y);
         //gmp_printf ("%s D is an mpz %Zd\n", "here", D);
        mpz_set(C,A);
        //gmp_printf("%s C is an mpz %Zd\n", "here", C);
        mpz_mul(C,two,C);
         //gmp_printf("%s C is an mpz %Zd\n", "here", C);
        mpz_sub(C,D,C);
       //  gmp_printf("%s C is an mpz %Zd\n", "here", C);
        
        mpz_add(C,C,one);
         //gmp_printf ("%s C an mpz %Zd\n", "here", C);
        mpz_set(Y,C);
        //gmp_printf ("%s Y an mpz %Zd\n", "here", Y);
        //C=2*pow(A,2)-2*A+1;
        //cout <<B<<endl;
        mpz_sqrtrem(Y,R,Y);
        if (mpz_sgn(R)!=0) {
            mpz_add(A,A,one);
            count+=1;
            if (count%100000000==0){
                gmp_printf ("%s  A is at %Zd\n", "here", A);
            }
        }
        else{
        //gm/p_printf ("%s Y an mpz %Zd\n", "here", Y);
        
        mpz_add(Y,Y,one);
         //gmp_printf ("%s Y an mpz %Zd\n", "here", Y);
        mpz_tdiv_qr(D,R,Y,two);
        //gmp_printf ("%s D is an mpz %Zd\n", "here", D);
     //   gmp_printf ("%s R is an mpz %Zd\n", "here", R);

        mpz_set(R,D);
            mpz_mul(D,D,two);
       // gmp_printf ("%s D is an mpz %Zd\n", "here", D);

            mpz_sub(D,D,one);
        //gmp_printf ("%s D is an mpz %Zd\n", "here", D);

            mpz_pow_ui(D,D,g);
        //gmp_printf ("%s  D is an mpz %Zd\n", "here", D);
        //gmp_printf ("%s  C is an mpz %Zd\n", "here", C);
            if (mpz_cmp(D,C)==0) {
                
                cout<<"found one"<<endl;
                   gmp_printf ("%s Number of Blue %Zd\n", "here", R);
                 gmp_printf ("%s Number in Set %Zd\n", "here", A);
              
                cout<<"_______________________"<<endl;
                mpz_pow_ui(Y,C,g);
                mpz_tdiv_qr(v,R,Y,chain);
                mpz_set(chain,C);
                mpz_mul_ui(Y,v,eight);
                mpz_sub_ui(Y,Y,g);
                
                 mpz_sub_ui(Y,Y,g);
                mpz_sqrt(Y,Y);
                mpz_add_ui(Y,Y,g);
                mpz_tdiv_qr(A,R,Y,four);
                
               
                
               
                             
            }
            else {
                 mpz_add(A,A,one);
              
            }
        }
        }
        /*
        Q=int((pow(C,.5)+1)/2.0);
        if (pow((Q*2-1),2)==C) {
            cout<<A<<"   "<<B<<endl;
            A=A+1;
        }
        else {
            
            A=A+1;
            if (A%(10000000)==0){
                cout<<"NOW  "<<A<<"   "<<B<<endl;
            }
        }
        */
        
        
        
        
        
        
   
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

