public class Logger {
    private static Logger instance;

    private Logger() {
        // Constructor privado
    }

    public static Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }

    public void log(String message) {
        System.out.println("[LOG]: " + message);
    }
}

public class App {
    public static void main(String[] args) {
        Logger logger1 = Logger.getInstance();
        Logger logger2 = Logger.getInstance();

        logger1.log("Sistema iniciado");
        logger2.log("Acción del usuario");

        // Comprobamos que ambos objetos son el mismo
        System.out.println(logger1 == logger2);  // true
    }
}

