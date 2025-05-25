public interface Luz {
    void emitir();
}

public class LuzVisible implements Luz {
    public void emitir() {
        System.out.println("🌈 Emitiendo luz visible");
    }
}

public class LuzInfrarroja implements Luz {
    public void emitir() {
        System.out.println("🌡️ Emitiendo luz infrarroja");
    }
}

public interface LuzFactory {
    Luz crearLuz();
}

public class LuzVisibleFactory implements LuzFactory {
    public Luz crearLuz() {
        // 👁️ Delegación adicional: se asume que también se crea un observador aquí
        System.out.println("👁️ Creando observador para luz visible");
        return new LuzVisible();
    }
}

public class LuzInfrarrojaFactory implements LuzFactory {
    public Luz crearLuz() {
        // 👓 Delegación adicional: se asume que también se crea un observador aquí
        System.out.println("👓 Creando observador para luz infrarroja");
        return new LuzInfrarroja();
    }
}

public class ClienteLuz {
    private Luz luz;

    public ClienteLuz(LuzFactory factory) {
        // 🔁 Delegación a la fábrica concreta
        this.luz = factory.crearLuz();
    }

    public void ejecutar() {
        luz.emitir();
    }
}

public class Main {
    public static void main(String[] args) {
        // Cambia de fábrica aquí según lo que quieras crear
        LuzFactory factory = new LuzVisibleFactory();  // o LuzInfrarrojaFactory
        ClienteLuz cliente = new ClienteLuz(factory);
        cliente.ejecutar();
    }
}
