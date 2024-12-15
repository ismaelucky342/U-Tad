package Mario_Kart;

import java.util.ArrayList;

public class CampeonatoMarioKart {
    private ArrayList<CarreraMarioKart> carreras;
    private ArrayList<Personaje> personajes;

    public CampeonatoMarioKart() {
        this.carreras = new ArrayList<>();
        this.personajes = new ArrayList<>();
    }

    public void agregarPersonaje(Personaje personaje) {
        personajes.add(personaje);
    }

    public void organizarCarrera(Pista pista, int vueltas) {
        CarreraMarioKart carrera = new CarreraMarioKart(pista, vueltas);
        for (Personaje personaje : personajes) {
            carrera.agregarPersonaje(personaje);
        }
        carreras.add(carrera);
    }

    public void mostrarRanking() {
        System.out.println("\nRANKING FINAL DEL CAMPEONATO:");
        ArrayList<Personaje> ranking = new ArrayList<>(personajes);
        ranking.sort((p1, p2) -> p2.getVictorias() - p1.getVictorias());

        for (int i = 0; i < ranking.size(); i++) {
            Personaje p = ranking.get(i);
            System.out.println((i + 1) + ". " + p.getNombre() + 
                             " - Victorias: " + p.getVictorias() + 
                             " - Nivel: " + p.getNivel() + 
                             " - Monedas totales: " + p.getMonedas());
        }
    }

    public ArrayList<CarreraMarioKart> getCarreras() {
        return carreras;
    }
}
