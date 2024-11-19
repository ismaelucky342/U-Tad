package Mario_Kart;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class CarreraMarioKart {
    private ArrayList<Personaje> personajes;
    private Pista pista;
    private int vueltas;
    private Map<Personaje, Integer> vueltasCompletadas;
    private Map<Personaje, Integer> posiciones;

    public CarreraMarioKart(Pista pista, int vueltas) {
        this.personajes = new ArrayList<>();
        this.pista = pista;
        this.vueltas = vueltas;
        this.vueltasCompletadas = new HashMap<>();
        this.posiciones = new HashMap<>();
    }

    public void agregarPersonaje(Personaje personaje) {
        personajes.add(personaje);
    }

    public void iniciarCarrera() {
        System.out.println("\n¡Comienza la carrera en " + pista.getNombre() + "!");
        System.out.println("Vueltas totales: " + vueltas);
        
        inicializarCarrera();
        
        while (!carreraTerminada()) {
            actualizarCarrera();
            mostrarEstadoCarrera();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        finalizarCarrera();
    }

    private void inicializarCarrera() {
        for (Personaje p : personajes) {
            vueltasCompletadas.put(p, 0);
            posiciones.put(p, 0);
        }
        
        // Cuenta atrás
        for (int i = 3; i > 0; i--) {
            System.out.println(i + "...");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        System.out.println("¡YA!");
    }

    private void actualizarCarrera() {
        for (Personaje p : personajes) {
            if (p.getKart().getEstado()) {
                p.avanzar();
                int posicionActual = p.getPosicionActual();
                
                // Comprobar vuelta completada
                if (posicionActual >= pista.getLongitud()) {
                    vueltasCompletadas.put(p, vueltasCompletadas.get(p) + 1);
                    p.setPosicionActual(posicionActual % pista.getLongitud());
                    System.out.println("¡" + p.getNombre() + " completa la vuelta " + vueltasCompletadas.get(p) + "!");
                }

                // Comprobar puntos clave
                String mensajePuntoClave = pista.checkPuntoClave(posicionActual);
                if (mensajePuntoClave != null) {
                    System.out.println(p.getNombre() + ": " + mensajePuntoClave);
                }

                procesarEventosAleatorios(p);
                p.actualizarEstado();
            }
        }
        
        actualizarPosiciones();
    }

    private void procesarEventosAleatorios(Personaje p) {
        Random rand = new Random();
        
        // Probabilidad de encontrar moneda
        if (rand.nextInt(100) < 15) {
            p.recogerMoneda();
            System.out.println(p.getNombre() + " recoge una moneda!");
        }

        // Probabilidad de encontrar item
        if (rand.nextInt(100) < 20 && !pista.getItems().isEmpty()) {
            Item item = pista.getItems().get(rand.nextInt(pista.getItems().size()));
            item.aplicarEfecto(p);
        }

        // Probabilidad de encontrar obstáculo
        if (rand.nextInt(100) < 15 && !pista.getObstaculos().isEmpty() && !p.tieneInmunidad()) {
            Obstaculo obs = pista.getObstaculos().get(rand.nextInt(pista.getObstaculos().size()));
            obs.aplicarEfecto(p.getKart());
        }

        // Probabilidad de cargar miniturbo
        if (rand.nextInt(100) < 10) {
            p.getKart().cargarMiniturbo();
        }
    }

    private void actualizarPosiciones() {
        List<Personaje> ranking = new ArrayList<>(personajes);
        ranking.sort((p1, p2) -> {
            int vueltasP1 = vueltasCompletadas.get(p1);
            int vueltasP2 = vueltasCompletadas.get(p2);
            if (vueltasP1 != vueltasP2) {
                return vueltasP2 - vueltasP1;
            }
            return p2.getPosicionActual() - p1.getPosicionActual();
        });
        
        for (int i = 0; i < ranking.size(); i++) {
            posiciones.put(ranking.get(i), i + 1);
        }
    }

    private void mostrarEstadoCarrera() {
        System.out.println("\nEstado de la carrera:");
        for (Personaje p : personajes) {
            System.out.printf("%s - Posición: %d - Vuelta: %d/%d%n",
                p.getNombre(),
                posiciones.get(p),
                vueltasCompletadas.get(p),
                vueltas);
        }
    }

    private boolean carreraTerminada() {
        return personajes.stream()
            .anyMatch(p -> vueltasCompletadas.get(p) >= vueltas);
    }

    private void finalizarCarrera() {
        Personaje ganador = determinarGanador();
        if (ganador != null) {
            ganador.sumarVictoria();
            System.out.println("\n¡" + ganador.getNombre() + " ha ganado la carrera!");
            ganador.ganarExperiencia(100);
            ganador.ganarMonedas(50);
        }
        
        mostrarResultadosFinales();
    }

    private void mostrarResultadosFinales() {
        System.out.println("\nResultados finales:");
        List<Personaje> ranking = new ArrayList<>(personajes);
        ranking.sort((p1, p2) -> posiciones.get(p1) - posiciones.get(p2));
        
        for (int i = 0; i < ranking.size(); i++) {
            Personaje p = ranking.get(i);
            System.out.printf("%d. %s - Nivel: %d - Monedas: %d%n",
                i + 1,
                p.getNombre(),
                p.getNivel(),
                p.getMonedas());
        }
    }

    public Personaje determinarGanador() {
        return personajes.stream()
            .max(Comparator.comparingInt(p -> vueltasCompletadas.get(p)))
            .orElse(null);
    }

    public Pista getPista() {
        return pista;
    }

    public void setPista(Pista pista) {
        this.pista = pista;
    }

    public int getVueltas() {
        return vueltas;
    }

    public void setVueltas(int vueltas) {
        this.vueltas = vueltas;
    }

    public Map<Personaje, Integer> getVueltasCompletadas() {
        return vueltasCompletadas;
    }

    public void setVueltasCompletadas(Map<Personaje, Integer> vueltasCompletadas) {
        this.vueltasCompletadas = vueltasCompletadas;
    }

    public ArrayList<Personaje> getPersonajes() {
        return personajes;
    }

    public void setPersonajes(ArrayList<Personaje> personajes) {
        this.personajes = personajes;
    }

    public Map<Personaje, Integer> getPosiciones() {
        return posiciones;
    }

    public void setPosiciones(Map<Personaje, Integer> posiciones) {
        this.posiciones = posiciones;
    }
}
