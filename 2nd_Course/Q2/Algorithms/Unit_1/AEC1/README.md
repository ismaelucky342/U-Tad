## Project Description

This project includes two exercises designed to practice basic algorithmic thinking and C++ programming skills. Each exercise should be implemented in a separate `.cpp` file, and the program logic should follow good programming practices. Each function is well-documented, includes preconditions (if applicable), and performs an analysis of its time and space complexity.

### Exercise 1: Sum of First N Numbers

In this exercise, you are tasked with writing a program that reads a positive integer and calculates the sum of all numbers from 1 to that number.

### Input:

- A positive integer `n`.

### Output:

- The sum of the integers from 1 to `n`.

### Example:

**Input**:

```
5
```

**Output**:

```
15
```

### Exercise 2: Palindrome Checker

In this exercise, the goal is to write a program that reads a string and checks if it is a palindrome (i.e., it reads the same forwards and backwards).

### Input:

- A string of up to 20 characters.

### Output:

- `1` if the string is a palindrome.
- `0` if the string is not a palindrome.

## Requirements

- Each function must include a description of its purpose, preconditions (if applicable), and an analysis of its time and space complexity.
- The code must be organized into separate files, with clear names for each exercise (e.g., `SumFirstNNumbers.cpp` and `Palindrome.cpp`).
- Follow the best programming practices provided in the course, and ensure the code is well-commented.
- Submit the files via the specified platforms (Blackboard).

## Files in the Project

```
bash

AEC1/
├── src/
│   ├── SumFirstNNumbers.cpp    # Sum of First N Numbers exercise
│   └── Palindrome.cpp          # Palindrome Checker exercise
├── Makefile                    # Makefile for compilation
└── README                      # This README file

```

## Instructions

### Compilation

To compile the project, use the provided `Makefile`. Run the following command:

```bash
make
```

This will compile the source files and generate the corresponding executables for both exercises.

### Running the Programs:

1. **Sum of First N Numbers**: To run the program that calculates the sum of the first `n` numbers, execute:

```bash
./SumFirstNNumbers
```

The program will prompt for a positive integer and then calculate and display the sum of all integers from 1 to that number.

1. **Palindrome Checker**: To run the palindrome checker program, execute:

```bash
./Palindrome
```

It will prompt for a string, and the program will check if it is a palindrome, displaying `1` for palindromes and `0` otherwise.

---

## Makefile

The `Makefile` includes the following targets:

- **all**: The default target that compiles the source files and generates the executables `SumFirstNNumbers` and `Palindrome`.
- **clean**: Removes the generated object files and executables, cleaning the project directory.

### Usage

1. **To compile the program:**

```bash
make
```

1. **To clean the project:**

```bash
make clean
```

---

## License

This project is licensed under the [MIT License](https://www.notion.so/LICENSE). You are free to use, modify, and distribute the code in this repository as long as you include the original license. This license applies to all files in the repository.

---

## Activity Description and Evaluation Criteria

### 1. Sum of First N Numbers

- **Objective**: Write a program that reads an integer `n` and calculates the sum of numbers from 1 to `n`.
- **Input**: A positive integer `n`.
- **Output**: The sum of the numbers from 1 to `n`.
- **Requirements**:
    - Each function must include a description of its purpose.
    - Preconditions must be indicated via exceptions (if applicable).
    - An analysis of the time and space complexity must be provided for each function.

### 2. Palindrome Checker

- **Objective**: Write a program that checks if a string is a palindrome (reads the same forwards and backwards).
- **Input**: A string with a maximum length of 20 characters.
- **Output**: `1` if the string is a palindrome, `0` otherwise.
- **Requirements**:
    - Each function must include a description of its purpose.
    - Preconditions must be indicated via exceptions (if applicable).
    - An analysis of the time and space complexity must be provided for each function.

### Evaluation Criteria:

- **Functionality**: Does the program correctly implement the requested tasks?
- **Code Quality**: Is the code well-organized and well-commented? Does it follow best practices?
- **Error Handling**: Does the program handle invalid inputs (e.g., non-positive integers or empty strings) appropriately?
- **Efficiency**: Does the program consider the time and space complexity of the implemented algorithms?

## Extras
Throughout this project, I have gained valuable insights into the practical application of fundamental programming concepts in C++, including algorithmic thinking, function design, error handling, and efficiency analysis. 
![image](https://github.com/user-attachments/assets/a8443dae-b7f1-43eb-87a8-1d67c5e69409)
