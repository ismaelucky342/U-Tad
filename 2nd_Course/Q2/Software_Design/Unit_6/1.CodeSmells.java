public class OrderProcessor {

    // 1. **God Object**: The class is handling too many responsibilities.
    // This class is responsible for too many details: processing the order, calculating the total,
    // verifying payment methods, sending confirmations, etc. It should be split into multiple classes.
    
    public void processOrder(Order order, String paymentMethod, String shippingAddress, String email) {
        // 2. **Long Method**: The 'processOrder' method is too long. It performs multiple actions 
        // in a single block, making it hard to understand and modify.
        
        // 3. **Large Class**: The class is responsible for many related tasks, 
        // such as total calculation, payment validation, and sending confirmations.
        double total = calculateTotal(order);
        
        if (total > 0) {
            // 4. **Duplicated Code**: Payment verification and shipping logic are repeated
            // in different parts of the class. We should have independent payment logic and 
            // separate handling for shipping.
            if (paymentMethod.equals("CreditCard")) {
                if (processCreditCardPayment(paymentMethod, total)) {
                    sendConfirmation(email);
                    sendShippingDetails(shippingAddress);
                }
            } else if (paymentMethod.equals("PayPal")) {
                if (processPayPalPayment(paymentMethod, total)) {
                    sendConfirmation(email);
                    sendShippingDetails(shippingAddress);
                }
            } else {
                System.out.println("Unsupported payment method");
            }
        } else {
            // 5. **Magic Numbers**: '0' in the condition should be replaced with a constant
            // that has a descriptive name to make the code clearer.
            System.out.println("Invalid total amount");
        }
    }

    // 6. **Feature Envy**: The 'calculateTotal' method accesses too many attributes
    // of the Order class to do its job. This suggests that it might be better to move
    // this logic into the Order class.
    public double calculateTotal(Order order) {
        double total = order.getPrice() * order.getQuantity();
        if (order.isTaxable()) {
            total += order.getPrice() * 0.15;  // 15% tax as a magic number
        }
        return total;
    }

    // 7. **Primitive Obsession**: Using 'String' to represent payment methods, addresses, and emails
    // is problematic. We should use more specific data types, such as enums for payment methods
    // and specialized classes for addresses or emails.
    private boolean processCreditCardPayment(String paymentMethod, double total) {
        // Logic to process credit card payment
        return true;
    }

    private boolean processPayPalPayment(String paymentMethod, double total) {
        // Logic to process PayPal payment
        return true;
    }

    private void sendConfirmation(String email) {
        // Logic to send email confirmation
    }

    private void sendShippingDetails(String address) {
        // Logic to send shipping details
    }
}
