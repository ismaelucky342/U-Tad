#include <iostream>
#include <queue>

int main() {
    std::queue<int> q;

    // Adding elements to the queue
    q.push(10);
    q.push(20);
    q.push(30);

    std::cout << "Queue size: " << q.size() << std::endl;

    // Accessing the front element
    std::cout << "Front element: " << q.front() << std::endl;

    // Accessing the back element
    std::cout << "Back element: " << q.back() << std::endl;

    // Removing elements from the queue
    while (!q.empty()) {
        std::cout << "Removing: " << q.front() << std::endl;
        q.pop();
    }

    std::cout << "Queue is now empty." << std::endl;

    return 0;
}