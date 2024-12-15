package Mario_Kart;

public class SimuladorMarioKart {
    public static void main(String[] args) {
        // Crear personajes con sus karts
        Personaje mario = new Personaje("Mario", "Estrella invencible", 
            new Kart("Kart Estándar", 100, 80, 70, 60));
        Personaje luigi = new Personaje("Luigi", "Rayo", 
            new Kart("Kart Verde", 95, 85, 75, 55));
        Personaje peach = new Personaje("Peach", "Corazón protector", 
            new Kart("Kart Rosa", 90, 90, 80, 50));
        Personaje yoshi = new Personaje("Yoshi", "Huevo explosivo", 
            new Kart("Kart Dinosaurio", 98, 82, 72, 58));

        // Crear items
        Item estrella = new Item("Estrella", "inmunidad", 3);
        Item hongo = new Item("Hongo", "velocidad", 2);
        Item pluma = new Item("Pluma", "miniturbo", 1);

        // Crear obstáculos
        Obstaculo platano = new Obstaculo("Plátano", "ralentizar");
        Obstaculo caparazonRojo = new Obstaculo("Caparazón Rojo", "chocar");
        Obstaculo caparazonAzul = new Obstaculo("Caparazón Azul", "chocar");

        // Crear pistas
        Pista circuitoVerde = new Pista("Circuito Verde", 1000, TipoPista.HIERBA);
        circuitoVerde.agregarObstaculo(platano);
        circuitoVerde.agregarObstaculo(caparazonRojo);
        circuitoVerde.agregarItem(estrella);
        circuitoVerde.agregarItem(hongo);

        Pista pistaHielo = new Pista("Pista Helada", 800, TipoPista.HIELO);
        pistaHielo.agregarObstaculo(caparazonAzul);
        pistaHielo.agregarItem(pluma);

        // Crear campeonato
        CampeonatoMarioKart campeonato = new CampeonatoMarioKart();
        
        // Agregar personajes al campeonato
        campeonato.agregarPersonaje(mario);
        campeonato.agregarPersonaje(luigi);
        campeonato.agregarPersonaje(peach);
        campeonato.agregarPersonaje(yoshi);

        // Organizar carreras
        System.out.println("=== PRIMERA CARRERA - CIRCUITO VERDE ===");
        campeonato.organizarCarrera(circuitoVerde, 3);
        campeonato.getCarreras().get(0).iniciarCarrera();

        System.out.println("\n=== SEGUNDA CARRERA - PISTA HELADA ===");
        campeonato.organizarCarrera(pistaHielo, 3);
        campeonato.getCarreras().get(1).iniciarCarrera();

        // Mostrar ranking final del campeonato
        campeonato.mostrarRanking();
        }
    }