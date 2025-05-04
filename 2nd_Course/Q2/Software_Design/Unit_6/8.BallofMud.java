public class UserManager {
    public void createUser(String name, String email) {
        // Some validation
        System.out.println("Validating user info...");
        System.out.println("Creating user: " + name);
    }

    public void saveUser(String name, String email) {
        System.out.println("Saving user to the database...");
    }

    public void deleteUser(String email) {
        System.out.println("Deleting user...");
        System.out.println("Sending deletion email...");
    }

    public void sendEmail(String email, String subject, String message) {
        // Some email logic
        System.out.println("Sending email to: " + email);
    }

    public void logAction(String action) {
        // Logging
        System.out.println("Logging action: " + action);
    }
}
