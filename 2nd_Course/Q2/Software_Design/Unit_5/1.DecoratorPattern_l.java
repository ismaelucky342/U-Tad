// Componente
public interface Device {
    void turnOn();
    void turnOff();
    void setVolume(int volume);
}

// Componente Concreto
public class TV implements Device {
    @Override
    public void turnOn() {
        System.out.println("TV is turned on.");
    }

    @Override
    public void turnOff() {
        System.out.println("TV is turned off.");
    }

    @Override
    public void setVolume(int volume) {
        System.out.println("TV volume set to " + volume);
    }
}

// Componente Concreto
public class Radio implements Device {
    @Override
    public void turnOn() {
        System.out.println("Radio is turned on.");
    }

    @Override
    public void turnOff() {
        System.out.println("Radio is turned off.");
    }

    @Override
    public void setVolume(int volume) {
        System.out.println("Radio volume set to " + volume);
    }
}

// Decorador base
public abstract class DeviceDecorator implements Device {
    protected Device decoratedDevice;

    public DeviceDecorator(Device decoratedDevice) {
        this.decoratedDevice = decoratedDevice;
    }

    @Override
    public void turnOn() {
        decoratedDevice.turnOn();
    }

    @Override
    public void turnOff() {
        decoratedDevice.turnOff();
    }

    @Override
    public void setVolume(int volume) {
        decoratedDevice.setVolume(volume);
    }
}

// Decorador concreto
public class MuteDecorator extends DeviceDecorator {
    public MuteDecorator(Device decoratedDevice) {
        super(decoratedDevice);
    }

    public void mute() {
        decoratedDevice.setVolume(0);
        System.out.println("Device is muted.");
    }
}

// Cliente
public class DecoratorPatternExample {
    public static void main(String[] args) {
        Device tv = new TV();
        tv.turnOn();
        tv.setVolume(10);
        tv.turnOff();

        Device radio = new Radio();
        MuteDecorator radioWithMute = new MuteDecorator(radio);
        radioWithMute.turnOn();
        radioWithMute.setVolume(5);
        radioWithMute.mute();
        radioWithMute.turnOff();
    }
}
