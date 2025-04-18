# Singleton Pattern

Before defining this pattern, let's identify scenarios that help us recognize the key components and functionality necessary for applying it.

The **Singleton Pattern** is a creational design pattern that ensures a class has only **one instance** and provides a global point of access to it.

---

### **Example: Database Connection**

Consider a **database connection** in an application. If multiple instances were allowed, each instance might create a separate connection, consuming unnecessary resources. The Singleton pattern ensures that only one connection instance exists throughout the application.

- The **database connection** is a **singleton**.
- Multiple parts of the application access this **single instance**.
- Any attempt to create a new instance returns the existing one.

The key elements of this pattern are:

1. **Private Constructor:** Prevents external instantiation.
2. **Static Instance Variable:** Holds the single instance.
3. **Public Static Method:** Provides a global access point to the instance.

---

### **Definition**

**Singleton Pattern.** Ensures a class has only one instance and provides a global access point to it.

---

### **Characteristics**

- **Ensures a single instance:** No duplicate objects are created.
- **Global access point:** Provides easy access to the instance.
- **Lazy Initialization:** Instance is created only when first accessed.
- **Thread Safety Considerations:** Special handling is needed in multi-threaded environments.

---

### **When to Use It?**

- **Database Connections:** To manage a single connection pool.
- **Configuration Managers:** To maintain global settings.
- **Logging Mechanisms:** To ensure a single log instance.
- **Thread Pools:** To avoid redundant thread creation.

---

### **Functionality**

- The instance is stored in a static variable.
- A method provides controlled access to this instance.
- The constructor is private to restrict external instantiation.

---

### **UML Diagram**

A UML class diagram for the Singleton Pattern includes:

1. A **Singleton** class with a **private constructor**.
2. A **static method** that returns the unique instance.

---

### **Exercise 1: Singleton Database Connection**

### **Problem Statement**

Create a **Singleton Database Connection** class that ensures only one instance is created and shared across the application.

### **1.a Implementation - Singleton Class**

```
public class DatabaseConnection {
    private static DatabaseConnection instance;

    private DatabaseConnection() {
        System.out.println("Database Connection Initialized");
    }

    public static DatabaseConnection getInstance() {
        if (instance == null) {
            instance = new DatabaseConnection();
        }
        return instance;
    }

    public void connect() {
        System.out.println("Connected to Database");
    }
}
```

### **1.b Testing the Singleton Pattern**

```
public class SingletonPatternDemo {
    public static void main(String[] args) {
        DatabaseConnection connection1 = DatabaseConnection.getInstance();
        DatabaseConnection connection2 = DatabaseConnection.getInstance();

        connection1.connect();
        connection2.connect();

        System.out.println(connection1 == connection2);
    }
}
```

### **Console Output**

```
Database Connection Initialized
Connected to Database
Connected to Database
true
```

This example illustrates how the **Singleton Pattern** ensures that only one instance of `DatabaseConnection` is created, making the application more efficient and manageable.

# Factory Pattern

The **Factory Pattern** is a creational design pattern that provides an interface for creating objects in a super class but allows subclasses to alter the type of objects that will be created.

---

### **Example: Shape Creation**

Consider an application that needs to create different types of shapes like circles, rectangles, and squares. Instead of creating instances of each shape directly in the code, a **Factory** can provide a method to create these objects based on the shape type requested.

- The **Shape Factory** creates objects of different shapes.
- The client code calls the factory method to create the shape it needs.
- The factory determines which specific shape object to create.

The key elements of this pattern are:

1. **Product Interface:** Defines the interface for the objects that the factory will create.
2. **Concrete Products:** Implement the product interface and define specific objects.
3. **Creator (Factory):** Declares the factory method, which returns a product.
4. **Concrete Creator:** Implements the factory method to return an instance of a concrete product.

---

### **Definition**

**Factory Pattern** defines an interface for creating objects but allows subclasses to alter the type of objects that will be created.

---

### **Characteristics**

- **Encapsulates Object Creation:** Creation logic is abstracted in the factory.
- **Decouples Code:** The client doesn't need to know how objects are created, only what type it needs.
- **Extensibility:** New product types can be added easily without modifying client code.
- **Centralizes Object Creation:** Helps centralize the instantiation logic in a single class.

---

### **When to Use It?**

- **When the object creation process is complex.**
- **When you need to create families of related objects.**
- **When you need to decouple object creation from the actual use.**
- **When objects need to be created based on some input (e.g., type or configuration).**

---

### **Functionality**

- The factory provides an interface to create objects.
- Concrete classes implement the factory interface to generate specific products.
- The client uses the factory to obtain objects without needing to know the details of their creation.

---

### **UML Diagram**

A UML class diagram for the Factory Pattern includes:

1. **Product Interface** that defines the methods for the objects.
2. **Concrete Products** that implement the product interface.
3. **Creator (Factory)** that declares a method to create products.
4. **Concrete Creator** that implements the factory method to return concrete products.

---

### **Exercise 1: Factory Pattern for Shape Creation**

### **Problem Statement**

Create a **Shape Factory** that can generate different types of shapes like **Circle** and **Rectangle** based on the requested type.

### **1.a Implementation - Factory Class**

```java
java

// Product interface
interface Shape {
    void draw();
}

// Concrete Products
class Circle implements Shape {
    public void draw() {
        System.out.println("Drawing Circle");
    }
}

class Rectangle implements Shape {
    public void draw() {
        System.out.println("Drawing Rectangle");
    }
}

// Factory (Creator)
class ShapeFactory {
    // Factory method
    public Shape getShape(String shapeType) {
        if (shapeType == null) {
            return null;
        }
        if (shapeType.equalsIgnoreCase("CIRCLE")) {
            return new Circle();
        } else if (shapeType.equalsIgnoreCase("RECTANGLE")) {
            return new Rectangle();
        }
        return null;
    }
}

```

