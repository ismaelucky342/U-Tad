#include <iostream>
#include <stack>
using namespace std;

void stackAlgorithmExample() {
    stack<int> s;

    // Push elements onto the stack
    s.push(10);
    s.push(20);
    s.push(30);

    cout << "Stack size: " << s.size() << endl;

    // Pop elements from the stack
    while (!s.empty()) {
        cout << "Top element: " << s.top() << endl;
        s.pop();
    }

    cout << "Stack is now empty." << endl;
}

int main() {
    stackAlgorithmExample();
    return 0;
}