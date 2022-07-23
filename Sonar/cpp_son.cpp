#include <iostream>

using namespace std;

void expoCalc(double time)
{
    if (time == 0)
    {
        cout << "The time was taken as 0.\nYou are dead, congrats." << endl;
    } else if (time > 0)
    {
        cout << "The explosion was within a" << time * 343 << "meter radius." << endl;
    } else
    {
        cout << "You are dead.";}
}

void litCalc(double diff)
{
    if (diff == 0)
    {
        cout << "Youre in it, either watch or seek shelter" << endl;
    } else if (diff > 0)
    {
        cout << "You are " << diff * 343 << " meters from the storm. Good luck!" << endl;
    } else
    {
        cout << "Wut";
    }
}

int main()
{
    int chois;
    cout << "Hi! Count the seconds btwn when you saw the light and the sound first. "
         << "Or guess, no ones judging\n"
         << endl;
    cout << "What do you want to calculate?\n1. Explosion\n2. Lightning\n3. Quit" << endl;

    cout << "Pick the num: ";
    cin >> chois;

    if (chois == 1)
    {
        double exploTim;
        cout << "What was the time diffrence between the cloud and the kaboom? ";
        cin >> exploTim;
        expoCalc(exploTim);
    }
    else if (chois == 2)
    {
        double flashThunTim;
        cout << "What was the time btwn flash and thunder? " << endl;
        cin >> flashThunTim;
        litCalc(flashThunTim);
    }
    else if (chois == 3)
    {

        cout << "Bye have a great time" << endl;
    }
    else
    {
        cout << "Had to pick one of the options..." << endl;
    };
    return 0;
}