package src;

import java.util.ArrayList;
import java.util.List;

public class GameController {
    // Singleton instance of GameController
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
        // World 1 setup
        System.out.println("***** WORLD 1 *****");
        System.out.println("Generating " + 100 + " enemies, with " + (int)(0.5 * 100) 
        + "% witches and " + (int)(0.5 * 100) + "% daemons.");
        // Generate enemies for World 1
        List<Enemy> enemiesWorld1 = generateEnemies(new World1AbstractFactory(), 100, 
        0.5);

        // World 2 setup
        System.out.println("\n***** WORLD 2 *****");
        System.out.println("Generating " + 100 + " enemies, with " + (int)(0.5 * 100) 
        + "% witches and " + (int)(0.5 * 100) + "% daemons.");
        // Generate enemies for World 2
        List<Enemy> enemiesWorld2 = generateEnemies(new World2AbstractFactory(), 100, 
        0.25);
    }

    // Method to generate enemies for a given world
    private List<Enemy> generateEnemies(EnemyAbstractFactory factory, int count, 
    double daemonProbability) {
        // Input validations
        if (factory == null) {
            throw new IllegalArgumentException("Factory cannot be null.");
        }
        if (count <= 0) {
            throw new IllegalArgumentException("Count must be greater than 0.");
        }
        if (daemonProbability < 0 || daemonProbability > 1) {
            throw new IllegalArgumentException("Daemon probability must be between 0-1.");
        }

        List<Enemy> enemies = new ArrayList<>();
        int daemons = 0;
        int witches = 0;

        // Generate enemies based on the probability
        for (int i = 0; i < count; i++) {
            if (Math.random() < daemonProbability) {
                enemies.add(factory.createDaemon());
                daemons++;
            } else {
                enemies.add(factory.createWitch());
                witches++;
            }
        }

        // Print the count of generated daemons and witches
        System.out.println("Daemons generated: " + daemons);
        System.out.println("Witches generated: " + witches);

        // Example of a randomly selected daemon and witch
        Enemy exampleDaemon = null;
        Enemy exampleWitch = null;

        // Find one example of each type (daemon and witch)
        for (Enemy enemy : enemies) {
            if (exampleDaemon == null && enemy instanceof Daemon) {
                exampleDaemon = enemy;
            }
            if (exampleWitch == null && enemy instanceof Witch) {
                exampleWitch = enemy;
            }
            if (exampleDaemon != null && exampleWitch != null) {
                break;
            }
        }

        // Print details of the example daemon and witch
        if (exampleDaemon != null) {
            System.out.println("daemon type generated: " + exampleDaemon);
        } else {
            System.out.println("No daemons were generated.");
        }

        if (exampleWitch != null) {
            System.out.println("witch type generated: " + exampleWitch);
        } else {
            System.out.println("No witches were generated.");
        }

        return enemies;
    }
}