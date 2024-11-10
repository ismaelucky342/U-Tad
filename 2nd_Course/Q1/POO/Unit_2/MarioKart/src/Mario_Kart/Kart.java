package Mario_Kart;

import java.util.Random;
import java.util.HashMap;
import java.util.Map;

public class Kart {
    private String nombre;
    private int velocidadMaximaBase;
    private int velocidadMaximaActual;
    private boolean estado;
    private int velocidadActual;
    private int aceleracion;
    private int manejo;
    private int peso;
    private int miniturbosCargados;
    private Map<String, Integer> mejoras;
    private boolean efectoTemporal;
    private int duracionEfectoTemporal;

    public Kart(String nombre, int velocidadMaxima, int aceleracion, int manejo, int peso) {
        this.nombre = nombre;
        this.velocidadMaximaBase = velocidadMaxima;
        this.velocidadMaximaActual = velocidadMaxima;
        this.estado = true;
        this.velocidadActual = 0;
        this.aceleracion = aceleracion;
        this.setManejo(manejo);
        this.setPeso(peso);
        this.miniturbosCargados = 0;
        this.setMejoras(new HashMap<>());
        this.efectoTemporal = false;
        this.duracionEfectoTemporal = 0;
    }

    public void acelerar() {
        if (estado) {
            int incremento = aceleracion + new Random().nextInt(10);
            velocidadActual = Math.min(velocidadActual + incremento, velocidadMaximaActual);
        }
    }

    public void frenar() {
        velocidadActual = Math.max(0, velocidadActual - new Random().nextInt(15));
    }

    public void chocar() {
        estado = false;
        velocidadActual = 0;
    }

    public void cargarMiniturbo() {
        if (estado && velocidadActual > velocidadMaximaActual * 0.7) {
            miniturbosCargados++;
            System.out.println(nombre + " ha cargado un miniturbo! (" + miniturbosCargados + ")");
        }
    }

    public void aplicarMiniturbo() {
        if (miniturbosCargados > 0) {
            velocidadActual = (int)(velocidadMaximaActual * 1.5);
            miniturbosCargados--;
            System.out.println(nombre + " usa un miniturbo!");
        }
    }

    public void aumentarVelocidadMaxima(int aumento, int duracion) {
        velocidadMaximaActual += aumento;
        efectoTemporal = true;
        duracionEfectoTemporal = duracion;
    }

    public void actualizarEfectosTemporales() {
        if (efectoTemporal) {
            duracionEfectoTemporal--;
            if (duracionEfectoTemporal <= 0) {
                velocidadMaximaActual = velocidadMaximaBase;
                efectoTemporal = false;
            }
        }
    }

    // Getters y setters
    public String getNombre() {
        return nombre;
    }

    public boolean getEstado() {
        return estado;
    }

    public int getVelocidadActual() {
        return velocidadActual;
    }

	public int getManejo() {
		return manejo;
	}

	public void setManejo(int manejo) {
		this.manejo = manejo;
	}

	public int getPeso() {
		return peso;
	}

	public void setPeso(int peso) {
		this.peso = peso;
	}

	public Map<String, Integer> getMejoras() {
		return mejoras;
	}

	public void setMejoras(Map<String, Integer> mejoras) {
		this.mejoras = mejoras;
	}
}