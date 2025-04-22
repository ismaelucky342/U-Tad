# Unit 2: The Limit of a Function 

The concept of a limit is essential in calculus and plays a fundamental role in understanding the behavior of functions. The limit of a function at a specific point describes the value that the function approaches as the independent variable gets closer to that point. It is important to note that the limit of a function at a point does not necessarily coincide with the value of the function at that point, and in some cases, that value may not even exist.

The continuity of a function at a point is established when the limit of the function at that point exactly matches its value. More intuitively, a function is continuous if its graph can be drawn without interruptions, without needing to lift the pencil from the paper.

## Definition of the Limit of a Function

The limit of a function \(f(x)\) as \(x\) approaches \(a\) is denoted as:
```math
\lim_{x \to a} f(x) = L
```
This means that as \(x\) gets arbitrarily close to \(a\), the value of \(f(x)\) approaches \(L\). The limit can be approached from the left (\(x \to a^-\)) or from the right (\(x \to a^+\)). If both limits exist and are equal, we can say that the limit exists.

```math
\lim_{x \to a^-} f(x) = L \quad \text{and} \quad \lim_{x \to a^+} f(x) = L
```

### Derivated Theorems with Limits

**-> T1:**If the limit of a function exists at a point, then that limit is unique.

```math
\lim_{x \to a} f(x) = L \implies \lim_{x \to a} f(x) = L
```

**-> T2:**If the limit of a function exists at a point, then the function is bounded in a neighborhood of that point.

```math
\lim_{x \to a} f(x) = L \implies \exists \delta > 0 : |f(x) - L| < \epsilon
```

### Side Limits

The left-hand limit and right-hand limit are defined as follows:
```math
\lim_{x \to a^-} f(x) = L \quad \text{and} \quad \lim_{x \to a^+} f(x) = L
```
```math
\lim_{x \to a^-} f(x) = L \quad \text{and} \quad \lim_{x \to a^+} f(x) = L
```
**-> T3:**If the left-hand limit and right-hand limit exist and are equal, then the limit exists:
```math
\lim_{x \to a} f(x) = L \implies \lim_{x \to a^-} f(x) = L \quad \text{and} \quad \lim_{x \to a^+} f(x) = L
```

## Properties of Limits and Limit Calculation

The most important properties of limits are:

1. **Sum Rule**: 
```math
\lim_{x \to a} (f(x) + g(x)) = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)
```
2. **Difference Rule**: 
```math
\lim_{x \to a} (f(x) - g(x)) = \lim_{x \to a} f(x) - \lim_{x \to a} g(x)
```
3. **Product Rule**: 
```math
\lim_{x \to a} (f(x) \cdot g(x)) = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)
```
4. **Quotient Rule**: 
```math
\lim_{x \to a} \left(\frac{f(x)}{g(x)}\right) = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}
```
5. **Constant Multiple Rule**: 
```math
\lim_{x \to a} (c \cdot f(x)) = c \cdot \lim_{x \to a} f(x)
```
6. **Power Rule**: 
```math
\lim_{x \to a} (f(x))^n = \left(\lim_{x \to a} f(x)\right)^n
```
7. **Root Rule**: 
```math
\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x)}
```
8. **Absolute Value Rule**: 
```math
\lim_{x \to a} |f(x)| = |\lim_{x \to a} f(x)|
```


### Direct Substitution Rule

The direct substitution rule states that if \(f(x)\) is continuous at \(x = a\), then:
```math
\lim_{x \to a} f(x) = f(a)
```
This means that if you can directly substitute \(x = a\) into the function without any issues (like division by zero), then the limit is simply the value of the function at that point.
```math
\lim_{x \to a} f(x) = f(a)
```
**Example:**
```math
\lim_{x \to 2} (3x + 1) = 3(2) + 1 = 7
```

### Functions that match except in one point

```math
\lim_{x \to a} f(x) = L \quad \text{if } f(x) \text{ is defined at } x = a
```

