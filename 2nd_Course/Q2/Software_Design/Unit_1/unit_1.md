# Introduction to Design Patterns

Design patterns in OOP are reusable solutions to common problems that arise when developing software. They provide a structured and tested approach to solving specific and recurring situations during software development.

We highlight four key aspects:

1. **Reusability**: Allows the reuse of proven solutions instead of reinventing the wheel.
2. **Maintainability**: Improves code readability, organization, and maintenance, promoting "clean code."
3. **Scalability**: Facilitates the adaptation and expansion of software as requirements evolve.
4. **Communication**: Establishes a common language among developers, improving understanding and team collaboration.

A design pattern is therefore defined as a general and reusable solution to a recurring problem in object-oriented programming. It represents an architecture, description, or template for solving that specific problem.

These patterns encompass best practices, assigning a name to the pattern that covers the solution and the proven experiences of the community throughout history.

### Classification of Design Patterns

**Behavioral Patterns**

They focus on the interaction between objects. To address possible interactions between objects, this unit will review the different types of relationships between them.

**Creational Patterns**

They focus on the creation of objects or class instances. They establish an efficient and flexible way to centralize both the object creation processes and the logic applied to the object or family of objects.

**Structural Patterns**

They deal with the composition of classes and objects to form more complex structures. These solutions promote class reusability.

## Basic Concepts of Design Patterns

Recalling the fundamental concepts of OOP, everything is an object, and every object has state, behavior, and identity. Everything is treated as an object except for primitive types, which can be cast into objects.

An algorithm is a collection of objects exchanging messages. The paradigm shift from procedural programming to object-oriented programming is based on the conversation that objects have. Instead of an algorithm with sequential steps from beginning to end, object-oriented programming involves an exchange of messages between objects that are part of a solution.

Each object has its own memory, formed by other objects. Attributes, in turn, are composed of other objects and can correspond to primitive types like char, int, or float, or to new classes with specific functionalities, forming what is known as composition.

Every object has an associated type that should be understood as an interface that an object offers to communicate with another object. All objects of a particular type can receive the same messages.

Finally, the notation we use to refer to objects follows the camelCase convention, which differentiates references to objects, attributes, methods, and classes.

## Class Design

Since OOP requires understanding the message exchange between elements in a solution, the first step is representing a class, regardless of the programming language used for its implementation. To represent a class design, we use a rectangle with the class name at the top.

The use of these rectangles is the most basic notation of the **Unified Modeling Language (UML)**, which we will describe in detail as we need to represent different parts of a class or relationships between classes.

Following the previous example, a rectangle labeled "Lightbulb" can represent a class named Lightbulb.

Typically, in addition to the class name, we indicate the declaration of its components, both private and public. In most cases, the class name alone is not enough to show the interface that an object belonging to a class offers. Therefore, we extend the rectangle by listing private components first, followed by public components (invocable by other objects).

The distinction between private and public components corresponds to the encapsulation provided by objects. As seen in object-oriented programming, attributes are kept as private components, accessible only by the object itself. This means we represent an object's state using private attributes.

Conversely, we represent an object's behavior through public components, its methods, making them invocable by other objects.

## Code Organization

Any programmed solution typically consists of a large number of interacting classes and objects. Therefore, organizing the source code that forms part of a solution is crucial.

This organization allows code reuse for other solutions, a concept known as component-based programming or code libraries. The specific use of classes to solve a problem is called client-side programming.

Since it is highly likely that a class name will be the same as one used by another development team, a naming convention is used to ensure a fully qualified class name is unique.

The organization of source code depends on the team or company, but a general convention follows this structure:

**domain.entity.department.subsystem.layer.type**

## Reusability

When a piece of code successfully implements a functionality, it is beneficial to reuse it due to its specialization, avoiding code duplication.

Two techniques are used for code reuse:

### **Composition**

- Indicates that an object maintains a "has-a" relationship.
- The strength of this ownership is differentiated into:
    - Composition.
    - Aggregation.

### **Inheritance**

- Indicates that an object is a specialization of another object.

**Composition** is a type of association where the contained class's lifespan must coincide with that of the container class. The components constitute part of the composite object. Thus, components cannot be shared among multiple composite objects. Deleting the composite object results in the deletion of its components.

The symbol for composition is a black diamond placed at the end where the class representing the "whole" (composite) is located.

