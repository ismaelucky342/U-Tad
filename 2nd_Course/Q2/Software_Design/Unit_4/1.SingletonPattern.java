//Singleton

//1. public class singleton 

public class ConfigManager {

    private static ConfigManager instance;
    private String configurationValue;

    private ConfigManager() {
        configurationValue = "Valor predeterminado";
    }

    public static ConfigManager getInstance() {
        if (instance == null) {
            instance = new ConfigManager();
        }
        return instance;
    }

    public String getConfigurationValue() {
        return configurationValue;
    }

    public void setConfigurationValue(String value) {
        configurationValue = value;
    }
}

//2. main class to demonstrate the Singleton pattern:
public class Main {
    public static void main(String[] args) {
        ConfigManager config1 = ConfigManager.getInstance();
        System.out.println("Config 1: " + config1.getConfigurationValue());

        ConfigManager config2 = ConfigManager.getInstance();
        config2.setConfigurationValue("Nuevo valor");

        System.out.println("Config 2: " + config2.getConfigurationValue());
        System.out.println("Config 1: " + config1.getConfigurationValue());
    }
}
