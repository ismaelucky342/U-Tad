public class HashCodeExample {
	private String nombre;

	public HashCodeExample(String nombre) {
		this.nombre = nombre;
	}

	@Override
	public int hashCode() {
		return nombre.hashCode();
	}
}
