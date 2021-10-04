#include<iostream>
using namespace std;

int main() {
    int n; cin >> n;
    int *arr = new int[n];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    cout << sum << '\n';
    delete[] arr;
    return 0;
}