# Unit 5: Integration of Functions

The integral of a function emerges as the inverse operation to differentiation, allowing us to recover a function from its derivative. Beyond its mathematical definition, the integral finds numerous applications in modeling real-world phenomena, from calculating areas and volumes to determining probabilities.

The integral is, therefore, not only a mathematical tool of great importance but also an essential concept for modeling various real-world phenomena.

# Indefinite Integrals
The indefinite integral of a function `f(x)` is defined as the set of all functions `F(x)` such that the derivative of `F(x)` equals `f(x)`. Mathematically, this is expressed as:

```math
\int f(x) \, dx = F(x) + C
```

where `C` is a constant of integration. The indefinite integral represents a family of functions that share the same derivative. The indefinite integral is used to calculate areas under the curve of a function, as well as to solve problems of accumulation and change. Additionally, it is fundamental in probability calculations and in modeling physical and economic phenomena.

### Properties of the Indefinite Integral


```math
\int (f(x) + g(x)) \, dx = \int f(x) \, dx + \int g(x) \, dx
```

2. **Constant times function**: The integral of a constant multiplied by a function is equal to the constant multiplied by the integral of the function. That is, if `c` is a constant and `f(x)` is a function, then:

```math
\int c \cdot f(x) \, dx = c \cdot \int f(x) \, dx
```

### Properties that do not hold

1. **Multiplication property does not hold**: The integral of a product of functions is not equal to the product of the integrals of each function. That is, in general:

```math
\int f(x) \cdot g(x) \, dx \neq \int f(x) \, dx \cdot \int g(x) \, dx
```

2. **Division property does not hold**: The integral of a function divided by another is not equal to the division of the integrals of each function. That is, in general:

```math
\int \frac{f(x)}{g(x)} \, dx \neq \frac{\int f(x) \, dx}{\int g(x) \, dx}
```

3. **Power inside property does not hold**: The integral of a function raised to a power is not equal to the power of the integral of the function. That is, in general:

```math
\int (f(x))^n \, dx \neq (\int f(x) \, dx)^n
```
# Immediate integrals and their primitives

Immediate integrals are a set of integrals that can be calculated directly without the need for complex calculations or transformations.

```math
\int dx = x + C
```
```math
\int a \, dx = ax + C

```
```math
\int x \, dx = \frac{x^2}{2} + C

```
```math
\int x^2 \, dx = \frac{x^3}{3} + C
```
```math
\int x^n \, dx = \frac{x^{n+1}}{n+1} + C, \quad (n \neq -1)
```
```math
\int u^n u' \, dx = \frac{u^{n+1}}{n+1} + C, \quad (n \neq -1)
```
```math
\int \frac{1}{x} \, dx = \ln|x| + C
```
```math
\int \frac{u'}{u} \, dx = \ln|u| + C
```
```math
\int \frac{1}{x+a} \, dx = \ln|x+a| + C
```
```math
\int \frac{u'}{u+a} \, dx = \ln|u+a| + C
```
```math
\int e^x \, dx = e^x + C
```
```math
\int u' e^u \, dx = e^u + C
```
```math
\int a^x \, dx = \frac{a^x}{\ln a} + C, \quad (a > 0, a \neq 1)
```
```math
\int u' a^u \, dx = \frac{a^u}{\ln a} + C, \quad (a > 0, a \neq 1)
```
```math
\int \sin x \, dx = -\cos x + C
```
```math
\int u' \sin u \, dx = -\cos u + C
```
```math
\int \cos x \, dx = \sin x + C
```
```math
\int u' \cos u \, dx = \sin u + C
```
```math
\int \tan x \, dx = -\ln|\cos x| + C
```
```math
\int u' \tan u \, dx = -\ln|\cos u| + C
```
```math
\int \frac{1}{\cos^2 x} \, dx = \tan x + C
```
```math
\int \frac{u'}{\cos^2 u} \, dx = \tan u + C
```
```math
\int (1 + \tan^2 x) \, dx = \tan x + C
```
```math
\int u'(1 + \tan^2 u) \, dx = \tan u + C
```
```math
\int \frac{1}{\sin^2 x} \, dx = -\cot x + C
```
```math
\int \frac{u'}{\sin^2 u} \, dx = -\cot u + C
```
```math
\int \frac{1}{\sqrt{1 - x^2}} \, dx = \arcsin x + C
```
```math
\int \frac{u'}{\sqrt{1 - u^2}} \, dx = \arcsin u + C
```
```math
\int \frac{1}{1 + x^2} \, dx = \arctan x + C
```
```math
\int \frac{u'}{1 + u^2} \, dx = \arctan u + C
```
```math
\int \frac{1}{a^2 + b^2 x^2} \, dx = \frac{1}{ab} \arctan \frac{bx}{a} + C
```
```math
\int \frac{u'}{a^2 + b^2 u^2} \, dx = \frac{1}{ab} \arctan \frac{bu}{a} + C
```

