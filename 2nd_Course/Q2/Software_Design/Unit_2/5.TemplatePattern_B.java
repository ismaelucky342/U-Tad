//1.abstract class with the template method
public abstract class PaymentProcessor {
    public final void processPayment() {
        validateCustomerDetails();
        autenticatePaymentMethod();
        executePayment();
        sendConfirmation();
    }

    protected abstract void validateCustomerDetails();
    protected abstract void autenticatePaymentMethod();
    protected abstract void executePayment();

    protected void sendConfirmation() {
        System.out.println("Sending payment confirmation to customer.");
    }
}

//2. Concrete subclasses
class CreditCardPaymentProcessor extends PaymentProcessor {
    @Override
    protected void validateCustomerDetails() {
        System.out.println("Validating customer details for credit card payment.");
    }

    @Override
    protected void autenticatePaymentMethod() {
        System.out.println("Authenticating credit card payment method.");
    }

    @Override
    protected void executePayment() {
        System.out.println("Executing credit card payment.");
    }
}

class PayPalPaymentProcessor extends PaymentProcessor {
    @Override
    protected void validateCustomerDetails() {
        System.out.println("Validating customer details for PayPal payment.");
    }

    @Override
    protected void autenticatePaymentMethod() {
        System.out.println("Authenticating PayPal payment method.");
    }

    @Override
    protected void executePayment() {
        System.out.println("Executing PayPal payment.");
    }
}

class CrytoPaymentProcessor extends PaymentProcessor {
    @Override
    protected void validateCustomerDetails() {
        System.out.println("Validating customer details for crypto payment.");
    }

    @Override
    protected void autenticatePaymentMethod() {
        System.out.println("Authenticating crypto payment method.");
    }

    @Override
    protected void executePayment() {
        System.out.println("Executing crypto payment.");
    }
}

//3. Main class to demonstrate the template pattern
public class PaymentTestDrive {
    public static void main(String[] args) {
        PaymentProcessor creditCardPayment = new CreditCardPaymentProcessor();
        creditCardPayment.processPayment();

        System.out.println("\n");

        PaymentProcessor payPalPayment = new PayPalPaymentProcessor();
        payPalPayment.processPayment();

        System.out.println("\n");

        PaymentProcessor cryptoPayment = new CrytoPaymentProcessor();
        cryptoPayment.processPayment();
    }
}