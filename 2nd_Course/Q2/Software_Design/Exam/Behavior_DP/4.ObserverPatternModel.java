// El patrón Observer es un patrón de diseño que permite a un objeto
// notificar a otros objetos (los observadores) sobre cambios en su estado. 
// Este patrón es útil cuando se necesita mantener la coherencia entre 
// diferentes partes de un sistema sin acoplarlas fuertemente.

// En este ejemplo, implementaremos un modelo básico del patrón Observer
// en Java. Tendremos un sujeto (Subject) que mantiene una lista de
// observadores y notifica a todos ellos cuando su estado cambia.
// El sujeto puede ser cualquier objeto que necesite notificar a otros
// objetos sobre cambios en su estado. Los observadores son objetos
// que se suscriben al sujeto y reciben notificaciones cuando el
// estado del sujeto cambia.


// Observador
interface Observer {
    void update(String message);
}

// Sujeto
class Subject {
    private List<Observer> observers = new ArrayList<>();

    public void attach(Observer o) {
        observers.add(o);
    }

    public void detach(Observer o) {
        observers.remove(o);
    }

    public void notifyObservers(String message) {
        for (Observer o : observers) {
            o.update(message);
        }
    }

    // Cambia estado y notifica
    public void changeState(String newState) {
        System.out.println("Estado cambiado a: " + newState);
        notifyObservers(newState);
    }
}

// Observador concreto
class ConcreteObserver implements Observer {
    private String name;

    public ConcreteObserver(String name) {
        this.name = name;
    }

    public void update(String message) {
        System.out.println(name + " recibió notificación: " + message);
    }
}

// Main para probar
public class Main {
    public static void main(String[] args) {
        Subject subject = new Subject();

        Observer obs1 = new ConcreteObserver("Observador 1");
        Observer obs2 = new ConcreteObserver("Observador 2");

        subject.attach(obs1);
        subject.attach(obs2);

        subject.changeState("ON");
        subject.changeState("OFF");

        subject.detach(obs1);

        subject.changeState("ON de nuevo");
    }
}
