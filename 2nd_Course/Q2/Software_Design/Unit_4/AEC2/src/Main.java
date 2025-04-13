package src;

// Main class to start the application
public class Main {
    public static void main(String[] args) {
        // Get the singleton instance of GameController and start the game
        GameController game = GameController.getInstance();
        game.play();
    }
}