### Lace Theorem

The lace theorem states that if \(f(x)\) is continuous at \(x = a\) and \(g(x)\) is continuous at \(x = b\), then:
```math
\lim_{x \to a} f(g(x)) = f(\lim_{x \to a} g(x))
```

## Infinite Limits
An infinite limit occurs when the function approaches infinity as \(x\) approaches a certain value. This can happen when the function has a vertical asymptote at that point. In such cases, we write:
```math
\lim_{x \to a} f(x) = +\infty \quad \text{or} \quad \lim_{x \to a} f(x) = -\infty
```

### Possible Cases of Infinite Limits

1. **Vertical Asymptote**: The function approaches infinity or negative infinity as \(x\) approaches a certain value.
2. **Oscillatory Behavior**: The function oscillates between two values as \(x\) approaches a certain value, leading to an undefined limit.
3. **Unbounded Behavior**: The function grows without bound as \(x\) approaches a certain value, but does not approach a specific value.
4. **Indeterminate Forms**: The limit may be in an indeterminate form, such as \(\frac{0}{0}\) or \(\frac{\infty}{\infty}\), which requires further analysis to resolve.

### Indeterminate Forms
Indeterminate forms are expressions that do not have a well-defined limit. The most common indeterminate forms are:
```math
- \frac{0}{0}
- \frac{\infty}{\infty}
- 0 \cdot \infty
- \infty - \infty
- 0^0
- \infty^0
- 1^\infty
- \infity * 0
```
These forms require additional techniques, such as L'Hôpital's Rule or algebraic manipulation, to evaluate the limit.

### equivalent infinitesimals
An infinitesimal is a quantity that is infinitely small, meaning it is smaller than any positive real number but greater than zero. In calculus, infinitesimals are often used to describe the behavior of functions as they approach certain values.

**Example:**
```math
\lim_{x \to 0} \frac{\sin(x)}{x} = 1
```

This means that as \(x\) approaches 0, the ratio of \(\sin(x)\) to \(x\) approaches 1. In this case, both \(\sin(x)\) and \(x\) are infinitesimals as \(x\) approaches 0, and their ratio approaches a finite value (1).

## In what cases does a function have no limit?
A function may not have a limit at a certain point if:
1. The function oscillates infinitely as \(x\) approaches that point.
2. The function approaches different values from the left and right sides.
3. The function has a vertical asymptote at that point.
4. The function is not defined at that point and does not approach a specific value.
5. The function has a removable discontinuity at that point, meaning it can be made continuous by redefining the function at that point, but it is not defined there.
6. The function has a jump discontinuity at that point, meaning it jumps from one value to another without approaching any specific value.
7. The function has an infinite discontinuity at that point, meaning it approaches infinity or negative infinity as \(x\) approaches that point.

## Continuity of a Function

We define the continuity of a function at a point \(x = a\) as follows:
```math
f(a) \text{ is defined} \quad \text{and} \quad \lim_{x \to a} f(x) = f(a)
```

### Continuity of an open interval
A function is continuous on an open interval \((a, b)\) if it is continuous at every point in that interval. This means that for every point \(c\) in the interval, the following conditions hold:
```math
f(c) \text{ is defined} \quad \text{and} \quad \lim_{x \to c} f(x) = f(c)
```
### Continuity of a closed interval
A function is continuous on a closed interval \([a, b]\) if it is continuous at every point in that interval, including the endpoints. This means that for every point \(c\) in the interval, the following conditions hold:
```math
f(c) \text{ is defined} \quad \text{and} \quad \lim_{x \to c} f(x) = f(c)
```

## Non-continuous functions

A function is non-continuous at a point \(x = a\) if any of the following conditions hold:
1. The function is not defined at that point.
2. The limit of the function does not exist at that point.
3. The limit of the function exists, but it does not equal the value of the function at that point.
4. The function has a removable discontinuity at that point, meaning it can be made continuous by redefining the function at that point, but it is not defined there.