# Methods of Integration

## Integration by Parts
Integration by parts is a technique used to calculate integrals of products of functions. It is based on the product rule of differentiation and is expressed by the following formula:

```math
\int u \, dv = uv - \int v \, du
```
Where `u` and `v` are differentiable functions, `du` is the derivative of `u`, and `dv` is the derivative of `v`. The proper choice of `u` and `dv` is crucial to simplify the calculation of the integral.

### Example of Integration by Parts
```math
\int x \cdot e^x \, dx
```
1. Choose `u = x` and `dv = e^x \, dx`.
2. Compute `du = dx` and `v = e^x`.
3. Substitute into the integration by parts formula:

```math
\int x \cdot e^x \, dx = x \cdot e^x - \int e^x \, dx
```
4. Solve the remaining integral:

```math
\int e^x \, dx = e^x + C
```
5. Substitute the result into the original expression:

```math
\int x \cdot e^x \, dx = x \cdot e^x - e^x + C
```
6. Simplify:

```math
\int x \cdot e^x \, dx = (x - 1) \cdot e^x + C
```

### Example of Integration by Parts with Trigonometric Functions
```math
\int x \cdot \sin(x) \, dx
```
1. Choose `u = x` and `dv = \sin(x) \, dx`.
2. Compute `du = dx` and `v = -\cos(x)`.
3. Substitute into the integration by parts formula:

```math
\int x \cdot \sin(x) \, dx = -x \cdot \cos(x) - \int -\cos(x) \, dx
```
4. Solve the remaining integral:

```math
\int -\cos(x) \, dx = -\sin(x) + C
```
5. Substitute the result into the original expression:

```math
\int x \cdot \sin(x) \, dx = -x \cdot \cos(x) + \sin(x) + C
```
6. Simplify:

```math
\int x \cdot \sin(x) \, dx = -x \cdot \cos(x) + \sin(x) + C
```

## Integration of Rational Functions

The integration of rational functions refers to the technique of calculating integrals of functions that are quotients of polynomials. Different methods can be used to solve these integrals, such as partial fraction decomposition or trigonometric substitution.

### Example of Integration of Rational Functions
```math
\int \frac{1}{x^2 + 1} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int \frac{1}{x^2 + 1} \, dx = \arctan(x) + C
```
2. Therefore, the result is:

```math
\int \frac{1}{x^2 + 1} \, dx = \arctan(x) + C
```

### Example of Integration of Rational Functions with Partial Fractions
```math
\int \frac{1}{x^2 - 1} \, dx
```
1. Decompose the function into partial fractions:

```math
\frac{1}{x^2 - 1} = \frac{1}{(x - 1)(x + 1)} = \frac{A}{x - 1} + \frac{B}{x + 1}
```
2. Multiply both sides by `(x - 1)(x + 1)` and solve for `A` and `B`:

```math
1 = A(x + 1) + B(x - 1)
```
3. Match coefficients and solve the system of equations:

```math
A + B = 0
A - B = 1
```
4. Obtain `A = \frac{1}{2}` and `B = -\frac{1}{2}`.
5. Substitute into the integral:

```math
\int \left( \frac{1/2}{x - 1} - \frac{1/2}{x + 1} \right) \, dx
```
6. Solve each integral separately:

```math
\int \frac{1/2}{x - 1} \, dx - \int \frac{1/2}{x + 1} \, dx
```
7. Obtain:

```math
\frac{1}{2} \ln|x - 1| - \frac{1}{2} \ln|x + 1| + C
```
8. Simplify using logarithmic properties:

```math
\frac{1}{2} \ln \left| \frac{x - 1}{x + 1} \right| + C
```

### Example of Integration of Rational Functions with Trigonometric Substitution
```math
\int \frac{1}{\sqrt{1 - x^2}} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int \frac{1}{\sqrt{1 - x^2}} \, dx = \arcsin(x) + C
```
2. Therefore, the result is:

