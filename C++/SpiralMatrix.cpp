#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int n = matrix.size();
        if (n == 0) return ans; // handle empty matrix
        int m = matrix[0].size();

        int top = 0, bottom = n - 1;
        int l = 0, r = m - 1;
        int traversedCount = 0;
        int total = n * m;

        while (traversedCount < total) {
            // Traverse top row
            for (int j = l; j <= r && traversedCount < total; j++) {
                ans.push_back(matrix[top][j]);
                traversedCount++;
            }
            top++;

            // Traverse right column
            for (int i = top; i <= bottom && traversedCount < total; i++) {
                ans.push_back(matrix[i][r]);
                traversedCount++;
            }
            r--;

            // Traverse bottom row
            for (int j = r; j >= l && traversedCount < total; j--) {
                ans.push_back(matrix[bottom][j]);
                traversedCount++;
            }
            bottom--;

            // Traverse left column
            for (int i = bottom; i >= top && traversedCount < total; i--) {
                ans.push_back(matrix[i][l]);
                traversedCount++;
            }
            l++;
        }
        return ans;
    }
};

int main() {
    Solution sol;

    int n, m;
    cout << "Enter number of rows and columns: ";
    cin >> n >> m;

    vector<vector<int>> matrix(n, vector<int>(m));
    cout << "Enter matrix elements:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    vector<int> result = sol.spiralOrder(matrix);

    cout << "Spiral order: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
