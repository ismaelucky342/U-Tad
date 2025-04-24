#include <iostream>
#include <queue>
#include <cmath> // For log2

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int value) : val(value), left(nullptr), right(nullptr) {}
};

// Function to calculate the height of a complete binary tree
int heightCompleteBinaryTree(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    // For a complete binary tree with N nodes, the height is floor(log2(N)) + 1
    // We can find the number of nodes using a level order traversal (BFS)

    std::queue<TreeNode*> q;
    q.push(root);
    int nodeCount = 0;

    while (!q.empty()) {
        TreeNode* current = q.front();
        q.pop();
        nodeCount++;
        if (current->left) q.push(current->left);
        if (current->right) q.push(current->right);
    }

    if (nodeCount == 0) {
        return 0;
    }
    return static_cast<int>(std::floor(std::log2(nodeCount))) + 1;
}

// Helper function to build a sample complete binary tree
TreeNode* buildCompleteBinaryTree() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    return root;
}

int main() {
    TreeNode* root = buildCompleteBinaryTree();
    int height = heightCompleteBinaryTree(root);
    std::cout << "Height of the complete binary tree: " << height << std::endl;

    // Memory cleanup (important!)
    std::queue<TreeNode*> cleanupQueue;
    if (root) cleanupQueue.push(root);
    while (!cleanupQueue.empty()) {
        TreeNode* current = cleanupQueue.front();
        cleanupQueue.pop();
        if (current->left) cleanupQueue.push(current->left);
        if (current->right) cleanupQueue.push(current->right);
        delete current;
    }

    return 0;
}