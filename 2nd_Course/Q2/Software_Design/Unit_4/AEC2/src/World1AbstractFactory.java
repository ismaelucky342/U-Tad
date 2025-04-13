package src;

// Concrete factory for World1 - Abstract Factory Pattern: Concrete Factory
// This class implements the EnemyAbstractFactory interface and provides
// specific implementations for creating World1-specific enemies (Daemon and Witch).
public class World1AbstractFactory implements EnemyAbstractFactory {

    // Creates and returns a World1-specific Daemon instance
    @Override
    public Daemon createDaemon() {
        return new World1Daemon();
    }
    
    // Creates and returns a World1-specific Witch instance
    @Override
    public Witch createWitch() {
        return new World1Witch();
    }
}
