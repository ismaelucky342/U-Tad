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
    // If value is equal, we typically ignore it (no duplicates)
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

void inorderTraversal(TreeNode* root) {
    if (root != nullptr) {
        inorderTraversal(root->left);
        std::cout << root->val << " ";
        inorderTraversal(root->right);
    }
}

// Helper function for memory cleanup
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

    int searchVal = 40;
    TreeNode* searchResult = search(root, searchVal);
    if (searchResult) {
        std::cout << searchVal << " found in the BST." << std::endl;
    } else {
        std::cout << searchVal << " not found in the BST." << std::endl;
    }

    searchVal = 90;
    searchResult = search(root, searchVal);
    if (searchResult) {
        std::cout << searchVal << " found in the BST." << std::endl;
    } else {
        std::cout << searchVal << " not found in the BST." << std::endl;
    }

    deleteTree(root); // Clean up memory
    return 0;
}