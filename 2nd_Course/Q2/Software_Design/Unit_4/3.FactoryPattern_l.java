// Interface for the Factory Pattern

interface Enemy {
    void attack();
}

class Goblin implements Enemy {
    @Override
    public void attack() {
        System.out.println("Goblin attacks with a club!");
    }
}

class Troll implements Enemy {
    @Override
    public void attack() {
        System.out.println("Troll attacks with a boulder!");
    }
}

abstract class EnemyFactory {
    public abstract Enemy createEnemy(); // Factory method to create enemies
}

// Concrete factory class

class OrcoFactory extends EnemigoFactory {
    public Enemigo crearEnemigo() {
        return new Orco();
    }
}

class TrollFactory extends EnemigoFactory {
    public Enemigo crearEnemigo() {
        return new Troll();
    }
}

class DragonFactory extends EnemigoFactory {
    public Enemigo crearEnemigo() {
        return new Dragon();
    }
}

// Main class to demonstrate the Factory Pattern

public class Main {
    public static void main(String[] args) {
        EnemyFactory goblinFactory = new GoblinFactory();
        Enemy goblin = goblinFactory.createEnemy();
        goblin.attack(); // Output: Goblin attacks with a club!

        EnemyFactory trollFactory = new TrollFactory();
        Enemy troll = trollFactory.createEnemy();
        troll.attack(); // Output: Troll attacks with a boulder!
    }
}