### **1.b Testing the Factory Pattern**

```java
java

public class FactoryPatternDemo {
    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();

        // Get a Circle object and call its draw method
        Shape shape1 = shapeFactory.getShape("CIRCLE");
        shape1.draw();

        // Get a Rectangle object and call its draw method
        Shape shape2 = shapeFactory.getShape("RECTANGLE");
        shape2.draw();
    }
}

```

### **Console Output**

```
mathematica

Drawing Circle
Drawing Rectangle

```

This example illustrates how the **Factory Pattern** simplifies object creation by providing a centralized method for producing shapes, allowing the client to request specific types without needing to know the details of object instantiation.

### Abstract Factory Pattern

The **Abstract Factory Pattern** is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

This pattern works well when you need to create multiple related objects, but the exact type of objects may vary based on the system's configuration, operating environment, or user preferences.

---

### **Example: GUI Framework**

Consider a GUI framework where the application may need different widgets based on the operating system. For example, buttons and checkboxes might look different on Windows, MacOS, or Linux.

- The **Abstract Factory** will define the interface for creating GUI components (e.g., buttons, checkboxes).
- Concrete factories will implement this interface for each operating system.
- The client code will work with the abstract factory and will not need to know the specific operating system-specific details of how the components are created.

The key elements of this pattern are:

1. **Abstract Factory:** Declares methods for creating abstract product families (e.g., buttons, checkboxes).
2. **Concrete Factory:** Implements the abstract factory interface and creates concrete product families.
3. **Abstract Product:** Defines the interface for product objects (e.g., Button, Checkbox).
4. **Concrete Product:** Implements the abstract product interface and represents the specific product (e.g., WindowsButton, MacOSButton).

---

### **Definition**

**Abstract Factory Pattern** provides an interface for creating families of related or dependent objects without specifying their concrete classes.

---

### **Characteristics**

- **Product Families:** The factory produces a set of related objects.
- **Decouples Client Code:** The client is decoupled from the concrete classes of the objects it needs to create.
- **Extensible:** New families of products can be added easily by implementing new concrete factories.
- **Abstracts Object Creation:** Allows the client to work with abstract product types while concrete factories take care of the creation details.

---

### **When to Use It?**

- **When the system needs to be independent of how its products are created, composed, and represented.**
- **When the system should be configured with one of multiple families of products.**
- **When the client needs to work with products that belong to different families but shouldn’t depend on their concrete classes.**

---

### **Functionality**

- The abstract factory defines the interface for creating product families.
- Concrete factories implement this interface and produce actual objects.
- The client uses the abstract factory to create product families without worrying about the details of object creation.

---

### **UML Diagram**

A UML class diagram for the Abstract Factory Pattern includes:

1. **Abstract Factory** with methods for creating abstract products.
2. **Concrete Factories** that implement the abstract factory methods.
3. **Abstract Products** that define the interface for product families.
4. **Concrete Products** that implement the abstract product interface.

---

### **Exercise 1: Abstract Factory Pattern for GUI Creation**

### **Problem Statement**

Create an **Abstract Factory** that can produce **buttons** and **checkboxes** for different operating systems like **Windows** and **MacOS**.

### **1.a Implementation - Abstract Factory Class**

```java
java

// Abstract Products
interface Button {
    void render();
}

interface Checkbox {
    void render();
}

// Concrete Products for Windows
class WindowsButton implements Button {
    public void render() {
        System.out.println("Rendering Windows Button");
    }
}

class WindowsCheckbox implements Checkbox {
    public void render() {
        System.out.println("Rendering Windows Checkbox");
    }
}

// Concrete Products for MacOS
class MacOSButton implements Button {
    public void render() {
        System.out.println("Rendering MacOS Button");
    }
}

class MacOSCheckbox implements Checkbox {
    public void render() {
        System.out.println("Rendering MacOS Checkbox");
    }
}

// Abstract Factory
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

// Concrete Factory for Windows
class WindowsFactory implements GUIFactory {
    public Button createButton() {
        return new WindowsButton();
    }

    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}

// Concrete Factory for MacOS
class MacOSFactory implements GUIFactory {
    public Button createButton() {
        return new MacOSButton();
    }

    public Checkbox createCheckbox() {
        return new MacOSCheckbox();
    }
}

```

### **1.b Testing the Abstract Factory Pattern**

```java
java

public class AbstractFactoryPatternDemo {
    public static void main(String[] args) {
        // Client code: Decide which factory to use based on OS type
        GUIFactory factory;

        String osType = "Windows"; // Simulate OS type

        if (osType.equalsIgnoreCase("Windows")) {
            factory = new WindowsFactory();
        } else {
            factory = new MacOSFactory();
        }

        // Create button and checkbox using the factory
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();

        button.render();
        checkbox.render();
    }
}

```

### **Console Output**

```
mathematica

Rendering Windows Button
Rendering Windows Checkbox

```

In this example, the **Abstract Factory Pattern** allows the creation of GUI components (buttons and checkboxes) for different operating systems (Windows, MacOS) without the client needing to know the concrete classes involved.

By using the **GUIFactory** interface, the client code can easily switch between different operating system-specific implementations just by changing the factory instance, ensuring flexibility and scalability.