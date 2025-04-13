package src;

// The World1Witch class implements the Witch interface and represents a witch character in World1.
public class World1Witch implements Witch {
    // Constants for the base health and attack values of the witch.
    private static final int BASE_HEALTH = 80;
    private static final int BASE_ATTACK = 20;

    // Instance variables to store the current health and attack values of the witch.
    private int health;
    private int attack;

    // Constructor initializes the witch's health and attack to their base values.
    public World1Witch() {
        this.health = BASE_HEALTH;
        this.attack = BASE_ATTACK;
    }

    // Getter method to retrieve the current health of the witch.
    @Override
    public int getHealth() {
        return health;
    }

    // Getter method to retrieve the current attack value of the witch.
    @Override
    public int getAttack() {
        return attack;
    }

    // Overrides the toString method to provide a string representation of the witch.
    @Override
    public String toString() {
        return "Witch (World1) [Health=" + health + ", Attack=" + attack + "]";
    }
}
