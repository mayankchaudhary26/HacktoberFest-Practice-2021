#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

/**
 * Function to find the maximum number of points on a line
 * @param points vector of points
 * @return maximum number of points on a line
 */
int maxPoints(vector<vector<int>>& points) {
    int n = points.size();
    int result = 1;

    // Iterate through each point
    for (int i = 0; i < n; i++) {
        unordered_map<double, int> um; // Use unordered map to store the slopes with their frequency
        int duplicate = 1; // Count the duplicates of point i

        // Iterate through each other point
        for (int j = i + 1; j < n; j++) {
            int dx = points[i][0] - points[j][0];
            int dy = points[i][1] - points[j][1];

            // Handle special cases when dx is 0
            if (dx == 0) {
                um[dy == 0 ? 0.0 : INT_MAX]++; // Handle vertical lines separately
            } else {
                double slope = (double) dy / dx; // Calculate slope
                um[slope]++; // Increment frequency of slope in map
            }
        }

        result = max(result, duplicate); // Update the result with duplicates of point i

        // Update the result with the frequency of slope and duplicates of point i
        for (auto& p : um) {
            result = max(result, p.second + duplicate);
        }
    }

    return result;
}

int main() {
    // Example usage
    vector<vector<int>> points = {{1,1},{2,2},{3,3}};
    cout << maxPoints(points) << endl; // Output: 3

    return 0;
}
