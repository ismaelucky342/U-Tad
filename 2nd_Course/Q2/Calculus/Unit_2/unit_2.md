# Unit 2: The Limit of a Function and Continuity

---

## 🎯 Introduction and Objectives

In this unit, you will:

- Understand what a **limit** is and how to interpret it both graphically and algebraically.
- Apply properties and laws of limits to solve problems.
- Identify and handle **indeterminate forms** using various algebraic strategies.
- Understand the concept of **continuity**, both at a point and over intervals.
- Classify types of **discontinuities** and their implications.
- Build strong foundational skills necessary for **calculus**, particularly **derivatives**.

---

## 🔚 The Limit of a Function

### 📌 Introduction

A **limit** describes how a function behaves as the input approaches a specific value. It answers the question:

> "As x gets closer to a certain value, what value does f(x) get closer to?"

This is not necessarily the value of the function at that point—it’s about the **trend** or **approach** of the values.

---

### 📐 Formal Definition of Limit

We write:

```math
\lim_{x \to a} f(x) = L
```

If we can make the value of \( f(x) \) **as close as we like** to **L** by choosing \( x \) values **sufficiently close** to **a** (but not equal to \( a \)), then the limit exists and equals **L**.

🧪 **Example 1:**
Let \( f(x) = 3x + 1 \). Find \( \lim_{x \to 2} f(x) \):

Just substitute:
```math
f(2) = 3(2) + 1 = 7
```

✅ The limit exists and is 7.

🧪 **Example 2:**
Let

```math
f(x) =
\begin{cases} 
x^2 & \text{if } x \neq 2 \\
5 & \text{if } x = 2 
\end{cases}
```

Then:

```math
\lim_{x \to 2} f(x) = 4, \quad \text{but } f(2) = 5.
```

➡️ The limit depends on the **approach**, not the actual value at the point.

---

### 📈 One-Sided Limits

Sometimes we want to consider the behavior of \( f(x) \) as \( x \) approaches from **one side** only:

- **Left-hand limit**: \( \lim_{x \to a^-} f(x) \) → \( x \) approaches \( a \) from values **less than \( a \)**
- **Right-hand limit**: \( \lim_{x \to a^+} f(x) \) → \( x \) approaches \( a \) from values **greater than \( a \)**

🧪 **Example 3:**
Let

```math
f(x) =
\begin{cases} 
1 & \text{if } x < 0 \\
2 & \text{if } x \geq 0 
\end{cases}
```

Then:

```math
\lim_{x \to 0^-} f(x) = 1, \quad \lim_{x \to 0^+} f(x) = 2
```

Because these one-sided limits differ:

```math
\lim_{x \to 0} f(x) \quad \text{does not exist.}
```

---

## 🧠 Properties and Limit Calculations

### 🧾 Limit Laws

These rules simplify the computation of limits:

Let \( \lim_{x \to a} f(x) = L \) and \( \lim_{x \to a} g(x) = M \):

- **Sum Rule**: \( \lim_{x \to a}(f(x) + g(x)) = L + M \)
- **Difference Rule**: \( \lim_{x \to a}(f(x) - g(x)) = L - M \)
- **Product Rule**: \( \lim_{x \to a}(f(x) \cdot g(x)) = L \cdot M \)
- **Quotient Rule**: \( \lim_{x \to a}\frac{f(x)}{g(x)} = \frac{L}{M} \) (as long as \( M \neq 0 \))
- **Constant Multiple**: \( \lim_{x \to a}(c \cdot f(x)) = c \cdot L \)

🧪 **Example 4:**
Find \( \lim_{x \to 2} (3x^2 - x + 4) \):

Use substitution:
```math
= 3(2)^2 - 2 + 4 = 12 - 2 + 4 = 14
```

---

### 🔁 Direct Substitution

If the function is continuous at \( x = a \), the limit can be computed by **plugging in the value**:

🧪 **Example 5:**
\( f(x) = \sqrt{x + 1} \), find \( \lim_{x \to 3} f(x) \):

Just plug in:
```math
\sqrt{3 + 1} = \sqrt{4} = 2
```

---

### 🧩 Matching Functions Except at a Point

Sometimes a function is undefined at a point, but we can simplify it to evaluate the limit.

🧪 **Example 6:**
\( f(x) = \frac{x^2 - 1}{x - 1}, \, x \neq 1 \)

Factor:
```math
\frac{(x - 1)(x + 1)}{x - 1} = x + 1 \quad \text{(for \( x \neq 1 \))}
```

Now:
```math
\lim_{x \to 1} f(x) = 1 + 1 = 2
```

✅ Even though \( f(1) \) is undefined, the **limit exists**.

---

### 🔒 Squeeze Theorem (Sandwich Theorem)

If:

