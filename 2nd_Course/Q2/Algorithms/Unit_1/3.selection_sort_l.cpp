// selection short 

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

void SelectionSort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
	int minIndex = i;
	for (int j = i + 1; j < n; j++)
	{
	    if (arr[j] < arr[minIndex])
		minIndex = j;
	}
	std::swap(arr[i], arr[minIndex]);
    }
}

int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    SelectionSort(arr, n);

    std::cout << "Sorted array: \n";
    for (int i = 0; i < n; i++)
	std::cout << arr[i] << " ";

    return 0;
}	


