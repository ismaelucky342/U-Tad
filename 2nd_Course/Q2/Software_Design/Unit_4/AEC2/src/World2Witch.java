package src;

// The World2Witch class implements the Witch interface and represents a witch character
// with specific base health and attack values in the "World2" context.
public class World2Witch implements Witch {
    // Constants for the base health and attack values of the witch
    private static final int BASE_HEALTH = 90;
    private static final int BASE_ATTACK = 25;

    // Instance variables to store the current health and attack values of the witch
    private int health;
    private int attack;

    // Constructor initializes the witch's health and attack to their base values
    public World2Witch() {
        this.health = BASE_HEALTH;
        this.attack = BASE_ATTACK;
    }

    // Getter method to retrieve the current health of the witch
    @Override
    public int getHealth() {
        return health;
    }

    // Getter method to retrieve the current attack value of the witch
    @Override
    public int getAttack() {
        return attack;
    }

    // Overridden toString method to provide a string representation of the witch
    @Override
    public String toString() {
        return "Witch (World2) [Health=" + health + ", Attack=" + attack + "]";
    }
}
