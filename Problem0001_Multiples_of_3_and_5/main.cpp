/*
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/




#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main()
{   int i=0;
    set<int> numbers;
    for (  i=3;i<1000;i+=3){
        numbers.insert(i);
    }
    for (i=5;i<1000;i+=5){
        numbers.insert(i);
    }
    set<int>::iterator setI;
    int total=0;

    for (setI=numbers.begin();setI!=numbers.end();setI++){
        total+=*setI;

    }
    cout<<"The answer is  "<<total<<endl;

    return 0;
}
