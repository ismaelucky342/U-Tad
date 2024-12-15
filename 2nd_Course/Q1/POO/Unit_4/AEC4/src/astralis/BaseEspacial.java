package astralis;

public class BaseEspacial {
    private int recursos;
    private int puntosDefensa;

    // Constructor: inicializa la base con recursos y defensa iniciales
    public BaseEspacial() {
        this.recursos = 50; // Valor inicial
        this.puntosDefensa = 20; // Valor inicial
    }

    // Método para recolectar recursos
    public void recolectarRecursos() {
        recursos += 10;
        System.out.println("¡Has recolectado recursos! Recursos actuales: " + recursos);
    }

    // Método para construir defensas
    public void construirDefensas() throws RecursoInsuficienteException {
        if (recursos < 5) {
            throw new RecursoInsuficienteException("No tienes suficientes recursos para construir defensas.");
        }
        recursos -= 5;
        puntosDefensa += 5;
        System.out.println("¡Has construido defensas! Recursos: " + recursos + ", Defensa: " + puntosDefensa);
    }

    // Método para atacar
    public void atacar() throws RecursoInsuficienteException {
        if (recursos < 10) {
            throw new RecursoInsuficienteException("No tienes suficientes recursos para atacar.");
        }
        recursos -= 10;
        puntosDefensa -= 2;
        System.out.println("¡Has atacado al enemigo! Recursos: " + recursos + ", Defensa: " + puntosDefensa);
    }

    // Mostrar el estado actual de la base
    public void mostrarEstado() {
        System.out.println("Estado de la base - Recursos: " + recursos + ", Defensa: " + puntosDefensa);
    }

    // Métodos adicionales para obtener el estado actual
    public int getRecursos() {
        return recursos;
    }

    public int getPuntosDefensa() {
        return puntosDefensa;
    }

    // Métodos adicionales para verificar el estado de la base
    public boolean estaDestruida() {
        return puntosDefensa <= 0;
    }

    public boolean sinRecursos() {
        return recursos <= 0;
    }
}
