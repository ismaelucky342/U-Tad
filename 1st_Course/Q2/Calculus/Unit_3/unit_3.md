## Unit 3: Differentiation of Functions
---

### 🎯 Introduction and Objectives

In this unit, you will:

- Learn the concept of the derivative and understand its formal and geometric definitions.
- Explore how differentiation relates to continuity and local behavior of functions.
- Apply differentiation rules to various types of functions.
- Use derivatives to analyze functions in terms of growth, concavity, and extrema (maximum and minimum points).

---

### 🧮 The Derivative of a Function

### 📌 Introduction

Differentiation is a fundamental concept in calculus. It allows us to understand how a function changes at any point and provides tools to analyze its behavior.

### 📐 Formal Definition of the Derivative

The derivative of a function `f(x)` at a point `x = a` is defined as the limit:

```math
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
```

This expression represents the *instantaneous rate of change* of the function at `x = a`.

### 🧭 Geometric Interpretation

Geometrically, the derivative at a point is the **slope of the tangent line** to the graph of the function at that point.

**Example:**

For `f(x) = x^2`,

```math
f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = 2x
```

So the slope of the tangent line at any point `x` is `2x`.

### 🔗 Differentiation and Continuity

If a function is differentiable at a point, then it must also be continuous at that point.

**But the reverse is not always true**: A function can be continuous but not differentiable (e.g., at a sharp corner or cusp).

---

### 🛠️ Properties and Calculation of Derivatives

### 📘 Common Functions and Their Derivatives

| Function | Derivative |
| --- | --- |
| `f(x) = c` | `f'(x) = 0` |
| `f(x) = x^n` | `f'(x) = n x^{n - 1}` |
| `f(x) = \sin x` | `f'(x) = \cos x` |
| `f(x) = \cos x` | `f'(x) = -\sin x` |
| `f(x) = e^x` | `f'(x) = e^x` |
| `f(x) = \ln x` | `f'(x) = \frac{1}{x}` |

### ⚙️ Rules for Differentiation

1. **Constant Rule**:
    ```math
    \frac{d}{dx}[c] = 0
    ```

2. **Power Rule**:
    ```math
    \frac{d}{dx}[x^n] = n x^{n - 1}
    ```

3. **Sum and Difference Rule**:
    ```math
    \frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)
    ```

4. **Product Rule**:
    ```math
    \frac{d}{dx}[f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x)
    ```

5. **Quotient Rule**:
    ```math
    \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
    ```

6. **Chain Rule** (for composition of functions):
    ```math
    \frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)
    ```

**Example using the chain rule**:

If `f(x) = \sin(x^2)`, then:

Let `u = x^2`, so `f(x) = \sin(u)`,

```math
f'(x) = \cos(u) \cdot 2x = \cos(x^2) \cdot 2x
```

---

### 📊 Applications to Local Behavior of a Function

### 📈 Increasing and Decreasing Intervals

- If `f'(x) > 0` on an interval, the function is **increasing** there.
- If `f'(x) < 0` on an interval, the function is **decreasing** there.

**Example:**

For `f(x) = x^2`, we have `f'(x) = 2x`.

- When `x > 0`, `f'(x) > 0` → Increasing
- When `x < 0`, `f'(x) < 0` → Decreasing

### 📉 Concavity and Convexity

- The **second derivative** `f''(x)` gives information about concavity:
  - If `f''(x) > 0`, the function is **concave upward** (convex).
  - If `f''(x) < 0`, the function is **concave downward** (concave).

**Example:**

For `f(x) = x^3`:

- `f'(x) = 3x^2`,
- `f''(x) = 6x`

So it's:

- Concave down when `x < 0`
- Concave up when `x > 0`

### 📍 Local Maxima and Minima (Extrema)

Use the **first derivative test** or **second derivative test**:

- **First derivative test**:
  - If `f'(x)` changes from `+` to `-` at a point, it's a local **maximum**.
  - If it changes from `-` to `+`, it's a **minimum**.

- **Second derivative test**:
  - If `f''(x) > 0`, local **min**
  - If `f''(x) < 0`, local **max**

**Example:**

`f(x) = -x^2 + 4x`

- `f'(x) = -2x + 4`

Set `f'(x) = 0`:

```math
-2x + 4 = 0 \Rightarrow x = 2
```

- `f''(x) = -2 < 0` → local maximum at `x = 2`

### 📌 The Mean Value Theorem

If a function is continuous on `[a, b]` and differentiable on `(a, b)`, then there exists at least one `c \in (a, b)` such that:

```math
f'(c) = \frac{f(b) - f(a)}{b - a}
```

This means there is a point where the instantaneous rate of change equals the average rate of change.

**Example:**

Let `f(x) = x^2` on `[1, 3]`,

```math
\frac{f(3) - f(1)}{3 - 1} = \frac{9 - 1}{2} = 4
```

Find `c` such that `f'(c) = 4`:

- `f'(x) = 2x` → `2c = 4 \Rightarrow c = 2`, which lies in `(1, 3)`.

### 🌟 Higher-Order Derivatives

The **second derivative** `f''(x)` is the derivative of the first derivative `f'(x)`. It provides information about the concavity of the function, as discussed earlier.

