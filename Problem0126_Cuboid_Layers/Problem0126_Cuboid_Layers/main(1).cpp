/*
 Cuboid layers
 Problem 126
 The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.
 
 
 If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.
 
 However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.
 
 We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.
 
 It turns out that 154 is the least value of n for which C(n) = 10.
 
 Find the least value of n for which C(n) = 1000.
 
 
 Answer:
 18522
 Completed on Sun, 24 Mar 2013, 00:09
*/

#include <iostream>
#include <set>
#include <vector>
#include <map>
using namespace std;

void printIt(set <uint64_t> &bird) {
    set<uint64_t>::iterator s;
    
    for (s=bird.begin();s!=bird.end();++s) {
        
        cout<<"   "<<*s;
    }
    cout<<"   the end"<<endl;
        return;
    
    
}


int main(int argc, const char * argv[])
{
    map<uint64_t,uint64_t> tree;
    set<uint64_t> swallow;
    uint64_t t=0;
    uint64_t re=0;
    uint64_t dd=0;
    set<uint64_t>::iterator sit;
    uint64_t minS=20000;
    uint64_t ConstantMin=minS;
    for (uint64_t k=2; k<5000;k++){
         uint64_t g=4*k*k-20*k+24;
         uint64_t h=4*k-8;
        
        if (g>minS) {
            cout<<"Stopping"<<endl;
            set<uint64_t>::iterator s;
            
            for (s=swallow.begin();s!=swallow.end();++s) {
                
                if (tree[(*s)]==1000){
                    cout<<"AMAZING  "<<(*s)<<endl;
                }
                else {
                    
                    cout<<"This "<<(*s)<<"="<<tree[(*s)]<<endl;
                }
            }


//printIt(swallow);
            break;
        }
        
        for (uint64_t x=1; x<ConstantMin;x++){
            
              t =g+h*x;
            if (t>minS) {
                break;
            }
           
            
            for (uint64_t y=1;y<=x;y++) {
                 
                
                re=t+h*y+2*x*y;
                
                if (re>minS) {
                    break;
                    
                }
                              for (uint64_t z=1;z<=y;z++) {
                    
                    dd=re+h*z+2*(x*z+y*z);
                     //cout<<x<<" "<<y<<" "<<z<<" "<<t<<endl;
                    if (dd>minS) {
                        break;
                    }
                   
                    
                    if (tree.count(dd)>0) {
                        // cout<<tree[154]<<"  ";
                        tree[dd]++;
                       // cout<<tree[t]<<endl;
                        if (tree[dd]==1000){
                           // cout<<t<<endl;
                            swallow.insert(dd);
                                                }
                       
                        if (tree[dd]>1000){
                            swallow.erase(dd);
                        
                        }
                        
                        
                        
                        
                    }
                    else {
                        tree[dd]=1;
                    }
                    
                    
                }
                
                
            
        
    }
            
        }
        
    }
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

