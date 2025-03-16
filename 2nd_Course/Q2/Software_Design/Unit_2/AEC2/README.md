![image.png](attachment:a2135ad5-5d3c-4a20-b4b2-877d68fa7f35:image.png)

# Introduction

In this project, I worked with two behavioral patterns: **Strategy Pattern** and **Template Method Pattern**, applying them in the context of a medical service in a kindergarten. The goal was to structure the code so that the behavior of the medical service (child inspection, sending results, and billing) was flexible according to the doctor, but also with a common workflow that could not be altered.

### Tools used:

- **Notion**: For project development and organization. I used Notion to divide the project into sections, define milestones, easily insert code, and perform a subsequent conversion to PDF, which facilitated the entire project.
- **Eclipse IDE**: I used Eclipse as the development environment to program the project in Java. Eclipse provided me with tools such as debugging, autocompletion, dependency management, and the ability to work with multiple classes and files efficiently.
- **Draw.io**: For designing the UML diagram. I used Draw.io to visually represent the system architecture and the applied patterns. This diagram helped me plan the interactions between the classes and visualize how the Strategy and Template Method patterns were applied in the solution.

# **Strategy Pattern**

The **Strategy Pattern** allowed me to define different behaviors for each doctor without modifying the context or the general workflow of the service. This seemed to me the most appropriate way to handle the different types of medical services offered in the kindergarten, as each doctor (Fong, Wang, etc.) has their own way of inspecting the children, but the rest of the actions (sending results and invoice) must be the same for all doctors.

### Approach and Resolution:

- **Classes `DoctorServiceStrategy`, `FongDoctorStrategy`, `WangDoctorStrategy`, and `NoDoctorServiceStrategy`**: I created an abstract class `DoctorServiceStrategy` to define common actions and specific tasks for each doctor. The concrete classes implement `inspectChildren()` specifically for each doctor, while the other tasks (`sendResultsInspection()` and `sendInvoice()`) are common and have the same implementation for all doctors.

    The idea here is that the inspection behavior is variable depending on the doctor, but the other tasks remain fixed. This allows changing a doctor's strategy without altering the general workflow, which must follow the same pattern.

- **Class `KinderGardenServiceContext`**: This context handles the assignment of the medical service strategy (the doctor) and the execution of tasks in order. In my design, this class has an attribute `serviceStrategy` that defines which doctor's strategy is being used at any given time.

    I decided that the context should be responsible for managing the active strategy. This means that doctors (and therefore strategies) can be changed at runtime, making the system flexible.

### Class `NoDoctorServiceStrategy`:

Additionally, I included the class `NoDoctorServiceStrategy`, which represents the case where no medical service is available in the kindergarten. This class extends `DoctorServiceStrategy` and only implements the task of `inspectChildren()`, which in this case adapts to the absence of a doctor.

---

# **Template Method Pattern**

The **Template Method Pattern** was used to define the order of execution of the medical service tasks. This was necessary because the tasks must follow a specific flow that should not be altered: first, the children are inspected, then the results are sent, and finally, the invoice is sent. However, only the inspection task should be variable depending on the doctor, while the rest follows a common flow.

### Resolution:

- **Method `applyServiceStrategy()` in `DoctorServiceStrategy`**: I implemented a method `applyServiceStrategy()` in the abstract class `DoctorServiceStrategy`, which contains the common workflow of the tasks. This method defines the order of execution: first `inspectChildren()`, then `sendResultsInspection()`, and finally `sendInvoice()`. Each doctor can override only `inspectChildren()` to customize the inspection, but the other tasks are executed the same for all.

    With this, the Template Method pattern ensures that the task flow is fixed and cannot be altered, while allowing each doctor to customize their inspection. This structure is ideal when a common process needs to be maintained but with some specific variations in a context.

---

**Implementation and Expected Result**

Regarding the code, I developed the following set of classes that I will break down and explain in detail later:

- **Class `KinderGardenServiceContext`**: Manages the context and has a method `applyServiceStrategy()` that orchestrates the execution of tasks in order.
- **Strategy classes (`FongDoctorStrategy`, `WangDoctorStrategy`, `NoDoctorServiceStrategy`)**: Implement the inspection logic, with a personalized message for each doctor.
- **Common methods in `DoctorServiceStrategy`**: The methods `sendResultsInspection()` and `sendInvoice()` have a common implementation used by all doctors.

