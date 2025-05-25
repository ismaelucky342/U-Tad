import java.util.ArrayList;
import java.util.List;

public class WeatherStation implements Subject {
    private List<Observer> observers;
    private float temperature;
    private float humidity;

    public WeatherStation() {
        observers = new ArrayList<>();
    }

    public void registerObserver(Observer o) {
        observers.add(o);
    }

    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    public void notifyObservers() {
        for (Observer o : observers) {
            o.update(temperature, humidity);
        }
    }

    public void setMeasurements(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        notifyObservers();
    }
}


public class CurrentConditionsDisplay implements Observer {
    public void update(float temperature, float humidity) {
        System.out.println("Pantalla actual: " + temperature + "°C, " + humidity + "% humedad");
    }
}

public class StatisticsDisplay implements Observer {
    public void update(float temperature, float humidity) {
        System.out.println("Estadísticas: Temp media ahora " + temperature + "°C");
    }
}

public class WeatherApp {
    public static void main(String[] args) {
        WeatherStation weatherStation = new WeatherStation();

        Observer screen1 = new CurrentConditionsDisplay();
        Observer screen2 = new StatisticsDisplay();

        weatherStation.registerObserver(screen1);
        weatherStation.registerObserver(screen2);

        weatherStation.setMeasurements(25.5f, 65.0f); // Ambos observadores son notificados
        weatherStation.setMeasurements(26.0f, 70.0f);
    }
}
