package src;

//
// The {@code World1Daemon} class represents a daemon entity in the World1 environment.
// It implements the {@code Daemon} interface and provides basic attributes such as health and attack.
// 
// <p>
// This class uses constant base values for health and attack, which are initialized in the constructor.
// </p>
 //
public class World1Daemon implements Daemon {
    // Base health value for the daemon
    private static final int BASE_HEALTH = 100;
    // Base attack value for the daemon
    private static final int BASE_ATTACK = 30;

    // Minimum and maximum allowed values for health and attack
    private static final int MIN_HEALTH = 0;
    private static final int MAX_HEALTH = 200;
    private static final int MIN_ATTACK = 0;
    private static final int MAX_ATTACK = 50;

    // Current health of the daemon
    private int health;
    // Current attack value of the daemon
    private int attack;

    //
    // Constructs a new {@code World1Daemon} with default base health and attack values.
     //
    public World1Daemon() {
        this.health = validateHealth(BASE_HEALTH);
        this.attack = validateAttack(BASE_ATTACK);
    }

    //
    // Returns the current health of the daemon.
    // 
    // @return the health value
     //
    @Override
    public int getHealth() {
        return health;
    }

    //
    // Sets the health of the daemon, ensuring it is within valid bounds.
    // 
    // @param health the new health value
     //
    public void setHealth(int health) {
        this.health = validateHealth(health);
    }

    //
    // Returns the current attack value of the daemon.
    // 
    // @return the attack value
     //
    @Override
    public int getAttack() {
        return attack;
    }

    //
    // Sets the attack value of the daemon, ensuring it is within valid bounds.
    // 
    // @param attack the new attack value
    //
    public void setAttack(int attack) {
        this.attack = validateAttack(attack);
    }

    //
    // Returns a string representation of the daemon, including its health and attack values.
    // 
    // @return a string describing the daemon
     //
    @Override
    public String toString() {
        return "Daemon (World1) [Health=" + health + ", Attack=" + attack + "]";
    }

    //
    // Validates the health value to ensure it is within the allowed range.
    // 
    // @param health the health value to validate
    // @return the validated health value
    // @throws IllegalArgumentException if the health value is out of bounds
     //
    private int validateHealth(int health) {
        if (health < MIN_HEALTH || health > MAX_HEALTH) {
            throw new IllegalArgumentException("Health must be between " + MIN_HEALTH + " and " + MAX_HEALTH);
        }
        return health;
    }

    //
    // Validates the attack value to ensure it is within the allowed range.
    // 
    // @param attack the attack value to validate
    // @return the validated attack value
    // @throws IllegalArgumentException if the attack value is out of bounds
     //
    private int validateAttack(int attack) {
        if (attack < MIN_ATTACK || attack > MAX_ATTACK) {
            throw new IllegalArgumentException("Attack must be between " + MIN_ATTACK + " and " + MAX_ATTACK);
        }
        return attack;
    }
}
