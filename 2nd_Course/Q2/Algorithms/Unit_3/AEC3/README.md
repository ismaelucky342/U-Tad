# AEC3: Circular Lists and Stacks

This project consists of two exercises that implement solutions to classic problems using efficient and recursive algorithms. The first exercise solves the Towers of Hanoi problem, while the second simulates the Russian Roulette game.

## Project Structure

```
/
├── src/
│   ├── hanoi.cpp       # Implementation of the Towers of Hanoi
│   ├── pila.cpp        # Implementation of the stack data structure
│   └── ruleta_rusa.cpp # Implementation of the Russian Roulette simulation
├── includes/
│   └── lib.hpp         # Header files, including macros and common functions
├── Makefile            # Build file to compile the project
└── [README.md](http://readme.md/)           # This file
```

## Exercise Descriptions

### 1. **Towers of Hanoi** (File: `hanoi.cpp`)

This function solves the Towers of Hanoi problem using a recursive algorithm. It moves a specified number of disks from a source stack to a destination stack, using an auxiliary stack.

### Prototype:

```cpp
void hanoi(int n, Stack &source, Stack &auxiliary, Stack &destination)
```

### Parameters:

- `n`: The number of disks to move.
- `source`: The source stack.
- `auxiliary`: The auxiliary stack.
- `destination`: The destination stack.

### Functionality:

- Receives the number of disks from the command line.
- Initializes three stacks (source, auxiliary, destination).
- Moves the disks using the recursive `hanoi` function.
- Prints the steps of the movement to the standard output.

### Complexity:

- **Time**: O(2^n), where `n` is the number of disks.
- **Space**: O(n), due to the recursive call stack.

## **Stacks in the Towers of Hanoi**

In the Towers of Hanoi game, we use stacks to represent the three rods (source, auxiliary, and destination). Imagine each rod as a stack of disks:

- **Push:** When you place a disk on a rod, you are "pushing" the disk onto the stack. The disk is placed on top of the others.
- **Pop:** When you move a disk from one rod to another, you are "popping" the disk from the stack. The top disk is removed.
- **LIFO (Last In, First Out):** You can only move the top disk of each rod. The last disk placed is the first one that can be moved.

The `Stack` class handles this. Within that class, you have the `push()` and `pop()` functions that perform these operations.

---

### 2. **Russian Roulette Simulation** (File: `ruleta_rusa.cpp`)

This exercise simulates the Russian Roulette game, allowing you to specify the number of chambers, the position of the bullet, and the number of spins before firing.

### Prototype:

```cpp
int main(int argc, char *argv[])
```

### Parameters (command line arguments):

- `<N>`: The number of chambers in the cylinder.
- `<bullet_pos>`: The initial position of the bullet.
- `<spins ...>`: The number of spins before firing.

### Functionality:

- Receives arguments from the command line.
- Validates the input values.
- Simulates the game, printing the result of each spin and shot.
- Prints the final result to the standard output.

### Complexity:

- **Time**: O(m), where `m` is the number of spins.
- **Space**: O(1), as constant space variables are used.

## **Explanation of Circular Lists in Russian Roulette**

In Russian Roulette, the revolver's cylinder is like a circular list. Imagine each chamber of the cylinder as a node in the list:

- **Circular:** The last chamber of the cylinder is connected to the first chamber, forming a circle.
- **Spin:** When you spin the cylinder, you are moving through the circular list. The bullet's position changes from one chamber to another.

In our program, we use `std::vector` to represent the cylinder, and the variable `current_position` holds the bullet's position. The `spin()` function modifies `current_position` to simulate the cylinder's spin. If the position reaches the end of the vector, it returns to the beginning, like a circle.

---

## Usage and Files

### Prerequisites

- A C++ compiler compatible with C++11 or higher.
- The C++ standard library (including `iostream`, `vector`, and `string`).

### Compilation

This project uses a `Makefile` for compilation. To compile the exercises, simply run:

```makefile
make
```

This will generate the `hanoi` and `ruleta` executables.

### Cleaning

To clean the files generated during compilation, run:

Bash

`make clean`

To recompile the project from scratch, run:

Bash

`make re`

## Additional Files

### `lib.hpp`

This file includes definitions of common functions, macros for terminal colors, and other utilities. It is used to avoid code duplication and improve project readability.

### `Makefile`

The `Makefile` automates the project's compilation. It is compatible with `g++` and generates the `hanoi` and `ruleta` executables.

## Running the Exercises

### Exercise 1: Towers of Hanoi

```bash
./hanoi <number_of_disks>
<number_of_disks>: The number of disks to move.
```

Example:

```makefile
./hanoi 3
```

### Exercise 2: Russian Roulette

```bash
`./ruleta <N> <bullet_pos> <spins ...>`

- `<N>`: The number of chambers.
- `<bullet_pos>`: The initial position of the bullet.
- `<spins ...>`: The spins before firing.
```

Example:

```
./ruleta 6 2 1 -2
```

## Extra

This project taught me how to solve classic problems using recursive algorithms and efficient data structures. In the Towers of Hanoi exercise, I learned to use stacks to simulate the movement of disks between three rods. In the Russian Roulette exercise, I understood how to simulate a revolver's cylinder using a circular list, which allowed me to practice data manipulation in cyclic structures. These exercises helped me improve my understanding of stacks, circular lists, and recursion.

![image](https://github.com/user-attachments/assets/a8443dae-b7f1-43eb-87a8-1d67c5e69409)

