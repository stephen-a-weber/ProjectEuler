//
//  main.cpp
//  poker hand euler 54
//
//  Created by Stephen Weber on 1/28/13.
//  Copyright (c) 2013 Stephen Weber. All rights reserved.
//

#include <iostream>
#include <string.h> 
#include <fstream>
#include <vector>
#include <stdio.h>


using namespace std;

vector<int> numberOnCards( vector<string>  hand ){
    
    vector<int> cards;
    int point=0;
    for (int i =0;i<5;i++){
        string d=hand[i];
        char c=d[0];
        if (c=="A"){
            point=13;
        }
        else if (c=="K") {
            point=13;
        }
        else if (c=="Q") {
            point=12;
        }
        else if (c=="J") {
            point=11;
        }
        
    }
    
}
int main(int argc, const char * argv[])
{   int player1=0;
    int player2=0;
    vector<string> hand[1000];
    vector<string>::iterator dealer;
    int game=0;
    fstream file;
    file.open("/Users/sweber/Desktop/codeFolder/poker.txt");
    string p;
    if (file.is_open()){
        
        while (file.good() ){
            
            getline(file,p);
            
            char *a=new char[p.size()+1];
            a[p.size()]=0;
            memcpy(a,p.c_str(),p.size());
            char * pch;
            
            pch=strtok(a," ");
             while (pch !=NULL){
                 hand[game].push_back(pch);
                // printf("%s\n",pch);
                 pch=strtok(NULL," ");
                
            }
            game+=1;
            cout<<p<<endl;
        }
        file.close();
    }
    
    for (int game=0;game<1000;game++){
        vector<string> hand1[5];
        vector<string> hand2[5];
        for (int i =0;i<5;i++) {
            hand1[i]=hand[game];
            hand2[i]=hand[game+5];
        }
        bool value1=true;
        
        
        
        
        
        
        
    }
     
  
    /*
    for (dealer=hand[999].begin();dealer!=hand[999].end();dealer++){
        cout<<*dealer<<" . "<<endl;
    }
    for (int i=0;i<10;i++){
        cout<<hand[0][i]<<endl;
        
    }*/
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

