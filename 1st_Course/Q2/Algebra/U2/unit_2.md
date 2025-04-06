# Unit 2: Vectors

This unit introduces **vectors**, which are quantities that have both magnitude and direction. Vectors are essential in algebra, geometry, physics, and engineering. This unit covers the basic operations on vectors, their properties, and their geometric interpretations.

### 1. **Definition of Vectors**

- A **vector** is a mathematical object that has both **magnitude** (size) and **direction**. It is usually represented by an arrow in a geometric context, where:
    - The **length** of the arrow represents the magnitude.
    - The **direction** of the arrow represents the vector’s direction.
- Vectors are denoted by boldface letters (e.g., **v**, **u**, **w**) or with an arrow above them (e.g., `\vec{v}`).
- **Scalar**: A scalar is a quantity that only has magnitude, without direction (e.g., temperature, mass).

### 2. **Vector Notation and Representation**

- A vector in **2D** or **3D space** can be represented by its components. For example:
    - In 2D: `\vec{v} = (v_x, v_y)`
    - In 3D: `\vec{v} = (v_x, v_y, v_z)`
- Vectors can be represented in component form, where each component corresponds to the projection of the vector along the coordinate axes (x, y, z).

### 3. **Operations with Vectors**

- **Addition**: Vectors are added component-wise:
    - In 2D: `\vec{u} + \vec{v} = (u_x + v_x, u_y + v_y)`
    - In 3D: `\vec{u} + \vec{v} = (u_x + v_x, u_y + v_y, u_z + v_z)`

- **Subtraction**: Vectors are subtracted component-wise:
    - In 2D: `\vec{u} - \vec{v} = (u_x - v_x, u_y - v_y)`
    - In 3D: `\vec{u} - \vec{v} = (u_x - v_x, u_y - v_y, u_z - v_z)`

- **Scalar Multiplication**: A vector is multiplied by a scalar (a number) by multiplying each component of the vector:
    - In 2D: `c \cdot \vec{v} = (c \cdot v_x, c \cdot v_y)`
    - In 3D: `c \cdot \vec{v} = (c \cdot v_x, c \cdot v_y, c \cdot v_z)`

- **Dot Product (Scalar Product)**: The dot product of two vectors:
    - In 2D: `\vec{u} \cdot \vec{v} = u_x \cdot v_x + u_y \cdot v_y`
    - In 3D: `\vec{u} \cdot \vec{v} = u_x \cdot v_x + u_y \cdot v_y + u_z \cdot v_z`
    - The dot product gives a scalar value and is related to the **angle** between the two vectors.

- **Cross Product (Vector Product)**: The cross product of two vectors in 3D results in a new vector:
    ```
    \vec{u} \times \vec{v} = \begin{vmatrix} 
    \hat{i} & \hat{j} & \hat{k} \\ 
    u_x & u_y & u_z \\ 
    v_x & v_y & v_z 
    \end{vmatrix}
    ```
    where `\hat{i}`, `\hat{j}`, and `\hat{k}` are the unit vectors along the x, y, and z axes. The cross product gives a vector that is perpendicular to both `\vec{u}` and `\vec{v}`, with magnitude equal to the area of the parallelogram formed by the vectors.

### 4. **Magnitude of a Vector**

- The **magnitude** (or length) of a vector in 2D:
    ```
    |\vec{v}| = \sqrt{v_x^2 + v_y^2}
    ```
- In 3D:
    ```
    |\vec{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2}
    ```
- The magnitude represents the distance from the origin to the point described by the vector.

### 5. **Unit Vectors**

- A **unit vector** is a vector with a magnitude of 1. Any vector can be converted into a unit vector by dividing the vector by its magnitude:
    ```
    \hat{v} = \frac{\vec{v}}{|\vec{v}|}
    ```
- Unit vectors are often used to represent direction in space.

### 6. **Geometric Interpretation of Vectors**

- **Direction**: A vector’s direction is the angle it makes with the positive x-axis (or another reference direction).
- **Magnitude**: The magnitude of a vector is the length of the arrow representing the vector.
- **Angle Between Vectors**: The angle `\theta` between two vectors can be found using the **dot product**:
    ```
    \cos \theta = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}| |\vec{v}|}
    ```
- **Parallel and Perpendicular Vectors**:
    - Two vectors are **parallel** if they are scalar multiples of each other.
    - Two vectors are **perpendicular** (or orthogonal) if their dot product is zero.

### 7. **Vector Applications**

- **Displacement**: Vectors are used to represent displacement, which is a change in position.
- **Velocity and Acceleration**: In physics, velocity and acceleration are vector quantities, representing the rate of change of position and velocity, respectively.
- **Force**: Force is another vector quantity, where both the magnitude and direction matter.
- **Physics and Engineering**: Vectors are used extensively in mechanics, electromagnetism, and fluid dynamics to represent quantities like electric fields, magnetic fields, and forces.

### 8. **Vector Spaces**

- A **vector space** is a set of vectors that can be added together and multiplied by scalars, while satisfying certain axioms (such as commutativity, associativity, etc.).
- **Subspaces**: A subspace is a subset of a vector space that is also a vector space under the same operations.
```

```markdown
### 9. **Projection of Vectors**

- The **projection** of a vector `\vec{u}` onto another vector `\vec{v}` is a vector that represents the component of `\vec{u}` in the direction of `\vec{v}`.
- The formula for the projection is:
    ```
    \text{proj}_{\vec{v}} \vec{u} = \frac{\vec{u} \cdot \vec{v}}{|\vec{v}|^2} \cdot \vec{v}
    ```
- The projection is useful in applications such as physics (e.g., resolving forces) and computer graphics.

### 10. **Orthogonal Decomposition**

- Any vector `\vec{u}` can be decomposed into two components:
    - One parallel to a vector `\vec{v}`.
    - One perpendicular to `\vec{v}`.
- The decomposition is given by:
    ```
    \vec{u} = \text{proj}_{\vec{v}} \vec{u} + \vec{u}_{\perp}
    ```
    where `\vec{u}_{\perp} = \vec{u} - \text{proj}_{\vec{v}} \vec{u}`.

### 11. **Linear Independence**

- A set of vectors is said to be **linearly independent** if no vector in the set can be written as a linear combination of the others.
- If the vectors are linearly dependent, at least one vector can be expressed as a combination of the others.
- Linear independence is a key concept in understanding vector spaces and subspaces.

### 12. **Basis and Dimension**

- A **basis** of a vector space is a set of linearly independent vectors that span the entire space.
- The **dimension** of a vector space is the number of vectors in its basis.
- For example:
    - The standard basis for 2D space is `{(1, 0), (0, 1)}`.
    - The standard basis for 3D space is `{(1, 0, 0), (0, 1, 0), (0, 0, 1)}`.

### 13. **Applications in Computer Science**

- **Graphics and Animation**: Vectors are used to represent positions, directions, and transformations in 2D and 3D graphics.
- **Machine Learning**: Vectors represent data points in high-dimensional spaces.
- **Robotics**: Vectors are used to model motion, forces, and orientations.
- **Optimization**: Vectors are used in algorithms to find optimal solutions in multidimensional spaces.

