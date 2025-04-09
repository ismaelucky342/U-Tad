#include <iostream>

struct Node {
    int data;
    Node* next;
    Node* prev;
};

class CircularDoublyLinkedList {
private:
    Node* head;

public:
    CircularDoublyLinkedList() : head(nullptr) {}

    ~CircularDoublyLinkedList() {
        while (head) {
            remove(head->data);
        }
    }

    void insert(int value) {
        Node* newNode = new Node{value, nullptr, nullptr};
        if (!head) {
            head = newNode;
            head->next = head;
            head->prev = head;
        } else {
            Node* tail = head->prev;
            tail->next = newNode;
            newNode->prev = tail;
            newNode->next = head;
            head->prev = newNode;
        }
    }

    void remove(int value) {
        if (!head) return;

        Node* current = head;
        do {
            if (current->data == value) {
                if (current->next == current) {
                    delete current;
                    head = nullptr;
                    return;
                }

                Node* prevNode = current->prev;
                Node* nextNode = current->next;

                prevNode->next = nextNode;
                nextNode->prev = prevNode;

                if (current == head) {
                    head = nextNode;
                }

                delete current;
                return;
            }
            current = current->next;
        } while (current != head);
    }

    void display() const {
        if (!head) {
            std::cout << "List is empty.\n";
            return;
        }

        Node* current = head;
        do {
            std::cout << current->data << " ";
            current = current->next;
        } while (current != head);
        std::cout << "\n";
    }
};

int main() {
    CircularDoublyLinkedList list;

    list.insert(10);
    list.insert(20);
    list.insert(30);

    std::cout << "List after insertion: ";
    list.display();

    list.remove(20);
    std::cout << "List after removing 20: ";
    list.display();

    list.remove(10);
    std::cout << "List after removing 10: ";
    list.display();

    list.remove(30);
    std::cout << "List after removing 30: ";
    list.display();

    return 0;
}