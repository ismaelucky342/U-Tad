//1. state interface

public interface ATMState {
    void insertCard();
    void ejectCard();
    void enterPin(int pin);
    void requestCash(int amount);
}

//2. main class
public class ATMMachine {
    private ATMState currentState;

    private ATMState noCardState = new NoCardState(this);
    private ATMState hasCardState = new HasCardState(this);
    private ATMState authenticatedState = new AuthenticatedState(this);

    public ATMMachine() {
        this.currentState = noCardState;
    }

    public void setState(ATMState state) {
        this.currentState = state;
    }

    public ATMState getNoCardState() { return noCardState; }
    public ATMState getHasCardState() { return hasCardState; }
    public ATMState getAuthenticatedState() { return authenticatedState; }

    public void insertCard() { currentState.insertCard(); }
    public void ejectCard() { currentState.ejectCard(); }
    public void enterPin(int pin) { currentState.enterPin(pin); }
    public void requestWithdrawal(int amount) { currentState.requestWithdrawal(amount); }
}

//3. states implementations
class NoCardState implements ATMState {
    private ATMMachine atmMachine;

    public NoCardState(ATMMachine atmMachine) {
        this.atmMachine = atmMachine;
    }

    @Override
    public void insertCard() {
        System.out.println("Card inserted.");
        atmMachine.setState(atmMachine.getHasCardState());
    }

    @Override
    public void ejectCard() {
        System.out.println("No card to eject.");
    }

    public void enterPin(int pin) {
        System.out.println("Please insert a card first.");
    }

    public void requestWithdrawal(int amount) {
        System.out.println("Please insert a card first.");
    }
}

class HasCardState implements ATMState {
    private ATMMachine atmMachine;

    public HasCardState(ATMMachine atmMachine) {
        this.atmMachine = atmMachine;
    }

    @Override
    public void insertCard() {
        System.out.println("Card already inserted.");
    }

    @Override
    public void ejectCard() {
        System.out.println("Card ejected.");
        atmMachine.setState(atmMachine.getNoCardState());
    }

    @Override
    public void enterPin(int pin) {
        System.out.println("PIN entered: " + pin);
        atmMachine.setState(atmMachine.getAuthenticatedState());
    }

    @Override
    public void requestWithdrawal(int amount) {
        System.out.println("Please enter your PIN first.");
    }

}

class AuthenticatedState implements ATMState {
    private ATMMachine atmMachine;

    public AuthenticatedState(ATMMachine atmMachine) {
        this.atmMachine = atmMachine;
    }

    @Override
    public void insertCard() {
        System.out.println("Card already inserted.");
    }

    @Override
    public void ejectCard() {
        System.out.println("Card ejected.");
        atmMachine.setState(atmMachine.getNoCardState());
    }

    @Override
    public void enterPin(int pin) {
        System.out.println("Already authenticated. You can request cash.");
    }

    public void requestWithdrawal(int amount) {
        System.out.println("Withdrawing " + amount + " euros.");
        atmMachine.setState(atmMachine.getNoCardState());
    }
}

//4. main class to demonstrate the state pattern:
public class Main {
    public static void main(String[] args) {
        ATMMachine atmMachine = new ATMMachine();

        atmMachine.insertCard(); // Card inserted
        atmMachine.enterPin(1234); // PIN entered
        atmMachine.requestWithdrawal(100); // Withdrawing 100 euros
        atmMachine.ejectCard(); // Card ejected
    }
}
