#include <iostream>
#include <vector>
using namespace std;

// Function to perform rank sort
void rankSort(vector<int>& arr) {
    int n = arr.size();
    vector<int> rank(n, 0);
    vector<int> sortedArr(n);

    // Calculate ranks
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[j] < arr[i] || (arr[j] == arr[i] && j < i)) {
                rank[i]++;
            }
        }
    }

    // Place elements in sorted order based on ranks
    for (int i = 0; i < n; i++) {
        sortedArr[rank[i]] = arr[i];
    }

    // Copy sorted array back to original array
    arr = sortedArr;
}

int main() {
    vector<int> arr = {40, 10, 20, 50, 30};

    cout << "Original array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    rankSort(arr);

    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}