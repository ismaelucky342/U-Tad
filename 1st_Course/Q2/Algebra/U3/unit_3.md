# Unit 3: Matrix and Determinants – Detailed Overview

This unit covers **matrix** and **determinants**, which are central concepts in linear algebra. matrix are rectangular arrays of numbers arranged in rows and columns, and determinants are scalar values that can be computed from a square matrix. Both matrix and determinants are used extensively in solving systems of linear equations, transformations, and in various areas of mathematics, physics, economics, and engineering.

### 1. **Definition of Matrix**

- A **matrix** is a rectangular array of numbers, organized in rows and columns. It is typically denoted by a capital letter, such as `A`, `B`, or `C`. A matrix with `m` rows and `n` columns is called an `m x n` matrix. The elements of a matrix are often written as `a[i][j]`, where `i` represents the row and `j` represents the column of the element.

    Example:
    ```plaintext
    A = [[a11, a12, a13],
         [a21, a22, a23],
         [a31, a32, a33]]
    ```
    This is a `3 x 3` matrix.

- **Order of a Matrix**: The order of a matrix is described by the number of rows and columns it has. An `m x n` matrix has `m` rows and `n` columns.

### 2. **Types of matrix**

- **Square Matrix**: A matrix is called a **square matrix** if the number of rows is equal to the number of columns, i.e., `m = n`.
- **Identity Matrix**: The identity matrix, denoted `I`, is a square matrix in which all the diagonal elements are `1`, and all other elements are `0`.

    Example:
    ```plaintext
    I = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]
    ```

- **Zero Matrix**: A zero matrix is a matrix in which all of its elements are zero. It can be of any order.

    Example:
    ```plaintext
    O = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    ```

- **Diagonal Matrix**: A diagonal matrix is a square matrix in which all elements outside the main diagonal are zero.

    Example:
    ```plaintext
    D = [[d1, 0, 0],
         [0, d2, 0],
         [0, 0, d3]]
    ```

- **Symmetric Matrix**: A matrix is symmetric if it is equal to its transpose, i.e., `A == A^T`.
- **Skew-Symmetric Matrix**: A matrix is skew-symmetric if it is equal to the negative of its transpose, i.e., `A == -A^T`.
- **Upper Triangular Matrix**: An upper triangular matrix is a square matrix in which all the elements below the main diagonal are zero.
- **Lower Triangular Matrix**: A lower triangular matrix is a square matrix in which all the elements above the main diagonal are zero.
- **Row Matrix**: A matrix with only one row is called a row matrix.
- **Column Matrix**: A matrix with only one column is called a column matrix.

### 3. **Matrix Operations**

- **Matrix Addition**: Two matrix of the same order can be added by adding their corresponding elements.

    Example:
    ```plaintext
    A = [[a11, a12],
         [a21, a22]]

    B = [[b11, b12],
         [b21, b22]]

    A + B = [[a11 + b11, a12 + b12],
             [a21 + b21, a22 + b22]]
    ```

- **Matrix Subtraction**: Matrix subtraction is performed by subtracting the corresponding elements of the matrix.

    Example:
    ```plaintext
    A - B = [[a11 - b11, a12 - b12],
             [a21 - b21, a22 - b22]]
    ```

- **Scalar Multiplication**: A matrix can be multiplied by a scalar by multiplying each element of the matrix by the scalar.

    Example:
    ```plaintext
    c * A = [[c * a11, c * a12],
             [c * a21, c * a22]]
    ```

- **Matrix Multiplication**: The multiplication of two matrix `A` and `B` is only possible if the number of columns of matrix `A` is equal to the number of rows of matrix `B`. If `A` is an `m x n` matrix and `B` is an `n x p` matrix, the product `C = A * B` is an `m x p` matrix, where each element is computed as:

    ```plaintext
    C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    ```

- **Transpose of a Matrix**: The transpose of a matrix `A`, denoted `A^T`, is obtained by swapping the rows and columns of `A`.

    Example:
    ```plaintext
    A = [[1, 2],
         [3, 4]]

    A^T = [[1, 3],
           [2, 4]]
    ```

