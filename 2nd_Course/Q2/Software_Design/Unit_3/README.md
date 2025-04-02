# State Pattern

Before defining this pattern, let's identify situations that help us recognize the key components and functionality necessary for applying the pattern.

This first image corresponds to the possible **states** in which a door can be found: open or closed, and the possible **transitions** that allow moving from one state to another. In this simple example, it is obvious that if the door is closed, we can open it, and if it is open, we can logically close it.

In other words, the important thing to understand is that a system represented by states will have a **set of states and a set of transitions** that allow moving from one state to another under certain conditions. The **behavior**, as if it were a service, offered by state-based systems is requested from a **context**, and its result or behavior will depend on the current state.

Imagine being able to communicate with the door and telling it to act(), the door’s behavior upon receiving our invocation to act would be to open if it were closed and to close if it were open. Here lies the important concept: **the context’s behavior depends on the current state.**

The door example only has two states; let's look at the next example. In this case, we have a traffic light that cycles through three states. **From one state, it is only possible to move to the next logical state.** Let’s identify the same key elements here. The context providing the service is the traffic light itself, which indicates to a vehicle whether it must stop (red light), continue driving (green light), or slow down and stop (amber light).

In this context, we have three **states**, and a possible **transition** that moves from one state to another could be nextState(), for example. In any case, we must seek a service interface (with the appropriate abstraction available). Achieving the highest available level of abstraction is always advisable.

For vehicles, the traffic light is the context that provides traffic regulation, but the traffic light itself must **delegate the displayed signal to the current state.** This delegation is characteristic of the state pattern: **delegation of service to the current state.**

### **Summary of the Analysis**

A state pattern consists of:

- Context.
- Common superclass for services.
- Set of states and transitions, including the concept of the current state.
- Delegation to the current state by composition.

### **Definition**

**State Pattern (State Pattern).** Also known as Objects for States. It allows an object to modify its behavior whenever its internal state changes.

### **Characteristics**

- Enables managing objects that can have multiple states and need to dynamically change behavior in response to state changes.
- Uses an abstraction layer to define behaviors that the observable model and observer model must comply with.
- The context’s behavior is delegated, through composition, to its internal states.

### **When to Use It?**

- **State Machines:** Used to model finite-state machines where an object can be in different states and transition between them.
- **User Interfaces:** Useful in UI development to manage component behavior based on the current state.
- **Games:** Used in game development to manage the behavior of characters, enemies, and objects according to their current state.

Three main components define the state pattern. Additionally, for the pattern to function correctly, there must be detailed elements that allow delegation by composition and state interchangeability.

### **Functionality**

- The context delegates the specific state request to the current Concrete State object.
- A context may pass itself as an argument to the State object handling the request, allowing the State object to access the context if necessary.
- The context serves as the main interface for clients. Once a context is configured with state objects, clients do not need to deal with state objects directly.
- Either the Context subclasses or Concrete State objects can decide which state follows another and under what circumstances.

If we compare the strategy behavior pattern with the state behavior pattern, we see they are like 'close relatives'. They are based on:

### **Additional Considerations for the State Pattern**

**Composition Relationship**

- **Question:** Can you identify how? Think about it before checking the answer.
- **Answer:** The context will have **a private attribute, a reference to the current state** with the behavior defined in the common superclass. Since a composition relationship implies that the instance is created by the context itself, it is usually instantiated **in the constructor.**

**Interchangeability of Internal States**

- **Question:** Can you identify how? Think about it before checking the answer.
- **Answer:** The interchangeability of internal states is ensured through the **setter corresponding to the private attribute representing the strategy object for the current state.**

**Delegation to the Current State**

- **Question:** Can you identify how? Think about it before checking the answer.
- **Answer:** The context exposes the **service method** defined as a strategy whose execution **is delegated to the current state,** in this case, the state object, which actually performs the execution.

### UML Diagram

The UML class diagram must define the common superclass as an abstract component, which may be an interface or an abstract class, implemented by each of the concrete states.

Regarding the common superclass (shown as State in the image), it is important to note that it applies to both an abstract class and an interface. In this specific diagram, the common superclass is an interface. Depending on the level of abstraction of the common superclass (abstract class or interface), the UML diagram will use different lines to distinguish between specialization or implementation by concrete states.

# **Exercise 1: Traffic Light State Pattern - Initial Solution**

### **Problem Statement**

We will represent the behavior of a traffic light by displaying a message corresponding to the color, based on the traffic light’s current state. The different states of the traffic light are:

- Green: Go.
- Amber: Stop.
- Red: Do not go.

### **1.a Objective - State Transition**

Modify the design so that after executing the **show method for each state**, the state itself changes the traffic light to the next corresponding state.

