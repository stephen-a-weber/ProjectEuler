#include "monopoly.h"

monopoly::monopoly()
{
    //ctor
    CCCard=0;
    CHCard=0;
    sizeOfDice=4;
    nextturn=false;
    vector<int>places(0,40);
    vector<int>chances(16);
    vector<int>communityChest(16);
    moves=1000000;
    games=1000;
    position=0;
    srand(time(NULL));
 }

monopoly::~monopoly()
{
    //dtor
}
void monopoly::rolling()
{
    diceA=rand()%sizeOfDice+1;
    diceB=rand()%sizeOfDice+1;
    bones=make_pair(diceA,diceB);
}

void monopoly::card(int &position)
{
    if (position==7 or position==22 or position==36) {//CHANCE LANDING



if (chance[CHCard]==1) {
position=0;//Advance to GO
}

if (chance[CHCard]==2) {
position=10;//GO to Jail
nextturn=false;
}

if (chance[CHCard]==3){
position=11;// Advance to St.Charles Place
}

if (chance[CHCard]==4) {
position=24;//Advance to Illinois
}

if (chance[CHCard]==5) {
position=39;//Advance to Boardwalk
}

if (chance[CHCard]==6) {
position=5;//advance to reading
}

if (chance[CHCard]==7) {
if (position==36){//go to next Railroad
position=5;}
if (position==22){
position=25;}
if (position==7){
position=15;}
}

if (chance[CHCard]==8) {
if (position==36){//go to next Railroad
position=5;}
if (position==22){
position=25;}
if (position==7){
position=15;}
}

if (chance[CHCard]==9) {
if(position==36 or position==7){
position=12;}//go to next utility
else{
position=28;}
}

if (chance[CHCard]==10) {
position=position-3;
}

CHCard+=1;
CHCard=CHCard%16;

}

    if (position==2 or position==17 or position==33){//COMMUNITYCHEST PLACES
  if (communityChest[CCCard]==1){//1==go

  position=0;
  nextturn=false;}
  if (communityChest[CCCard]==2){//2=Jail
  position=10;
  }

  CCCard+=1;
  CCCard=CCCard%16;
}

}

void monopoly::moving(int &position)
{







    rolling();
    position=(bones.first+bones.second+position)%40;

    if (bones.first==bones.second){
        nextturn=true;
    }

     card(position);//check for motion from cards
     card(position);//oh the hard way from getting two cards in one turn posibbility

    if (position==30){
        position=10;
        nextturn=false;
         }

    if (nextturn){
        nextturn=false;
        rolling();
        position=(bones.first+bones.second+position)%40;
        if (bones.first==bones.second){
            nextturn=true;
        }
         card(position);
         card(position);
        if (position==30){
               position=10;
               nextturn=false;
                }


        if(nextturn){

            nextturn=false;
            rolling();

            if (bones.first==bones.second){
                position=10;

            }
            else{

                position=(bones.first+bones.second+position)%40;
                 card(position);
                 card(position);
                if (position==30){
                    position=10;
                    nextturn=false;
                    }

            }
        }






        }





}


void monopoly::shuffle(vector<int> &cards)
{
    cards.clear();

    for (int i=1;i<=16;i++){
    cards.push_back(i);
    }
    random_shuffle(cards.begin(),cards.end());
}

void monopoly::single_sample()
{
    shuffle(chance);
    shuffle(communityChest);
    for (int i=0;i<moves;i++){
    moving(position);
    places[position]+=1;

    }

}

void monopoly::sample()
{

    for (int j=0;j<games;j++){
    single_sample();
    }

}

void monopoly::run()
{
     init();
     sample();


     vector<int>::iterator it;

    for(it=places.begin();it!=places.end();it++){

    cout<<"  "<<*it;

    }
    cout<<endl;
    float high1,high2,high3=0;
    int highest=0;
    float trial=0;
    for (int i =0;i<40;i++) {
        if (places[i]>trial){
        trial=places[i];
        highest=i;
        }
    }
    cout<<"highest "<<highest<<endl;
    cout<<"places "<<places[highest]<<endl;
    high1=places[highest];
    places[highest]=0;

    int secondhighest=0;
    trial=0;
    for (int i =0;i<40;i++) {
        if (places[i]>trial){
        trial=places[i];
        secondhighest=i;
        }
    }
    high2=places[secondhighest];
    places[secondhighest]=0;
    int thirdhighest=0;
    trial=0;
    for (int i =0;i<40;i++) {
        if (places[i]>trial){
        trial=places[i];
        thirdhighest=i;
        }
    }
    high3=places[thirdhighest];


    cout<<"  "<<highest<<"         "<<secondhighest<<"         "<<thirdhighest<<endl;
    cout<<"  "<<100*high1/float(moves*games)<<"    "<< 100*high2/float(moves*games)<<"    "<< 100*high3/float(moves*games)<<endl<<endl;



}

void monopoly::init()
{

    for (int i =0; i<40;i++){
    places.push_back(0);
    }
    places[0]=1;
}
