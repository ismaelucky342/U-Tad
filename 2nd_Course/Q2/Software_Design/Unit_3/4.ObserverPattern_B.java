// 1.Interface Observer
public interface Observer {
    void update(String message);
}

// 2. Interface Subject

public interface Subject {
    void addObserver(Observer o);
    void removeObserver(Observer o);
    void notifyObservers();
}

// 3. Concrete Subject

public class SalesSystem implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private String message;

    @Override
    public void addObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        for (Observer o : observers) {
            o.update(message);
        }
    }

    public void setMessage(String message) {
        this.message = message;
        notifyObservers();
    }

    public void newSale(String saleDetails) {
        this.saleDetails = saleDetails;
        System.out.println("Nueva venta realizada: " + saleDetails);
        notifyObservers();
    }
}

// 3. Concrete Observers
public class WebDisplay implements Observer {
    private String name;

    public WebDisplay(String name) {
        this.name = name;
    }

    @Override
    public void update(String message) {
        System.out.println(name + " Web está mostrando la venta: " + message);
    }
}

public class MobileAppDisplay implements Observer {
    private String name;

    public MobileAppDisplay(String name) {
        this.name = name;
    }

    @Override
    public void update(String message) {
        System.out.println(name + " App está mostrando la venta: " + message);
    }
}

public class EmailNotification implements Observer {
    private String name;

    public EmailNotification(String name) {
        this.name = name;
    }

    @Override
    public void update(String message) {
        System.out.println(name + " Email notificando la venta: " + message);
    }
}

// 4. Main class to demonstrate the Observer pattern
public class Main {
    public static void main(String[] args) {
        SalesSystem salesSystem = new SalesSystem();

        // Observadores
        Observer webDisplay = new WebDisplay("Pantalla Web");
        Observer mobileDisplay = new MobileAppDisplay("Aplicación Móvil");
        Observer emailNotification = new EmailNotification("Correo Electrónico");

        // Suscribimos los observadores
        salesSystem.addObserver(webDisplay);
        salesSystem.addObserver(mobileDisplay);
        salesSystem.addObserver(emailNotification);

        // Realizamos una venta y notificamos a todos los observadores
        salesSystem.newSale("Venta de Laptop - $1200");

        // Desuscribir la pantalla web
        salesSystem.removeObserver(webDisplay);

        // Realizamos otra venta
        salesSystem.newSale("Venta de Smartphone - $800");
    }
}