# Unit 4: Function Interpolation
Graphical representation is not the only way to approach a function. Function interpolation using polynomials emerges as a powerful alternative to approximate and analyze functions. Taylor's theorem and Lagrange's interpolation method provide us with tools to approximate functions using polynomials from a local perspective, focusing on the vicinity of a specific point, and from a global perspective, considering an entire interval.

# Graphical Representation of Functions
We first introduce the concept of an asymptote, which, along with the concepts studied in previous units, helps us sketch the graph of a function.

## Graphical Representation of Functions

An asymptote of a function (f(x)) whose graph is the curve (C), is a line (r) to which the curve (C) gets closer and closer, so that in the limit, they become infinitesimally close, but without fully coinciding with the line (r) itself. In other words, the curve "sticks" to the line as we move toward infinity or toward a specific point.

**Types of Asymptotes:**

The text focuses on two main types of asymptotes:

### Vertical Asymptotes

- **Definition:** The vertical line \(x = a\) is a vertical asymptote of the function \(f(x)\) if at least one of the following limits holds:
    - \(\lim_{x \to a^+} f(x) = +\infty\) (The function tends to infinity as \(x\) approaches \(a\) from the right)
    - \(\lim_{x \to a^+} f(x) = -\infty\) (The function tends to negative infinity as \(x\) approaches \(a\) from the right)
    - \(\lim_{x \to a^-} f(x) = +\infty\) (The function tends to infinity as \(x\) approaches \(a\) from the left)
    - \(\lim_{x \to a^-} f(x) = -\infty\) (The function tends to negative infinity as \(x\) approaches \(a\) from the left)
- **How do they occur in rational functions?** For rational functions (those that are the quotient of two polynomials), vertical asymptotes occur at the values of \(x\) that make the denominator of the function zero, after simplifying the fraction by removing any common factors between the numerator and the denominator.

### Horizontal Asymptotes

- **Definition:** The horizontal line \(y = k\) (where \(k\) is a finite real value) is a horizontal asymptote of the function \(f(x)\) if at least one of the following limits holds:
    - \(\lim_{x \to +\infty} f(x) = k\) (The function tends to \(k\) as \(x\) tends to infinity)
    - \(\lim_{x \to -\infty} f(x) = k\) (The function tends to \(k\) as \(x\) tends to negative infinity)
- **Important Note:** To determine horizontal asymptotes, only the behavior of the function as \(x\) tends to \(+\infty\) or \(-\infty\) matters.


### Oblicue Asymptotes

- **Definition:** The oblique asymptote of a function \(f(x)\) is a line of the form \(y = mx + b\) (where \(m\) and \(b\) are real numbers) that the function approaches as \(x\) tends to infinity or negative infinity.

- **How do they occur in rational functions?** Oblique asymptotes occur in rational functions when the degree of the numerator is one greater than the degree of the denominator. In this case, the oblique asymptote can be found by performing polynomial long division on the function.

- **Example:** For the function \(f(x) = \frac{x^2 + 3x + 2}{x + 1}\), the oblique asymptote is \(y = x + 2\) because the degree of the numerator (2) is one greater than the degree of the denominator (1).

## Guide to Sketching the curve of a function

### 1. Identify the domain of the function
- Determine the values of \(x\) for which the function is defined. This may involve finding restrictions based on the function's formula (e.g., avoiding division by zero).
### 2. Find the intercepts
- **X-intercept:** Set \(f(x) = 0\) and solve for \(x\).
- **Y-intercept:** Set \(x = 0\) and find \(f(0)\).

### 3. Determine the asymptotes
- Find vertical asymptotes by identifying values of \(x\) that make the denominator zero.
- Find horizontal asymptotes by analyzing the behavior of the function as \(x\) approaches infinity or negative infinity.
### 4. Analyze the behavior of the function
- **Increasing/Decreasing Intervals:** Use the first derivative to find intervals where the function is increasing or decreasing.
- **Concavity:** Use the second derivative to determine intervals of concavity (upward or downward).
### 5. Maximum and Minimum Points
- Find critical points by setting the first derivative equal to zero and solving for \(x\).
- Use the second derivative test to classify critical points as local maxima, minima, or points of inflection.
### 6. Simetry
- Check for symmetry about the y-axis (even function) or the origin (odd function).
### 7. Sketch the curve
- Plot the intercepts, asymptotes, critical points, and any other important features.
- Connect the points smoothly, considering the behavior of the function in different intervals.

## Taylor Polynomial and MacLaurin Polynomial

### Taylor Polynomial and Maclaurin Polynomial

Taylor's theorem provides a way to approximate a function using polynomials. The Taylor polynomial of degree \(n\) for a function \(f(x)\) at a point \(a\) is given by:

```math
P_n(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x - a)^n
```

where \(f^{(k)}(a)\) is the \(k\)-th derivative of \(f(x)\) evaluated at \(x = a\).

The Maclaurin polynomial is a special case of the Taylor polynomial where \(a = 0\):

```math
P_n(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n
```

### Maclaurin Polynomial

The Maclaurin polynomial is a Taylor polynomial centered at \(x = 0\). It is useful for approximating functions near the origin. The Maclaurin polynomial of degree \(n\) for a function \(f(x)\) is given by:

```math
P_n(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n
```
```math
P_n(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n
```

### Rest of the Taylor Polynomial

The Taylor polynomial can be expressed in a more compact form using the Lagrange form of the remainder:

```math
R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1} \quad \text{for some } c \text{ between } a \text{ and } x
```
```math
R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1} \quad \text{for some } c \text{ between } a \text{ and } x
```

This remainder term \(R_n(x)\) gives an estimate of the error in the approximation provided by the Taylor polynomial. The smaller the value of \(R_n(x)\), the better the approximation.

### Error height

The error height of the Taylor polynomial is given by the maximum value of the remainder term \(R_n(x)\) over the interval of interest. This can be estimated using the maximum value of the \((n+1)\)-th derivative of \(f(x)\) in that interval.

### Example of Taylor Polynomial
```math
f(x) = e^x
```
```math
P_n(x) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!}
```
```math
R_n(x) = \frac{e^c}{(n+1)!}x^{n+1} \quad \text{for some } c \text{ between } 0 \text{ and } x
```

### Lagrange Interpolation Polynomial

The Lagrange interpolation polynomial is a polynomial that passes through a given set of points \((x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)\). It is given by:

```math
P(x) = \sum_{i=0}^{n} y_i L_i(x)
```

where \(L_i(x)\) is the Lagrange basis polynomial defined as:

```math
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
```
```math
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
```

