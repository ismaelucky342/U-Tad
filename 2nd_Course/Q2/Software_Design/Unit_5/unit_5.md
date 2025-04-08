# **Unit 5. Structural Patterns**

## **Bridge Pattern**

---

### 📘 **Introduction and Objectives**

The **Bridge Pattern** is a **structural design pattern** that decouples an abstraction from its implementation, allowing the two to vary independently. It is particularly useful when you want to avoid a permanent binding between an abstraction and its implementation.

**Objective**:

- To understand how the **Bridge Pattern** separates abstraction from implementation.
- To learn its definition, when to use it, its components, and how it is represented in UML.

---

### 🎯 **Bridge Pattern**

---

### 🧾 **Definition**

The **Bridge Pattern** is a **structural design pattern** that separates the abstraction (interface) from its implementation, enabling them to evolve independently.

> It provides a bridge between the abstraction and the implementation, allowing flexibility and scalability.

---

### 🧩 **Characteristics and Uses**

### **Characteristics**

- **Decouples Abstraction and Implementation**: The abstraction and implementation can be developed and extended independently.
- **Promotes Composition Over Inheritance**: Uses composition to delegate implementation details.
- **Improves Scalability**: Adding new abstractions or implementations is straightforward.
- **Supports Open/Closed Principle**: New functionality can be added without modifying existing code.

### **When to Use It**

- When you want to decouple an abstraction from its implementation.
- When you need to combine different abstractions with different implementations.
- When changes in the implementation should not affect the abstraction and vice versa.
- When you want to avoid a proliferation of subclasses due to multiple dimensions of variation.

### **Examples in Real Life**

- A remote control (abstraction) that works with different devices (TV, radio, etc.) using a bridge to connect the two.
- A drawing application where shapes (abstraction) can be rendered using different rendering engines (implementation).
- A payment system where payment methods (credit card, PayPal) are decoupled from payment gateways.

---

### 🧱 **Components of the Bridge Pattern**

| Component            | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Abstraction**       | Defines the high-level interface and maintains a reference to the implementor. |
| **RefinedAbstraction**| Extends the abstraction and adds additional functionality.                 |
| **Implementor**       | Defines the interface for the implementation classes.                     |
| **ConcreteImplementor**| Implements the Implementor interface and provides specific functionality. |

---

### 📐 **UML Representation**

```plaintext
+-------------------+
|   Abstraction     |
+-------------------+
| - implementor:    |
|   Implementor     |
| + operation()     |
+-------------------+
         |
         v
+-------------------+       +-------------------+
| RefinedAbstraction
| + operation()      |
+--------------------+
          ^
          |
+--------------------+       +--------------------+
| ConcreteComponent  |<------|     Decorator      |
+--------------------+       +--------------------+
| + operation()      |       | + operation()      |
+--------------------+       | - component: Component |
                              +--------------------+
                                       ^
                                       |
                          +--------------------+
                          | ConcreteDecorator  |
                          +--------------------+
                          | + operation()      |
                          +--------------------+
```

---

### 💻 **Code Example**

#### **Java Example**

```java
// Component Interface
public interface Component {
    void operation();
}

// ConcreteComponent
public class ConcreteComponent implements Component {
    @Override
    public void operation() {
        System.out.println("Base operation");
    }
}

// Decorator Abstract Class
public abstract class Decorator implements Component {
    protected Component component;

    public Decorator(Component component) {
        this.component = component;
    }

    @Override
    public void operation() {
        component.operation();
    }
}

// ConcreteDecorator
public class ConcreteDecorator extends Decorator {
    public ConcreteDecorator(Component component) {
        super(component);
    }

    @Override
    public void operation() {
        super.operation();
        System.out.println("Additional behavior");
    }
}

// Client Code
public class Main {
    public static void main(String[] args) {
        Component base = new ConcreteComponent();
        Component decorated = new ConcreteDecorator(base);
        decorated.operation();
    }
}
```

---

### 🔑 **Key Takeaways**

- The **Decorator Pattern** is a flexible alternative to subclassing for extending functionality.
- It adheres to the **Open/Closed Principle**, allowing new behaviors to be added without modifying existing code.
- It is particularly useful when you need to add responsibilities to objects dynamically at runtime.

# **Adapter Pattern**

### 🧾 **Definition**

The **Adapter Pattern** is a **structural design pattern** that allows objects with incompatible interfaces to collaborate. It acts as a **bridge** between the client and an existing class or system.

> It converts the interface of one class into another interface that clients expect.
> 

---

### 🧩 **Characteristics and Uses**

### **Characteristics**

- Allows classes with incompatible interfaces to work together.
- Supports **reuse of existing code** by adapting it to new use cases.
- Comes in **two main forms**:
    - **Object Adapter**: Uses composition.
    - **Class Adapter**: Uses inheritance.