- **Inverse of a Matrix**: The inverse of a square matrix `A`, denoted `A^-1`, is a matrix such that:

    ```plaintext
    A * A^-1 = I
    ```

    Not all matrix have an inverse. A matrix has an inverse if and only if its determinant is non-zero.

### 4. **Determinants**

- The **determinant** of a square matrix is a scalar value that is computed from the elements of the matrix and provides important properties such as whether a matrix is invertible. The determinant is denoted as `det(A)` or `|A|`.

    **For a 2x2 matrix**:
    ```plaintext
    A = [[a, b],
         [c, d]]

    det(A) = a * d - b * c
    ```

    **For a 3x3 matrix**:
    ```plaintext
    A = [[a, b, c],
         [d, e, f],
         [g, h, i]]

    det(A) = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    ```

- **Properties of Determinants**:
    1. `det(A^T) = det(A)`
    2. If `A` is a triangular matrix (upper or lower), `det(A)` is the product of the diagonal elements.
    3. If two rows (or columns) of a matrix are identical, the determinant is zero.
    4. If `A` and `B` are square matrix of the same size, then `det(A * B) = det(A) * det(B)`.
    5. The determinant of a matrix is zero if and only if the matrix is singular (not invertible).
    6. If a matrix has a row or column of zeros, its determinant is zero.

### 5. **Cofactor and Adjoint**

- **Cofactor**: The cofactor of an element `a[i][j]` of a matrix is the signed determinant of the matrix formed by removing the `i`-th row and `j`-th column, multiplied by `(-1)^(i+j)`.

    ```plaintext
    Cofactor of a[i][j] = (-1)^(i+j) * det(minor of a[i][j])
    ```

- **Adjoint (Adjugate) Matrix**: The adjoint (or adjugate) of a matrix `A` is the transpose of the cofactor matrix. It is used to find the inverse of a matrix.

    ```plaintext
    adj(A) = transpose of cofactor matrix of A
    ```

### 6. **Solving Systems of Linear Equations**

- **Cramer's Rule**: Cramer's Rule is a method used to solve a system of linear equations using the determinants of matrix. For a system `Ax = b`, where `A` is a square matrix, the solution for each variable is given by:

    ```plaintext
    x[i] = det(A_i) / det(A)
    ```

    where `A_i` is the matrix formed by replacing the `i`-th column of `A` with the vector `b`.

- **Matrix Inversion Method**: A system of linear equations `Ax = b` can be solved by finding the inverse of `A` (if it exists) and multiplying it by `b`:

    ```plaintext
    x = A^-1 * b
    ```

### 7. **Applications of matrix and Determinants**

- **Linear Systems**: matrix and determinants are used to solve systems of linear equations, particularly in the context of large systems where manual solutions are impractical.
- **Computer Graphics**: matrix are used in computer graphics for transformations, including rotations, scaling, and translations of objects.
- **Economics and Game Theory**: matrix are applied in models of economics and game theory, particularly in the representation of multi-variable problems.
- **Physics**: matrix are used to represent physical systems, particularly in quantum mechanics, electrical circuits, and optimization problems.

### 8. **Eigenvalues and Eigenvectors**

- **Eigenvalues**: For a square matrix `A`, an eigenvalue `λ` is a scalar that satisfies the equation:

    ```plaintext
    A * v = λ * v
    ```

    where `v` is a non-zero vector, called the **eigenvector**, that only changes in scale and not in direction.

- **Characteristic Equation**: The eigenvalues are found by solving the characteristic equation:

    ```plaintext
    det(A - λ * I) = 0
    ```

- **Diagonalization**: A matrix `A` can be diagonalized if it has enough eigenvectors to form a basis, and it can be written as:

    ```plaintext
    A = P * D * P^-1
    ```

    where `P` is the matrix of eigenvectors, and `D` is a diagonal matrix with the eigenvalues on the diagonal.

    ### 9. **Rank of a Matrix**

