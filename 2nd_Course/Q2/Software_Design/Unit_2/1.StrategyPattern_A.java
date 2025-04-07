//1. Define the strategy interface:
public interface PaymentStrategy {
    void pay(double amount);
}

//2. Create concrete implementations:

public class CreditCardPayment implements PaymentStrategy {
    private String cardNumber;

    public CreditCardPayment(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    @Override
    public void pay(double amount) {
        System.out.println("Paying " + amount + "€ with card: " + cardNumber);
    }
}

public class PayPalPayment implements PaymentStrategy {
    private String email;

    public PayPalPayment(String email) {
        this.email = email;
    }

    @Override
    public void pay(double amount) {
        System.out.println("Paying " + amount + "€ with PayPal: " + email);
    }
}

//3. Create a class that uses the strategy:
public class ShoppingCart {
    private PaymentStrategy paymentStrategy;

    public void setPaymentStrategy(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void checkout(double amount) {
        if (paymentStrategy == null) {
            System.out.println("Payment method not defined.");
            return;
        }
        paymentStrategy.pay(amount);
    }
}

//4. Usage in the main:
public class Main {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();

        // Use credit card
        cart.setPaymentStrategy(new CreditCardPayment("1234-5678-9012-3456"));
        cart.checkout(50.0);

        // Switch to PayPal
        cart.setPaymentStrategy(new PayPalPayment("user@email.com"));
        cart.checkout(75.0);
    }
}
