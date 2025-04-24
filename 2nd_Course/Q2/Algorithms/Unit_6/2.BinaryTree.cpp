#include <iostream>
#include <vector>
#include <queue>

// Definition of the Node structure for a binary tree
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int value) : val(value), left(nullptr), right(nullptr) {}
};

// Function to insert a node into a complete binary tree (based on index property)
TreeNode* insertCompleteBinaryTree(TreeNode* root, int value, int index) {
    if (root == nullptr) {
        return new TreeNode(value);
    }

    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;

    while (!q.empty()) {
        TreeNode* current = q.front();
        q.pop();

        if (i == index) {
            delete new TreeNode(value); // Clean up unnecessary node creation
            return root;
        }

        if (current->left) {
            q.push(current->left);
        } else if (2 * i == index) {
            current->left = new TreeNode(value);
            return root;
        }

        if (current->right) {
            q.push(current->right);
        } else if (2 * i + 1 == index) {
            current->right = new TreeNode(value);
            return root;
        }
        i++;
    }
    return root;
}

// Function to insert a node at the end of a complete binary tree (maintaining completeness)
TreeNode* insertAtEndCompleteBinaryTree(TreeNode* root, int value, int& nodeCount) {
    nodeCount++;
    return insertCompleteBinaryTree(root, value, nodeCount);
}

// Function for Preorder Traversal
void preorderTraversal(TreeNode* root) {
    if (root != nullptr) {
        std::cout << root->val << " ";
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

// Function for Inorder Traversal
void inorderTraversal(TreeNode* root) {
    if (root != nullptr) {
        inorderTraversal(root->left);
        std::cout << root->val << " ";
        inorderTraversal(root->right);
    }
}

// Function for Postorder Traversal
void postorderTraversal(TreeNode* root) {
    if (root != nullptr) {
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        std::cout << root->val << " ";
    }
}

int main() {
    TreeNode* root = nullptr;
    int nodeCount = 0;

    // Inserting nodes into a complete binary tree
    root = insertAtEndCompleteBinaryTree(root, 10, nodeCount); // Root (index 1)
    root = insertAtEndCompleteBinaryTree(root, 6, nodeCount);  // Left child of 10 (index 2)
    root = insertAtEndCompleteBinaryTree(root, 14, nodeCount); // Right child of 10 (index 3)
    root = insertAtEndCompleteBinaryTree(root, 5, nodeCount);  // Left child of 6 (index 4)
    root = insertAtEndCompleteBinaryTree(root, 8, nodeCount);  // Right child of 6 (index 5)
    root = insertAtEndCompleteBinaryTree(root, 12, nodeCount); // Left child of 14 (index 6)
    // (Node with value 16 would be the right child of 14 if fully complete up to this level)

    std::cout << "Preorder Traversal: ";
    preorderTraversal(root);
    std::cout << std::endl;

    std::cout << "Inorder Traversal: ";
    inorderTraversal(root);
    std::cout << std::endl;

    std::cout << "Postorder Traversal: ";
    postorderTraversal(root);
    std::cout << std::endl;

    // Memory cleanup
    std::queue<TreeNode*> cleanupQueue;
    if (root) cleanupQueue.push(root);
    while (!cleanupQueue.empty()) {
        TreeNode* current = cleanupQueue.front();
        cleanupQueue.pop();
        if (current->left) cleanupQueue.push(current->left);
        if (current->right) cleanupQueue.push(current->right);
        delete current;
    }
    root = nullptr;

    return 0;
}