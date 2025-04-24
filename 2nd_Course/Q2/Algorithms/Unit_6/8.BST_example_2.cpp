#include <iostream>
#include <algorithm> // For std::max

struct AVLNode {
    int val;
    AVLNode* left;
    AVLNode* right;
    int height;

    AVLNode(int value) : val(value), left(nullptr), right(nullptr), height(1) {}
};

// Function to get the height of a node (handles null nodes)
int height(AVLNode* node) {
    if (node == nullptr) {
        return 0;
    }
    return node->height;
}

// Function to get the balance factor of a node
int getBalance(AVLNode* node) {
    if (node == nullptr) {
        return 0;
    }
    return height(node->left) - height(node->right);
}

// Function to update the height of a node
void updateHeight(AVLNode* node) {
    if (node != nullptr) {
        node->height = 1 + std::max(height(node->left), height(node->right));
    }
}

// Left Rotation
AVLNode* leftRotate(AVLNode* y) {
    AVLNode* x = y->right;
    AVLNode* T2 = x->left;

    // Perform rotation
    x->left = y;
    y->right = T2;

    // Update heights
    updateHeight(y);
    updateHeight(x);

    // Return new root
    return x;
}

// Right Rotation
AVLNode* rightRotate(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* T2 = x->right;

    // Perform rotation
    x->right = y;
    y->left = T2;

    // Update heights
    updateHeight(y);
    updateHeight(x);

    // Return new root
    return x;
}

// Left-Right Rotation
AVLNode* leftRightRotate(AVLNode* z) {
    z->left = leftRotate(z->left);
    return rightRotate(z);
}

// Right-Left Rotation
AVLNode* rightLeftRotate(AVLNode* z) {
    z->right = rightRotate(z->right);
    return leftRotate(z);
}

// Insert function (skeleton - balance checks and rotations needed)
AVLNode* insertAVL(AVLNode* root, int value) {
    // Standard BST insertion
    if (root == nullptr) {
        return new AVLNode(value);
    }
    if (value < root->val) {
        root->left = insertAVL(root->left, value);
    } else if (value > root->val) {
        root->right = insertAVL(root->right, value);
    } else {
        return root; // Duplicate values not allowed
    }

    // Update height of current node
    updateHeight(root);

    // Get the balance factor to check if this node became unbalanced
    int balance = getBalance(root);

    // Left Left Case
    if (balance > 1 && value < root->left->val) {
        return rightRotate(root);
    }

    // Right Right Case
    if (balance < -1 && value > root->right->val) {
        return leftRotate(root);
    }

    // Left Right Case
    if (balance > 1 && value > root->left->val) {
        return leftRightRotate(root);
    }

    // Right Left Case
    if (balance < -1 && value < root->right->val) {
        return rightLeftRotate(root);
    }

    return root;
}

void preOrder(AVLNode* root) {
    if (root != nullptr) {
        std::cout << root->val << "(" << getBalance(root) << ") ";
        preOrder(root->left);
        preOrder(root->right);
    }
}

void deleteAVLTree(AVLNode* root) {
    if (root == nullptr) return;
    deleteAVLTree(root->left);
    deleteAVLTree(root->right);
    delete root;
}

int main() {
    AVLNode* root = nullptr;

    root = insertAVL(root, 10);
    root = insertAVL(root, 20);
    root = insertAVL(root, 30);
    root = insertAVL(root, 40);
    root = insertAVL(root, 50);
    root = insertAVL(root, 25);

    std::cout << "Preorder traversal of the AVL tree (with balance factors): ";
    preOrder(root);
    std::cout << std::endl;

    deleteAVLTree(root);
    return 0;
}