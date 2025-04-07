## Unit 4: Function Interpolation

---

### 🎯 Introduction and Objectives

In this unit, you will:

- Understand how to graph functions and identify their key features.
- Learn how to trace curves based on asymptotic and derivative behavior.
- Explore Taylor and Maclaurin polynomials as approximations of functions.
- Learn how to construct Taylor polynomials and estimate their error.

---

### 🧾 Graphical Representation of Functions

### 📌 Introduction

Graphing a function is essential for visualizing its behavior. Before sketching, it’s important to understand its basic properties, such as domain, continuity, asymptotes, and derivative signs.

### 📉 Asymptotes

Asymptotes are lines that the graph of a function approaches but never touches. There are three types:

1. **Vertical Asymptotes**:

    Occur when the function tends to infinity as \(x\) approaches a certain value.

    Example:

    ```math
    f(x) = \frac{1}{x} \Rightarrow \text{Vertical asymptote at } x = 0
    ```

2. **Horizontal Asymptotes**:

    Describe the behavior of the function as \(x \to \pm\infty\).

    Example:

    ```math
    f(x) = \frac{2x + 3}{x + 1} \Rightarrow \text{Horizontal asymptote at } y = 2
    ```

3. **Oblique (Slant) Asymptotes**:

    Occur when the degree of the numerator is one more than the denominator.

    Use polynomial division to find them.

### ✏️ Curve Sketching Guide

To sketch a function accurately:

1. **Find the domain**
2. **Identify intercepts** (x and y)
3. **Determine asymptotes**
4. **Compute the first derivative**
    - Analyze increasing/decreasing behavior
    - Locate local maxima/minima
5. **Compute the second derivative**
    - Find concavity and inflection points
6. **Plot key points and sketch based on all gathered information**

---

### 🧮 Taylor and Maclaurin Polynomials

### 📌 Introduction

Taylor and Maclaurin polynomials allow us to approximate functions using polynomials. These approximations are especially useful when functions are complex or do not have elementary forms.

### 🧠 Taylor Polynomial

The **Taylor polynomial** of degree \(n\) for a function \(f(x)\) centered at \(x = a\) is:

```math
P_n(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \dots + \frac{f^{(n)}(a)}{n!}(x - a)^n
```

**Example:**

For \(f(x) = e^x\), centered at \(a = 0\),

```math
P_3(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!}
```

This polynomial approximates \(e^x\) near 0.

### 🧾 Remainder (Error) of the Taylor Polynomial

The **Lagrange remainder** helps estimate how accurate the polynomial is. For a Taylor polynomial of degree \(n\), the remainder is:

```math
R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}, \quad \text{for some } c \in (a, x)
```

This tells you how far the approximation is from the actual function. The smaller \(R_n(x)\), the better the approximation.

### 📝 Answered Exercises

#### Exercise 1: Identify Asymptotes

**Question:** Determine the vertical, horizontal, and oblique asymptotes of the function \(f(x) = \frac{x^2 + 3x + 2}{x - 1}\).

**Answer:**

- **Vertical Asymptote:** \(x = 1\) (denominator equals zero).
- **Horizontal Asymptote:** None (degree of numerator is greater than denominator).
- **Oblique Asymptote:** Perform polynomial division: \(f(x) = x + 4 + \frac{6}{x - 1}\). The oblique asymptote is \(y = x + 4\).

---

#### Exercise 2: Sketch a Function

**Question:** Sketch the function \(f(x) = x^3 - 3x^2 + 2x\).

**Answer:**

1. **Domain:** All real numbers (\(\mathbb{R}\)).
2. **Intercepts:** \(x = 0, 1, 2\) (roots of \(f(x)\)).
3. **Asymptotes:** None (polynomial function).
4. **First Derivative:** \(f'(x) = 3x^2 - 6x + 2\).
    - Critical points: Solve \(f'(x) = 0\), giving \(x = 1\) and \(x = \frac{2}{3}\).
    - Increasing on \((-\infty, \frac{2}{3}) \cup (1, \infty)\), decreasing on \((\frac{2}{3}, 1)\).
5. **Second Derivative:** \(f''(x) = 6x - 6\).
    - Inflection point: Solve \(f''(x) = 0\), giving \(x = 1\).
    - Concave up on \((1, \infty)\), concave down on \((-\infty, 1)\).
6. **Sketch:** Plot intercepts, critical points, and inflection points, and use concavity to draw the curve.

---

#### Exercise 3: Taylor Polynomial Approximation

**Question:** Find the Taylor polynomial of degree 2 for \(f(x) = \sin(x)\) centered at \(a = 0\).

**Answer:**

The Taylor polynomial is:

```math
P_2(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2
```

For \(f(x) = \sin(x)\):
- \(f(0) = 0\), \(f'(x) = \cos(x)\), \(f'(0) = 1\),
- \(f''(x) = -\sin(x)\), \(f''(0) = 0\).

Thus, \(P_2(x) = x\).

---

#### Exercise 4: Error Estimation

**Question:** Estimate the error of the Taylor polynomial \(P_2(x) = x\) for \(f(x) = \sin(x)\) at \(x = 0.1\).

**Answer:**

The remainder is:

```math
R_2(x) = \frac{f^{(3)}(c)}{3!}x^3, \quad c \in (0, x)
```

For \(f(x) = \sin(x)\), \(f^{(3)}(x) = -\cos(x)\). At \(c \approx 0.1\), \(|f^{(3)}(c)| \leq 1\).

Thus:

```math
|R_2(0.1)| \leq \frac{1}{6}(0.1)^3 = 0.0001667
```

The error is approximately \(0.0001667\).
