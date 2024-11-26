package astralis;

import java.util.ArrayList;
import java.util.List;

public class Jugador {
    private int recursos;
    private int defensas;
    private List<Nave> naves; // Lista de naves del jugador

    // Constructor del jugador, inicializando recursos y defensas
    public Jugador() {
        this.recursos = 50;
        this.defensas = 20;
        this.naves = new ArrayList<>(); // Inicializando la lista de naves
    }

    // Método para recolectar recursos
    public void recolectarRecursos() throws RecursoInsuficienteException {
        this.recursos += 10;
        System.out.println("Has recolectado recursos. Recursos actuales: " + recursos);
    }

    // Método para construir defensas
    public void construirDefensas() throws RecursoInsuficienteException {
        if (this.recursos < 5) {
            throw new RecursoInsuficienteException("No tienes suficientes recursos para construir defensas.");
        }
        this.recursos -= 5;
        this.defensas += 5;
        System.out.println("Has construido defensas. Recursos actuales: " + recursos + ", Puntos de defensa: " + defensas);
    }

    // Método para atacar
    public void atacar(Enemigo enemigo, Nave naveSeleccionada) throws RecursoInsuficienteException {
        if (this.recursos < 10) {
            throw new RecursoInsuficienteException("No tienes suficientes recursos para atacar.");
        }
        
        this.recursos -= 10;
        this.defensas -= 2;  // El jugador pierde defensas tras atacar
        
        // Determinar el daño basado en la nave seleccionada
        int danio = naveSeleccionada.getPoderDeAtaque();

        // Verificar si la nave seleccionada es débil frente a las naves del enemigo
        for (Nave naveEnemiga : enemigo.obtenerNaves()) {
            if (naveSeleccionada.getCounter().equals(naveEnemiga.getTipo())) {
                System.out.println("¡Tu nave ha sido contraatacada!");
                danio /= 2; // La nave es contrarrestada, reduciendo el daño
            }
        }

        enemigo.recibirDanio(danio); // Infligir daño al enemigo
        
        System.out.println("Has atacado al enemigo con la nave " + naveSeleccionada.getTipo() + " infligiendo " + danio + " puntos de daño.");
    }

    // Método para agregar una nave a la lista de naves
    public void agregarNave(Nave nave) {
        naves.add(nave);  // Agrega la nave a la lista
        System.out.println("Nave agregada: " + nave.getTipo());
    }

    public void ejecutarAccion(int opcion, Enemigo enemigo, Nave naveSeleccionada) throws AccionInvalidaException, RecursoInsuficienteException {
        switch (opcion) {
            case 1:
                recolectarRecursos();
                break;
            case 2:
                construirDefensas();
                break;
            case 3:
                // Llamamos al método atacar con los parámetros requeridos
                atacar(enemigo, naveSeleccionada);
                break;
            default:
                throw new AccionInvalidaException("Opción inválida. Elige una acción válida.");
        }
    }
	

    // Método para mostrar el estado del jugador
    public void mostrarEstado() {
        System.out.println("Estado del jugador - Recursos: " + recursos + ", Puntos de defensa: " + defensas);
        System.out.println("Naves: ");
        for (Nave nave : naves) {
            System.out.println(nave.getTipo());
        }
    }

    // Getters
    public int getRecursos() {
        return recursos;
    }

    public int getDefensas() {
        return defensas;
    }

    public List<Nave> getNaves() {
        return naves;
    }

    // Método para modificar las defensas del jugador, si es necesario
    public void setDefensas(int defensas) {
        this.defensas = defensas;
    }
}
