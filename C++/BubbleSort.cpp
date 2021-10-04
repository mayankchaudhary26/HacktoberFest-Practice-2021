// Bubble Sort Program

#include<iostream>
using namespace std;


int main() {
	int n;
	cin >> n;
	int arr[n];
	for (int i = 0 ; i < n ; i++)
		cin >> arr[i];
  
	// Bubble Sort
	for (int i = 0 ; i < n - 1 ; i++)
	{
		for (int j = 0 ; j < n - i - 1; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}

	for (int i = 0 ; i < n ; i++)
		cout << arr[i] << " ";
	return 0;
}


/*
	Test Cases

	INPUT -
	5
  1 4 2 3 5

	OUTPUT -
	1 2 3 4 5
  
*/

