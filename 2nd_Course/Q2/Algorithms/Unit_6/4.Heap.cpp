#include <iostream>
#include <vector>
#include <algorithm> // For std::push_heap, std::pop_heap, std::make_heap

class MinHeap {
private:
    std::vector<int> heap;

    // Helper function to get the parent index
    int parent(int i) {
        return (i - 1) / 2;
    }

    // Helper function to get the left child index
    int leftChild(int i) {
        return (2 * i) + 1;
    }

    // Helper function to get the right child index
    int rightChild(int i) {
        return (2 * i) + 2;
    }

    // Helper function to heapify up (for insertion)
    void heapifyUp(int i) {
        while (i > 0 && heap[i] < heap[parent(i)]) {
            std::swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }

    // Helper function to heapify down (for extraction)
    void heapifyDown(int i) {
        int smallest = i;
        int left = leftChild(i);
        int right = rightChild(i);

        if (left < heap.size() && heap[left] < heap[smallest]) {
            smallest = left;
        }

        if (right < heap.size() && heap[right] < heap[smallest]) {
            smallest = right;
        }

        if (smallest != i) {
            std::swap(heap[i], heap[smallest]);
            heapifyDown(smallest);
        }
    }

public:
    MinHeap() {}

    // Insert a value into the min-heap
    void insert(int value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }

    // Get the minimum value (root)
    int peekMin() {
        if (isEmpty()) {
            std::cerr << "Heap is empty!" << std::endl;
            return -1; // Or throw an exception
        }
        return heap[0];
    }

    // Extract the minimum value (root)
    int extractMin() {
        if (isEmpty()) {
            std::cerr << "Heap is empty!" << std::endl;
            return -1; // Or throw an exception
        }
        if (heap.size() == 1) {
            int min = heap[0];
            heap.pop_back();
            return min;
        }
        int min = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
        return min;
    }

    // Check if the heap is empty
    bool isEmpty() {
        return heap.empty();
    }

    // Get the size of the heap
    int size() {
        return heap.size();
    }

    // Print the heap (for visualization - array representation)
    void printHeap() {
        std::cout << "Heap (array representation): ";
        for (int val : heap) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    MinHeap minHeap;

    std::cout << "Inserting elements..." << std::endl;
    minHeap.insert(4);
    minHeap.insert(2);
    minHeap.insert(7);
    minHeap.insert(1);
    minHeap.insert(5);
    minHeap.insert(3);
    minHeap.printHeap(); // Output: Heap (array representation): 1 2 3 4 5 7

    std::cout << "Peeking min: " << minHeap.peekMin() << std::endl; // Output: Peeking min: 1

    std::cout << "Extracting min..." << std::endl;
    std::cout << "Extracted: " << minHeap.extractMin() << std::endl; // Output: Extracted: 1
    minHeap.printHeap(); // Output: Heap (array representation): 2 4 3 7 5

    std::cout << "Extracting min..." << std::endl;
    std::cout << "Extracted: " << minHeap.extractMin() << std::endl; // Output: Extracted: 2
    minHeap.printHeap(); // Output: Heap (array representation): 3 4 5 7

    std::cout << "Size of heap: " << minHeap.size() << std::endl; // Output: Size of heap: 4

    return 0;
}