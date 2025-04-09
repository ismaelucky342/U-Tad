/*Develop a recursive function that finds the sum of the first n natural numbers. Remember that the sum of the first n natural numbers can be expressed as 1+2+3+...+n.*/

#include <iostream>

int sumNaturals(int n) {
    if (n <= 1) {
        return n;
    } else {
        return n + sumNaturals(n - 1);
    }
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    std::cout << "La suma de los primeros " << n << " números naturales es: " << sumaNaturales(n) << std::endl;
    return 0;
}    std::cout << "The sum of the first " << n << " natural numbers is: " << sumNaturals(n) << std::endl;