```math
\int \frac{1}{\sqrt{1 - x^2}} \, dx = \arcsin(x) + C
```

### Example of Integration of Rational Functions with Complex Numbers
```math
\int \frac{1}{x^2 + 4} \, dx
```
1. Decompose the function into partial fractions:

```math
\frac{1}{x^2 + 4} = \frac{1}{(x - 2i)(x + 2i)} = \frac{A}{x - 2i} + \frac{B}{x + 2i}
```
2. Multiply both sides by `(x - 2i)(x + 2i)` and solve for `A` and `B`:

```math
1 = A(x + 2i) + B(x - 2i)
```
3. Match coefficients and solve the system of equations:

```math
A + B = 0
A - B = 1
```
4. Obtain `A = \frac{1}{4i}` and `B = -\frac{1}{4i}`.
5. Substitute into the integral:

```math
\int \left( \frac{1/4i}{x - 2i} - \frac{1/4i}{x + 2i} \right) \, dx
```
6. Solve each integral separately:

```math
\int \frac{1/4i}{x - 2i} \, dx - \int \frac{1/4i}{x + 2i} \, dx
```
7. Obtain:

```math
\frac{1}{4i} \ln|x - 2i| - \frac{1}{4i} \ln|x + 2i| + C
```
8. Simplify using logarithmic properties:

```math
\frac{1}{4i} \ln \left| \frac{x - 2i}{x + 2i} \right| + C
```
9. Finally, apply the property of complex logarithms:

```math
\frac{1}{4i} \ln \left| \frac{x - 2i}{x + 2i} \right| = \frac{1}{4} \ln \left| \frac{x - 2i}{x + 2i} \right| + C
```
10. Therefore, the result is:

```math
\int \frac{1}{x^2 + 4} \, dx = \frac{1}{4} \ln \left| \frac{x - 2i}{x + 2i} \right| + C
```

## Integraction of Trigonometric Functions
The integration of trigonometric functions refers to the technique of calculating integrals of functions that involve trigonometric functions. Different methods can be used to solve these integrals, such as substitution or integration by parts.
### Example of Integration of Trigonometric Functions
```math
\int \sin(x) \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int \sin(x) \, dx = -\cos(x) + C
```
2. Therefore, the result is:

```math
\int \sin(x) \, dx = -\cos(x) + C
``` 
### Example of Integration of Trigonometric Functions with Substitution
```math
\int \sin^2(x) \, dx
```
1. Use the identity `sin^2(x) = \frac{1 - \cos(2x)}{2}` to rewrite the integral:

```math
\int \sin^2(x) \, dx = \frac{1}{2} \int (1 - \cos(2x)) \, dx
```
2. Solve the integral:

```math
\frac{1}{2} \left( x - \frac{1}{2} \sin(2x) \right) + C
```
3. Therefore, the result is:

```math
\int \sin^2(x) \, dx = \frac{1}{2} x - \frac{1}{4} \sin(2x) + C
```
### Example of Integration of Trigonometric Functions with Integration by Parts
```math
\int x \cdot \sin(x) \, dx
```
1. Choose `u = x` and `dv = \sin(x) \, dx`.
2. Compute `du = dx` and `v = -\cos(x)`.    
3. Substitute into the integration by parts formula:

```math
\int x \cdot \sin(x) \, dx = -x \cdot \cos(x) - \int -\cos(x) \, dx
```
4. Solve the remaining integral:

```math
\int -\cos(x) \, dx = -\sin(x) + C
```
5. Substitute the result into the original expression:

```math
\int x \cdot \sin(x) \, dx = -x \cdot \cos(x) + \sin(x) + C
```
6. Simplify:

```math
\int x \cdot \sin(x) \, dx = -x \cdot \cos(x) + \sin(x) + C
```

### Example of Integration of Trigonometric Functions with Complex Numbers
```math
\int e^{ix} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int e^{ix} \, dx = \frac{1}{i} e^{ix} + C
```
2. Therefore, the result is:

```math
\int e^{ix} \, dx = \frac{1}{i} e^{ix} + C
```
### Example of Integration of Trigonometric Functions with Polar Coordinates
```math
\int \frac{1}{x^2 + y^2} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int \frac{1}{x^2 + y^2} \, dx = \frac{1}{y} \arctan \left( \frac{x}{y} \right) + C
```
2. Therefore, the result is:

