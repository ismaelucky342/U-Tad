package Zoo;

public class Mamifero extends Animal {
    private String tipoPelo;

    public Mamifero(String nombre, int edad, double peso, Habitat habitat, String tipoPelo) {
        super(nombre, edad, peso, habitat);
        this.setTipoPelo(tipoPelo);
    }

    @Override
    public void comer() {
        System.out.println("El mamífero está comiendo.");
    }

    @Override
    public void dormir() {
        System.out.println("El mamífero está durmiendo.");
    }

    @Override
    public void hacerSonido() {
        System.out.println("El mamífero hace un rugido.");
    }

	public String getTipoPelo() {
		return tipoPelo;
	}

	public void setTipoPelo(String tipoPelo) {
		this.tipoPelo = tipoPelo;
	}
}

