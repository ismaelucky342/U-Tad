# ifndef LIB_HPP
# define LIB_HPP

/*====================================INCLUDES=========================================*/

#include <stdio.h>
#include <math.h>
#include <stdexcept> 
#include <vector>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

/*====================================COLORS===========================================*/

#define RESET "\033[0m"
#define RED "\033[31m"
#define GREEN "\033[32m"
#define YELLOW "\033[33m"
#define BLUE "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN "\033[36m"
#define WHITE "\033[37m"

/*====================================FUNCTIONS=======================================*/

void selection_sort(std::vector<int>& arr); 
void bubble_sort(int arr[], int n);

#endif