### Evitable discontinuity

A removable discontinuity occurs when a function is not defined at a certain point, but can be made continuous by redefining the function at that point. This means that the limit of the function exists at that point, but the value of the function does not equal that limit.

```math
\lim_{x \to a} f(x) = L \quad \text{and} \quad f(a) \text{ is not defined}
```
```math
\lim_{x \to a} f(x) = L \quad \text{and} \quad f(a) \neq L
```
```math
\lim_{x \to a} f(x) = L \quad \text{and} \quad f(a) \text{ is defined}
```
```math
\lim_{x \to a} f(x) = L \quad \text{and} \quad f(a) \neq L
```

### Non-removable discontinuity
A non-removable discontinuity occurs when a function is not defined at a certain point, and cannot be made continuous by redefining the function at that point. This means that the limit of the function does not exist at that point, or the limit exists but does not equal the value of the function at that point.
```math
\lim_{x \to a} f(x) \neq f(a)
```
```math
\lim_{x \to a} f(x) \text{ does not exist}
```
```math
\lim_{x \to a} f(x) \text{ exists but } \lim_{x \to a} f(x) \neq f(a)
```

## Properties of Continuous Functions

1. **Sum Rule**: The sum of two continuous functions is continuous.
```math
f(x) + g(x) \text{ is continuous if } f(x) \text{ and } g(x) \text{ are continuous}
```
2. **Difference Rule**: The difference of two continuous functions is continuous.
```math
f(x) - g(x) \text{ is continuous if } f(x) \text{ and } g(x) \text{ are continuous}
```
3. **Product Rule**: The product of two continuous functions is continuous.
```math
f(x) \cdot g(x) \text{ is continuous if } f(x) \text{ and } g(x) \text{ are continuous}
```
4. **Quotient Rule**: The quotient of two continuous functions is continuous, provided the denominator is not zero.
```math
\frac{f(x)}{g(x)} \text{ is continuous if } f(x) \text{ and } g(x) \text{ are continuous and } g(x) \neq 0
```
5. **Composition Rule**: The composition of two continuous functions is continuous.
```math
f(g(x)) \text{ is continuous if } f(x) \text{ and } g(x) \text{ are continuous}
```

## Intermediate Value Theorem (Darboux's Theorem)

The Intermediate Value Theorem states that if \(f(x)\) is continuous on the closed interval \([a, b]\), and \(N\) is any number between \(f(a)\) and \(f(b)\), then there exists at least one point \(c\) in the interval \((a, b)\) such that:
```math
f(c) = N
```
This theorem is useful for proving the existence of roots in a continuous function. It guarantees that if a continuous function takes on two different values at two points, it must take on every value in between those two points at least once.
```math
f(a) < N < f(b) \implies \exists c \in (a, b) : f(c) = N
```

## Intermediate Cero Theorem (Bolzano's Theorem)

The Intermediate Cero Theorem, also known as Bolzano's Theorem, is a specific case of the Intermediate Value Theorem. It states that if \(f(x)\) is continuous on the closed interval \([a, b]\), and \(f(a) \cdot f(b) < 0\), then there exists at least one point \(c\) in the interval \((a, b)\) such that:
```math
f(c) = 0
```
This theorem is particularly useful for finding roots of continuous functions. It guarantees that if a continuous function takes on opposite signs at two points, it must have at least one root in between those two points.
```math
f(a) \cdot f(b) < 0 \implies \exists c \in (a, b) : f(c) = 0
```

## Weierstrass Theorem
The Weierstrass Theorem states that every continuous function defined on a closed interval \([a, b]\) is uniformly continuous. This means that for any given positive number \(\epsilon\), there exists a positive number \(\delta\) such that for all \(x_1, x_2 \in [a, b]\):
```math
|x_1 - x_2| < \delta \implies |f(x_1) - f(x_2)| < \epsilon
```
This theorem is important because it guarantees that continuous functions on closed intervals behave nicely and do not have abrupt changes in their values.


