public class DiscountService {
    public double calculateDiscountForMember(double amount) {
        if (amount > 100) {
            return amount * 0.1;  // 10% discount for high-value members
        } else {
            return amount * 0.05;  // 5% discount for low-value members
        }
    }

    public double calculateDiscountForNonMember(double amount) {
        if (amount > 100) {
            return amount * 0.1;  // Same logic as for members
        } else {
            return amount * 0.05;  // Same logic as for members
        }
    }
}
