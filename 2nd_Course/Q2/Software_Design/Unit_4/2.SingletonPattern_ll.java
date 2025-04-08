// 1. class logger singleton

public class Logger {
    private static Logger instance; 

    private Logger() {
        sysout.println("Logger initialized.");
    }

    public static Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }

    public void log(String message) {
        System.out.println("Log: " + message);
    }
}

// 2. main class to demonstrate the Singleton pattern:
public class Main {
    public static void main(String[] args) {
        Logger logger1 = Logger.getInstance();
        logger1.log("This is a log message from logger1.");

        Logger logger2 = Logger.getInstance();
        logger2.log("This is a log message from logger2.");

        System.out.println("Are both loggers the same instance? " + (logger1 == logger2));
    }
}