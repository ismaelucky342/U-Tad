# Strategy Pattern

A **Strategy Pattern**, also known as **Policy**, consists of encapsulating related algorithms into classes that are subclasses of a common superclass. This allows the selection of an algorithm that varies depending on the object and also enables variation over time. *GoF95* Gamma E., Helm, R., Johnson, R., Vlissides J.: *Design Patterns: Elements of Reusable Object-Oriented Software*, Addison Wesley, 1995.

## **Characteristics**

- The **Strategy Pattern** describes how to implement a family of algorithms by encapsulating them to make them interchangeable. It allows defining a **family of algorithms**, placing each one in a separate class, and making their objects interchangeable.
- **Abstraction** to select one or more algorithms. It is usually implemented with interfaces.
- Based on **composition**, it often describes different ways of performing the same task.
- It favors composition over inheritance. The general idea is to identify what varies and encapsulate it for future reuse and interchangeability.
- The **Strategy Pattern** could be implemented with inheritance. In this case, we would have multiple subclasses of a **Context**, each with a different algorithm. The downside is that the algorithm cannot be changed dynamically.

## **When do we use it?**

- Many classes differ only in their behavior.
- Client requirements involve different variations of an algorithm. In this case, we define a family of algorithms, encapsulate each one, and make them interchangeable.
- We have multiple algorithms—Algorithm A, Algorithm B, Algorithm C—and at different times, we want to use each of them to solve a specific task without changing our interface for client communication.
- The application of the **Strategy Pattern** allows modifications to algorithms without changing the client code that invokes them.

The **Strategy Pattern** consists of three main components. Additionally, for the pattern to function correctly, there are supporting elements that enable delegation by aggregation and the interchangeability of strategies.

- **The Context**, which is composed of a Strategy object and instantiated with a specific strategy.
- **The Strategy**, which defines a common interface for the supported algorithms.
- **The Concrete Strategy**, which provides a specific implementation of an algorithm using the abstract strategy interface.

### **Additional Requirements**

### **Composition-Aggregation Relationship**

- The **Context** will have a **private attribute** that references a **Strategy object**, with the behavior defined in the common superclass. Since a **composition-aggregation relationship** implies that the instance can come from outside the object that will use it, we must provide a **Context constructor that accepts a Strategy object as a parameter**.

### **Interchangeability of Strategies**

- Strategies must be interchangeable through a **setter method** for the private attribute representing the Strategy object.

### **Delegation by Aggregation**

- The **Context** exposes the service method defined as a **Strategy**, delegating execution to the **Strategy object** that actually performs the operation.

## **UML Diagram**

This diagram helps describe the relationships among the three main components:

- **Context**: Composed of a **Strategy** object and instantiated with a specific strategy. It often includes a default strategy. It maintains a **composition-aggregation** relationship with the Strategy (hence, the white diamond in the class diagram). The **Context constructor and setter method** expose the Strategy for interchangeability.
- **Strategy**: Defines a common interface for the supported algorithms. This component can be either an **abstract class** or an **interface**. In both cases, it declares the service to be implemented by specialized classes corresponding to each encapsulated algorithm.
- **Concrete Strategy**: Implements a specific algorithm using the **abstract Strategy interface**. Concrete strategies provide different ways to implement the strategy method defined in the common superclass.

### **UML Class Diagram for the Strategy Pattern**

The following image shows a **simplified UML class diagram** for a **Strategy Pattern**:

---

## **Example Implementation**

Here is an example of the **Strategy Pattern** in Java:

```java
// Strategy Interface
public interface Strategy {
    String execute(String data);
}

// Concrete Strategies
public class ConcreteStrategyA implements Strategy {
    @Override
    public String execute(String data) {
        return "Strategy A processed " + data;
    }
}

public class ConcreteStrategyB implements Strategy {
    @Override
    public String execute(String data) {
        return "Strategy B processed " + data;
    }
}

// Context
public class Context {
    private Strategy strategy;

    public Context(Strategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }

    public String executeStrategy(String data) {
        return strategy.execute(data);
    }
}

// Client Code
public class Main {
    public static void main(String[] args) {
        Context context = new Context(new ConcreteStrategyA());
        System.out.println(context.executeStrategy("input data")); // Output: Strategy A processed input data

        context.setStrategy(new ConcreteStrategyB());
        System.out.println(context.executeStrategy("input data")); // Output: Strategy B processed input data
    }
}
```

This example demonstrates how the **Strategy Pattern** allows dynamic switching of algorithms at runtime by encapsulating them in separate classes.

---

# Template Pattern

The **Template Pattern** is another type of behavioral pattern that can even be used in combination with the **Strategy Pattern**. Below, we describe its functionality and analyze the UML class diagram for this pattern. Exploring the **combined use of the Strategy and Template patterns** is left as an open task.

The **Template Pattern** defines the **steps of an algorithm or service**.

In other words, it **establishes what must be done and in what order (this is the key aspect of the pattern)**, but not **how** it should be done. Instead, it leaves the implementation details to specialized subclasses that follow the **template method**, ensuring that each subclass executes the steps in the same order.

### **When should we use it?**

Whenever a service consists of **multiple ordered tasks**, and we want to allow flexibility in **how** these tasks are executed while maintaining a fixed **execution order**.

### **Definition**

The **Template Pattern** defines a method that specifies the **skeleton of an algorithm**, delegating some steps to **subclasses**.

## **Characteristics and Uses**

- Allows subclasses to **define certain steps** of the algorithm **without modifying its structure**.
- Allows subclasses to **implement variable behavior** by overriding specific methods.
- Prevents **code duplication** by implementing the overall workflow structure **once** in the abstract class, while subclasses define **variations**.

It consists of two main components:

### **1. Abstract Class**

- Defines the **skeleton of the algorithm** in the **template method**.
- Declares **abstract steps** as methods.
- Because the class contains at least one abstract method, it must be declared as an **abstract class**.

### **2. Concrete Class(es)**

- Implements the **abstract methods** declared in the abstract class.
- Encapsulates the algorithm as defined in the **template method**.

## **UML Diagram**

The following image shows the UML **class diagram** for the **Template Pattern**.

We can see how the **template method**, which is public, consists of **calls to methods within the class**, but **without implementation**.

The **Concrete Classes** must provide implementations for the **abstract parts** declared in the **Abstract Class**.

---

## **Example Implementation**

Here is an example of the **Template Pattern** in Java:

```java
// Abstract Class
public abstract class AbstractTemplate {
    public final void templateMethod() {
        stepOne();
        stepTwo();
        stepThree();
    }

    protected abstract void stepOne();
    protected abstract void stepTwo();

    protected void stepThree() {
        System.out.println("Step three is the same for all implementations.");
    }
}

// Concrete Class A
public class ConcreteClassA extends AbstractTemplate {
    @Override
    protected void stepOne() {
        System.out.println("ConcreteClassA: Step one implementation.");
    }

    @Override
    protected void stepTwo() {
        System.out.println("ConcreteClassA: Step two implementation.");
    }
}

// Concrete Class B
public class ConcreteClassB extends AbstractTemplate {
    @Override
    protected void stepOne() {
        System.out.println("ConcreteClassB: Step one implementation.");
    }

    @Override
    protected void stepTwo() {
        System.out.println("ConcreteClassB: Step two implementation.");
    }
}

// Client Code
public class Main {
    public static void main(String[] args) {
        AbstractTemplate concreteA = new ConcreteClassA();
        concreteA.templateMethod();

        AbstractTemplate concreteB = new ConcreteClassB();
        concreteB.templateMethod();
    }
}
```

This example demonstrates how the **Template Pattern** enforces a fixed structure for an algorithm while allowing subclasses to define specific steps.