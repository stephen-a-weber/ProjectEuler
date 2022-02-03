//
//  main.cpp
//  cuboid_route_problem86
//
//  Created by Stephen Weber on 2/7/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//
/*
 A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.... nope no diagram here...
 
 
 However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.
 
 By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest route has integer length when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.
 
 Find the least value of M such that the number of solutions first exceeds one million.
 
 three routs
 
 sqrt(   6**2 + (5+3)**2  ) = 10
 sqrt(   3**2 + (6+3)**2) ) = ??
 sqrt(   5**2 + (5+6)**2) ) = ??
 
 
*/
#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;
bool check(int n, int m, int p) {
    float ans1= sqrt(n*n+(m+p)*(m+p));
     
    float ans2= sqrt(m*m+(n+p)*(n+p));
         float ans3= sqrt(p*p+(m+n)*(m+n));
     
       if (ans1<=ans2 and ans1<=ans3){
        if (ans1==float(int(ans1))) {
            //cout<<"one"<<endl;
            //cout <<ans1<<"   "<<float(int(ans1))<<endl;
            //cout<<endl<<endl;

            return true;
        
        }
        else {
            return false;
        }
    }
    if (ans2<=ans1 and ans2<=ans3){
        if (ans2==float(int(ans2))) {
            //cout<<"two"<<endl;
            //cout <<ans2<<"   "<<float(int(ans2))<<endl;
            //cout<<endl<<endl;

            return true;
            
        }
        else {
            return false;
        }
    }
    if (ans3<=ans2 and ans3<=ans3){
        if (ans3==float(int(ans3))) {
            //cout<<"three"<<endl;
            //cout <<ans3<<"   "<<float(int(ans3))<<endl;
            //cout<<endl<<endl;

            return true;
            
        }
        else {
            return false;
        }
    }
    
     
    
};
int main(int argc, const char * argv[])
{   clock_t rtime=clock();
    int M,total;
    //cout <<check(3,5,6)<<endl;
    for (M=1817;M<=2000;M+=1){
        total=0;
    int m,n,p;
    for (m=1;m<=M;m++) {
        for (n=m;n<=M;n++) {
            for (p=n;p<=M;p++) {
                
                if (check(m,n,p)){
                    total+=1;
                     
                }
                
                
                
                
            }// end of p
            
            
        }// end of n
        
        
    }// end of m
        cout<<M<<"    "<<total<<endl;
        clock_t rtimer=clock()-rtime;
        cout<<"THIS TOOK "<<((float)rtimer)/CLOCKS_PER_SEC<<endl;
    }// end of M
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

