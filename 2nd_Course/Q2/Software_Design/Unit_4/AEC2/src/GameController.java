package src;

import java.util.ArrayList;
import java.util.List;

public class GameController {
    private static GameController instance = null;

    // Private constructor to enforce Singleton pattern
    private GameController() {
    }

    // Method to get the single instance of GameController
    public static GameController getInstance() {
        if (instance == null) {
            instance = new GameController();
        }
        return instance;
    }

    // Main game logic
    public void play() {
        System.out.println("***** WORLD 1 *****");
        List<Enemy> enemiesWorld1 = generateEnemies(new World1AbstractFactory(), 100, 0.5);
        System.out.println("\n***** WORLD 2 *****");
        List<Enemy> enemiesWorld2 = generateEnemies(new World2AbstractFactory(), 100, 0.25);
    }

    // Method to generate enemies for a given world
    private List<Enemy> generateEnemies(EnemyAbstractFactory factory, int count, double daemonProbability) {
        // Verifications
        if (factory == null) {
            throw new IllegalArgumentException("Factory cannot be null.");
        }
        if (count <= 0) {
            throw new IllegalArgumentException("Count must be greater than 0.");
        }
        if (daemonProbability < 0 || daemonProbability > 1) {
            throw new IllegalArgumentException("Daemon probability must be between 0 and 1.");
        }

        List<Enemy> enemies = new ArrayList<>();
        int daemons = 0;
        int witches = 0;

        for (int i = 0; i < count; i++) {
            if (Math.random() < daemonProbability) {
                enemies.add(factory.createDaemon());
                daemons++;
            } else {
                enemies.add(factory.createWitch());
                witches++;
            }
        }

        System.out.println("Daemons generated: " + daemons);
        System.out.println("Witches generated: " + witches);

        // Example of a randomly selected enemy
        if (!enemies.isEmpty()) {
            Enemy exampleEnemy = enemies.get((int) (Math.random() * enemies.size()));
            System.out.println("Example of an enemy generated: " + exampleEnemy);
        } else {
            System.out.println("No enemies were generated.");
        }

        return enemies;
    }
}
