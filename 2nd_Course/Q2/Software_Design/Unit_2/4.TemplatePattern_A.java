//1.abstract class with the template method

public abstract class HotTea {
    // Template method
    public final void prepareTea() {
        boilWater();
        steepTeaBag();
        pourInCup();
        addCondiments();
    }

    // Steps to be implemented by subclasses
    protected abstract void addCondiments();

    private void boilWater() {
        System.out.println("Boiling water");
    }

    private void steepTeaBag() {
        System.out.println("Steeping the tea bag");
    }

    private void pourInCup() {
        System.out.println("Pouring into cup");
    }
}

// 2.Concrete subclasses 
class GreenTea extends HotTea {
    @Override
    protected void addCondiments() {
        System.out.println("Adding lemon");
    }
}

class BlackTea extends HotTea {
    @Override
    protected void addCondiments() {
        System.out.println("Adding milk and sugar");
    }
}

//3. Main class to demonstrate the template pattern
public class TeaTestDrive {
    public static void main(String[] args) {
        HotTea greenTea = new GreenTea();
        greenTea.prepareTea();

        System.out.println("\n");

        HotTea blackTea = new BlackTea();
        blackTea.prepareTea();
    }
}