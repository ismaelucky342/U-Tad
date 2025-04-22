## Unit 3: Derivatives of Functions

The derivative of a function measures how the function changes as its input changes. It is defined as the limit of the average rate of change of the function over an interval as the interval approaches zero. The derivative is denoted by \( f'(x) \) or \( \frac{df}{dx} \).

### Definition of Derivative

The derivative of a function \( f(x) \) at a point \( x = a \) is defined as:
```math 
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
```
```math
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
```

**Example 1**
```math
f(x) = x^2
```
```math
f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = 2x
```
```math
f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = 2x
```
```math
f'(x) = 2x
```

**Example 2**
```math
f(x) = \sin(x)
```
```math
f'(x) = \lim_{h \to 0} \frac{\sin(x + h) - \sin(x)}{h} = \cos(x)
```
```math
f'(x) = \lim_{h \to 0} \frac{\sin(x + h) - \sin(x)}{h} = \cos(x)
```
```math
f'(x) = \cos(x)
```

### Geometric Interpretation of Derivative
The derivative of a function at a point represents the slope of the tangent line to the graph of the function at that point. If the derivative is positive, the function is increasing; if it is negative, the function is decreasing.
If the derivative is zero, the function has a local maximum or minimum at that point.

### Higher-Order Derivatives
Higher-order derivatives are the derivatives of the derivative. The second derivative, denoted \( f''(x) \), is the derivative of the first derivative \( f'(x) \). It provides information about the concavity of the function.
The second derivative is defined as:
```math
f''(x) = \frac{d^2f}{dx^2} = \frac{d}{dx}\left(\frac{df}{dx}\right)
```
```math 
f''(x) = \frac{d^2f}{dx^2} = \frac{d}{dx}\left(\frac{df}{dx}\right)
```
**Example 3**
```math
f(x) = x^3
```
```math
f'(x) = 3x^2
```
```math
f''(x) = 6x
```
```math
f''(x) = 6x
```

### Derivation and Continuity

A function is continuous at a point \( x = a \) if:
1. \( f(a) \) is defined.
2. The limit of \( f(x) \) as \( x \) approaches \( a \) exists.
3. The limit of \( f(x) \) as \( x \) approaches \( a \) is equal to \( f(a) \).
```math
\lim_{x \to a} f(x) = f(a)
```
```math
\lim_{x \to a} f(x) = f(a)
```
#### Differentiability and Continuity
A function is differentiable at a point \( x = a \) if the derivative exists at that point. If a function is differentiable at a point, it is also continuous at that point. However, the converse is not necessarily true; a function can be continuous but not differentiable at a point (e.g., a corner or cusp).
```math
f'(a) \text{ exists} \implies f(a) \text{ is continuous}
```
```math
f'(a) \text{ exists} \implies f(a) \text{ is continuous}
```

## Properties of Derivatives and Dervative calculation

the most important properties of derivatives are:

1. **Sum Rule**: 

```math
(f + g)' = f' + g'
```
The derivative of the sum of two functions is the sum of their derivatives.

```math
(f + g)' = f' + g'
```

2. **Product of a Function and a Scalar**: 

```math
(c \cdot f)' = c \cdot f'
```
The derivative of a constant multiplied by a function is the constant multiplied by the derivative of the function.

```math
(c \cdot f)' = c \cdot f'
```
3. **Product Rule**: 

```math
(f \cdot g)' = f' \cdot g + f \cdot g'
```
The derivative of the product of two functions is given by the product of the first function and the derivative of the second function plus the product of the second function and the derivative of the first function.

```math
(f \cdot g)' = f' \cdot g + f \cdot g'
```

4. **Quotient Rule**: 

```math
\left(\frac{f}{g}\right)' = \frac{f' \cdot g - f \cdot g'}{g^2}
```
The derivative of the quotient of two functions is given by the derivative of the numerator multiplied by the denominator minus the numerator multiplied by the derivative of the denominator, all divided by the square of the denominator.

```math
\left(\frac{f}{g}\right)' = \frac{f' \cdot g - f \cdot g'}{g^2}
```
5. **Chain Rule**: 

```math
(f(g(x)))' = f'(g(x)) \cdot g'(x)
```
The derivative of a composite function is given by the derivative of the outer function evaluated at the inner function multiplied by the derivative of the inner function.

```math
(f(g(x)))' = f'(g(x)) \cdot g'(x)
```

### Table of Derivatives

```math
\begin{array}{|c|c|}
\hline
\text{Function} & \text{Derivative} \\
\hline
c \, (\text{constant}) & 0 \\
x^n & nx^{n-1} \\
e^x & e^x \\
\ln(x) & \frac{1}{x} \\
\sin(x) & \cos(x) \\
\cos(x) & -\sin(x) \\
\tan(x) & \sec^2(x) \\
\arcsin(x) & \frac{1}{\sqrt{1 - x^2}} \\
\arccos(x) & -\frac{1}{\sqrt{1 - x^2}} \\
\arctan(x) & \frac{1}{1 + x^2} \\
\sinh(x) & \cosh(x) \\
\cosh(x) & \sinh(x) \\
\tanh(x) & \text{sech}^2(x) \\
\text{sech}(x) & -\text{sech}(x) \cdot \tanh(x) \\
\text{csch}(x) & -\text{csch}(x) \cdot \coth(x) \\
\text{coth}(x) & -\text{csch}^2(x) \\
\text{arcsinh}(x) & \frac{1}{\sqrt{x^2 + 1}} \\
\text{arccosh}(x) & \frac{1}{\sqrt{x^2 - 1}} \\
\text{arctanh}(x) & \frac{1}{1 - x^2} \\
\text{arccsch}(x) & -\frac{1}{|x|\sqrt{x^2 + 1}} \\
\text{arcsech}(x) & -\frac{1}{|x|\sqrt{1 - x^2}} \\
\text{arcoth}(x) & -\frac{1}{|x|\sqrt{x^2 - 1}} \\
\text{arccoth}(x) & -\frac{1}{|x|\sqrt{x^2 - 1}} \\
\text{arccsch}(x) & -\frac{1}{|x|\sqrt{x^2 + 1}} \\
\hline
\end{array}
```

## Aplication to the local study of functions

### 1. **Critical Points**
Critical points of a function are points where the derivative is either zero or undefined. These points are important because they can indicate local maxima, minima, or points of inflection.

**-> Example:** Find the critical points of \( f(x) = x^3 - 3x^2 + 4 \).
```math
f'(x) = 3x^2 - 6x
```
```math
f'(x) = 3x(x - 2)
```
Setting \( f'(x) = 0 \):
```math
3x(x - 2) = 0
```
This gives us \( x = 0 \) and \( x = 2 \) as critical points.

### 2. **Increasing and Decreasing Intervals**
To determine where a function is increasing or decreasing, we analyze the sign of the derivative:
- If \( f'(x) > 0 \), the function is increasing on that interval.
- If \( f'(x) < 0 \), the function is decreasing on that interval.

**-> Example:** For \( f(x) = x^3 - 3x^2 + 4 \):
```math
f'(x) = 3x(x - 2)
```
```math
f'(x) > 0 \text{ for } x < 0 \text{ and } x > 2
```
```math
f'(x) < 0 \text{ for } 0 < x < 2
```
### 3. **Concavity and Inflection Points**
Concavity refers to the direction in which a function curves. A function is concave up if its second derivative is positive and concave down if its second derivative is negative. Inflection points are points where the concavity changes.

**-> Example:** For \( f(x) = x^3 - 3x^2 + 4 \):
```math
f''(x) = 6x - 6
```
```math
f''(x) = 0 \text{ at } x = 1
```
```math
f''(x) > 0 \text{ for } x > 1 \text{ (concave up)}
```
```math
f''(x) < 0 \text{ for } x < 1 \text{ (concave down)}
```
### 4. **Local Maxima and Minima**
Local maxima and minima can be found using the first derivative test:
- If \( f'(x) \) changes from positive to negative at a critical point, it is a local maximum.
- If \( f'(x) \) changes from negative to positive at a critical point, it is a local minimum.
- If \( f'(x) \) does not change sign, it is neither a maximum nor a minimum.
**-> Example:** For \( f(x) = x^3 - 3x^2 + 4 \):
```math
f'(x) = 3x(x - 2)
```
```math
f'(x) \text{ changes from positive to negative at } x = 0 \text{ (local maximum)}
```
```math
f'(x) \text{ changes from negative to positive at } x = 2 \text{ (local minimum)}
```
### 5. **Global Maxima and Minima**

Global maxima and minima are the highest and lowest points of a function over its entire domain. To find them, we evaluate the function at critical points and endpoints of the interval.

**-> Example:** For \( f(x) = x^3 - 3x^2 + 4 \):
```math
f(0) = 4 \text{ (local maximum)}
```
```math
f(2) = 2 \text{ (local minimum)}
```
```math
f(x) \text{ has a global maximum at } x = 0 \text{ and a global minimum at } x = 2.
```

### Role's Theorem
Role's theorem states that if a function is continuous on a closed interval \([a, b]\) and differentiable on the open interval \((a, b)\), and if \(f(a) = f(b)\), then there exists at least one point \(c\) in \((a, b)\) such that \(f'(c) = 0\).
**-> Example:** For \( f(x) = x^2 - 4x + 4 \) on the interval \([0, 4]\):
```math
f(0) = 4 \text{ and } f(4) = 4
```
```math
f'(x) = 2x - 4
```
```math
f'(c) = 0 \text{ at } c = 2
```
```math
\text{So, } c = 2 \text{ is a point where the derivative is zero.}
```
### Mean Value Theorem of Lagrange
The Mean Value Theorem states that if a function is continuous on a closed interval \([a, b]\) and differentiable on the open interval \((a, b)\), then there exists at least one point \(c\) in \((a, b)\) such that:
```math
f'(c) = \frac{f(b) - f(a)}{b - a}
```
```math
f'(c) = \frac{f(b) - f(a)}{b - a}
```
**-> Example:** For \( f(x) = x^2 \) on the interval \([1, 3]\):
```math
f(1) = 1 \text{ and } f(3) = 9
```
```math
f'(c) = \frac{9 - 1}{3 - 1} = 4
```
```math
f'(c) = 2c \text{ so } c = 2
```
```math
\text{So, } c = 2 \text{ is a point where the derivative equals the average rate of change.}
```