**Aggregation** is a type of association that indicates that a class is part of another class (**weak composition**). Components can be shared by multiple composites, either from the same aggregation association or from different associations.

Aggregation is represented in UML by a white diamond placed at the end where the class representing the "whole" is located.

Due to the reusability and specialization of objects, they use an operation called delegation, by which they decide not to handle the request themselves under certain conditions. Instead, they delegate the service flow to the specialized object.

In delegation, two objects are responsible for handling a request:

- A receiver or context object
- A delegate object that provides the requested service

Based on the type of delegate object, we distinguish between:

- Composition delegation
- Injection delegation

# UML Unified Modeling Language

There are different design programs available for using UML. They are usually very similar, with the most well-known being Microsoft Visio, which requires a paid license, and Draw.io, which is free to use.

In this video, Microsoft Visio is presented as an option for representing UML diagrams.

### Classes

In the following image, two possibilities for representing a class named Engine are shown. One option is simply indicating the existence of the class (example on the left), or alternatively, specifying the class by differentiating its private and public components. For private elements, the symbol '-' is used to indicate that it is a private, encapsulated element.

For public components, the '+' symbol is used to indicate the possibility of invoking methods. In the example on the right, the existence of a constructor is noted, bearing the same name as the class and indicating the type of its parameters.

**Classes can be represented as:**

- **Without details**
    - Only the class name is indicated.
- **With details**
    - Includes its private and public components.
    - Attributes are represented as:
        - visibility attribute_name: Type = initial_value
    - Methods are represented as:
        - visibility method_name (parameter_list) : Return_Type
    - Default values for attributes and even pseudocode can be included.
- **Visibility**

| **Symbol** | **Access Type** |
| --- | --- |
| **+** | Public |
| **-** | Private |
| **#** | Protected |
| **~** | Default (package access) |
- **Abstract components are in italics or marked with << >>.**
- **Static components are underlined.**

### Relationships

The following sections present UML examples that illustrate relationships between classes. The relationships used in design patterns include inheritance or specialization, composition, aggregation, and creation or usability relationships.

**Inheritance or Specialization**

In object-oriented programming, the concept of inheritance or specialization has already been introduced. In UML, inheritance or specialization is represented using a solid line arrow with an empty head to indicate an **"is a"** relationship or specialization through inheritance (extends).

The interpretation of the UML diagram in the image is that a Beagle is a specific type of Dog, and Dog, in turn, is a specialized type of Animal. The example also illustrates the possible specialization of game pieces on a board, such as in chess. Here, we indicate that a QueenPiece is a specialized piece with its own behavior, derived from a GamePiece (which could represent any type of piece), as a specialization of a GameForm (which can abstract any shape, board, or piece).

**Interface Implementation or Behavior**

Also covered in object-oriented programming, it is common to represent that a class complies with an interface declared in an interface. Using a dashed line arrow with an empty head, we represent the **"Behavior of"** relationship or **implementation** (implements) of the methods declared in an interface.

The interpretation of the example shown indicates that there is an interface called GeometricArea, which states that a geometric body can have its area calculated if it implements the getArea() method that returns the area value.

In this example, the geometric bodies Square and Circle implement the getArea() method and generally adhere to the behavior declared in the corresponding interface.

**Composition**

We already know that a composition relationship indicates that an object is made up of another. Additionally, in the case of composition, the relationship is strong, meaning that the object cannot provide its functional service without having a composed object of the required type. A solid line arrow with a **filled diamond** (usually black) at the origin represents a **"Has a"** relationship through strong composition.

In the image, it is shown that an ElectricCar class is composed of an engine.

**Aggregation**

Aggregation is very similar to composition. However, with aggregation, we indicate that the composed object has "its own life" and does not necessarily depend on the container object. Therefore, we refer to it as a weak composition relationship. A solid line arrow with an **unfilled diamond** at the origin represents a **"Has a"** relationship through weak composition.

**Creation or Usability**

When neither composition nor aggregation is present, a dashed line is used to express a usability or object creation relationship. In creation relationships, an object can create other objects, whereas in usability relationships, an object uses another object. The same type of arrow is used for both cases, so it is explicitly indicated on the line whether it represents a "creates" (capable of creating an object) or "uses" (utilizes an object of that class) relationship.