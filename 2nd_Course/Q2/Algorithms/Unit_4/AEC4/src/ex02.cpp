#include "../includes/Lib.h"


/**
 * bubble_sort - Ordena un array de enteros usando el algoritmo de burbuja.
 * @arr: Array de enteros.
 * @n: Tamaño del array.
 *
 * Complejidad temporal: O(n^2) en el peor y promedio de los casos.
 * Complejidad espacial: O(1) ya que se ordena en su lugar.
 */
void bubble_sort(int arr[], int n) 
{
    bool swapped;
    for (int i = 0; i < n - 1; i++) 
    {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) 
        {
            if (arr[j] > arr[j + 1]) 
            {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        for (int k = 0; k < n; k++) 
            std::cout << arr[k] << " ";
        std::cout << std::endl;

        if (!swapped) break;
    }
}

int main(int argc, char *argv[]) 
{
    if (argc < 2) 
    {
        std::cerr << RED "Error: You must provide at least one number." RESET << std::endl;
        return 1;
    }
    
    int n = argc - 1;
    std::vector<int> arr(n);
    
    for (int i = 0; i < n; i++) 
    {
        try 
        {
            arr[i] = std::stoi(argv[i + 1]);
        } 
        catch (const std::invalid_argument&) 
        {
            std::cerr << RED "Error: Invalid input '" << argv[i + 1] << "'. Please enter only integers." RESET << std::endl;
            return 1;
        } 
        catch (const std::out_of_range&) 
        {
            std::cerr << RED "Error: Input '" << argv[i + 1] << "' is out of range." RESET << std::endl;
            return 1;
        }
    }
    bubble_sort(arr.data(), n);
    return 0;
}