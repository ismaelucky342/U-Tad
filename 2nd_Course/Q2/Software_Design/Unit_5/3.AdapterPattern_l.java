public interface PaymentGateway {
    void pay(String customer, double amount);
}

public class OldPaymentProcessor {
    public void makePayment(String name, double money) {
        System.out.println("Processing payment for " + name + " of amount $" + money + " using OLD system.");
    }
}

public class PaymentAdapter implements PaymentGateway {
    private OldPaymentProcessor oldProcessor;

    public PaymentAdapter(OldPaymentProcessor oldProcessor) {
        this.oldProcessor = oldProcessor;
    }

    @Override
    public void pay(String customer, double amount) {
        oldProcessor.makePayment(customer, amount);
    }
}

public class App {
    
    public static void main(String[] args) {
        OldPaymentProcessor oldSystem = new OldPaymentProcessor();
        PaymentGateway payment = new PaymentAdapter(oldSystem); // Use adapter

        payment.pay("Alice", 150.0);
    }
}

