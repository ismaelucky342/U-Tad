# Unit 5: Vector Spaces – Detailed Overview

**Vector spaces** are central to many areas of mathematics, physics, and engineering. A vector space is a collection of vectors that can be added together and multiplied by scalars, subject to certain conditions. The study of vector spaces provides the foundation for linear algebra and is essential for understanding structures in mathematics that are important for various scientific and engineering disciplines.

### 1. **Definition of a Vector Space**

A **vector space** (also called a **linear space**) is a set of vectors, along with two operations: **vector addition** and **scalar multiplication**. These operations must satisfy several properties (called **axioms**) that ensure the structure behaves in a certain way.

A vector space `V` over a field `F` must satisfy the following axioms:

1. **Closure under addition**: If `u` and `v` are vectors in `V`, then `u + v` is also in `V`.
2. **Closure under scalar multiplication**: If `v` is a vector in `V` and `c` is a scalar in `F`, then `c * v` is also in `V`.
3. **Commutativity of vector addition**: For any vectors `u` and `v`, `u + v = v + u`.
4. **Associativity of vector addition**: For any vectors `u`, `v`, and `w`, `(u + v) + w = u + (v + w)`.
5. **Existence of an additive identity**: There is a vector `0 ∈ V` such that `v + 0 = v` for all `v ∈ V`.
6. **Existence of additive inverses**: For every vector `v ∈ V`, there exists a vector `-v ∈ V` such that `v + (-v) = 0`.
7. **Distributivity of scalar multiplication over vector addition**: `c * (u + v) = c * u + c * v`.
8. **Distributivity of scalar multiplication over scalar addition**: `(c + d) * v = c * v + d * v`.
9. **Compatibility of scalar multiplication with field multiplication**: `c * (d * v) = (c * d) * v`.
10. **Existence of a multiplicative identity for scalars**: `1 * v = v`, where `1` is the multiplicative identity in `F`.

The field `F` is typically the set of real numbers `ℝ` or complex numbers `ℂ`, but it can be any field.

### 2. **Examples of Vector Spaces**

- **Euclidean Space** (`ℝ^n`): The set of all `n`-dimensional vectors with real components, where vector addition and scalar multiplication are performed component-wise.
    - Example: The space `ℝ^2` consists of all 2-dimensional vectors of the form `(x, y)`, where `x, y ∈ ℝ`.
- **Function Spaces**: The set of all continuous functions, polynomials, or other types of functions that satisfy the axioms of a vector space. For example, the space of all polynomials of degree `n` forms a vector space.
- **Matrices as Vectors**: The set of all `m × n` matrices forms a vector space under matrix addition and scalar multiplication.
- **Sequence Spaces**: The set of all infinite sequences of numbers forms a vector space under the usual addition and scalar multiplication operations.

### 3. **Subspaces**

A **subspace** is a subset of a vector space that is itself a vector space under the same operations. For a subset `W` of a vector space `V` to be a subspace, it must satisfy the following conditions:

- **Zero vector**: The zero vector of `V` must be in `W`.
- **Closed under addition**: If `u` and `v` are in `W`, then `u + v` must also be in `W`.
- **Closed under scalar multiplication**: If `v` is in `W` and `c` is a scalar, then `c * v` must be in `W`.

### 4. **Linear Combinations**

A **linear combination** of a set of vectors `{v₁, v₂, ..., vₖ}` is any vector that can be expressed as:

```
c₁ * v₁ + c₂ * v₂ + ... + cₖ * vₖ
```

where `c₁, c₂, ..., cₖ` are scalars. The set of all possible linear combinations of a set of vectors forms a **subspace** of the vector space.

### 5. **Span of a Set of Vectors**

The **span** of a set of vectors `{v₁, v₂, ..., vₖ}` is the set of all linear combinations of those vectors. It represents the smallest subspace of the vector space that contains all the given vectors. The span of a set of vectors is important because it describes the space that can be "reached" by scaling and adding the vectors in the set.

### 6. **Linear Independence and Dependence**

- **Linearly Independent Vectors**: A set of vectors `{v₁, v₂, ..., vₖ}` is said to be linearly independent if the only solution to the equation:

    ```
    c₁ * v₁ + c₂ * v₂ + ... + cₖ * vₖ = 0
    ```

    is `c₁ = c₂ = ... = cₖ = 0`. In other words, no vector in the set can be written as a linear combination of the others.

- **Linearly Dependent Vectors**: If there exist scalars `c₁, c₂, ..., cₖ`, not all zero, such that:

    ```
    c₁ * v₁ + c₂ * v₂ + ... + cₖ * vₖ = 0
    ```

    then the set of vectors is said to be linearly dependent. This means that at least one vector in the set can be written as a linear combination of the others.

### 7. **Basis of a Vector Space**

A **basis** of a vector space `V` is a set of linearly independent vectors that span the entire vector space. Any vector in the vector space can be written as a linear combination of the basis vectors. The number of vectors in the basis of a vector space is called the **dimension** of the vector space.

- **Example**: The standard basis of `ℝ³` is the set `{(1, 0, 0), (0, 1, 0), (0, 0, 1)}`, as these vectors are linearly independent and span the entire space.

### 8. **Dimension of a Vector Space**

