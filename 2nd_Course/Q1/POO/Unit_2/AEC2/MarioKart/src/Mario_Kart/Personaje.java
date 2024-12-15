package Mario_Kart;

import java.util.ArrayList;
import java.util.List;

public class Personaje {
    private String nombre;
    private String habilidadEspecial;
    private int victorias;
    private Kart kart;
    private int posicionActual;
    private int monedas;
    private int experiencia;
    private int nivel;
    private boolean inmunidad;
    private int duracionInmunidad;
    private List<Item> inventario;

    public Personaje(String nombre, String habilidadEspecial, Kart kart) {
        this.nombre = nombre;
        this.habilidadEspecial = habilidadEspecial;
        this.victorias = 0;
        this.kart = kart;
        this.posicionActual = 0;
        this.monedas = 0;
        this.setExperiencia(0);
        this.nivel = 1;
        this.inmunidad = false;
        this.duracionInmunidad = 0;
        this.setInventario(new ArrayList<>());
    }

    public void usarHabilidadEspecial() {
        System.out.println(nombre + " usa " + habilidadEspecial + "!");
    }

    public void sumarVictoria() {
        victorias++;
    }

    public void recogerMoneda() {
        monedas++;
        if (monedas % 10 == 0) {
            subirNivel();
        }
    }

    public void subirNivel() {
        nivel++;
        System.out.println(nombre + " ha subido al nivel " + nivel + "!");
    }

    public void setInmunidad(boolean inmunidad, int duracion) {
        this.inmunidad = inmunidad;
        this.duracionInmunidad = duracion;
    }

    public void actualizarEstado() {
        if (inmunidad) {
            duracionInmunidad--;
            if (duracionInmunidad <= 0) {
                inmunidad = false;
            }
        }
        kart.actualizarEfectosTemporales();
    }

    public void avanzar() {
        if (kart.getEstado()) {
            kart.acelerar();
            posicionActual += kart.getVelocidadActual();
        }
    }

    public void ganarExperiencia(int cantidad) {
        setExperiencia(getExperiencia() + cantidad);
    }

    public void ganarMonedas(int cantidad) {
        monedas += cantidad;
    }

    // Getters y setters
    public String getNombre() {
        return nombre;
    }

    public int getVictorias() {
        return victorias;
    }

    public Kart getKart() {
        return kart;
    }

    public int getPosicionActual() {
        return posicionActual;
    }

    public void setPosicionActual(int posicionActual) {
        this.posicionActual = posicionActual;
    }

    public int getMonedas() {
        return monedas;
    }

    public int getNivel() {
        return nivel;
    }

    public boolean tieneInmunidad() {
        return inmunidad;
    }

	public int getExperiencia() {
		return experiencia;
	}

	public void setExperiencia(int experiencia) {
		this.experiencia = experiencia;
	}

	public List<Item> getInventario() {
		return inventario;
	}

	public void setInventario(List<Item> inventario) {
		this.inventario = inventario;
	}
}