Similarly, we can compute **higher-order derivatives**:

- The **third derivative** `f'''(x)` is the derivative of `f''(x)`.
- The **n-th derivative** `f^{(n)}(x)` is obtained by differentiating `f^{(n-1)}(x)`.

**Example:**

For `f(x) = x^4`:

- `f'(x) = 4x^3`
- `f''(x) = 12x^2`
- `f'''(x) = 24x`
- `f^{(4)}(x) = 24`

---

### 🌐 Implicit Differentiation

Sometimes, functions are not given explicitly as `y = f(x)` but rather in an implicit form, such as `F(x, y) = 0`. In such cases, we use **implicit differentiation**.

**Steps for Implicit Differentiation**:

1. Differentiate both sides of the equation with respect to `x`, treating `y` as a function of `x` (i.e., apply the chain rule to terms involving `y`).
2. Solve for `\frac{dy}{dx}`.

**Example:**

For the equation `x^2 + y^2 = 1`:

1. Differentiate both sides:
    ```math
    2x + 2y\frac{dy}{dx} = 0
    ```
2. Solve for `\frac{dy}{dx}`:
    ```math
    \frac{dy}{dx} = -\frac{x}{y}
    ```

---

### 🌀 Derivatives of Parametric Equations

When a curve is defined parametrically by `x = f(t)` and `y = g(t)`, the derivative `\frac{dy}{dx}` is computed as:

```math
\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}
```

**Example:**

For `x = t^2` and `y = t^3`:

1. Compute `\frac{dx}{dt} = 2t` and `\frac{dy}{dt} = 3t^2`.
2. Then:
    ```math
    \frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}
    ```

---

### 🔄 Derivatives of Inverse Functions

If `y = f^{-1}(x)` is the inverse of `f(x)`, then the derivative of the inverse function is given by:

```math
\frac{dy}{dx} = \frac{1}{f'(f^{-1}(x))}
```

**Example:**

For `f(x) = x^3`, its inverse is `f^{-1}(x) = \sqrt[3]{x}`.

1. Compute `f'(x) = 3x^2`.
2. Then:
    ```math
    \frac{dy}{dx} = \frac{1}{3(f^{-1}(x))^2} = \frac{1}{3(\sqrt[3]{x})^2}
    ```

---

### 📐 Tangents and Normals to Curves

The **equation of the tangent line** to a curve at a point `(x_0, y_0)` is:

```math
y - y_0 = f'(x_0)(x - x_0)
```

The **equation of the normal line** (perpendicular to the tangent) is:

```math
y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)
```

**Example:**

For `f(x) = x^2` at `x_0 = 1`:

1. `f'(x) = 2x`, so `f'(1) = 2`.
2. Tangent line:
    ```math
    y - 1 = 2(x - 1) \Rightarrow y = 2x - 1
    ```
3. Normal line:
    ```math
    y - 1 = -\frac{1}{2}(x - 1) \Rightarrow y = -\frac{1}{2}x + \frac{3}{2}
    ```

---

### 🌊 Related Rates

In problems involving related rates, two or more quantities are related by an equation, and their rates of change with respect to time are connected.

**Steps for Solving Related Rates Problems**:

1. Identify the given rates and the rate to be found.
2. Write an equation relating the variables.
3. Differentiate the equation with respect to time `t`.
4. Substitute the known values and solve for the unknown rate.

**Example:**

A balloon is being inflated such that its volume increases at a rate of `\frac{dV}{dt} = 100 \, \text{cm}^3/\text{s}`. Find the rate at which the radius is increasing when the radius is `r = 10 \, \text{cm}`.

1. The volume of a sphere is:
    ```math
    V = \frac{4}{3}\pi r^3
    ```
2. Differentiate with respect to `t`:
    ```math
    \frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}
    ```
3. Solve for `\frac{dr}{dt}`:
    ```math
    \frac{dr}{dt} = \frac{\frac{dV}{dt}}{4\pi r^2} = \frac{100}{4\pi (10)^2} = \frac{100}{400\pi} = \frac{1}{4\pi} \, \text{cm/s}
    ```

---

### 🧩 L'Hôpital's Rule

L'Hôpital's Rule is used to evaluate limits of indeterminate forms like `\frac{0}{0}` or `\frac{\infty}{\infty}`. If:

```math
\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{0}{0} \text{ or } \frac{\infty}{\infty},
```

then:

```math
\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)},
```

provided the limit on the right-hand side exists.

**Example:**

Evaluate:
```math
\lim_{x \to 0} \frac{\sin x}{x}
```

1. Direct substitution gives `\frac{0}{0}`.
2. Apply L'Hôpital's Rule:
    ```math
    \lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{\cos x}{1} = 1
    ```

---

### 🔍 Taylor and Maclaurin Series

The **Taylor series** of a function `f(x)` about `x = a` is:

```math
f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f'''(a)}{3!}(x - a)^3 + \dots
```

The **Maclaurin series** is a special case of the Taylor series with `a = 0`:

```math
f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots
```

**Example:**

For `f(x) = e^x`, the Maclaurin series is:

```math
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots
```
