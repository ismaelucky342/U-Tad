# Unit 4: Systems of Linear Equations

**Systems of linear equations** are collections of one or more linear equations involving the same set of variables. Solving systems of linear equations is essential in fields such as mathematics, economics, engineering, physics, and computer science. The methods covered include **graphical**, **substitution**, **elimination**, **matrix**, and **Cramer's Rule** solutions. Additionally, the concepts of **consistency** and **dependence** are crucial when analyzing the solutions to these systems.

### 1. **Definition of a System of Linear Equations**

A **system of linear equations** is a set of equations where each equation is linear, meaning it represents a straight line or hyperplane. A linear equation in `n` variables can be written as:

```
a1 * x1 + a2 * x2 + ... + an * xn = b
```

where `a1, a2, ..., an` are constants (coefficients), `x1, x2, ..., xn` are the variables, and `b` is the constant term. A system may have two, three, or more equations involving these variables.

Example of a system of two equations in two variables:

```
2x + 3y = 5
4x - y = 6
```

### 2. **Types of Solutions to a System of Linear Equations**

- **Consistent System**: A system has at least one solution. It can either be:
    - **Unique Solution**: There is exactly one set of values for the variables that satisfies all equations in the system.
    - **Infinitely Many Solutions**: There are an infinite number of solutions that satisfy the system.
- **Inconsistent System**: A system has no solution. This occurs when the equations are contradictory, i.e., they represent parallel lines or planes that never intersect.

### 3. **Methods for Solving Systems of Linear Equations**

#### 3.1 **Graphical Method**

- In this method, each equation in the system is graphed as a straight line (in two variables) or a plane (in three or more variables). The point(s) where the lines or planes intersect represent the solution(s) to the system.
- **Advantages**: Easy to understand and visualize.
- **Disadvantages**: Not suitable for solving systems with many variables or for precise solutions.

#### 3.2 **Substitution Method**

- This method involves solving one equation for one variable and substituting that expression into the other equations.
- **Steps**:
    1. Solve one equation for one variable.
    2. Substitute this expression into the other equation(s).
    3. Solve for the remaining variables.
    4. Substitute back to find all variables.
- **Example**:
    ```
    2x + 3y = 5  # Solve for x: x = (5 - 3y) / 2
    4x - y = 6
    ```
    Substituting `x` into the second equation, solve for `y`, and then substitute back to find `x`.

#### 3.3 **Elimination Method**

- In this method, the goal is to eliminate one variable by adding or subtracting equations.
- **Steps**:
    1. Multiply one or more equations by suitable numbers to make the coefficients of one of the variables the same (or opposites).
    2. Add or subtract the equations to eliminate that variable.
    3. Solve the resulting equation for the remaining variable.
    4. Substitute back to find all variables.
- **Example**:
    ```
    2x + 3y = 5
    4x - y = 6
    ```
    Multiply the second equation by 3 to align the `y`-terms:
    ```
    12x - 3y = 18
    ```
    Now, add the equations to eliminate `y`:
    ```
    (2x + 3y) + (12x - 3y) = 5 + 18
    ```

#### 3.4 **Matrix Method (Using Augmented Matrices)**

- Systems of linear equations can be represented using matrices. An augmented matrix contains both the coefficients of the variables and the constants from the equations.
- **Steps**:
    1. Write the system as an augmented matrix.
    2. Perform **row operations** to reduce the matrix to **row echelon form** or **reduced row echelon form**.
    3. Back-substitute to find the solution.
- **Example**:
    ```
    [ 2  3 |  5 ]
    [ 4 -1 |  6 ]
    ```
    Row operations are performed to reduce this matrix to row echelon form.

#### 3.5 **Cramer's Rule**

- Cramer's Rule is a method for solving a system of linear equations using **determinants**. It is only applicable to square systems (the number of equations equals the number of variables).
- The system of equations is written in matrix form `Ax = b`, where `A` is the coefficient matrix, `x` is the column matrix of variables, and `b` is the column matrix of constants.
- The solution for each variable is given by:
    ```
    xi = det(Ai) / det(A)
    ```
    where `Ai` is the matrix formed by replacing the `i`-th column of `A` with the column vector `b`.
- **Example**:
    ```
    2x + 3y = 5
    4x - y = 6
    ```
    The determinant of the coefficient matrix `A` and the modified matrices `A1` and `A2` are calculated, and the solutions for `x` and `y` are found.

### 4. **Types of Systems of Linear Equations**

- **Homogeneous System**: A system of linear equations is homogeneous if all the constant terms are zero (i.e., the system is of the form `Ax = 0`).
    - Homogeneous systems always have at least the trivial solution (`x1 = x2 = ... = xn = 0`).
    - If the determinant of the coefficient matrix is non-zero, the only solution is the trivial solution; otherwise, the system has infinitely many solutions.
