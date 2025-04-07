// 1. Interface for the state:
public interface DoorState {
    void open();
    void close();
    void lock();
    void unlock();
}

//2. context class
public class Door {
    private DoorState currentState;
    private DoorState openState;
    private DoorState closedState;
    private DoorState lockedState;

    public Door() {
        openState = new OpenState(this);
        closedState = new ClosedState(this);
        lockedState = new LockedState(this);
        currentState = closedState; // Initial state
    }

    public void setCurrentState(DoorState state) {
        this.currentState = state;
    }

    public DoorState getOpenState() {
        return openState;
    }

    public DoorState getClosedState() {
        return closedState;
    }

    public DoorState getLockedState() {
        return lockedState;
    }

    public void open() {
        currentState.open();
    }

    public void close() {
        currentState.close();
    }
    
    public void lock() {
        currentState.lock();
    }

    public void unlock() {
        currentState.unlock();
    }
}

//3. states implementations
class OpenState implements DoorState {
    private Door door;

    public OpenState(Door door) {
        this.door = door;
    }

    @Override
    public void open() {
        System.out.println("The door is already open.");
    }

    @Override
    public void close() {
        System.out.println("Closing the door.");
        door.setCurrentState(door.getClosedState());
    }

    @Override
    public void lock() {
        System.out.println("Cannot lock an open door.");
    }

    @Override
    public void unlock() {
        System.out.println("Cannot unlock an open door.");
    }
}

class ClosedState implements DoorState {
    private Door door;

    public ClosedState(Door door) {
        this.door = door;
    }

    @Override
    public void open() {
        System.out.println("Opening the door.");
        door.setCurrentState(door.getOpenState());
    }

    @Override
    public void close() {
        System.out.println("The door is already closed.");
    }

    @Override
    public void lock() {
        System.out.println("Locking the door.");
        door.setCurrentState(door.getLockedState());
    }

    @Override
    public void unlock() {
        System.out.println("Cannot unlock a closed door.");
    }
}

class LockedState implements DoorState {
    private Door door;

    public LockedState(Door door) {
        this.door = door;
    }

    @Override
    public void open() {
        System.out.println("Cannot open a locked door.");
    }

    @Override
    public void close() {
        System.out.println("The door is already closed.");
    }

    @Override
    public void lock() {
        System.out.println("The door is already locked.");
    }

    @Override
    public void unlock() {
        System.out.println("Unlocking the door.");
        door.setCurrentState(door.getClosedState());
    }
}

//4. Main class to demonstrate the state pattern:
public class Main {
    public static void main(String[] args) {
        Door door = new Door();

        door.open(); // The door is already closed, so it will open
        door.lock(); // Cannot lock an open door
        door.close(); // Closing the door
        door.lock(); // Locking the door
        door.unlock(); // Unlocking the door
        door.open(); // Opening the door
    }
}