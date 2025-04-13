package src;

// The World2Witch class implements the Witch interface and represents a witch character
// with specific base health and attack values in the "World2" context.
public class World2Witch implements Witch {
    // Constants for the base health and attack values of the witch
    private static final int BASE_HEALTH = 90;
    private static final int BASE_ATTACK = 25;
    private static final int MAX_HEALTH = 120; // Maximum health limit
    private static final int MAX_ATTACK = 60;  // Maximum attack limit

    // Instance variables to store the current health and attack values of the witch
    private int health;
    private int attack;

    // Constructor initializes the witch's health and attack to their base values
    public World2Witch() {
        this.health = validateHealth(BASE_HEALTH);
        this.attack = validateAttack(BASE_ATTACK);
    }

    // Getter method to retrieve the current health of the witch
    @Override
    public int getHealth() {
        return health;
    }

    // Setter method to update the health with validation
    public void setHealth(int health) {
        this.health = validateHealth(health);
    }

    // Getter method to retrieve the current attack value of the witch
    @Override
    public int getAttack() {
        return attack;
    }

    // Setter method to update the attack with validation
    public void setAttack(int attack) {
        this.attack = validateAttack(attack);
    }

    // Private method to validate health values
    private int validateHealth(int health) {
        if (health < 0) {
            throw new IllegalArgumentException("Health cannot be negative.");
        }
        return Math.min(health, MAX_HEALTH);
    }

    // Private method to validate attack values
    private int validateAttack(int attack) {
        if (attack < 0) {
            throw new IllegalArgumentException("Attack cannot be negative.");
        }
        return Math.min(attack, MAX_ATTACK);
    }

    // Overridden toString method to provide a string representation of the witch
    @Override
    public String toString() {
        return "Witch (World2) [Health=" + health + ", Attack=" + attack + "]";
    }
}
