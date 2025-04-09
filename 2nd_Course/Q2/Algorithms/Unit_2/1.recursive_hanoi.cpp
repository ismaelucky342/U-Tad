// Towers of Hanoi
#include <iostream>

using namespace std;

void hanoi(int n, char from_rod, char to_rod, char aux_rod)
{
    if (n == 1)
    {
        cout << "Move disk 1 from rod " << from_rod << " to rod " << to_rod << endl;
        return;
    }
    hanoi(n - 1, from_rod, aux_rod, to_rod);
    cout << "Move disk " << n << " from rod " << from_rod << " to rod " << to_rod << endl;
    hanoi(n - 1, aux_rod, to_rod, from_rod);
}

int main(int argc, char **argv)
{

    if (argc != 2)
    {
        cout << "Usage: " << argv[0] << " <number_of_disks>" << endl;
        return 1;
    }
    int n = atoi(argv[1]);
    if (n <= 0)
    {
        cout << "Number of disks must be a positive integer." << endl;
        return 1;
    }
    hanoi(n, 'A', 'C', 'B');
    return 0;
}