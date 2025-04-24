#include <iostream>
#include <vector>
#include <queue> // For level-order traversal (BFS)

// Definition of the structure of a node for a binary tree
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Function to insert a node into a complete binary tree (based on index property)
Node* insertComplete(Node* root, int value, int index) {
    if (root == nullptr) {
        return new Node(value);
    }

    std::queue<Node*> queue;
    queue.push(root);
    int i = 1;

    while (!queue.empty()) {
        Node* currentNode = queue.front();
        queue.pop();

        if (i == index) {
            // We should not reach here if we are inserting at the end
            delete new Node(value); // Clean up unnecessarily created node
            return root;
        }

        if (currentNode->left) {
            queue.push(currentNode->left);
        } else if (2 * i == index) {
            currentNode->left = new Node(value);
            return root;
        }

        if (currentNode->right) {
            queue.push(currentNode->right);
        } else if (2 * i + 1 == index) {
            currentNode->right = new Node(value);
            return root;
        }
        i++;
    }
    return root;
}

// Function to insert a node at the end of a complete binary tree (maintaining completeness property)
Node* insertAtEndComplete(Node* root, int value, int& numNodes) {
    numNodes++;
    return insertComplete(root, value, numNodes);
}

// Function to perform Preorder traversal
void preorder(Node* root) {
    if (root != nullptr) {
        std::cout << root->data << " ";
        preorder(root->left);
        preorder(root->right);
    }
}

// Function to perform Inorder traversal
void inorder(Node* root) {
    if (root != nullptr) {
        inorder(root->left);
        std::cout << root->data << " ";
        inorder(root->right);
    }
}

// Function to perform Postorder traversal
void postorder(Node* root) {
    if (root != nullptr) {
        postorder(root->left);
        postorder(root->right);
        std::cout << root->data << " ";
    }
}

int main() {
    Node* root = nullptr;
    int numNodes = 0;

    // Inserting nodes into a complete binary tree
    root = insertAtEndComplete(root, 5, numNodes); // Root (index 1)
    root = insertAtEndComplete(root, 3, numNodes); // Left child of 5 (index 2)
    root = insertAtEndComplete(root, 8, numNodes); // Right child of 5 (index 3)
    root = insertAtEndComplete(root, 1, numNodes); // Left child of 3 (index 4)
    root = insertAtEndComplete(root, 4, numNodes); // Right child of 3 (index 5)
    root = insertAtEndComplete(root, 9, numNodes); // Right child of 8 (index 7)
    // (The node with value 6 would be the left child of 8 if the tree were complete at that level)

    std::cout << "Preorder Traversal: ";
    preorder(root);
    std::cout << std::endl;

    std::cout << "Inorder Traversal: ";
    inorder(root);
    std::cout << std::endl;

    std::cout << "Postorder Traversal: ";
    postorder(root);
    std::cout << std::endl;

    // Clean up memory (important in C++)
    std::queue<Node*> cleanupQueue;
    if (root) cleanupQueue.push(root);
    while (!cleanupQueue.empty()) {
        Node* current = cleanupQueue.front();
        cleanupQueue.pop();
        if (current->left) cleanupQueue.push(current->left);
        if (current->right) cleanupQueue.push(current->right);
        delete current;
    }
    root = nullptr;

    return 0;
}