The **dimension** of a vector space is the number of vectors in any basis for the space. It is a measure of the "size" of the space in terms of the number of independent directions it contains.

- For example, `ℝ³` has dimension 3, and the space of all polynomials of degree less than or equal to `n` has dimension `n + 1`.
- A vector space with finite dimension is called a **finite-dimensional vector space**. If the space has infinitely many basis vectors, it is called an **infinite-dimensional vector space**.

### 9. **Coordinate Systems and Change of Basis**

The **coordinates** of a vector relative to a basis are the scalars that multiply the basis vectors in a linear combination to express the vector. Changing the basis of a vector space is an important concept when working with vector spaces in different coordinate systems.

- **Change of Basis Matrix**: The transition between two different bases can be represented by a **change of basis matrix**, which allows the conversion of a vector’s coordinates from one basis to another.

### 10. **Applications of Vector Spaces**

Vector spaces have vast applications in many fields:

- **Physics**: Used in the representation of forces, velocities, and other vector quantities.
- **Engineering**: Applied in areas such as circuit analysis, mechanical systems, and signal processing.
- **Computer Science**: Essential in machine learning, computer graphics, and data science, where vector spaces model high-dimensional data.
- **Economics**: Used in modeling economic systems, optimization, and decision theory.

### 11. **Orthogonality and Orthonormality**

- **Orthogonal Vectors**: Two vectors `u` and `v` in a vector space are said to be orthogonal if their dot product is zero, i.e., `u · v = 0`. Orthogonality is a key concept in geometry and linear algebra, as it represents perpendicularity in Euclidean spaces.
- **Orthonormal Basis**: A basis is orthonormal if all its vectors are orthogonal to each other and each vector has a magnitude of 1. Orthonormal bases simplify computations in vector spaces, especially in applications like Fourier analysis and quantum mechanics.

### 12. **Inner Product Spaces**

An **inner product space** is a vector space equipped with an additional structure called an **inner product**. The inner product allows the definition of angles and lengths in the vector space. For vectors `u` and `v`, the inner product is denoted as `<u, v>` and satisfies the following properties:

1. **Linearity in the first argument**: `<au + bv, w> = a<u, w> + b<v, w>` for scalars `a` and `b`.
2. **Symmetry**: `<u, v> = <v, u>` (or conjugate symmetry in complex vector spaces).
3. **Positive-definiteness**: `<u, u> ≥ 0`, and `<u, u> = 0` if and only if `u = 0`.

### 13. **Projection of Vectors**

The **projection** of a vector `u` onto another vector `v` is given by:

```
proj_v(u) = (u · v / v · v) * v
```

Projections are widely used in applications such as computer graphics, signal processing, and solving systems of linear equations.

### 14. **Eigenvalues and Eigenvectors**

- **Eigenvalues**: A scalar `λ` is an eigenvalue of a linear transformation `T` if there exists a non-zero vector `v` such that `T(v) = λv`.
- **Eigenvectors**: The vector `v` associated with the eigenvalue `λ` is called an eigenvector. Eigenvalues and eigenvectors are fundamental in understanding the behavior of linear transformations and are used in areas like stability analysis, quantum mechanics, and principal component analysis.

### 15. **Norms and Metrics**

- **Norm**: A norm is a function that assigns a non-negative length or size to each vector in a vector space. Common norms include the Euclidean norm (`||v|| = sqrt(v · v)`) and the Manhattan norm (`||v||₁ = Σ|vᵢ|`).
- **Metric**: A metric defines a distance between two vectors in a vector space. For example, the Euclidean distance between vectors `u` and `v` is `||u - v||`.

### 16. **Dual Spaces**

The **dual space** of a vector space `V` is the set of all linear functionals on `V`. A linear functional is a linear map from `V` to its field of scalars. Dual spaces are important in advanced mathematics, particularly in functional analysis and differential geometry.

### 17. **Tensor Products**

The **tensor product** of two vector spaces `V` and `W` is a new vector space, denoted `V ⊗ W`, that allows the combination of vectors from `V` and `W` in a bilinear way. Tensor products are widely used in physics, particularly in quantum mechanics and relativity.

### 18. **Applications in Machine Learning**

Vector spaces are foundational in machine learning, where data points are often represented as vectors in high-dimensional spaces. Key applications include:

- **Principal Component Analysis (PCA)**: A technique to reduce the dimensionality of data while preserving as much variance as possible.
- **Word Embeddings**: Representing words as vectors in natural language processing to capture semantic relationships.
- **Neural Networks**: Operations in neural networks, such as matrix multiplications, rely on vector space concepts.

### 19. **Fourier and Wavelet Transforms**

Vector spaces provide the framework for Fourier and wavelet transforms, which are used to analyze signals in terms of their frequency components. These transforms are essential in fields like signal processing, image compression, and audio analysis.

### 20. **Advanced Topics**

- **Hilbert Spaces**: Infinite-dimensional inner product spaces that generalize Euclidean spaces and are used in quantum mechanics and functional analysis.
- **Banach Spaces**: Complete normed vector spaces that are central to modern analysis.
- **Representation Theory**: The study of how algebraic structures can be represented as transformations of vector spaces.

These advanced topics extend the utility of vector spaces to abstract and infinite-dimensional settings, enabling their application in cutting-edge research and technology.