- **Non-Homogeneous System**: A system where at least one of the constant terms is non-zero.

### 5. **Row Operations and Gaussian Elimination**

- **Row Operations** are used to manipulate augmented matrices and solve systems of linear equations. The three types of row operations are:
    1. **Row swapping**: Swap two rows.
    2. **Scaling a row**: Multiply a row by a non-zero scalar.
    3. **Row addition**: Add or subtract a multiple of one row from another.
- **Gaussian Elimination** is a method of reducing the augmented matrix to row echelon form (REF) using row operations. Once in REF, back-substitution is used to solve the system.
- **Reduced Row Echelon Form (RREF)**: A further simplified form of REF, where each leading entry is 1, and each column containing a leading entry has all other entries equal to zero.

### 6. **Properties of Linear Systems**

- **Existence of Solutions**: A system may have a **unique solution**, **no solution**, or **infinitely many solutions**. This is determined by the rank of the coefficient matrix and the augmented matrix.
    - If the rank of the coefficient matrix equals the rank of the augmented matrix and is equal to the number of unknowns, the system has a unique solution.
    - If the rank of the coefficient matrix equals the rank of the augmented matrix but is less than the number of unknowns, the system has infinitely many solutions.
    - If the rank of the coefficient matrix is less than the rank of the augmented matrix, the system is inconsistent and has no solution.

### 7. **Applications of Systems of Linear Equations**

- **Engineering**: Solving for unknowns in circuit analysis, stress and strain calculations, etc.
- **Economics**: Modeling economic systems, such as supply and demand, cost functions, and optimization problems.
- **Computer Graphics**: Solving transformations and projections in rendering models.
- **Network Theory**: Solving for flow, voltage, and other unknowns in networks.

### 8. **Numerical Methods for Solving Systems of Linear Equations**

In cases where analytical methods are impractical, numerical methods are used to approximate solutions. These methods are particularly useful for large systems or systems with no exact solutions.

#### 8.1 **Gauss-Seidel Method**

- An iterative method for solving a system of linear equations. It assumes an initial guess for the solution and refines it iteratively.
- **Steps**:
    1. Rearrange the equations so that the diagonal elements of the coefficient matrix are dominant.
    2. Use the current values of the variables to compute the next iteration.
    3. Repeat until the solution converges to a desired level of accuracy.
- **Advantages**: Simple to implement and computationally efficient for large, sparse systems.
- **Disadvantages**: Convergence is not guaranteed unless the system satisfies certain conditions (e.g., the coefficient matrix is diagonally dominant).

#### 8.2 **Jacobi Method**

- Another iterative method similar to the Gauss-Seidel method but updates all variables simultaneously using values from the previous iteration.
- **Steps**:
    1. Rearrange the equations to isolate each variable on the left-hand side.
    2. Use the values from the previous iteration to compute the next iteration for all variables.
    3. Repeat until convergence.
- **Advantages**: Easier to parallelize compared to the Gauss-Seidel method.
- **Disadvantages**: Slower convergence and requires more iterations.

#### 8.3 **LU Decomposition**

- A direct method that decomposes the coefficient matrix `A` into the product of a lower triangular matrix `L` and an upper triangular matrix `U`.
- **Steps**:
    1. Decompose `A` into `L` and `U`.
    2. Solve `Ly = b` using forward substitution.
    3. Solve `Ux = y` using back substitution.
- **Advantages**: Efficient for solving multiple systems with the same coefficient matrix but different constant terms.
- **Disadvantages**: Computationally expensive for very large systems.

#### 8.4 **Iterative Refinement**

- A technique to improve the accuracy of a solution obtained by a direct method.
- **Steps**:
    1. Solve the system using a direct method to obtain an initial solution.
    2. Compute the residual vector.
    3. Solve a correction equation for the residual.
    4. Update the solution and repeat until the residual is sufficiently small.

### 9. **Common Pitfalls and Tips**

- **Ill-Conditioned Systems**: Systems where small changes in the coefficients or constants lead to large changes in the solution. Use numerical methods with caution and consider scaling the system.
- **Round-Off Errors**: In numerical methods, round-off errors can accumulate and affect the accuracy of the solution. Use higher precision arithmetic if necessary.
- **Choosing the Right Method**: The choice of method depends on the size of the system, the properties of the coefficient matrix, and the desired accuracy.

### 10. **Software Tools for Solving Systems of Linear Equations**

- **MATLAB**: Provides built-in functions like `linsolve`, `inv`, and `mldivide` for solving linear systems.
- **Python (NumPy)**: The `numpy.linalg.solve` function is used for solving systems of linear equations.
- **R**: The `solve` function can handle linear systems.
- **Octave**: Similar to MATLAB, Octave provides functions for solving linear systems.
- **Wolfram Mathematica**: Offers symbolic and numerical solutions for linear systems.

These tools are widely used in academia and industry for solving complex systems efficiently.
