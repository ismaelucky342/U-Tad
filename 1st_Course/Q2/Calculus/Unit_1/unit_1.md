## **Introduction and Objectives**

This unit explores the building blocks of real mathematics: the **real number system** and **real-valued functions**.

You'll learn to:

- Classify different types of numbers.
- Perform operations like exponentiation, roots, and logarithms.
- Solve various types of inequalities.
- Understand and analyze functions using notation, graphs, and algebraic expressions.

By mastering these concepts, you’ll build a strong foundation for algebra, calculus, and applied math.

---

## 🔢 **Classification of Numbers**

1. **Natural Numbers (ℕ)**
    
    Counting numbers starting from 1.
    
    ```markdown
    Example: 1, 2, 3, 10, 100
    ```
    
2. **Integers (ℤ)**
    
    Whole numbers including zero and negatives.
    
    ```markdown
    Example: -3, -2, 0, 4, 11
    ```
    
3. **Rational Numbers (ℚ)**
    
    Can be written as a **fraction** of integers (a/b), with *b ≠ 0*.
    
    ```markdown
    Example: 1/2, -3/4, 5 (since 5 = 5/1), 0.25 (since 0.25 = 1/4)
    ```
    
4. **Irrational Numbers**
    
    Cannot be written as a fraction. Their decimal expansion is **non-repeating** and **non-terminating**.
    
    ```markdown
    Example: √2 ≈ 1.4142..., π ≈ 3.1415..., e ≈ 2.718...
    ```
    
5. **Real Numbers (ℝ)**
    
    The **set of all** rational and irrational numbers.
    
    ```markdown
    Example: -2, 0, 0.333..., √3, π
    ```

📌 **Summary:**

Real numbers include **every number** that can be placed on the number line — essential for graphing and solving real-world problems.

---

## ➕ **Operations**

### **Powers (Exponents)**

An exponent represents repeated multiplication.

```markdown
Example:
- 3^2 = 3 × 3 = 9
- (-2)^3 = -8
```

### **Roots (Radicals)**

The inverse of powers. The *square root* of a number is a value that, when squared, gives the original number.

```markdown
Example:
- √16 = 4 because 4^2 = 16
- ∛27 = 3 because 3^3 = 27
```

### **Logarithms**

The inverse of exponential functions.

```markdown
Example:
- log₂(8) = 3 because 2^3 = 8
- log₁₀(1000) = 3 because 10^3 = 1000
```

### **Absolute Value**

The distance of a number from zero, **always positive**.

```markdown
Example:
- |5| = 5, |-5| = 5
```

---

## ❗ **Inequalities**

Inequalities compare two expressions. Solving them means finding **all values of x** that make the inequality true.

### **Basic Operations**

- Add/subtract on both sides:  
  ```markdown
  x + 3 < 7 ⇒ x < 4
  ```
- Multiply/divide by a **positive**: sign **stays the same**.
- Multiply/divide by a **negative**: **reverse** the inequality sign.  
  ```markdown
  Example: -2x > 6 ⇒ x < -3
  ```

### **Types of Inequalities**

- **Linear Inequality:**  
  ```markdown
  2x + 1 > 5
  ```
- **Quadratic Inequality:**  
  ```markdown
  x^2 - 4x + 3 < 0
  ```
- **Rational Inequality:**  
  ```markdown
  1 / (x - 2) > 0
  ```
- **Compound Inequality:**  
  ```markdown
  1 < x ≤ 5
  ```

---

## 📈 **Functions**

### **Basic Concepts**

A **function** relates an input *x* to a unique output *f(x)*.

```markdown
Example:
f(x) = x^2 + 1

If x = 2, then f(2) = 2^2 + 1 = 5
```

### **Function Notation**

```markdown
f(x) = "function of x" — think of it as a machine that processes input values.
```

### **Key Elements of a Function**

- **Domain:** Set of valid inputs (x-values).  
  ```markdown
  Example: For f(x) = 1 / x, domain is x ≠ 0
  ```
- **Range:** Set of outputs (f(x)-values).
- **Intercepts:** Points where the graph crosses axes.  
  ```markdown
  Example: f(x) = x^2 - 4 has x-intercepts at x = ±2
  ```
