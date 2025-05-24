/*
Supongamos que tenemos una lista de pagos (Payment) y queremos poder ordenarlos 
por diferentes estrategias:

Después

Por cantidad

Por nombre del pagador


*/
import java.time.LocalDate;
import java.util.list; 


public class Payment {
    private String payer;
    private double amount;
    private LocalDate date;

    public Payment(String payer, double amount, LocalDate date) {
        this.payer = payer;
        this.amount = amount;
        this.date = date;
    }

    public String getPayer() {
        return payer;
    }

    public double getAmount() {
        return amount;
    }

    public LocalDate getDate() {
        return date;
    }

    @Override
    public String toString() {
        return payer + " - $" + amount + " - " + date;
    }
}


public interface SortStrategy {
    void sort(List<Payment> payments);
}

public class DateSortStrategy implements SortStrategy {
    public void sort(List<Payment> payments) {
        payments.sort(Comparator.comparing(Payment::getDate));
    }
}

public class AmountSortStrategy implements SortStrategy {
    public void sort(List<Payment> payments) {
        payments.sort((p1, p2) -> Double.compare(p1.getAmount(), p2.getAmount()));
    }
}

public class NameSortStrategy implements SortStrategy {
    public void sort(List<Payment> payments) {
        payments.sort((p1, p2) -> p1.getPayer().compareToIgnoreCase(p2.getPayer()));
    }
}


public class PaymentProcessor {
    private SortStrategy strategy;

    public PaymentProcessor(SortStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(SortStrategy strategy) {
        this.strategy = strategy;
    }

    public void sortPayments(List<Payment> payments) {
        strategy.sort(payments);
    }
}