```math
\int \frac{1}{x^2 + y^2} \, dx = \frac{1}{y} \arctan \left( \frac{x}{y} \right) + C
```
### Example of Integration of Trigonometric Functions with Parametric Equations
```math
\int \frac{1}{x^2 + y^2} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int \frac{1}{x^2 + y^2} \, dx = \frac{1}{y} \arctan \left( \frac{x}{y} \right) + C
```
2. Therefore, the result is:

```math
\int \frac{1}{x^2 + y^2} \, dx = \frac{1}{y} \arctan \left( \frac{x}{y} \right) + C
```

## Integration of changes of variables

The integration of changes of variables refers to the technique of calculating integrals by changing the variable of integration. This method is useful when the integral is difficult to solve in its original form, but becomes simpler after a change of variables.

### Example of Integration of Changes of Variables
```math
\int x^2 \, dx
```
1. Choose `u = x^2`, then `du = 2x \, dx` or `dx = \frac{du}{2x}`.
2. Substitute into the integral:

```math
\int x^2 \, dx = \int u \cdot \frac{du}{2x}
```
3. Solve the integral:

```math
\int u \cdot \frac{du}{2x} = \frac{1}{2} \int u \, du
```
4. Obtain:

```math
\frac{1}{2} \cdot \frac{u^2}{2} + C = \frac{1}{4} u^2 + C
```
5. Substitute back `u = x^2`:

```math
\frac{1}{4} (x^2)^2 + C = \frac{1}{4} x^4 + C
```
6. Therefore, the result is:

```math
\int x^2 \, dx = \frac{1}{4} x^4 + C
```
### Example of Integration of Changes of Variables with Trigonometric Functions
```math
\int \sin^2(x) \, dx
```
1. Use the identity `sin^2(x) = \frac{1 - \cos(2x)}{2}` to rewrite the integral:

```math
\int \sin^2(x) \, dx = \frac{1}{2} \int (1 - \cos(2x)) \, dx
```
2. Solve the integral:

```math
\frac{1}{2} \left( x - \frac{1}{2} \sin(2x) \right) + C
```
3. Therefore, the result is:

```math
\int \sin^2(x) \, dx = \frac{1}{2} x - \frac{1}{4} \sin(2x) + C
```

### Example of Integration of Changes of Variables with Polar Coordinates
```math
\int \frac{1}{x^2 + y^2} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int \frac{1}{x^2 + y^2} \, dx = \frac{1}{y} \arctan \left( \frac{x}{y} \right) + C
```
2. Therefore, the result is:

```math
\int \frac{1}{x^2 + y^2} \, dx = \frac{1}{y} \arctan \left( \frac{x}{y} \right) + C
```
### Example of Integration of Changes of Variables with Parametric Equations
```math
\int \frac{1}{x^2 + y^2} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int \frac{1}{x^2 + y^2} \, dx = \frac{1}{y} \arctan \left( \frac{x}{y} \right) + C
```
2. Therefore, the result is:

```math
\int \frac{1}{x^2 + y^2} \, dx = \frac{1}{y} \arctan \left( \frac{x}{y} \right) + C
```
### Example of Integration of Changes of Variables with Complex Numbers
```math
\int e^{ix} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int e^{ix} \, dx = \frac{1}{i} e^{ix} + C
```
2. Therefore, the result is:

```math
\int e^{ix} \, dx = \frac{1}{i} e^{ix} + C
```
### Example of Integration of Changes of Variables with Substitution
```math
\int \frac{1}{x^2 + 4} \, dx
```
1. Recognize that the integral can be solved using the known formula:

```math
\int \frac{1}{x^2 + 4} \, dx = \frac{1}{2} \arctan \left( \frac{x}{2} \right) + C
```
2. Therefore, the result is:

```math 
\int \frac{1}{x^2 + 4} \, dx = \frac{1}{2} \arctan \left( \frac{x}{2} \right) + C
```

# Definite Integrals

The definite integral of a function `f(x)` over the interval `[a, b]` is defined as the limit of a Riemann sum as the number of subintervals approaches infinity. It represents the signed area under the curve of `f(x)` from `a` to `b`. Mathematically, it is expressed as:

```math
\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*) \Delta x
```

where `x_i^*` is a point in the `i-th` subinterval and `\Delta x` is the width of each subinterval.
The definite integral is used to calculate areas, volumes, and other quantities that can be represented as the accumulation of infinitesimal changes. It is also used in probability calculations and in modeling physical and economic phenomena.

### **Properties of the Definite Integral**

If `f(x)` and `g(x)` are functions of a real variable and `k` is a constant, the following properties hold:

