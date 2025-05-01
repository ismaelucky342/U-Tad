# **AEC3: Refactoring**

## **1. Code Analysis: Detecting and Locating *Code Smells***

In this activity, I was asked to analyze a class that manages orders in a sales system. The original class is as follows:

```java
public class OrderProcessor {
private double totalAmount;
private String customerName;
private int availableStock;
public OrderProcessor(double totalAmount, String customerName, int availableStock) {
this.totalAmount = totalAmount;
this.customerName = customerName;
this.availableStock = availableStock;
}
public void processOrder() {
// Check stock
if (availableStock < 1) {
System.out.println("Insufficient Stock");
return;
}

// Apply a possible discount
double discount = 0;
if (totalAmount > 100) { 
discount = totalAmount * 0.1; 
totalAmount -= discount; 
} 

// Payment processing 
boolean paymentProcessed = processPayment(totalAmount); 

// Generate notification to the client 
if (paymentProcessed) { 
sendNotification(); 
} 
} 

private boolean processPayment(double amount) { 
System.out.println("Processing payment for: " + amount); 
return true; 
} 

private void sendNotification() { 
System.out.println("Notification sent to " + customerName); 
}
}

```

After reading and analyzing the code, I identified the following code smells, which we studied in the unit:

### **Long Method**

A *long method* is a method that attempts to do too many things at once, which violates the **Single Responsibility Principle**. In this case, the `processOrder()` method is responsible for:

1. Checking stock,
2. Calculating the discount,
3. Processing the payment,
4. Sending the notification to the customer.

This makes it difficult to read and maintain.

This is evident throughout the `processOrder()` method.

```java
public void processOrder() {
if (availableStock < 1) {
System.out.println("Insufficient Stock");
return;
}

double discount = 0;
if (totalAmount > 100) {
discount = totalAmount * 0.1;
totalAmount -= discount;
}

boolean paymentProcessed = processPayment(totalAmount);

if (paymentProcessed) {
sendNotification();
}
}
```

**My Solution:** I used **Extract Method** to separate each of these tasks into smaller methods: `hasStock()`, `applyDiscount()`, `handlePayment()`, and `notifyCustomer()`.

---

### **Feature Envy**

This code smell occurs when a method accesses too many attributes of its own class to make decisions or perform logic that could be elsewhere, or when methods that don't apply to it are abused.

In this case, `processOrder()` directly manipulates the `availableStock`, `totalAmount`, and `customerName` attributes, suggesting that some of that logic should reside in other methods or classes.

We also find this in `processOrder()`.

```java
if (availableStock < 1) { ... }
if (totalAmount > 100) { ... }
System.out.println("Notification sent to " + customerName);
```

**My solution:** By separating responsibilities into smaller methods, each handles only the data it needs, reducing the main method's direct dependency on internal attributes.

---

### **Magic Numbers**

*Magic numbers* are numerical values ​​that appear directly in the code without any explanation, making them difficult to understand and maintain. Here, the numbers `100` (discount threshold) and `0.1` (10% discount) appear without context.

We can see it inside `processOrder()`, in the discount calculation.

```java
if (totalAmount > 100) {
discount = totalAmount * 0.1;
}
```

**My solution:** I applied **Extract Constant** and created two constants with meaningful names:

```java
private static final double DISCOUNT_THRESHOLD = 100;
private static final double DISCOUNT_RATE = 0.1;
```

Now the code is much easier to understand:

```java
if (totalAmount > DISCOUNT_THRESHOLD) {
discount = totalAmount * DISCOUNT_RATE;
}
```

### **Low Cohesion**

Cohesion measures how closely related a class's responsibilities are. A class with **poor cohesion** tries to handle too many different things. In `OrderProcessor`, the class handles:

- Stock checking,
- Discount logic,
- Payment processing,
- Customer notification.

This is clearly seen throughout the overall design of the class, especially in the `processOrder()` method.

This makes the class difficult to extend or modify without breaking additional functionality. If the system grows (for example, integrating multiple payment methods or multiple notification channels), this class will become unmanageable.

**What long-term solution do I see?** Separate the logic into different classes, for example:

- `StockManager`
- `DiscountCalculator`
- `PaymentService`
- `NotificationService`

For this practice, I partially solved it by separating logic into well-defined methods within the same class, which leads us to the second section.

## **2. Refactoring Techniques Applied**

Based on what I learned in the unit (especially in the *Composing Methods* and *Organizing Data* sections), I applied the following specific techniques:

---

### **Extract Method**

I split `processOrder()` into several smaller methods. The code before:

```java
// Original code: long and unclear
public void processOrder() {
if (availableStock < 1) { ... }
if (totalAmount > 100) { ... }
processPayment(totalAmount);
sendNotification();
}
```

After:

```java
public void processOrder() {
if (!hasStock()) return;
applyDiscountIfNeeded();
if (handlePayment()) {
notifyCustomer();
}
}
```

This greatly improves **readability and maintainability** and makes it easier to run separate unit tests.

### **Extract Constant**

Before:

```java
if (totalAmount > 100) {
discount = totalAmount * 0.1;
}
```

After:

```java
private static final double DISCOUNT_THRESHOLD = 100;
private static final double DISCOUNT_RATE = 0.1;

...

if (totalAmount > DISCOUNT_THRESHOLD) {
discount = totalAmount * DISCOUNT_RATE;
}
```

This prevents errors if those values ​​change and makes them easier to reuse.

---

### **Rename**

I renamed methods and variables to be **self-explanatory**, following the principle that code should be self-explanatory. For example:

- `processOrder()` → is maintained, but relies on:
- `hasStock()`
- `applyDiscountIfNeeded()`
- `handlePayment()`
- `notifyCustomer()`

---

## **Refactored code and explanation of changes**

```java
public class OrderProcessor {
    private double totalAmount;
    private String customerName;
    private int availableStock;

    private static final double DISCOUNT_THRESHOLD = 100;
    private static final double DISCOUNT_RATE = 0.1;

    public OrderProcessor(double totalAmount, String customerName, int availableStock) {
        this.totalAmount = totalAmount;
        this.customerName = customerName;
        this.availableStock = availableStock;
    }

    public void processOrder() {
        if (!hasStock()) {
            System.out.println("Stock insuficiente");
            return;
        }

        applyDiscountIfNeeded();

        if (processPayment()) {
            notifyCustomer();
        }
    }

    private boolean hasStock() {
        return availableStock > 0;
    }

    private void applyDiscountIfNeeded() {
        if (totalAmount > DISCOUNT_THRESHOLD) {
            double discount = totalAmount * DISCOUNT_RATE;
            totalAmount -= discount;
        }
    }

    private boolean processPayment() {
        System.out.println("Procesando pago de: " + totalAmount);
        return true;
    }

    private void notifyCustomer() {
        System.out.println("Notificación enviada a " + customerName);
    }
}
```
### **Changes**

- I split the `processOrder()` method into submethods: `hasStock()`, `applyDiscountIfNeeded()`, `processPayment()`, and `notifyCustomer()`.
- I replaced magic values ​​(`100`, `0.1`) with well-named constants.
- I named the methods clearly and precisely to indicate what they do.

---

## **4. Benefits of Refactoring (with personal examples)**

Throughout this unit, I have learned that **refactoring** is not simply "improving the code," but an essential practice for maintaining a healthy, flexible, and maintainable project over the long term. Applying refactoring has several very concrete benefits that I have seen both in theory and in practice.

### **Improves code readability**

One of the most obvious benefits is that, after refactoring, the code becomes much easier to understand. For example, in the exercise for the `OrderProcessor` class, the `processOrder()` method performed several tasks at once. Applying the **Extract Method** technique, I broke it down into smaller methods like `applyDiscountIfNeeded()` or `hasStock()`. This allowed each block to have a descriptive name, and now I can understand at a glance what each part does, without having to read all the internal details.

### **Facilitates maintenance**

When code is well-structured, any future changes are much simpler and less risky. Continuing with the previous example, if the discount policy changes tomorrow, I would only have to modify the content of `applyDiscountIfNeeded()`, without having to worry about breaking other parts of the `processOrder()` method. This separation of responsibilities also prevents unwanted side effects.

### **Reduces code duplication**

During the unit, we learned that one of the worst code smells is **duplicated logic**, as it causes errors to multiply. One of the catalog techniques that caught my attention was **Extract Constant**, which allowed me to avoid repeating the same magic numbers (for example, the discount threshold of `100` or the rate of `0.1`) and replaced them with well-named constants. This prevents errors if those values ​​change and improves code clarity.

### **Makes code more reusable and modular**

By dividing the code into small functions with clear responsibilities (following the *Single Responsibility* principle), it's easier to reuse those methods in other classes or scenarios. For example, the `hasStock()` method could be used in other features that need to know if inventory is available, without repeating the logic.

### **It makes it easier to detect errors**

One of the advantages that surprised me the most is that when refactoring, it's common to find hidden errors or poorly made decisions. Often, until you organize the code and name it appropriately, you don't realize there's unnecessary, repetitive, or misplaced logic. In my case, by separating the discount calculation into its own method, I noticed that scenarios such as the total being negative after the discount weren't considered, something I hadn't even considered before.

### **Prepare the code for growth**

One of the key concepts we learned was that software almost always grows. What is a simple program today can have many more features tomorrow. Refactoring is like preparing a solid foundation to build on. If my `OrderProcessor` class needs to integrate new payment methods in the future or send emails instead of console messages, it's already structured so that those changes can be easily integrated, without having to redo everything.

### **My conclusion about the unit**

For me, the biggest takeaway was that refactoring isn't optional; it's part of the professional development process. It's not about making the code "pretty," but rather making it **clear, sustainable, and ready for change**. I especially liked how Eclipse offers tools like *Rename*, *Extract Method*, and *Change Method Signature*, which help implement these techniques with less risk.

I think the `OrderProcessor` class example helped me ground all these concepts, and from now on, I'll try to apply these techniques from the very beginning in every project I do.