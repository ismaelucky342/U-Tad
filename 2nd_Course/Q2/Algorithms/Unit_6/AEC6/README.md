# AEC6: Genetic Algorithms and Graphs

This repository contains the implementation of two programming exercises:

## Exercise 1: Polynomial Roots Using Genetic Algorithms

### Description

This program implements a genetic algorithm to find a root of a given polynomial. A `Polynomial` class is defined to represent and evaluate polynomials. The genetic algorithm is implemented recursively in the `findRootRecursive` method.

### Code Structure

* `includes/polynomial.hpp`: Defines the interface for the `Polynomial` class and the auxiliary `PartialSolution` class.
* `src/Exercise_1/Polynomial.cpp`: Implements the methods of the `Polynomial` class.
* `src/Exercise_1/main.cpp`: Contains the `main` function that reads the input, creates a `Polynomial` object, and executes the genetic algorithm to find a root.

### `Polynomial` Class

* **Attributes:**
    * `degree`: Integer representing the degree of the polynomial.
    * `coefficients`: Pointer to an array of floats storing the polynomial's coefficients. The coefficient of the term of degree `i` is located at position `i` in the array.
* **Constructor:**
    * Receives the degree of the polynomial and a pointer to the coefficients array.
    * Copies the provided coefficients into its own internal array.
* **Public Methods:**
    * `evaluate(float x)`: Evaluates the polynomial for a given `x` value and returns the result (float).
    * `findRootRecursive(PartialSolution parent)`: Implements the recursive genetic algorithm to find a root of the polynomial. Receives a `PartialSolution` as the parent and returns an `x` value as the solution.

### `PartialSolution` Class

* Represents a partial solution in the genetic algorithm, containing an `x` value and the polynomial's value evaluated at `x` (the "y").
* Must have a method to print its contents in the specified format.

### Genetic Algorithm

1. The initial partial solution is `x = 0`.
2. In each generation, 10 children are created by mutating the parent.
3. A child's mutation is performed by adding a mutation value (generated from a standard normal distribution) to the parent's `x`.
4. Only the child with the smallest absolute value of `p(x)` (the best partial solution) survives to the next generation.
5. The algorithm stops when, in a generation, all children are worse than the parent (have an absolute value of `p(x)` greater than or equal to the parent's). The parent's `x` at that point is considered the found root.
6. In each iteration (generation), the parent's `x` and `p(x)` are printed to the screen using the `PartialSolution` print method.

### Input

The input consists of three parts:

1. An integer representing the random seed to initialize `rand()`.
2. An integer `n` indicating the number of coefficients in the polynomial.
3. A list of `n` numbers (floats) representing the polynomial's coefficients.

### Output

The output consists of one line per iteration of the genetic algorithm, showing the parent's `x` and `p(x)` in each generation, in the format specified in the example.

### Compilation

A `Makefile` is provided to facilitate project compilation. To compile, simply run the `make` command in the repository's root directory. The executable for Exercise 1 will be generated in the `bin` folder with the name `Exercise_1`.

### Execution

To run the Exercise 1 program, use the following syntax from the command line:

```bash
./bin/Exercise_1 < input_file.txt
```

Where `input_file.txt` contains the input data in the specified format.

## Exercise 2: Red-White Graph

### Description

This program determines whether a given graph can be colored with two colors (red and white) such that no two adjacent vertices (connected by an edge) have the same color. This type of graph is known as a bipartite graph or "red-white" graph in the context of this exercise.

### Code Structure

- `src/Exercise_2/Graph.cpp`: Contains the implementation of the logic to determine if the graph is red-white. Although the file name is "Graph," the implementation should work for general graphs, not necessarily trees.

### Algorithm

The algorithm to determine if a graph is bipartite can be based on traversal techniques like Breadth-First Search (BFS) or Depth-First Search (DFS). The main idea is:

1. Start with an uncolored vertex and assign it a color (e.g., red).
2. Traverse its neighbors and assign them the opposite color (white).
3. Continue the traversal, assigning alternate colors to the neighbors of already colored vertices.
4. If at any point a vertex is attempted to be colored with the same color as its neighbor, the graph is not bipartite.
5. If the traversal completes without finding color conflicts, the graph is bipartite.
6. It is important to consider that the graph may have multiple connected components, so the process must be repeated for each unvisited component.

### Input

The input consists of multiple test cases. For each case:

1. The first line contains an integer `V` (between 1 and 100), the number of vertices in the graph.
2. The second line contains an integer `E`, the number of edges in the graph.
3. The next `E` lines contain two integers each, representing the endpoints (indices between 0 and `V-1`) of each edge.
4. The input ends when the number of vertices `V` is 0.

### Output

For each test case, the program must print "YES" if the graph can be colored red-white, and "NO" otherwise.

### Compilation

As with Exercise 1, the `Makefile` is expected to also compile the code for Exercise 2, generating an executable in the `bin` folder with an appropriate name (e.g., `Exercise_2`).

### Execution

To run the Exercise 2 program, use a similar syntax:

```bash
./bin/Exercise_2 < input_file.txt
```

Where `input_file.txt` contains the input data for the test cases.

# Extra
![alt text](image.png)
