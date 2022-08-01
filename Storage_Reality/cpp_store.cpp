#include <iostream>

using namespace std;

void real_chk(long int diff)
{
    if (diff == 0)
    {
        cout << "You got pranked" << endl;
    } else if (diff > 0)
    {
            cout << "\nReality check, its not " << 
            diff << "!!\nIts " 
            << diff*0.9313226 << " GB" << endl;
    } else
    {
        cout << "Wut" << endl;
    }
}

int main()
{
    int storag;
    cout << "How much storage do you have? " << flush;
    cin >> storag;

    real_chk(storag);
    
    return 0;
}