I decided to keep the specific messages for each task (e.g., "Inspection task completed") within each corresponding method to make it clear what action is being executed at each moment. Additionally, this design ensures that, although the task flow is common for all doctors, each has their own logic in the inspection task.

# **Final Solution Implemented in Java**

### Overview of the code flow:

- In the `main` method, a context (`KinderGardenServiceContext`) is created with Dr. Fong's strategy (`FongDoctorStrategy`).
- `applyServiceStrategy()` is called, which executes the steps defined by Dr. Fong's strategy.
- Then, the strategy is changed to `WangDoctorStrategy` using `setServiceStrategy()` and `applyServiceStrategy()` is called again, which now executes the steps with Dr. Wang's logic.

### My final code:

```java
// Context Class
public class KinderGardenServiceContext {
    private DoctorServiceStrategy serviceStrategy;

    public KinderGardenServiceContext(DoctorServiceStrategy serviceStrategy) {
        this.serviceStrategy = serviceStrategy;
    }

    public void setServiceStrategy(DoctorServiceStrategy serviceStrategy) {
        this.serviceStrategy = serviceStrategy;
    }

    public void applyServiceStrategy() {
        serviceStrategy.inspectChildren();
        serviceStrategy.sendResultsInspection();
        serviceStrategy.sendInvoice();
    }
}

// Abstract Class - Medical Service Strategy
abstract class DoctorServiceStrategy {
    public void applyServiceStrategy() {
        inspectChildren();
        sendResultsInspection();
        sendInvoice();
    }

    protected abstract void inspectChildren();

    public void sendResultsInspection() {
        System.out.println("Inspection results have been sent");
    }

    public void sendInvoice() {
        System.out.println("The corresponding service invoice has been sent");
    }
}

// Fong Strategy
class FongDoctorStrategy extends DoctorServiceStrategy {
    @Override
    protected void inspectChildren() {
        System.out.println("FongDoctorStrategy: I am inspecting the children");
        System.out.println("Inspection task completed");
    }
}

// Wang Strategy
class WangDoctorStrategy extends DoctorServiceStrategy {
    @Override
    protected void inspectChildren() {
        System.out.println("WangDoctorStrategy: I am inspecting the children");
        System.out.println("Inspection task completed");
    }
}

// Main Class for Testing
public class TestKinderGardenService {
    public static void main(String[] args) {
        // Assuming Dr. Fong is on duty
        KinderGardenServiceContext kinderGardenContext = new KinderGardenServiceContext(new FongDoctorStrategy());
        kinderGardenContext.applyServiceStrategy();

        // Changing the medical service, now Dr. Wang is on duty
        kinderGardenContext.setServiceStrategy(new WangDoctorStrategy());
        kinderGardenContext.applyServiceStrategy();
    }
}
```

### Class Development:

**Class `KinderGardenServiceContext` (Context)**

- **Attribute `serviceStrategy`**: Maintains a reference to a medical service strategy that will be applied. The type of this strategy is a class that implements the interface or abstract class `DoctorServiceStrategy`.
- **Constructor Method**: Through the constructor, the initial strategy (an object that implements `DoctorServiceStrategy`) is assigned.
- **Method `setServiceStrategy`**: Allows changing the strategy at runtime, i.e., changing the doctor or the way the service is performed.
- **Method `applyServiceStrategy`**: Calls the methods of the defined strategy, such as `inspectChildren`, `sendResultsInspection`, and `sendInvoice`. This is the point of interaction with the strategies.

**Abstract Class `DoctorServiceStrategy` (Medical Service Strategy)**

- **Method `applyServiceStrategy`**: This is a method called from the context. This method applies a series of common steps in all strategies:
    - **`inspectChildren()`**: This is an abstract method, defined differently in each strategy (Fong or Wang).
    - **`sendResultsInspection()`**: This method is common to all strategies and simply prints a message indicating that the inspection results have been sent.
    - **`sendInvoice()`**: Similar to the previous one, this method is common and prints a message indicating that the invoice has been sent.

The `DoctorServiceStrategy` class provides a common structure for all service strategies but leaves the inspection details to be defined by the subclasses.

**Concrete Classes `FongDoctorStrategy` and `WangDoctorStrategy`**

- **`FongDoctorStrategy`**: This is a concrete implementation of the strategy. It defines how the children's inspection is carried out in the case of Dr. Fong. In this case, it simply prints a message indicating that Dr. Fong is inspecting the children.
- **`WangDoctorStrategy`**: This is another concrete implementation of the strategy, but with similar logic for Dr. Wang, with messages adapted to Dr. Wang.

