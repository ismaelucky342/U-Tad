// This program checks if a given string is a palindrome, ignoring spaces, punctuation, and case.
// It uses recursion to compare characters from the start and end of the string, moving towards the center.

#include <iostream>
#include <cctype>
#include <string>
#include <algorithm>

// Function to check if a character is alphanumeric
bool isAlphanumeric(char c)
{
    return std::isalnum(static_cast<unsigned char>(c));
}

// Recursive function to check if a string is a palindrome
bool isPalindrome(const std::string &str, int left, int right)
{
    // Base case: if left index is greater than or equal to right index
    if (left >= right)
    {
        return true;
    }

    // Ignore non-alphanumeric characters
    if (!isAlphanumeric(str[left]))
    {
        return isPalindrome(str, left + 1, right);
    }
    if (!isAlphanumeric(str[right]))
    {
        return isPalindrome(str, left, right - 1);
    }

    // Check if characters are equal (ignoring case)
    if (std::tolower(static_cast<unsigned char>(str[left])) != std::tolower(static_cast<unsigned char>(str[right])))
    {
        return false;
    }

    // Move towards the middle
    return isPalindrome(str, left + 1, right - 1);
}

// Wrapper function to call the recursive palindrome check
bool isPalindrome(const std::string &str)
{
    return isPalindrome(str, 0, str.length() - 1);
}

int main()
{
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);

    if (isPalindrome(input))
    {
        std::cout << "The string is a palindrome." << std::endl;
    }
    else
    {
        std::cout << "The string is not a palindrome." << std::endl;
    }

    return 0;
}