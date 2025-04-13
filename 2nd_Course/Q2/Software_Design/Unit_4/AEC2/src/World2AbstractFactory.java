package src;

// Concrete factory for World2 - Abstract Factory Pattern: Concrete Factory
// This class implements the EnemyAbstractFactory interface and provides
// specific implementations for creating Daemon and Witch objects for World2.
public class World2AbstractFactory implements EnemyAbstractFactory {
    @Override
    public Daemon createDaemon() {
        // Creates and returns a World2-specific Daemon instance
        return new World2Daemon();
    }
    
    @Override
    public Witch createWitch() {
        // Creates and returns a World2-specific Witch instance
        return new World2Witch();
    }
}