- **Asymptotes:** Lines the graph approaches but never touches.
- **Monotonicity:** Whether a function is increasing, decreasing, or constant.
- **Intervals of Increase/Decrease:** Where the function rises or falls.

---

## 🔍 **Types of Functions**

### 1. **Algebraic Functions**

- **Polynomial:**  
  ```markdown
  f(x) = x^2 + 2x + 1
  ```
- **Rational:**  
  ```markdown
  f(x) = (x + 1) / (x - 2)
  ```
- **Radical:**  
  ```markdown
  f(x) = √(x + 3)
  ```

### 2. **Transcendental Functions**

- **Exponential:**  
  ```markdown
  f(x) = 2^x
  ```
- **Logarithmic:**  
  ```markdown
  f(x) = log₂(x)
  ```
- **Trigonometric:**  
  ```markdown
  f(x) = sin(x), cos(x), tan(x)
  ```

### 3. **Piecewise-Defined Functions**

Functions defined by **different expressions** over different intervals.

```markdown
Example:
f(x) = {
  x^2, if x < 0
  x + 1, if x ≥ 0
}
```

### 4. **Function Transformations & Composition**

- **Shifting:**  
  ```markdown
  f(x) = (x - 2)^2 shifts the graph right by 2.
  ```
- **Reflecting:**  
  ```markdown
  f(x) = -x^2 reflects over the x-axis.
  ```
- **Stretching:**  
  ```markdown
  f(x) = 3x^2 makes it "narrower".
  ```
- **Composing:**  
  ```markdown
  f(g(x)) means plugging g(x) into f.

  Example:
  Let f(x) = x^2 and g(x) = x + 1
  Then f(g(x)) = f(x + 1) = (x + 1)^2
  ```

### **Inverse Functions**

An **inverse function** reverses the operation of the original function. If \( f(x) \) maps \( x \) to \( y \), then the inverse \( f^{-1}(x) \) maps \( y \) back to \( x \).

#### **Properties of Inverse Functions**
- A function must be **one-to-one** (bijective) to have an inverse.
- The graph of \( f^{-1}(x) \) is a reflection of \( f(x) \) across the line \( y = x \).

#### **Finding the Inverse**
1. Replace \( f(x) \) with \( y \).
2. Swap \( x \) and \( y \).
3. Solve for \( y \).
4. Replace \( y \) with \( f^{-1}(x) \).

```markdown
Example:
f(x) = 2x + 3

Step 1: Replace f(x) with y:
y = 2x + 3

Step 2: Swap x and y:
x = 2y + 3

Step 3: Solve for y:
y = (x - 3) / 2

Step 4: Replace y with f⁻¹(x):
f⁻¹(x) = (x - 3) / 2
```

#### **Verifying Inverses**
To verify that \( f(x) \) and \( f^{-1}(x) \) are inverses:
- \( f(f^{-1}(x)) = x \)
- \( f^{-1}(f(x)) = x \)

---

### **Even and Odd Functions**

#### **Even Functions**
- Symmetric about the **y-axis**.
- \( f(-x) = f(x) \) for all \( x \) in the domain.

```markdown
Example:
f(x) = x^2
f(-x) = (-x)^2 = x^2
```

#### **Odd Functions**
- Symmetric about the **origin**.
- \( f(-x) = -f(x) \) for all \( x \) in the domain.

```markdown
Example:
f(x) = x^3
f(-x) = (-x)^3 = -x^3
```

#### **Neither Even Nor Odd**
Some functions are neither even nor odd.

```markdown
Example:
f(x) = x^2 + x
```

---

### **Piecewise Functions**

A **piecewise function** is defined by different expressions depending on the input value.

#### **Graphing Piecewise Functions**
1. Identify the intervals for each piece.
2. Plot each piece on the graph, ensuring continuity or discontinuity as defined.

```markdown
Example:
f(x) = {
    x^2, if x < 0
    2x + 1, if x ≥ 0
}
```

#### **Continuity of Piecewise Functions**
A piecewise function is **continuous** if there are no breaks or jumps in the graph.

```markdown
Example:
Check continuity at x = 0 for the above function:
- Left-hand limit: lim (x → 0⁻) f(x) = 0^2 = 0
- Right-hand limit: lim (x → 0⁺) f(x) = 2(0) + 1 = 1
- Since the limits are not equal, f(x) is discontinuous at x = 0.
```
