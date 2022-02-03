#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector <vector <int> > Triplet;
vector <vector <int> >::iterator IT;
bool CreateTriplets(int &a, int &b, int &c)
{
    int k=1;
    int e=0;
    int f=0;
    int g=0;

        while ((e+f+g)<1000){

            e=k*a;
            f=k*b;
            g=k*c;
            vector <int> couch={e,f,g};

            Triplet.push_back(couch);

            if (e+f+g==1000) {

                cout<< "Solution of Pythagorean Triplet: "<<e<<" "<<f<<" "<<g<<"     is "<<e*f*g<<endl;
                return true;
            }

            k=k+1;


        }
    return false;

}
int main()
{  int a=0;
int b=0;
int c=0;

    for (int n=1;n<1000;n++){

        for (int m=n+1;m<1001;m++){
            a=(m*m-n*n);
            b=2*m*n;
            c=(m*m+n*n);
            vector <int> d={a,b,c};



                if (CreateTriplets(a,b,c)){

                    break;
                }

        }
    }

    return 0;
}