### **When to Use It**

- When you want to use an existing class but its interface doesn’t match what you need.
- When integrating third-party libraries or legacy code into new systems.
- When designing **middleware** or interface layers in large systems.

### **Real-Life Examples**

- A power adapter that lets a European plug fit into a US outlet.
- Software wrappers that allow old APIs to be used by modern clients.
- Adapting a JSON API to work with a system expecting XML.

---

### 🧱 **Components of the Adapter Pattern**

| Component | Description |
| --- | --- |
| **Target** | The interface expected by the client. |
| **Client** | Uses the Target interface. |
| **Adaptee** | The existing class with an incompatible interface. |
| **Adapter** | Implements the Target interface and translates calls to the Adaptee. |

---

### 📊 **UML Diagram – Object Adapter**

This is the most common form of the Adapter Pattern. It uses **composition**.

```

+----------+          uses        +------------------+
|  Client  |--------------------->|     Target       |
+----------+                     +------------------+
                                       ▲
                                       |
                               +---------------+
                               |   Adapter     |---> has a reference to
                               +---------------+     Adaptee
                               | - adaptee      |
                               | + request()    | --> calls adaptee.specificRequest()
                               +---------------+
                                       |
                                       v
                              +-------------------+
                              |     Adaptee       |
                              +-------------------+
                              | + specificRequest()|
                              +-------------------+

```

### 📌 How it works:

- **Client** calls `request()` on **Adapter**.
- **Adapter** translates and forwards the call to `specificRequest()` on **Adaptee**.

---

### 📘 **UML Diagram – Class Adapter**

This version uses **multiple inheritance** (supported in languages like C++).

```

+----------+         uses       +------------------+
|  Client  |------------------->|     Target       |
+----------+                   +------------------+
                                      ▲
                                      |
                           +---------------------+
                           |      Adapter        |
                           +---------------------+
                           | Inherits:           |
                           |  - Target           |
                           |  - Adaptee          |
                           | + request()         | --> calls Adaptee::specificRequest()
                           +---------------------+
                                      ▲
                                      |
                           +---------------------+
                           |      Adaptee        |
                           +---------------------+
                           | + specificRequest() |
                           +---------------------+

```

### 📌 Notes:

- **Adapter** inherits from both **Target** and **Adaptee**.
- Can override or extend functionality via inheritance.
- Less flexible in some languages, but useful when multiple inheritance is acceptable.


# Facade Pattern

---

### 🧾 **Definition**

The **Facade Pattern** is a **structural design pattern** that provides a **unified and simplified interface** to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use.

> It hides the complexity of the subsystem by encapsulating it behind a single entry point.
> 

---

### 🧩 **Characteristics and Uses**

### **Characteristics**

- **Simplifies** access to complex subsystems.
- Promotes **loose coupling** between the subsystem and the client.
- Improves **readability**, **maintainability**, and **usability** of code.
- Acts as a **wrapper** for multiple components.

### **When to Use It**

- When you want to provide a **simple interface** to a complex system.
- When working with a legacy system or third-party libraries that are difficult to use directly.
- When you want to **decouple** the client from internal implementation details.
- To implement **layers** in large applications (e.g., presentation layer calling the business logic layer via a facade).

### **Real-Life Examples**

- Remote control (Facade) that operates a complex entertainment system.
- Hotel concierge (Facade) that handles guest requests without exposing internal operations.
- A library API (Facade) that provides high-level functions while managing low-level modules internally.

---

### 🧱 **Components of the Facade Pattern**

| Component | Description |
| --- | --- |
| **Facade** | The main class that provides a simple interface and delegates calls to the subsystem classes. |
| **Subsystem Classes** | The complex set of classes or components that perform the actual work. These are hidden behind the facade. |
| **Client** | Interacts with the Facade instead of directly dealing with the subsystem. |

---

### 📊 **UML Diagram**

```

     +---------+
     | Client  |
     +---------+
         |
         v
     +-------------+
     |   Facade    |---------------------------+
     +-------------+                           |
     | + operation()|                          |
     +-------------+                          \|/
         |                        +----------------+   +-----------------+
         |---------------------->| SubsystemA     |   |  SubsystemB      |
         |                       +----------------+   +-----------------+
         |                       | + operationA() |   | + operationB()  |
         |                       +----------------+   +-----------------+
         |
         |                        +----------------+
         |---------------------->| SubsystemC     |
                                  +----------------+
                                  | + operationC() |
                                  +----------------+

```

### 🧭 How It Works:

- The **Client** interacts with the **Facade**, not the subsystems.
- The **Facade** handles communication with multiple **Subsystem Classes**.
- Each subsystem may perform part of the work, but the client remains unaware of this complexity.