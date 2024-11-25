package Zoo;

public class reptil extends Animal {
    private String tipoEscamas;

    public reptil(String nombre, int edad, double peso, Habitat habitat, String tipoEscamas) {
        super(nombre, edad, peso, habitat);
        this.setTipoEscamas(tipoEscamas);
    }

    @Override
    public void comer() {
        System.out.println("El reptil está comiendo.");
    }

    @Override
    public void dormir() {
        System.out.println("El reptil está durmiendo.");
    }

    @Override
    public void hacerSonido() {
        System.out.println("El reptil hace un siseo.");
    }

	public String getTipoEscamas() {
		return tipoEscamas;
	}

	public void setTipoEscamas(String tipoEscamas) {
		this.tipoEscamas = tipoEscamas;
	}
}
