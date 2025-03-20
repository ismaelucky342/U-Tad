#include "../includes/lib.hpp"

/**
 * Recursive function that solves the Towers of Hanoi problem.
 *
 * Moves n disks from the source stack to the destination stack,
 * using an auxiliary stack following the rules of the game.
 *
 * @details
 * - Recursion is used to divide the problem into smaller subproblems.
 * - The base case occurs when there is only one disk, which is moved directly.
 * - If there is more than one disk, first n-1 disks are moved to the auxiliary stack,
 *   then the largest disk to the destination stack, and finally the n-1 disks
 *   from the auxiliary stack to the destination stack.
 *
 * @param n Number of disks to move.
 * @param source Source stack from where the disks are moved.
 * @param auxiliary Auxiliary stack used in the process.
 * @param destination Destination stack where the disks should be stacked.
 *
 * @pre n must be a positive integer.
 * @pre The stacks must be properly initialized.
 *
 * @complexity
 * - Time: O(2^n), since each recursive call makes two subcalls.
 * - Space: O(n), due to the depth of the recursion.
 */
void hanoi(int n, Stack &source, Stack &auxiliary, Stack &destination)
{
    if (n == 1)
        destination.push(source.pop());
    else
    {
        hanoi(n - 1, source, destination, auxiliary);
        destination.push(source.pop());
        hanoi(n - 1, auxiliary, source, destination);
    }
}

/**
 * Main function that initializes the stacks and executes the Hanoi solution.
 *
 * @details
 * - The number of disks is received as an argument from the command line.
 * - Three stacks are initialized with names "A" (source), "B" (auxiliary), and "C" (destination).
 * - The disks are initially stacked in the source stack.
 * - The hanoi function is called to solve the problem.
 *
 * @param argc Number of arguments received from the command line.
 * @param argv Array of arguments passed during the program execution.
 *
 * @pre Exactly one valid numeric argument must be provided.
 *
 * @complexity
 * - Time: O(2^n), determined by the hanoi function.
 * - Space: O(n), due to the recursive call stack.
 */
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        std::cout << RED "ERROR: Usage: " << argv[0] << " <number of disks>" RESET << std::endl;
        return 1;
    }

    int n = std::stoi(argv[1]);

    std::cout << CYAN "\n*** Towers of Hanoi ***\n";
    std::cout << "Number of disks: " << n << "\n";
    std::cout << "Moves: " RESET << std::endl;

    Stack source("A"), auxiliary("B"), destination("C");
    for (int i = n; i >= 1; --i)
        source.push(i);
    hanoi(n, source, auxiliary, destination);

    std::cout << GREEN "\nResolution completed.\n" RESET << std::endl;
    return 0;
}
