## **Unit 2: Sets**

### 📌 **1. What is a Set?**

A **set** is a well-defined collection of distinct objects or elements. The elements of a set can be anything: numbers, letters, people, or even other sets. In set theory, the collection is considered as a whole, and the order in which elements are listed does not matter.

### Key Properties of Sets:

- **Well-defined**: The elements of the set must be clearly identifiable.
- **Distinct**: Each element can only appear once in the set; duplicates are not allowed.

**Example of a set:**

```text
A = {1, 2, 3}  # A set of integers.
B = {'a', 'b', 'c'}  # A set of letters.
```

---

### 📝 **2. Set Notation**

- **Roster (or Tabular) Form**: A set is described by listing all its elements, enclosed in curly braces.

    ```text
    A = {1, 2, 3}
    ```

- **Set-builder Notation**: Describes a set by stating a property that all its elements share.

    ```text
    A = {x | x is an integer, 1 ≤ x ≤ 3}
    ```

    This means "A is the set of integers between 1 and 3, inclusive."

---

### 🔗 **3. Types of Sets**

- **Finite Set**: A set with a limited number of elements.

    ```text
    A = {1, 2, 3}  # Finite set.
    ```

- **Infinite Set**: A set with an unlimited number of elements.

    ```text
    B = {1, 2, 3, ...}  # Infinite set of all positive integers.
    ```

- **Empty Set (Null Set)**: A set with no elements. It is denoted by `∅` or `{}`.

    ```text
    C = ∅  # Empty set.
    ```

- **Singleton Set**: A set that contains exactly one element.

    ```text
    D = {5}  # Singleton set.
    ```

- **Universal Set**: The set that contains all the elements under consideration, usually denoted by `U`.

---

### 🧮 **4. Operations on Sets**

#### 4.1 **Union of Sets ( ∪ )**

The **union** of two sets, `A` and `B`, is the set of elements that are in **either** `A`, **or** `B`, or in both.

```text
A = {1, 2, 3}
B = {3, 4, 5}
A ∪ B = {1, 2, 3, 4, 5}
```

#### 4.2 **Intersection of Sets ( ∩ )**

The **intersection** of two sets, `A` and `B`, is the set of elements that are **common** to both `A` and `B`.

```text
A = {1, 2, 3}
B = {3, 4, 5}
A ∩ B = {3}
```

#### 4.3 **Difference of Sets ( − )**

The **difference** of two sets, `A` and `B`, is the set of elements that are in `A` but not in `B`.

```text
A = {1, 2, 3}
B = {2, 3, 4}
A - B = {1}
```

#### 4.4 **Complement of a Set**

The **complement** of a set `A` (with respect to a universal set `U`) is the set of all elements in `U` that are not in `A`.

```text
A = {1, 2, 3}
U = {1, 2, 3, 4, 5}
A' = {4, 5}
```

---

### 🔢 **5. Venn Diagrams**

A **Venn diagram** is a visual representation of sets and their relationships. Each set is represented by a circle, and the placement of the circles shows the union, intersection, and difference between the sets.

#### Example:

- A **union** of two sets `A ∪ B` is represented by two overlapping circles, where the area inside both circles is shaded.
- An **intersection** `A ∩ B` is represented by the overlapping area of the two circles.
- The **difference** `A - B` is represented by the part of circle `A` that does not overlap with circle `B`.

---

### 🔄 **6. Subsets**

A set `A` is said to be a **subset** of a set `B` if every element of `A` is also an element of `B`.

```text
A = {1, 2}
B = {1, 2, 3}
A ⊆ B  # A is a subset of B.
```

A set `A` is a **proper subset** of `B` if `A ⊆ B` but `A ≠ B`.

```text
A = {1, 2}
B = {1, 2, 3}
A ⊂ B  # A is a proper subset of B.
```

---

### 🌐 **7. Power Set**

The **power set** of a set `A` is the set of all possible subsets of `A`, including the empty set and `A` itself.

```text
A = {1, 2}
P(A) = {∅, {1}, {2}, {1, 2}}
```

---

### 🔀 **8. Cartesian Product**

The **Cartesian product** of two sets `A` and `B`, denoted by `A × B`, is the set of ordered pairs where the first element comes from `A` and the second element comes from `B`.

```text
A = {1, 2}
B = {'x', 'y'}
A × B = {(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')}
```

---

### 🧑‍🏫 **9. Applications of Set Theory**

Set theory is widely used in various fields:

- **Mathematics**: To define structures like groups, rings, and vector spaces.
- **Computer Science**: In databases (SQL queries, set operations), algorithms, and data structures (hash sets, trees).
- **Logic**: In formal systems and reasoning.
- **Probability**: In calculating probabilities, where events are sets of outcomes.
- **Linguistics**: In analyzing languages as sets of words or phonemes.
- **Artificial Intelligence**: In knowledge representation and reasoning.

---

### 📚 **10. Advanced Topics in Set Theory**

- **Cardinality**: The number of elements in a set. For finite sets, it is simply the count of elements. For infinite sets, cardinality is used to compare sizes (e.g., countable vs. uncountable infinity).
- **Relations and Functions**: Sets are used to define relations and functions, which are fundamental in mathematics and computer science.
- **Zermelo-Fraenkel Set Theory (ZF)**: A formal system that provides axioms for set theory, including the Axiom of Choice.
- **Applications in Topology**: Sets are used to define open and closed sets, which are foundational in topology.

