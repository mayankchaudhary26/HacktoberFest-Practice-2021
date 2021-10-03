#include <bits/stdc++.h>

using namespace std;

// // Defining a long and vector of type 'int'
typedef long ll;
typedef vector<int> vi;

// Defining some functions for vector
#define PB push_back

// Defining a predetermined for-loop

int main()
{
    /* This file is a template for all the test programs . */

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long int n;
    cin >> n;
    while(n != 1)
    {
        cout << n << " ";

        if (n % 2 == 0)
            n = n / 2;
        else
            n = n * 3 + 1;
    }
    cout << n;

    return 0;
}
