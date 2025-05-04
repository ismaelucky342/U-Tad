public class OrderCalculator {
    public double calculateTotalAmount(int quantity, double price) {
        double discount = 0.2;  // Discount rate
        return quantity * price * (1 - discount);  // 0.2 as discount is hardcoded
    }
}
