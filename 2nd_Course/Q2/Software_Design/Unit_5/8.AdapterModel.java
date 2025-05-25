// Interfaz que el cliente espera
interface IDispositivo {
    void encender();
    void apagar();
}

// Clase existente con interfaz incompatible
class DispositivoViejo {
    public void powerOn() {
        System.out.println("Dispositivo viejo encendido");
    }
    public void powerOff() {
        System.out.println("Dispositivo viejo apagado");
    }
}

// Adaptador que traduce la interfaz vieja a la nueva
class AdaptadorDispositivo implements IDispositivo {
    private DispositivoViejo viejo;

    public AdaptadorDispositivo(DispositivoViejo viejo) {
        this.viejo = viejo;
    }

    @Override
    public void encender() {
        viejo.powerOn(); // Traduce la llamada
    }

    @Override
    public void apagar() {
        viejo.powerOff(); // Traduce la llamada
    }
}

// Uso
public class MainAdaptador {
    public static void main(String[] args) {
        DispositivoViejo viejo = new DispositivoViejo();
        IDispositivo dispositivo = new AdaptadorDispositivo(viejo);

        dispositivo.encender(); // Cliente usa la interfaz nueva, pero llama al viejo
        dispositivo.apagar();
    }
}
