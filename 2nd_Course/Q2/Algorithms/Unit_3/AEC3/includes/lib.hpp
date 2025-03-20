/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC2 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        01/03/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    15/03/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        */
/*                                                                                     */
/*       Github:  https://github.com/ismaelucky342/                                    */
/*                                                                                     */
/***************************************************************************************/

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

/*====================================STRUCTURES=======================================*/

//Stack
class Stack {
private:
    struct Node {
        int data;
        Node *next;
        Node(int d, Node *n = nullptr) : data(d), next(n) {}
    };
    
    Node *top;
    std::string name;

public:

    Stack(std::string name);
    std::string stackName() const;
    void push(int num);
    int pop();
    bool isEmpty() const;
    
    ~Stack();
};

class RussianRoulette {
    private:
        std::vector<std::string> drum;
        int current_position;
    
    public:

        RussianRoulette(int N, int bullet_position);
        void spin(int g);
        std::string shoot();
};

/*====================================FUNCTIONS========================================*/

void hanoi(int n, Stack &source, Stack &auxiliary, Stack &destination); 

#endif 