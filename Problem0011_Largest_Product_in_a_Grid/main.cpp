
/*
In the 2020 grid below, four numbers auint64_t a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
The product of these numbers is 26  63  78  14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 2020 grid?


Answer:
70600674
Completed on Tue, 22 Jan 2013, 23:33

*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector < vector <uint64_t> > Grid;
     vector <uint64_t> r1={8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8};

        vector <uint64_t> r2={49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0};
        vector <uint64_t> r3={81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65};
        vector <uint64_t> r4={52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91};
        vector <uint64_t> r5={22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80};
        vector <uint64_t> r6={24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50};
        vector <uint64_t> r7 ={32 ,98 ,81 ,28 ,64 ,23 ,67 ,10 ,26 ,38, 40 ,67 ,59 ,54 ,70 ,66 ,18 ,38 ,64,70};
        vector <uint64_t> r8={67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21};
        vector <uint64_t> r9={24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72};
        vector <uint64_t> r10={21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95};
        vector <uint64_t> r11={78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92};
        vector <uint64_t> r12 ={16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57};
        vector <uint64_t> r13={86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58};
        vector <uint64_t> r14={19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40};
        vector <uint64_t> r15={4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66};
        vector <uint64_t> r16={88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69};
        vector <uint64_t> r17={4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36};
        vector <uint64_t> r18={20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16};
        vector <uint64_t> r19={20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54};
        vector <uint64_t> r20={1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48};
        Grid.push_back(r1);
        Grid.push_back(r2);
        Grid.push_back(r3);
        Grid.push_back(r4);
        Grid.push_back(r5);
        Grid.push_back(r6);
        Grid.push_back(r7);
        Grid.push_back(r8);
        Grid.push_back(r9);
        Grid.push_back(r10);
        Grid.push_back(r11);
        Grid.push_back(r12);
        Grid.push_back(r13);
        Grid.push_back(r14);
        Grid.push_back(r15);
        Grid.push_back(r16);
        Grid.push_back(r17);
        Grid.push_back(r18);
        Grid.push_back(r19);
        Grid.push_back(r20);




        uint64_t maxProduct=0;
        uint64_t currentProduct=1;

        // rows
        for (uint64_t col=0;col<20;col++){

            for (uint64_t a=0;a<17;a++) {
                    currentProduct=1;
                    for (uint64_t b=0;b<4;b++){

             currentProduct*=Grid[col][a+b];
            }
            if (currentProduct>maxProduct) {
                maxProduct=currentProduct;
            }
            }
        }

        //columns
        for (uint64_t row=0;row<20;row++){

            for (uint64_t a=0;a<17;a++) {
                    currentProduct=1;
                    for (uint64_t b=0;b<4;b++){

             currentProduct*=Grid[a+b][row ];
            }
            if (currentProduct>maxProduct) {
                maxProduct=currentProduct;
            }
            }
        }

        //Diagonally
         for (uint64_t col=0;col<17;col++){

            for (uint64_t row=0;row<17;row++) {
                    currentProduct=1;
                    for (uint64_t b=0;b<4;b++){

             currentProduct*=Grid[col+b][row+b ];
            }
            if (currentProduct>maxProduct) {
                maxProduct=currentProduct;
            }
            }
        }

        //OtherDiagonal
          for (uint64_t col=4;col<20;col++){

            for (uint64_t row=0;row<17;row++) {
                    currentProduct=1;
                    for (uint64_t b=0;b<4;b++){

             currentProduct*=Grid[col-b][row+b ];
            }
            if (currentProduct>maxProduct) {
                maxProduct=currentProduct;
            }
            }
        }


        cout<<"THE Answer is :"<<maxProduct<<endl;

    cout << "Hello world!" << endl;
    return 0;
}
