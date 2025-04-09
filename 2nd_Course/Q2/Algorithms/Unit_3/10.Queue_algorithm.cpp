#include <iostream>
#include <queue>

void processQueue(std::queue<int>& q) {
    while (!q.empty()) {
        int front = q.front();
        std::cout << "Processing: " << front << std::endl;
        q.pop();
    }
}

int main() {
    std::queue<int> q;

    // Adding elements to the queue
    q.push(10);
    q.push(20);
    q.push(30);
    q.push(40);

    std::cout << "Queue processing starts:" << std::endl;
    processQueue(q);

    std::cout << "Queue processing completed." << std::endl;
    return 0;
}