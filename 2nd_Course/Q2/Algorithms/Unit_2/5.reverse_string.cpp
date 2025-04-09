/*
Write a recursive function that reverses a given string. 
The function must return a new string where the characters of the original string are in reverse order.
*/
#include <iostream>
#include <string>

std::string reverseString(const std::string &str) {
    if (str.empty()) {
        return "";
    } else {
        return reverseString(str.substr(1)) + str[0];
    }
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);

    std::string reversed = reverseString(input);
    std::cout << "Reversed string: " << reversed << std::endl;

    return 0;
}