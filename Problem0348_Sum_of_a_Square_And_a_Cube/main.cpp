#include <iostream>
#include <sstream>
#include <map>
#include <cmath>
using namespace std;
bool test(uint64_t n){
  string g ;
  ostringstream convert;
  convert <<n;
  g=convert.str();
  int h=0;
  int k=g.size();
  for (int i=0;i<k/2;i++){
    h=k-i-1;
    if (g[i]!=g[h]){
        return false;
    }

  }
return true;
}

bool t(uint64_t n){
int g=0;
uint64_t k=n;
while (k!=0){
    k/=10;
    g+=1;
}

for (int i =0;i<g/2;i++){

    uint64_t top=n;
    uint64_t bottom=n;

    for (int ii=0;ii<i ;ii++){
       top/=10;
    }
    top=top%10;
    for (int ii=0;ii<g-i-1;ii++){
        bottom/=10;
    }
    bottom=bottom%10;








   // cout<<n<<".."<<i<<":  "<<v<<"  :  "<<y<<"  :  "<<z<<"  :  "<<top<<"   :  "<<bottom<<endl;
    if (top!=bottom){
        return false;
    }

}
return true;

}
int main()

{

   // cout<<"WHAT IS THIS "<<t(1234321)<<endl;
     uint64_t a;
    map<uint64_t,int> the;
    map<uint64_t,int>::iterator it;

    for (uint64_t s=1; s<8000000 ;s++){
      if (s%10000==0){
        cout<<s<<endl;
      }
        for (uint64_t c=1;c<100000 ;c++){

              a=s*s+c*c*c;
              if (a>100000000000){
                break;
              }
              if (t(a)==true){
                    if (the.count(a)==0){
                        the[a]=1;
                    }
                    else{
                the[a]+=1;}
              }


        }
    }


 // cout<<t(5229225)<<endl;
 // cout<<test(5229225)<<endl;
//cout<<t(14531)<<endl;
cout<<endl<<endl<<endl;
    for(it=the.begin(); it!=the.end();++it){

        if (it->second==4){
            cout<<"here is one "<<it->first<<" : "<<it->second<<endl;
        }

    //    cout<<it->first<<"   "<<it->second<<endl;
    }

     cout << "Hello world!" << endl;
    return 0;
}
