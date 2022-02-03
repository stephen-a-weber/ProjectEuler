#ifndef MONOPOLY_H
#define MONOPOLY_H
#include <vector>
#include <utility>
#include <algorithm>
#include <ctime>
#include <iostream>
using namespace std;
typedef pair<int,int> roll;
class monopoly
{
    public:
        monopoly();
        virtual ~monopoly();
        int sizeOfDice;
        int CCCard;
        int CHCard;
        bool nextturn;
        vector<int> places;
        vector<int> chance;
        vector<int> communityChest;
        int moves;
        int games;
        int position;
        int diceA;
        int diceB;
        roll bones;
        void shuffle(vector<int> &cards);
        void rolling();
        void card(int &position);
        void moving(int &position);
        void single_sample();
        void sample();
        void run();
        void init();

    protected:
    private:
};

#endif // MONOPOLY_H
