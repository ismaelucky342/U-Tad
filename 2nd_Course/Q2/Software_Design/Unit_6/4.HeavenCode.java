// the code with all the code refactoring techniques applied

public class OrderProcessor {

    // Composing Methods: The `processOrder` method has been refactored into smaller, focused methods.
    public void processOrder(Order order) {
        if (isInvalidOrder(order)) {
            System.out.println("Invalid order.");
            return;
        }

        double total = calculateTotal(order);
        total = applyDiscount(total, order.getDiscount());

        processOrderByType(order);

        printReceipt(order);
        System.out.println("Total: " + total);
    }

    // Moving Features Between Objects: `calculateTotal` has been moved to the `Order` class
    // to make `OrderProcessor` more focused on processing orders and less on calculating totals.
    private double calculateTotal(Order order) {
        return order.calculateTotal();
    }

    // Moving Features Between Objects: `applyDiscount` is now a helper method.
    private double applyDiscount(double total, double discount) {
        return total - (total * discount);
    }

    // Simplifying Conditional Expressions: Replaced complex if/else with a polymorphic approach.
    private void processOrderByType(Order order) {
        OrderProcessorStrategy strategy = OrderProcessorStrategyFactory.getStrategy(order.getType());
        strategy.processOrder(order);
    }

    private boolean isInvalidOrder(Order order) {
        return order == null || order.getItems().isEmpty();
    }

    // Simplifying Method Calls: The `printReceipt` method has been simplified, now it only handles receipt printing.
    private void printReceipt(Order order) {
        System.out.println("Receipt:");
        order.printItems();
    }

    // Data Clumps: `Item` class encapsulates item details that are reused across methods. 
    // This class has been improved with better encapsulation of data (e.g., removing primitive obsession).
    class Item {
        private String name;
        private double price;

        public Item(String name, double price) {
            this.name = name;
            this.price = price;
        }

        public String getName() {
            return name;
        }

        public double getPrice() {
            return price;
        }
    }

    // Organizing Data: The `Order` class now encapsulates the total calculation logic and printing items.
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

        // Simplifying Conditional Expressions: The `calculateTotal` is now within the `Order` class,
        // which keeps the logic close to the data it operates on.
        public double calculateTotal() {
            double total = 0;
            for (Item item : items) {
                total += item.getPrice();
            }
            return total;
        }

        // Organizing Data: Moved item printing to the `Order` class to keep item-related behavior encapsulated.
        public void printItems() {
            for (Item item : items) {
                System.out.println(item.getName() + " - " + item.getPrice());
            }
        }
    }

    // Generalization: Created an interface for order processing strategies to avoid switching logic.
    interface OrderProcessorStrategy {
        void processOrder(Order order);
    }

    // Generalization: Using a factory to decide which strategy to use for processing the order.
    static class OrderProcessorStrategyFactory {
        public static OrderProcessorStrategy getStrategy(String orderType) {
            switch (orderType) {
                case "Standard":
                    return new StandardOrderProcessorStrategy();
                case "Large":
                    return new LargeOrderProcessorStrategy();
                default:
                    throw new IllegalArgumentException("Unknown order type: " + orderType);
            }
        }
    }

    // Generalization: Standard order processing strategy.
    static class StandardOrderProcessorStrategy implements OrderProcessorStrategy {
        @Override
        public void processOrder(Order order) {
            System.out.println("Processing standard order...");
            // Process standard order
        }
    }

    // Generalization: Large order processing strategy.
    static class LargeOrderProcessorStrategy implements OrderProcessorStrategy {
        @Override
        public void processOrder(Order order) {
            System.out.println("Processing large order...");
            // Process large order
        }
    }
}
