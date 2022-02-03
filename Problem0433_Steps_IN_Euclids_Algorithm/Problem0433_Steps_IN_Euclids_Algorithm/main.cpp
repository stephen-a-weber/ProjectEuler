//
//  main.cpp
//  Problem0433_Steps_IN_Euclids_Algorithm
//
//  Created by Isadmin on 8/13/13.
//  Copyright (c) 2013 Isadmin. All rights reserved.
//
/*
 The answer is 326624372659664 took 280961
 Hello, World!
 Steps in Euclid's algorithm
 Problem 433
 Let E(x0, y0) be the number of steps it takes to determine the greatest common divisor of x0 and y0 with Euclid's algorithm. More formally:
 x1 = y0, y1 = x0 mod y0
 xn = yn-1, yn = xn-1 mod yn-1
 E(x0, y0) is the smallest n such that yn = 0.
 
 We have E(1,1) = 1, E(10,6) = 3 and E(6,10) = 4.
 
 Define S(N) as the sum of E(x,y) for 1 ≤ x,y ≤ N.
 We have S(1) = 1, S(10) = 221 and S(100) = 39826.
 
 Find S(5·106).
 
 
 Answer:
 326624372659664
 Completed on Fri, 23 Aug 2013, 05:46

 
 */
#include <ctime>

#include <iostream>
using namespace std;
int64_t flask=5000000;
int64_t total=0;
int64_t i=0;

 
void got(int64_t a , int64_t b, int64_t step){
    
    int64_t c=0;
    
    int64_t h=flask/a;
     
    
    total += step*h;
    
    
    
    
    
    
    for (int64_t x=1;x<=h;x++) {
        
        c=x*a+b;
        if (c>flask){
            break;
        }
        else {
            
            if ((c+a)>flask) {
                total+=(step+1);
            }
            else {
        
               got(c,a,step+1);
            }
        
        }
    }
    
    return;
    
}
int main(int argc, const char * argv[])
{flask=5000000;
    
    
    clock_t r=clock();
    for (i=2;i<=flask;i++){
    
    got(i,1,1);
        
    }
    int64_t solution=total*2+(flask*(flask-1)/2)+flask;
    clock_t s =clock()-r;
    cout<<"The answer is "<<solution<<" took "<<((float) s)/CLOCKS_PER_SEC<<endl;
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
// 166202 secs ---- 46.17 hours
    // 314123870344656
}

/*
int flask=5000000;
int64_t total=0;
void got(int a , int b, int step){
 
 
    int h=1;
    if (a!=1) {
        h=flask/a;
    }
 
    total += step*h;
 
 
    int m=1;
 
    if (b==0) {
        m=2;
    }
 
    
    
    for (int x=m;x<=flask;x++) {
        
        int f=x*a+b;
        if (f>flask){
            break;
        }
        
        got(f,a,step+1);
        
    }
    
    return;
    
}
int main(int argc, const char * argv[])
{flask=5000000;
     
         
    clock_t r=clock();
    
    
    
    got(1,0,0);
    int64_t solution=total*2+(flask*(flask-1)/2)+flask;
    clock_t s =clock()-r;
    cout<<"The answer is "<<solution<<" took "<<((float) s)/CLOCKS_PER_SEC<<endl;
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

//295161 seconds or 81.9892 hours
*/

