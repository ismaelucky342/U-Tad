package src;

// Interface EnemyAbstractFactory - Abstract Factory Pattern: Abstract factory for enemies
public interface EnemyAbstractFactory {
    Daemon createDaemon();
    Witch createWitch();
}
