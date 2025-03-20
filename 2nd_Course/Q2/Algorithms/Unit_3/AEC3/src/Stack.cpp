#include "../includes/lib.hpp"

/**
 * Constructor of the Stack class.
 * 
 * Initializes an empty stack with the specified name.
 * 
 * @param name Name of the stack.
 */
Stack::Stack(std::string name) : top(nullptr), name(name) {}

/**
 * Returns the name of the stack.
 *
 * @return Name of the stack.
 */
std::string Stack::stackName() const
{
    return name;
}

/**
 * Pushes a new disk onto the stack.
 * 
 * Creates a new node with the specified value and places it on top of the stack.
 * 
 * @param num Value of the disk to push.
 */
void Stack::push(int num)
{
    Node *newNode = new Node(num, top);
    top = newNode;
    std::cout << GREEN "Pushing disk " << num << " onto post "  RESET<< name << std::endl;
}

/**
 * Pops the disk on top of the stack.
 * 
 * Removes the node from the top of the stack and returns the value of the disk.
 * If the stack is empty, an error message is displayed.
 * 
 * @return The value of the popped disk, or -1 if the stack is empty.
 */
int Stack::pop()
{
    if (isEmpty())
    {
        std::cerr << RED "Error: Attempt to pop from an empty stack." RESET << std::endl;
        return -1;
    }
    int value = top->data;
    Node *temp = top;
    top = top->next;
    delete temp;
    std::cout << YELLOW "Popping disk " << value << " from post " RESET << name << std::endl;
    return value;
}

/**
 * Checks if the stack is empty.
 * 
 * @return true if the stack is empty, false otherwise.
 */
bool Stack::isEmpty() const
{
    return top == nullptr;
}

/**
 * Destructor of the Stack class.
 * 
 * Removes all nodes from the stack to free memory.
 */
Stack::~Stack()
{
    while (!isEmpty())
        pop();
}