```math
\int_a^b (f(x) \pm g(x))\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx
```
```math
\int_a^b k f(x)\,dx = k \int_a^b f(x)\,dx
```
```math
\int_a^a f(x)\,dx = 0
```
```math
\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx
```
```math
\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx, \quad \text{where } a \leq c \leq b
```

### **Comparison Properties**
```math
\int_a^b f(x)\,dx \leq \int_a^b g(x)\,dx \quad \text{if } f(x) \leq g(x) \text{ for all } x \in [a,b]
```
```math
\int_a^b f(x)\,dx \geq \int_a^b g(x)\,dx \quad \text{if } f(x) \geq g(x) \text{ for all } x \in [a,b]
```
```math
\int_a^b f(x)\,dx = \int_a^b g(x)\,dx \quad \text{if } f(x) = g(x) \text{ for all } x \in [a,b]
```

## Fundamental Theorem of Calculus

The Fundamental Theorem of Calculus establishes a connection between differentiation and integration. It states that if `f(x)` is continuous on the interval `[a, b]`, then the definite integral of `f(x)` from `a` to `b` can be computed using an antiderivative `F(x)` of `f(x)`:

```math
\int_a^b f(x) \, dx = F(b) - F(a)
```
This theorem allows us to evaluate definite integrals without having to compute the limit of Riemann sums directly. It also provides a way to find the area under the curve of a function by using its antiderivative.
### Example of the Fundamental Theorem of Calculus
```math
\int_0^1 x^2 \, dx
```
1. Find an antiderivative of `f(x) = x^2`, which is `F(x) = \frac{x^3}{3}`.
2. Apply the Fundamental Theorem of Calculus:

```math
\int_0^1 x^2 \, dx = F(1) - F(0) = \frac{1^3}{3} - \frac{0^3}{3} = \frac{1}{3}
```
3. Therefore, the result is:

```math
\int_0^1 x^2 \, dx = \frac{1}{3}
```

## Second Fundamental Theorem of Calculus (Barrow rule)

The Second Fundamental Theorem of Calculus, also known as the Barrow rule, states that if `f(x)` is continuous on the interval `[a, b]`, then the derivative of the definite integral of `f(x)` with respect to `x` is equal to `f(x)`:

```math
\frac{d}{dx} \int_a^x f(t) \, dt = f(x)
```
This theorem allows us to compute the derivative of a definite integral without having to evaluate the integral itself. It is particularly useful in applications where we need to find the rate of change of an accumulated quantity.
### Example of the Second Fundamental Theorem of Calculus
```math
\frac{d}{dx} \int_0^x t^2 \, dt
```
1. Apply the Second Fundamental Theorem of Calculus:

```math
\frac{d}{dx} \int_0^x t^2 \, dt = x^2
```
2. Therefore, the result is:

```math
\frac{d}{dx} \int_0^x t^2 \, dt = x^2
```
### Example of the Second Fundamental Theorem of Calculus with a Constant
```math
\frac{d}{dx} \int_0^x 3t^2 \, dt
```
1. Apply the Second Fundamental Theorem of Calculus:

```math
\frac{d}{dx} \int_0^x 3t^2 \, dt = 3x^2
```
2. Therefore, the result is:

```math
\frac{d}{dx} \int_0^x 3t^2 \, dt = 3x^2
```

### Aplications of the Definite Integral
The definite integral has numerous applications in various fields, including physics, engineering, economics, and biology. Some common applications include:
1. **Area under a curve**: The definite integral can be used to calculate the area under a curve defined by a function `f(x)` over a specific interval `[a, b]`.
2. **Volume of solids**: The definite integral can be used to calculate the volume of solids of revolution by integrating the area of cross-sections.
3. **Average value of a function**: The definite integral can be used to calculate the average value of a function over an interval `[a, b]` using the formula:

```math
\text{Average value} = \frac{1}{b - a} \int_a^b f(x) \, dx
```
4. **Work done by a variable force**: The definite integral can be used to calculate the work done by a variable force acting on an object over a distance.
5. **Probability**: The definite integral can be used to calculate probabilities in continuous probability distributions by integrating the probability density function over a specific interval.
6. **Accumulated change**: The definite integral can be used to calculate the accumulated change of a quantity over time, such as distance traveled or total revenue.
7. **Center of mass**: The definite integral can be used to calculate the center of mass of a solid or a system of particles by integrating the mass distribution over the volume or area.