Both classes override the abstract method `inspectChildren()` to provide their own implementation of the inspection but use the `sendResultsInspection()` and `sendInvoice()` methods that are common to all strategies.

**Main Class `TestKinderGardenService` (Test)**

- In the `main` method, a context (`KinderGardenServiceContext`) is created with Dr. Fong's strategy (`FongDoctorStrategy`).
- `applyServiceStrategy()` is called, which executes the steps defined by Dr. Fong's strategy.
- Then, the strategy is changed to `WangDoctorStrategy` using `setServiceStrategy()` and `applyServiceStrategy()` is called again, which now executes the steps with Dr. Wang's logic.

### Expected Console Results

When running the code, the console results will be as follows:

```
FongDoctorStrategy: I am inspecting the children
Inspection task completed
Inspection results have been sent
The corresponding service invoice has been sent

WangDoctorStrategy: I am inspecting the children
Inspection task completed
Inspection results have been sent
The corresponding service invoice has been sent

```

## UML Diagram

It was necessary to develop and modify a UML diagram based on the one we already had in the activity sheet to represent the structure of the classes and the implementation of the **Strategy** and **Template Method** design patterns in a medical service for a kindergarten.

### 1. **Main Classes:**

- **`KinderGardenServiceContext`:** This class manages the medical service strategy (the doctor) and executes the workflow. It contains methods to change the strategy and apply the medical service according to the selected doctor.
- **`DoctorServiceStrategy`:** Abstract class that defines the common scheme of medical tasks (inspection, results, and invoice). It allows customizing the inspection for each doctor using the **Template Method** pattern.
- **`FongDoctorStrategy`, `WangDoctorStrategy`, `NoDoctorServiceStrategy`:** These are concrete classes that implement the children's inspection specifically for each doctor. The other tasks (results and invoice) follow the common flow.

### 2. **Relationships and Inheritance:**

- **Composition**: `KinderGardenServiceContext` has a composition relationship with `DoctorServiceStrategy`, allowing it to change the strategy at runtime.
- **Inheritance**: The classes `FongDoctorStrategy`, `WangDoctorStrategy`, and `NoDoctorServiceStrategy` inherit from `DoctorServiceStrategy`, customizing the inspection according to the doctor.

### 3. **Execution Flow:**

The diagram shows how, by invoking the `applyServiceStrategy()` method in `KinderGardenServiceContext`, the tasks are executed in the following order: inspection (customized by each doctor), sending results, and billing (common for all).

![image.png](attachment:b2792e6a-5629-42ea-92fb-e591faf8f2c5:image.png)

```java
@startuml

class KinderGardenServiceContext {
    - serviceStrategy: DoctorServiceStrategy
    + setServiceStrategy(serviceStrategy: DoctorServiceStrategy)
    + applyServiceStrategy()
}

abstract class DoctorServiceStrategy {
    + applyServiceStrategy()
    + inspectChildren()
    + sendResultsInspection()
    + sendInvoice()
}

class NoDoctorServiceStrategy {
    + inspectChildren()
}

class FongDoctorStrategy {
    + inspectChildren()
}

class WangDoctorStrategy {
    + inspectChildren()
}

KinderGardenServiceContext "1" --* "1" DoctorServiceStrategy : serviceStrategy
DoctorServiceStrategy <|-- NoDoctorServiceStrategy
DoctorServiceStrategy <|-- FongDoctorStrategy
DoctorServiceStrategy <|-- WangDoctorStrategy

class TestKinderGardenService {
    + main()
}

@enduml
```

# Bibliography and External Material

For the development of the activity, the use of complementary material was essential both for code development and for the assimilation of subject concepts. I attach links to the main tools I used in this project:

W3 Schools (tutorials with examples):

https://www.w3schools.com/java/java_regex.asp

https://www.w3schools.blog/java-design-patterns-tutorial-with-examples#google_vignette

Codewars (programming challenge site):
https://www.codewars.com/collections/design-patterns

Geeksforgeeks (additional documentation):

https://www.geeksforgeeks.org/software-design-patterns/

YouTube (additional tutorials):
https://www.youtube.com/watch?v=tDxnyop48mY&list=PLsyeobzWxl7r2ZX1fl-7CKnayxHJA_1ol

https://www.youtube.com/watch?v=v9ejT8FO-7I&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc
