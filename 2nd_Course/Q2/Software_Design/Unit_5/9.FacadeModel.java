// --- Subsistemas ---
class LuzVisible {
    void encender() { System.out.println("Luz visible encendida."); }
}

class LuzInfrarroja {
    void encender() { System.out.println("Luz infrarroja encendida."); }
}

class ObservadorLuzVisible {
    void actualizar() { System.out.println("Observador de luz visible notificado."); }
}

class ObservadorLuzInfrarroja {
    void actualizar() { System.out.println("Observador de luz infrarroja notificado."); }
}

// --- Fachada adicional para Luz Visible ---
class FachadaLuzVisible {
    private LuzVisible luz = new LuzVisible();
    private ObservadorLuzVisible observador = new ObservadorLuzVisible();

    void activarLuz() {
        luz.encender();
        observador.actualizar();
    }
}

// --- Fachada adicional para Luz Infrarroja ---
class FachadaLuzInfrarroja {
    private LuzInfrarroja luz = new LuzInfrarroja();
    private ObservadorLuzInfrarroja observador = new ObservadorLuzInfrarroja();

    void activarLuz() {
        luz.encender();
        observador.actualizar();
    }
}


// --- Fachada principal ---
class FachadaGeneradorLuz {
    private FachadaLuzVisible fachadaVisible = new FachadaLuzVisible();
    private FachadaLuzInfrarroja fachadaInfrarroja = new FachadaLuzInfrarroja();

    // Por defecto activa la luz visible
    void activarLuzVisible() {
        fachadaVisible.activarLuz();
    }

    void activarLuzInfrarroja() {
        fachadaInfrarroja.activarLuz();
    }
}

// --- Cliente ---
public class Cliente {
    public static void main(String[] args) {
        FachadaGeneradorLuz fachada = new FachadaGeneradorLuz();
        
        // Activa luz visible y su observador
        fachada.activarLuzVisible();

        // Activa luz infrarroja y su observador
        fachada.activarLuzInfrarroja();
    }
}
