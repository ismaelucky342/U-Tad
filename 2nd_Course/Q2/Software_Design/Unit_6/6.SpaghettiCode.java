public class PaymentProcessor {
    public void processPayment(int amount, String paymentMethod) {
        if (paymentMethod.equals("credit card")) {
            // Credit card payment processing logic
            System.out.println("Processing credit card payment...");
            if (amount > 1000) {
                // Specific logic for large payments
                System.out.println("Large payment: Additional verification required.");
            }
        } else if (paymentMethod.equals("paypal")) {
            // PayPal payment processing logic
            System.out.println("Processing PayPal payment...");
            if (amount < 100) {
                // Specific logic for small payments
                System.out.println("Small payment: Simplified process.");
            }
        } else if (paymentMethod.equals("bank transfer")) {
            // Bank transfer logic
            System.out.println("Processing bank transfer...");
            if (amount < 500) {
                // Specific logic for small transfers
                System.out.println("Small bank transfer: Simplified verification.");
            } else {
                System.out.println("Large bank transfer: Additional checks.");
            }
        }
    }
}
