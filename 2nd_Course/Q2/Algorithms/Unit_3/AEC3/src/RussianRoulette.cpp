#include "../includes/lib.hpp"
#include <unistd.h>

/**
 * Constructor of the RussianRoulette class.
 *
 * @param N Number of slots in the drum.
 * @param pos_bala Position where the bullet is placed in the drum (from 0 to N-1).
 *
 * @details
 * - The drum is initialized with N slots, all with the value "CLACK".
 * - The bullet is placed in the position indicated by pos_bala, replacing "CLACK" with "BANG".
 */
RussianRoulette::RussianRoulette(int N, int pos_bala) : drum(N, CYAN "CLACK" RESET), current_position(0)
{
    drum[pos_bala] = RED "BANG" RESET;
}


/**
 * Method that performs a spin on the drum.
 *
 * @param g Number of positions to spin (can be positive or negative).
 *
 * @details
 * - The spin adjusts the current position in the drum.
 * - If the new position is negative, it is adjusted to be within the valid range.
 */
void RussianRoulette::spin(int g)
{
    int N = drum.size();
    current_position = (current_position + g) % N;
    if (current_position < 0)
        current_position += N;
}

/**
 * Method that simulates the firing of the drum.
 *
 * @return Returns the value at the current position of the drum (can be "CLACK" or "BANG").
 *
 * @details
 * - The firing checks the value at the current position of the drum and returns it.
 */
std::string RussianRoulette::shoot()
{
    return drum[current_position];
}

/**
 * Main function that simulates Russian roulette.
 *
 * @param argc Number of command line arguments.
 * @param argv Command line arguments.
 *
 * @details
 * - The first argument is the number of slots in the drum (N).
 * - The second argument is the position of the bullet (from 0 to N-1).
 * - The remaining arguments are the spins to be performed before firing.
 * - If the bullet is fired, the program ends immediately.
 */
int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        std::cerr << RED "ERROR: Usage: " << argv[0] << " <N> <pos_bala> <spins ...>\n" RESET << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);
    int pos_bala = std::stoi(argv[2]);

    if (N <= 0)
    {
        std::cerr << RED "ERROR: The number of slots in the drum must be positive.\n" RESET << std::endl;
        return 1;
    }
    if (pos_bala < 0 || pos_bala >= N)
    {
        std::cerr << RED "ERROR: The position of the bullet must be between 0 and " RESET << (N - 1) << ".\n";
        return 1;
    }

    RussianRoulette ruleta(N, pos_bala);

    std::cout << YELLOW "============Welcome to Russian Roulette============" RESET << std::endl;
    for (int i = 3; i < argc; ++i)
    {
        int spin = std::stoi(argv[i]);
        ruleta.spin(spin);
        std::string result = ruleta.shoot();

        std::cout << YELLOW "Turn " << i - 2 << ": " RESET;
        //sleep(1); // Wait for 1 second to add suspense
        std::cout << result << std::endl;

        if (result == RED "BANG" RESET)
        {
            std::cout << RED "The bullet has been fired. End of the game." RESET << std::endl;
            break;
        }
    }

    return 0;
}
