public interface TrafficLightState {
    void show(TrafficLight context); // Ahora recibe el contexto para poder cambiar el estado
}

public class TrafficLight { // context 
    private TrafficLightState trafficLightState;

    public TrafficLight(TrafficLightState trafficLightState) {
        this.trafficLightState = trafficLightState;
    }

    public void setTrafficLightState(TrafficLightState state) {
        this.trafficLightState = state;
    }

    public void show() {
        trafficLightState.show(this);
    }
}

public class GreenLightState implements TrafficLightState {
    public void show(TrafficLight context) {
        System.out.println("Green light, go forward!!");
        context.setTrafficLightState(new AmberLightState()); // Transición automática
    }
}

public class AmberLightState implements TrafficLightState {
    public void show(TrafficLight context) {
        System.out.println("Amber light, get ready to stop!");
        context.setTrafficLightState(new RedLightState());
    }
}

public class RedLightState implements TrafficLightState {
    public void show(TrafficLight context) {
        System.out.println("Red light, stop and wait!!");
        context.setTrafficLightState(new GreenLightState());
    }
}

public class TrafficLightTest {
    public static void main(String[] args) {
        TrafficLight trafficLight = new TrafficLight(new GreenLightState());

        for (int i = 0; i < 5; i++) {
            trafficLight.show(); // Cada llamada cambia el estado internamente
        }
    }
}

