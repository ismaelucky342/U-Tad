#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> myStack;

    // Push elements onto the stack
    myStack.push(10);
    myStack.push(20);
    myStack.push(30);

    cout << "Stack size: " << myStack.size() << endl;

    // Access the top element
    cout << "Top element: " << myStack.top() << endl;

    // Pop elements from the stack
    while (!myStack.empty()) {
        cout << "Popping: " << myStack.top() << endl;
        myStack.pop();
    }

    cout << "Stack is now empty." << endl;

    return 0;
}