- **Definition**: The rank of a matrix is the maximum number of linearly independent rows or columns in the matrix. It provides important information about the solutions of a system of linear equations.

- **Full Rank**: A matrix is said to have full rank if its rank is equal to the smaller of the number of rows or columns.

- **Rank-Nullity Theorem**: For a matrix `A` of size `m x n`, the rank-nullity theorem states:

    ```plaintext
    rank(A) + nullity(A) = n
    ```

    where `nullity(A)` is the dimension of the null space of `A`.

### 10. **Applications of Eigenvalues and Eigenvectors**

- **Principal Component Analysis (PCA)**: Eigenvalues and eigenvectors are used in PCA, a dimensionality reduction technique in machine learning and data analysis.
- **Stability Analysis**: In control systems and differential equations, eigenvalues are used to analyze the stability of systems.
- **Quantum Mechanics**: Eigenvalues and eigenvectors are fundamental in quantum mechanics, where they represent observable quantities and their corresponding states.
- **Markov Chains**: In probability theory, eigenvalues and eigenvectors are used to study the long-term behavior of Markov chains.

### 11. **Singular Value Decomposition (SVD)**

- **Definition**: Singular Value Decomposition is a factorization of a matrix `A` into three matrix:

    ```plaintext
    A = U * Σ * V^T
    ```

    where:
    - `U` is an orthogonal matrix containing the left singular vectors.
    - `Σ` is a diagonal matrix containing the singular values.
    - `V^T` is the transpose of an orthogonal matrix containing the right singular vectors.

- **Applications**:
    - Data compression and noise reduction.
    - Solving ill-conditioned systems of linear equations.
    - Image processing and facial recognition.

### 12. **Norms of matrix**

- **Definition**: The norm of a matrix is a measure of its size or length. Common matrix norms include:
    - **Frobenius Norm**: The square root of the sum of the squares of all elements in the matrix.
    - **Spectral Norm**: The largest singular value of the matrix.
    - **Infinity Norm**: The maximum absolute row sum of the matrix.

    Example:
    ```plaintext
    Frobenius Norm of A = sqrt(sum(a[i][j]^2 for all i, j))
    ```

### 13. **LU Decomposition**

- **Definition**: LU decomposition is the factorization of a matrix `A` into the product of a lower triangular matrix `L` and an upper triangular matrix `U`:

    ```plaintext
    A = L * U
    ```

- **Applications**:
    - Solving systems of linear equations.
    - Computing the determinant and inverse of a matrix efficiently.

### 14. **Cholesky Decomposition**

- **Definition**: Cholesky decomposition is a special case of LU decomposition for symmetric, positive-definite matrix. It factors a matrix `A` as:

    ```plaintext
    A = L * L^T
    ```

    where `L` is a lower triangular matrix.

- **Applications**:
    - Numerical solutions of linear systems.
    - Optimization problems in machine learning.

### 15. **QR Decomposition**

- **Definition**: QR decomposition is the factorization of a matrix `A` into the product of an orthogonal matrix `Q` and an upper triangular matrix `R`:

    ```plaintext
    A = Q * R
    ```

- **Applications**:
    - Solving least squares problems.
    - Eigenvalue computations.

### 16. **Moore-Penrose Pseudoinverse**

- **Definition**: The Moore-Penrose pseudoinverse of a matrix `A`, denoted `A^+`, is a generalization of the inverse for non-square or singular matrix. It satisfies the following properties:

    ```plaintext
    A * A^+ * A = A
    A^+ * A * A^+ = A^+
    ```

- **Applications**:
    - Solving systems of linear equations that do not have a unique solution.
    - Machine learning algorithms, such as linear regression.

### 17. **Matrix Exponentials**

- **Definition**: The exponential of a square matrix `A` is defined as:

    ```plaintext
    exp(A) = I + A + (A^2 / 2!) + (A^3 / 3!) + ...
    ```

- **Applications**:
    - Solving systems of linear differential equations.
    - Modeling continuous-time Markov processes.
