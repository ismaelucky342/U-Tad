//this code has all the code smells

public class OrderProcessor {

    // 1. **Long Method**: This method does too many things, like checking order validity,
    // calculating totals, applying discounts, and processing payments.
    public void processOrder(Order order) {
        // Checking if the order has items
        if (order == null || order.getItems().isEmpty()) {
            System.out.println("Invalid order.");
            return;
        }

        double total = 0;
        for (Item item : order.getItems()) {
            total += item.getPrice();
        }

        // Applying discount if applicable
        if (order.getDiscount() > 0) {
            total = total - (total * order.getDiscount());
        }

        // Processing payment
        if (total > 1000) {
            processLargeOrder(order);
        } else {
            processStandardOrder(order);
        }

        System.out.println("Order processed successfully. Total: " + total);
    }

    // 2. **Large Class**: This class is responsible for processing orders, handling payments,
    // and printing receipts, which violates the Single Responsibility Principle.
    // It should be split into smaller classes like `OrderValidator`, `PaymentProcessor`, etc.
    
    private void processStandardOrder(Order order) {
        System.out.println("Processing standard order...");
        // Handle standard order payment
    }

    private void processLargeOrder(Order order) {
        System.out.println("Processing large order...");
        // Handle large order payment
    }

    // 3. **Duplicated Code**: The `processStandardOrder` and `processLargeOrder` methods are very similar.
    // They are both responsible for processing an order, but with minimal differences. This can be refactored.
    
    // 4. **Data Clumps**: We have `itemPrice` and `itemQuantity` that are always passed together.
    // It might be better to create a `CartItem` class that encapsulates both properties.
    public void updateCart(Item item, double itemPrice, int itemQuantity) {
        // Update the item in the cart with its price and quantity
        item.setPrice(itemPrice);
        item.setQuantity(itemQuantity);
    }

    // 5. **Switch Statements**: This method uses a large switch statement to handle different order types.
    // It would be better to use polymorphism or the strategy pattern to handle different order types.
    public void handleOrderType(Order order) {
        switch (order.getType()) {
            case "Standard":
                processStandardOrder(order);
                break;
            case "Large":
                processLargeOrder(order);
                break;
            default:
                System.out.println("Unknown order type.");
        }
    }

    // 6. **Feature Envy**: The `processOrder` method spends a lot of time checking the `Order` class properties,
    // which might be better handled inside the `Order` class itself. The method has too much logic about the order.
    public double calculateTotal(Order order) {
        double total = 0;
        for (Item item : order.getItems()) {
            total += item.getPrice();
        }
        return total;
    }

    // 7. **Inappropriate Intimacy**: The `OrderProcessor` class is too dependent on the `Order` and `Item` classes,
    // often accessing their internal properties directly. This creates tight coupling, and changes to these classes
    // might affect this class. Using methods in the `Order` and `Item` classes could improve encapsulation.
    public void printReceipt(Order order) {
        System.out.println("Receipt:");
        for (Item item : order.getItems()) {
            System.out.println(item.getName() + " - " + item.getPrice());
        }
    }

    // 8. **Lazy Class**: The `Item` class is underused and has very few methods. It's used in many places,
    // but it could be combined with other classes like `CartItem` or `Product` to make better use of its functionality.
    class Item {
        private String name;
        private double price;
        private int quantity;

        public Item(String name, double price) {
            this.name = name;
            this.price = price;
            this.quantity = 1;
        }

        public double getPrice() {
            return price;
        }

        public void setPrice(double price) {
            this.price = price;
        }

        public void setQuantity(int quantity) {
            this.quantity = quantity;
        }

        public String getName() {
            return name;
        }
    }

    // 9. **Primitive Obsession**: The method `updateCart` accepts primitive types like `double` and `int` for item price
    // and quantity. These should be encapsulated within a class like `CartItem` or `ProductDetails`.
}

// A simple order class that uses `Item`
class Order {
    private List<Item> items;
    private double discount;
    private String type;

    public Order(List<Item> items, double discount, String type) {
        this.items = items;
        this.discount = discount;
        this.type = type;
    }

    public List<Item> getItems() {
        return items;
    }

    public double getDiscount() {
        return discount;
    }

    public String getType() {
        return type;
    }
}
