# AEC3: Sorting Algorithms

This project involves the implementation of two sorting algorithms: **Selection Sort** and **Bubble Sort**. Both algorithms are fundamental in computer science and help understand the basic principles of data sorting.

## Project Structure

```
.
├── Makefile            # Build file for the project
├── includes/
│   └── Lib.hpp         # Header files with macros and common functions
├── src/
│   ├── ex01.cpp        # Implementation of the Selection Sort algorithm
│   ├── ex02.cpp        # Implementation of the Bubble Sort algorithm
└── README.md           # This file
```

## Exercise Descriptions

### **1. Selection Sort (File: `ex01.cpp`)**

This sorting algorithm finds the minimum value in the list and swaps it with the first element. It then repeats the process with the remaining elements until the list is completely sorted.

### **Prototype:**

```
void selection_sort(int arr[], int n);
```

### **Parameters:**

- `arr`: An array of integers.
- `n`: Size of the array.

### **How It Works:**

1. Select the minimum element from the unsorted list.
2. Swap it with the first unsorted element.
3. Repeat until the entire list is sorted.

### **Complexity:**

- **Time:** O(n^2) in all cases.
- **Space:** O(1) as it requires no additional memory.

---

### **2. Bubble Sort (File: `ex02.cpp`)**

This algorithm compares adjacent elements and swaps them if they are in the wrong order. The process is repeated until the array is completely sorted.

### **Prototype:**

```
void bubble_sort(int arr[], int n);
```

### **Parameters:**

- `arr`: An array of integers.
- `n`: Size of the array.

### **How It Works:**

1. Compare adjacent elements and swap if necessary.
2. Repeat until no more swaps are needed.

### **Complexity:**

- **Time:** O(n^2) in the worst and average cases, O(n) in the best case (when already sorted).
- **Space:** O(1) as it requires no additional memory.

---

## Usage and Files

### **Prerequisites**

- A C++ compiler compatible with C++11 or later.

### **Compilation**

The project uses a `Makefile` for compilation. To compile the exercises, simply run:

```
make
```

This will generate the executables `ex01` and `ex02`.

### **Cleaning**

To remove files generated during compilation, use:

```
make clean
```

To recompile everything from scratch:

```
make re
```

---

## **Running the Algorithms**

### **Exercise 1: Selection Sort**

```
./ex01 <numbers separated by space>
```

Example:

```
./ex01 5 3 8 6 2
```

### **Exercise 2: Bubble Sort**

```
./ex02 <numbers separated by space>
```

Example:

```
./ex02 7 1 4 9 2
```

---

## **Additional Explanation**

### **Selection Sort vs. Bubble Sort**

- **Selection Sort** is more efficient in terms of swaps, as it performs a minimum number of them (O(n)), though it still has a time complexity of O(n^2).
- **Bubble Sort** performs more swaps, making it less efficient in practice, but its implementation is simpler.

Both algorithms are educational and help understand sorting, though they are not the most efficient for large lists.

---

## **Extras**

These exercises help understand and compare different sorting approaches. While more efficient algorithms like QuickSort or MergeSort are used in practice, understanding the workings of these basic methods is essential for developing programming and algorithm analysis skills.

![image](https://github.com/user-attachments/assets/a8443dae-b7f1-43eb-87a8-1d67c5e69409)
