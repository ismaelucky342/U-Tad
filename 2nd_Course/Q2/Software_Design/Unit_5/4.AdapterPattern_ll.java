public interface USPlug {
    void connectToUSSocket();
}

public class EUPlug {
    public void connectToEUSocket() {
        System.out.println("Connected to EU socket.");
    }
}

public class EUtoUSAdapter implements USPlug {
    private EUPlug euPlug;

    public EUtoUSAdapter(EUPlug euPlug) {
        this.euPlug = euPlug;
    }

    @Override
    public void connectToUSSocket() {
        System.out.println("Using adapter to convert EU plug to US socket...");
        euPlug.connectToEUSocket();
    }
    
}

public class Main {
    public static void main(String[] args) {
        EUPlug euPlug = new EUPlug();
        USPlug adapter = new EUtoUSAdapter(euPlug);
        
        adapter.connectToUSSocket(); // This will use the adapter to connect to the US socket
    }
}