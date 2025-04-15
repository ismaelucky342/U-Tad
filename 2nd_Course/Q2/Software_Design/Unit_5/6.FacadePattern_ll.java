public class UserService {
    public boolean isUserLoggedIn(String username) {
        System.out.println("Checking if user '" + username + "' is logged in...");
        return true; // Simulamos que siempre está logueado
    }
}

public class GameCatalogService {
    public boolean isGameAvailable(String game) {
        System.out.println("Checking availability for game: " + game);
        return true; // Simulamos disponibilidad
    }
}

public class PaymentService {
    public void processPayment(String username, String game) {
        System.out.println("Processing payment for '" + username + "' to buy '" + game + "'");
    }
}

public class EmailService {
    public void sendConfirmation(String username, String game) {
        System.out.println("Sending confirmation email to '" + username + "' for game '" + game + "'");
    }
}


public class GameStoreFacade {
    private UserService userService;
    private GameCatalogService catalogService;
    private PaymentService paymentService;
    private EmailService emailService;

    public GameStoreFacade() {
        userService = new UserService();
        catalogService = new GameCatalogService();
        paymentService = new PaymentService();
        emailService = new EmailService();
    }

    public void buyGame(String username, String game) {
        if (!userService.isUserLoggedIn(username)) {
            System.out.println("User is not logged in.");
            return;
        }

        if (!catalogService.isGameAvailable(game)) {
            System.out.println("Game is not available.");
            return;
        }

        paymentService.processPayment(username, game);
        emailService.sendConfirmation(username, game);
        System.out.println("Game purchased successfully! ✅");
    }
}


public class Main {
    public static void main(String[] args) {
        GameStoreFacade gameStore = new GameStoreFacade();

        gameStore.buyGame("gamer123", "Elden Ring");
    }
}