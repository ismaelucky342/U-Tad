package Zoo;

public class Ave extends Animal {
    private boolean puedeVolar;

    public Ave(String nombre, int edad, double peso, Habitat habitat, boolean puedeVolar) {
        super(nombre, edad, peso, habitat);
        this.setPuedeVolar(puedeVolar);
    }

    @Override
    public void comer() {
        System.out.println("El ave está comiendo.");
    }

    @Override
    public void dormir() {
        System.out.println("El ave está durmiendo.");
    }

    @Override
    public void hacerSonido() {
        System.out.println("El ave hace un canto.");
    }

	public boolean isPuedeVolar() {
		return puedeVolar;
	}

	public void setPuedeVolar(boolean puedeVolar) {
		this.puedeVolar = puedeVolar;
	}
}
