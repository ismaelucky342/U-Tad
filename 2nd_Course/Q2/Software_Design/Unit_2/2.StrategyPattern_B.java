//1. Interface for the strategy:

public interface AttackStrategy {
    void attack();
}

//2. Concrete strategies:
public class SwordAttack implements AttackStrategy {
    @Override
    public void attack() {
        System.out.println("Attacking with a sword!");
    }
}

public class BowAttack implements AttackStrategy {
    @Override
    public void attack() {
        System.out.println("Attacking with a bow!");
    }
}

public class MagicAttack implements AttackStrategy {
    @Override
    public void attack() {
        System.out.println("Attacking with magic!");
    }
}

//3. Context class that uses the strategy:
public class Character {
    private AttackStrategy attackStrategy;

    public void setAttackStrategy(AttackStrategy attackStrategy) {
        this.attackStrategy = attackStrategy;
    }

    public void performAttack() {
        if (attackStrategy != null) {
            attackStrategy.attack();
        } else {
            System.out.println("No attack strategy defined!");
        }
    }
}

//4. Main class to demonstrate the strategy pattern:
public class Main {
    public static void main(String[] args) {
        Character character = new Character();

        // Set and perform sword attack
        character.setAttackStrategy(new SwordAttack());
        character.performAttack();

        // Change to bow attack
        character.setAttackStrategy(new BowAttack());
        character.performAttack();

        // Change to magic attack
        character.setAttackStrategy(new MagicAttack());
        character.performAttack();
    }
}