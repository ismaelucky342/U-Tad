#include <iostream>
using namespace std;

// Definition of a Node in the Binary Search Tree
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};

// Insert a new value into the Binary Search Tree
Node* insert(Node* root, int value) {
    if (!root) {
        return new Node(value);
    }
    if (value < root->data) {
        root->left = insert(root->left, value);
    } else if (value > root->data) {
        root->right = insert(root->right, value);
    }
    return root;
}

// Search for a value in the Binary Search Tree
bool search(Node* root, int value) {
    if (!root) {
        return false;
    }
    if (root->data == value) {
        return true;
    } else if (value < root->data) {
        return search(root->left, value);
    } else {
        return search(root->right, value);
    }
}

// In-order traversal of the Binary Search Tree
void inorderTraversal(Node* root) {
    if (root) {
        inorderTraversal(root->left);
        cout << root->data << " ";
        inorderTraversal(root->right);
    }
}

// Main function to demonstrate the Binary Search Tree
int main() {
    Node* root = nullptr;

    // Insert values into the BST
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 70);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 60);
    root = insert(root, 80);

    // Print in-order traversal
    cout << "In-order Traversal: ";
    inorderTraversal(root);
    cout << endl;

    // Search for values in the BST
    int searchValue = 40;
    if (search(root, searchValue)) {
        cout << searchValue << " is found in the BST." << endl;
    } else {
        cout << searchValue << " is not found in the BST." << endl;
    }

    return 0;
}