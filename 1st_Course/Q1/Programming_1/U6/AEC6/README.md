# AEC6 - Matrix, Valley Elements and Trace

## 📋 Description

This C program is designed to work with a two-dimensional integer matrix and perform the following operations:

1. **Prints the original matrix** to provide a clear view of its structure.
2. **Calculates the trace** of the matrix, which is the sum of the elements on its main diagonal.
3. **Detects "valley" elements**, which are elements smaller than all their adjacent neighbors.
4. **Prints the valley element** along with its neighbors when one is detected.

This program is a great example of working with matrix in C, demonstrating concepts such as nested loops, relative indexing, and modular programming.

---

## 🧠 What is a Valley Element?

A **valley element** is a cell in the matrix that satisfies the following conditions:

1. **Not located on the edge** of the matrix (it must have 8 neighbors).
2. **Smaller than all its neighbors**, including those in horizontal, vertical, and diagonal directions.

For example:

```plaintext
7  6  8
5  3  6  ← 3 is a valley
9  7  5
```

In this example, the value `3` is a valley element because it is smaller than all its adjacent neighbors.

---

## 📌 Technical Details

- The matrix is defined with a fixed size of `5x4` for simplicity.
- The program uses **modular functions** to improve code readability and maintainability.
- **Relative indexing** is used to access and compare neighboring elements (`i ± 1`, `j ± 1`).
- The **trace** is calculated as the sum of the elements on the main diagonal: `matrix[0][0] + matrix[1][1] + ...`.

---

## ⚙️ Main Functions

| Function           | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `printMatrix`      | Prints the content of the matrix in a formatted way.                       |
| `isValleyElement`  | Determines if a specific position in the matrix is a valley element.       |
| `printValley`      | Prints the detected valley element along with its neighbors.               |
| `calculateTrace`   | Computes the sum of the elements on the main diagonal (matrix trace).      |

---

## 🖥️ Example Output

Here is an example of the program's output:

```bash
==> Values of the Original Matrix:
2  3  5  3
4  2  5  1
8  3  9  4
9  1  6  9
2  5  8  1

==> The trace of the matrix is: 22

==> There is a Valley element at row 1 column 1:
2  5  3
2  5  1
3  9  4

==> There is a Valley element at row 3 column 1:
3  9  4
1  6  9
5  8  1
```

---

## ✅ Compilation and Execution

To compile and execute the program, follow these steps:

1. Open a terminal and navigate to the directory containing the source code.
2. Compile the program using `gcc`:

    ```bash
    gcc -o matrix_valley main.c
    ```

3. Run the compiled program:

    ```bash
    ./matrix_valley
    ```

---

## 📚 Additional Notes

- **Edge Cases**: The program ensures that no edge elements are considered as valley elements since they lack the required number of neighbors.
- **Matrix Size**: While the matrix size is fixed at `5x4`, the program can be adapted to work with matrix of different sizes by modifying the size constants.
- **Error Handling**: The program assumes valid input and does not handle cases such as empty matrix or invalid dimensions.

This program is an excellent exercise for understanding matrix operations, nested loops, and modular programming in C.