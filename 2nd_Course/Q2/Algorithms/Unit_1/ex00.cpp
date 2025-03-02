/*Insertion short*/

#include <iostream>
#include <vector>
#include <algorithm>

void InsertionSort(int arr[], int n)
{
    int i = 1;
    int key; 
    int j; 

    while (i < n)
    {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }

        arr[j + 1] = key;
        i++;
    }
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    InsertionSort(arr, n);

    std::cout << "Sorted array: \n";
    for (int i = 0; i < n; i++)
        std::cout << arr[i] << " ";

    return 0;
}