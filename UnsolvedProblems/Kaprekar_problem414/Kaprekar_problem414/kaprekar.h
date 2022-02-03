//
//  kaprekar.h
//  Kaprekar_problem414
//
//  Created by Stephen Weber on 2/11/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//

#ifndef __Kaprekar_problem414__kaprekar__
#define __Kaprekar_problem414__kaprekar__

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <functional>

using namespace std;

class kaprekar
{
    
public:
    kaprekar();
    virtual ~kaprekar();
    
    vector<uint64_t> CB;
    vector<uint64_t> number;
    vector<uint64_t> check;
    vector<uint64_t> rnumber;
    vector<uint64_t> diff;
    vector<uint64_t> last;
    vector<uint64_t>::reverse_iterator rit;
    vector<uint64_t>::iterator it;
    
    uint64_t SBofI;
    uint64_t SUMofB;
    
    bool cbValue;
    
    int base;
    
    void fill_number(uint64_t i, int base);
    void reverse_number();
    void subtract_number(int base);
    void loop_through_bases();
    void check_loop();
    void run();
    void init();
    void Copy(vector<uint64_t> &a, vector<uint64_t> &b);
    bool Equal(vector<uint64_t> &a, vector<uint64_t> &b);
    void Print(vector<uint64_t> &h);
    
    
    
};

#endif /* defined(__Kaprekar_problem414__kaprekar__) */

 