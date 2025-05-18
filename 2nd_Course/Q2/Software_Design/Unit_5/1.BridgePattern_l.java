// implementor 

public interface Device {
    void turnOn();
    void turnOff();
    void setVolume(int volume);
}

// ConcreteImplementor
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

// ConcreteImplementor
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

// Abstraction
public class RemoteControl {
    private Device device;

    public RemoteControl(Device device) {
        this.device = device;
    }

    public void turnOn() {
        device.turnOn();
    }

    public void turnOff() {
        device.turnOff();
    }

    public void setVolume(int volume) {
        device.setVolume(volume);
    }
}

// RefinedAbstraction
public class AdvancedRemote extends RemoteControl {
    public AdvancedRemote(Device device) {
        super(device);
    }

    public void mute() {
        setVolume(0);
        System.out.println("Device is muted.");
    }
}

// Client code
public class BridgePatternExample {
    public static void main(String[] args) {
        Device tv = new TV();
        RemoteControl tvRemote = new RemoteControl(tv);
        tvRemote.turnOn();
        tvRemote.setVolume(10);
        tvRemote.turnOff();

        Device radio = new Radio();
        AdvancedRemote radioRemote = new AdvancedRemote(radio);
        radioRemote.turnOn();
        radioRemote.setVolume(5);
        radioRemote.mute();
        radioRemote.turnOff();
    }
}

