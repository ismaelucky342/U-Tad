#include <iostream>

void insertionSort(int list[], int elements);

int main() {
    int list[] = {12, 11, 13, 5, 6};
    int n = sizeof(list) / sizeof(list[0]);

    std::cout << "Original array: ";
    for(int i = 0; i < n; i++)
        std::cout << list[i] << " ";
    std::cout << std::endl;

    insertionSort(list, n);

    std::cout << "Sorted array: ";
    for(int i = 0; i < n; i++)
        std::cout << list[i] << " ";
    std::cout << std::endl;

    return 0;
}
void insertionSort(int list[], int elements)
{
    for(int i = 1; i < elements; i++)
    {
        int key = list[i];
        int j = i - 1;
        while(j >= 0 && list[j] > key)
        {
            list[j + 1] = list[j];
            j = j - 1;
        }
        list[j + 1] = key;
    }
}
