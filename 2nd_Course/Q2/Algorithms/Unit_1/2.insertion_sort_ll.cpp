#include <iostream>
#include <vector>
#include <sstream>

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

void printList(Node* head) {
    Node* current = head;
    while (current) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

Node* insertionSort(Node* head) {
    if (!head || !head->next) return head;

    Node* sorted = nullptr;

    while (head) {
        Node* current = head;
        head = head->next;

        if (!sorted || sorted->data >= current->data) {
            current->next = sorted;
            sorted = current;
        } else {
            Node* temp = sorted;
            while (temp->next && temp->next->data < current->data) {
                temp = temp->next;
            }
            current->next = temp->next;
            temp->next = current;
        }
    }

    return sorted;
}

Node* createLinkedList(const std::vector<int>& values) {
    Node* head = nullptr;
    Node* tail = nullptr;

    for (int val : values) {
        Node* newNode = new Node(val);
        if (!head) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    return head;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <list of integers>" << std::endl;
        return 1;
    }

    std::vector<int> values;
    for (int i = 1; i < argc; ++i) {
        std::istringstream iss(argv[i]);
        int num;
        if (iss >> num) {
            values.push_back(num);
        } else {
            std::cerr << "Invalid input: " << argv[i] << std::endl;
            return 1;
        }
    }

    Node* head = createLinkedList(values);
    std::cout << "Original list: ";
    printList(head);

    head = insertionSort(head);
    std::cout << "Sorted list: ";
    printList(head);

    return 0;
}