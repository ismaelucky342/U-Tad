// Componente (interfaz)
interface Luz {
    void encender();
    void apagar();
}

// Componente concreto
class LuzVisible implements Luz {
    @Override
    public void encender() {
        System.out.println("Luz visible encendida");
    }
    @Override
    public void apagar() {
        System.out.println("Luz visible apagada");
    }
}

// Decorador abstracto
abstract class LuzDecorator implements Luz {
    protected Luz luzDecorada;

    public LuzDecorator(Luz luz) {
        this.luzDecorada = luz;
    }

    @Override
    public void encender() {
        luzDecorada.encender();
    }

    @Override
    public void apagar() {
        luzDecorada.apagar();
    }
}

// Decorador concreto que añade funcionalidad
class LuzConFiltroRojo extends LuzDecorator {
    public LuzConFiltroRojo(Luz luz) {
        super(luz);
    }

    @Override
    public void encender() {
        luzDecorada.encender();
        ponerFiltroRojo();
    }

    private void ponerFiltroRojo() {
        System.out.println("Filtro rojo activado");
    }
}

// Cliente
public class Main {
    public static void main(String[] args) {
        Luz luz = new LuzVisible();
        Luz luzConFiltro = new LuzConFiltroRojo(luz);

        luzConFiltro.encender();
        luzConFiltro.apagar();
    }
}