```math
h(x) \leq f(x) \leq g(x)
```

and both \( \lim_{x \to a} h(x) = \lim_{x \to a} g(x) = L \),

then:
```math
\lim_{x \to a} f(x) = L
```

🧪 **Example 7:**
Let:

- \( h(x) = -x^2 \)
- \( f(x) = x^2 \cdot \sin\left(\frac{1}{x}\right) \)
- \( g(x) = x^2 \)

Since \( -x^2 \leq x^2 \cdot \sin\left(\frac{1}{x}\right) \leq x^2 \), and \( \lim_{x \to 0} -x^2 = \lim_{x \to 0} x^2 = 0 \),

```math
\lim_{x \to 0} x^2 \cdot \sin\left(\frac{1}{x}\right) = 0
```

---

## ♾️ Infinite Limits and Indeterminate Forms

### 🔺 Infinite Limits

If the function grows without bound as \( x \) approaches a point:

```math
\lim_{x \to a} f(x) = \infty \quad \text{or} \quad \lim_{x \to a} f(x) = -\infty
```

🧪 **Example 8:**
```math
\lim_{x \to 0^+} \frac{1}{x} = \infty, \quad \lim_{x \to 0^-} \frac{1}{x} = -\infty
```

So the general limit does not exist (one side goes up, the other down).

---

### ❓ Indeterminate Forms

Forms like \( \frac{0}{0} \) or \( \frac{\infty}{\infty} \) don’t yield a clear answer and must be simplified:

Common types:

- \( \frac{0}{0} \)
- \( \frac{\infty}{\infty} \)
- \( 0 \cdot \infty \)
- \( \infty - \infty \)
- \( 1^\infty, 0^0, \infty^0 \)

🧪 **Example 9:**
```math
\lim_{x \to 2} \frac{x^2 - 4}{x - 2}
```

Factor:
```math
\frac{(x - 2)(x + 2)}{x - 2} \to x + 2
```

Now:
```math
\lim_{x \to 2} (x + 2) = 4
```

🧪 **Example 10 (rationalizing):**
```math
\lim_{x \to 0} \frac{\sqrt{x + 1} - 1}{x}
```

Multiply numerator and denominator by the conjugate:
```math
\frac{(\sqrt{x + 1} - 1)(\sqrt{x + 1} + 1)}{x(\sqrt{x + 1} + 1)} = \frac{x}{x(\sqrt{x + 1} + 1)}
```

Cancel \( x \) and simplify:
```math
\lim_{x \to 0} \frac{1}{\sqrt{x + 1} + 1} = \frac{1}{2}
```

---

### 🔄 Equivalent Infinitesimals

Some functions are nearly equal as \( x \to 0 \):

- \( \sin(x) \sim x \)
- \( \tan(x) \sim x \)
- \( 1 - \cos(x) \sim \frac{x^2}{2} \)

🧪 **Example 11:**
```math
\lim_{x \to 0} \frac{\sin(x)}{x} = 1
```

🧪 **Example 12:**
```math
\lim_{x \to 0} \frac{1 - \cos(x)}{x^2} = \frac{1}{2}
```

---

## 🔗 Continuity

### 📖 Definition of Continuity

A function \( f(x) \) is **continuous at \( x = a \)** if:

1. \( f(a) \) is defined
2. \( \lim_{x \to a} f(x) \) exists
3. \( \lim_{x \to a} f(x) = f(a) \)

If **any** of these conditions fail, the function is **discontinuous** at that point.

---

### ❌ Types of Discontinuity

- **Removable Discontinuity**: A hole in the graph. The limit exists, but \( f(a) \) is missing or incorrect.
    
    🧪 Example: \( f(x) = \frac{x^2 - 1}{x - 1}, \, x \neq 1 \)
    
- **Jump Discontinuity**: Left-hand and right-hand limits exist but are not equal.
    
    🧪 Example: Piecewise function with different values on either side of a point.
    
- **Infinite Discontinuity**: The function approaches \( \infty \) or \( -\infty \).
    
    🧪 Example: \( f(x) = \frac{1}{x - 2} \) at \( x = 2 \)
    

---

### 📐 Properties of Continuous Functions

The following are continuous **everywhere on their domains**:

- Polynomial functions (e.g., \( f(x) = x^2 + 3x - 1 \))
- Rational functions (except where denominator = 0)
- Trigonometric functions (e.g., \( \sin(x), \cos(x) \))
- Exponential and logarithmic functions

🧪 **Example 13:**
\( f(x) = \ln(x) \) is continuous for \( x > 0 \)

\( f(x) = \frac{1}{x} \) is continuous for \( x \neq 0 \)

🧪 **Example 14:**
\( f(x) = \frac{\sin(x)}{x} \) is not continuous at \( x = 0 \), but its **limit exists**.