#include "../includes/Lib.h"

/**
 * selection_sort - Ordena un array de enteros usando el algoritmo de selección.
 * @arr: Array de enteros.
 * @n: Tamaño del array.
 *
 * Complejidad temporal: O(n^2) en todos los casos.
 * Complejidad espacial: O(1) ya que se ordena en su lugar.
 */

void selection_sort(std::vector<int>& arr) 
{
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) 
    {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) 
            if (arr[j] < arr[min_idx]) 
                min_idx = j;
        std::swap(arr[i], arr[min_idx]);
        
        for (const auto& elem : arr) 
            std::cout << elem << " ";
        std::cout << std::endl;
    }
}

int main(int argc, char* argv[]) 
{
    if (argc < 2) 
    {
        std::cerr << RED "Error: You must provide at least one number." RESET<< std::endl;
        return 1;
    }
    
    try 
    {
        std::vector<int> arr;
        for (int i = 1; i < argc; i++) 
        {
            arr.push_back(std::stoi(argv[i]));
        }
        selection_sort(arr);
    } 
    catch (const std::invalid_argument& e) 
    {
        std::cerr << RED "Error: Invalid input. You must enter only integers." RESET<< std::endl;
        return 1;
    } 
    catch (const std::out_of_range& e) 
    {
        std::cerr << RED "Error: Input number out of range." RESET << std::endl;
        return 1;
    }

    return 0;
}