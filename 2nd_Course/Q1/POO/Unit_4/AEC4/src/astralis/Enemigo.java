package astralis;

import java.util.ArrayList;
import java.util.List;

public class Enemigo {
    private int recursos;
    private int poderDeAtaque;
    private int defensas;
    private List<Nave> naves;

    public Enemigo() {
        this.recursos = 50;
        this.defensas = 20;
        this.naves = new ArrayList<>();
    }

    public void agregarNave(Nave nave) {
        naves.add(nave);
    }

    public int obtenerDefensas() {
        return defensas;
    }

    public List<Nave> obtenerNaves() {
        return naves;
    }

    public void recibirDanio(int danio) {
        this.defensas -= danio;
        if (this.defensas < 0) this.defensas = 0; // Asegura que las defensas no sean negativas
    }

    public void mostrarEstado() {
        System.out.println("Estado del enemigo - Recursos: " + recursos + ", Puntos de defensa: " + defensas);
        System.out.println("Naves: ");
        for (Nave nave : naves) {
            System.out.println(nave.getTipo());
        }
    }
    // Método para establecer el poder de ataque
    public void setPoderDeAtaque(int poderDeAtaque) {
        this.poderDeAtaque = poderDeAtaque;
    }

    // Método para obtener el poder de ataque
    public int getPoderDeAtaque() {
        return poderDeAtaque;
    }
}
