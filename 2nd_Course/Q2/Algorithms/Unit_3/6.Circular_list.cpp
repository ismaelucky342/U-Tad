#include <iostream>
using namespace std;

// Node structure
struct Node {
    int data;
    Node* next;
};

// Circular Linked List class
class CircularList {
private:
    Node* last;

public:
    CircularList() : last(nullptr) {}

    // Function to check if the list is empty
    bool isEmpty() {
        return last == nullptr;
    }

    // Function to insert a node at the beginning
    void insertAtBeginning(int value) {
        Node* newNode = new Node();
        newNode->data = value;

        if (isEmpty()) {
            last = newNode;
            last->next = last;
        } else {
            newNode->next = last->next;
            last->next = newNode;
        }
    }

    // Function to insert a node at the end
    void insertAtEnd(int value) {
        Node* newNode = new Node();
        newNode->data = value;

        if (isEmpty()) {
            last = newNode;
            last->next = last;
        } else {
            newNode->next = last->next;
            last->next = newNode;
            last = newNode;
        }
    }

    // Function to display the list
    void display() {
        if (isEmpty()) {
            cout << "The list is empty." << endl;
            return;
        }

        Node* temp = last->next;
        do {
            cout << temp->data << " ";
            temp = temp->next;
        } while (temp != last->next);
        cout << endl;
    }

    // Function to delete a node by value
    void deleteNode(int value) {
        if (isEmpty()) {
            cout << "The list is empty. Cannot delete." << endl;
            return;
        }

        Node* current = last->next;
        Node* previous = last;

        do {
            if (current->data == value) {
                if (current == last && current->next == last) {
                    // Single node case
                    delete current;
                    last = nullptr;
                } else {
                    previous->next = current->next;
                    if (current == last) {
                        last = previous;
                    }
                    delete current;
                }
                cout << "Node with value " << value << " deleted." << endl;
                return;
            }
            previous = current;
            current = current->next;
        } while (current != last->next);

        cout << "Node with value " << value << " not found." << endl;
    }
};

int main() {
    CircularList clist;

    clist.insertAtEnd(10);
    clist.insertAtEnd(20);
    clist.insertAtEnd(30);
    clist.insertAtBeginning(5);

    cout << "Circular List: ";
    clist.display();

    clist.deleteNode(20);
    cout << "After deleting 20: ";
    clist.display();

    clist.deleteNode(5);
    cout << "After deleting 5: ";
    clist.display();

    return 0;
}