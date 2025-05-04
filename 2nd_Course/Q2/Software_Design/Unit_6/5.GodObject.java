public class UserManager {
    // God Object: This class is doing way too much
    public void createUser(String name, String email, String password) {
        // Database logic
        System.out.println("Creating user...");
        System.out.println("Saving to database...");
    }

    public void sendWelcomeEmail(String email) {
        // Email logic
        System.out.println("Sending welcome email to: " + email);
    }

    public void createUserAndSendWelcomeEmail(String name, String email, String password) {
        // Combining multiple responsibilities in one method
        createUser(name, email, password);
        sendWelcomeEmail(email);
    }

    public void deleteUser(String email) {
        // Deleting user
        System.out.println("Deleting user: " + email);
    }
    
    public void resetPassword(String email) {
        // Password reset logic
        System.out.println("Resetting password for: " + email);
    }
}
