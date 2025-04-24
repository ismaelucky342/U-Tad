#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int value) : val(value), left(nullptr), right(nullptr) {}
};

TreeNode* insert(TreeNode* root, int value) {
    if (root == nullptr) {
        return new TreeNode(value);
    }
    if (value < root->val) {
        root->left = insert(root->left, value);
    } else if (value > root->val) {
        root->right = insert(root->right, value);
    }
    return root;
}

TreeNode* search(TreeNode* root, int value) {
    if (root == nullptr || root->val == value) {
        return root;
    }
    if (value < root->val) {
        return search(root->left, value);
    } else {
        return search(root->right, value);
    }
}

TreeNode* findMin(TreeNode* root) {
    while (root != nullptr && root->left != nullptr) {
        root = root->left;
    }
    return root;
}

TreeNode* findMax(TreeNode* root) {
    while (root != nullptr && root->right != nullptr) {
        root = root->right;
    }
    return root;
}

void inorderTraversal(TreeNode* root) {
    if (root != nullptr) {
        inorderTraversal(root->left);
        std::cout << root->val << " ";
        inorderTraversal(root->right);
    }
}

TreeNode* deleteNode(TreeNode* root, int value) {
    if (root == nullptr) {
        return root;
    }

    if (value < root->val) {
        root->left = deleteNode(root->left, value);
    } else if (value > root->val) {
        root->right = deleteNode(root->right, value);
    } else {
        // Node with the value to be deleted found

        // Case 1: Node has no children or only one child
        if (root->left == nullptr) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
        } else if (root->right == nullptr) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
        }

        // Case 2: Node has two children
        // Find the inorder successor (smallest node in the right subtree)
        TreeNode* successor = findMin(root->right);

        // Copy the inorder successor's value to this node
        root->val = successor->val;

        // Delete the inorder successor
        root->right = deleteNode(root->right, successor->val);
    }
    return root;
}

void deleteTree(TreeNode* root) {
    if (root == nullptr) return;
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

int main() {
    TreeNode* root = nullptr;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    std::cout << "Inorder traversal of the BST: ";
    inorderTraversal(root);
    std::cout << std::endl; // Output: 20 30 40 50 60 70 80

    std::cout << "Minimum value: " << findMin(root)->val << std::endl; // Output: 20
    std::cout << "Maximum value: " << findMax(root)->val << std::endl; // Output: 80

    std::cout << "Deleting node with value 30..." << std::endl;
    root = deleteNode(root, 30);
    std::cout << "Inorder traversal after deletion: ";
    inorderTraversal(root);
    std::cout << std::endl; // Output: 20 40 50 60 70 80

    std::cout << "Deleting node with value 70..." << std::endl;
    root = deleteNode(root, 70);
    std::cout << "Inorder traversal after deletion: ";
    inorderTraversal(root);
    std::cout << std::endl; // Output: 20 40 50 60 80

    std::cout << "Deleting root node with value 50..." << std::endl;
    root = deleteNode(root, 50);
    std::cout << "Inorder traversal after deletion: ";
    inorderTraversal(root);
    std::cout << std::endl; // Output: 20 40 60 80

    deleteTree(root); // Clean up memory
    return 0;
}