```
public interface TrafficLightState {
    void show();
}

public class TrafficLight {
    private TrafficLightState trafficLightState;

    public TrafficLight(TrafficLightState trafficLightState) {
        this.trafficLightState = trafficLightState;
    }

    public void setTrafficLightState(TrafficLightState trafficLightState) {
        this.trafficLightState = trafficLightState;
    }

    public void show() {
        this.trafficLightState.show(); // Delegation
    }
}
```

**Console Output Before Modification:**

```
Green light, go forward!!
Amber light, stop!
Red light, stop and wait!!
```

# Observer Pattern

Before defining this pattern, let's identify scenarios that help us recognize the key components and functionality necessary for applying it.

The **Observer Pattern** is a behavioral design pattern that establishes a **one-to-many dependency** between objects. When one object (the subject) changes state, all its dependents (observers) are automatically notified and updated.

---

### **Example: Weather Monitoring System**

Consider a **weather station** that tracks temperature, humidity, and pressure. Multiple display elements, such as a phone app, a website, and a physical display board, need to reflect these values.

- The **weather station** is the **subject** that holds the data.
- The **display elements** are the **observers** that subscribe to updates.
- When the weather station updates its data, all display elements automatically refresh.

The key elements of this pattern are:

1. **Subject (Observable):** Maintains a list of observers and notifies them of any state changes.
2. **Observers:** Define an interface for receiving updates from the subject.
3. **Concrete Subject:** Implements the Subject interface and stores the state.
4. **Concrete Observers:** Implement the Observer interface to receive and process updates.

---

### **Definition**

**Observer Pattern.** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

---

### **Characteristics**

- **Loose Coupling:** Observers do not need to know the concrete implementation of the subject.
- **Scalability:** New observers can be added dynamically without modifying the subject.
- **Automatic Updates:** Observers automatically receive updates when the subject changes.

---

### **When to Use It?**

- **Event-driven systems:** When multiple objects need to react to state changes in another object.
- **GUI Components:** To notify UI elements when data changes.
- **Real-time Monitoring:** In applications like stock markets, weather tracking, or notifications.

---

### **Functionality**

- The subject maintains a list of observers.
- Observers register and unregister dynamically.
- When the subject changes state, all observers are notified.
- Each observer updates itself based on the new state.

---

### **UML Diagram**

A UML class diagram for the Observer Pattern includes:

1. An **Observer** interface that defines the `update()` method.
2. A **ConcreteObserver** class implementing the `update()` method.
3. A **Subject** interface that defines methods for registering, removing, and notifying observers.
4. A **ConcreteSubject** class that maintains a list of observers and calls `update()` when its state changes.

---

### **Exercise 1: Weather Station Observer Pattern**

### **Problem Statement**

Create a **Weather Station** system where multiple observers (such as mobile apps and dashboards) receive real-time weather updates.

### **1.a Implementation - Observer Interface**

```
public interface Observer {
    void update(float temperature, float humidity, float pressure);
}
```

### **1.b Implementation - Subject Interface**

```
import java.util.ArrayList;
import java.util.List;

public interface Subject {
    void registerObserver(Observer o);
    void removeObserver(Observer o);
    void notifyObservers();
}
```

### **1.c Implementation - Concrete Subject**

```
public class WeatherStation implements Subject {
    private List<Observer> observers;
    private float temperature;
    private float humidity;
    private float pressure;

    public WeatherStation() {
        this.observers = new ArrayList<>();
    }

    public void registerObserver(Observer o) {
        observers.add(o);
    }

    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(temperature, humidity, pressure);
        }
    }

    public void setMeasurements(float temperature, float humidity, float pressure) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        notifyObservers();
    }
}
```

### **1.d Implementation - Concrete Observer**

```
public class WeatherDisplay implements Observer {
    private float temperature;
    private float humidity;
    private float pressure;

    public void update(float temperature, float humidity, float pressure) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        display();
    }

    public void display() {
        System.out.println("Current weather: " + temperature + "C, " + humidity + "% humidity, " + pressure + "hPa");
    }
}
```

### **1.e Testing the Observer Pattern**

```
public class ObserverPatternDemo {
    public static void main(String[] args) {
        WeatherStation weatherStation = new WeatherStation();
        WeatherDisplay display1 = new WeatherDisplay();
        WeatherDisplay display2 = new WeatherDisplay();

        weatherStation.registerObserver(display1);
        weatherStation.registerObserver(display2);

        weatherStation.setMeasurements(25.0f, 65.0f, 1013.0f);
        weatherStation.setMeasurements(22.5f, 70.0f, 1012.5f);
    }
}
```

### **Console Output**

```
Current weather: 25.0C, 65.0% humidity, 1013.0hPa
Current weather: 25.0C, 65.0% humidity, 1013.0hPa
Current weather: 22.5C, 70.0% humidity, 1012.5hPa
Current weather: 22.5C, 70.0% humidity, 1012.5hPa
```

This example illustrates how the **Observer Pattern** allows multiple observers to receive real-time updates from a subject, ensuring **decoupled, scalable, and maintainable** code.