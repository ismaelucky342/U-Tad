/*
Decoradores de codificación y compresión
Este ejemplo muestra cómo puedes ajustar el comportamiento de un objeto sin cambiar su código.

Inicialmente, la clase de la lógica de negocio sólo podía leer y escribir datos en texto sin formato. Después creamos varias pequeñas clases envoltorio que añaden un nuevo comportamiento tras ejecutar operaciones estándar en un objeto envuelto.

El primer wrapper codifica y decodifica información, y el segundo comprime y extrae datos.

Puedes incluso combinar estos wrappers envolviendo un decorador con otro.
*/

public interface DataSource {
	void writeData(String data);
	String readData();
}

public class FileDataSource implements DataSource {

	// Atributo que representa el nombre del archivo
	// Este atributo almacena el nombre del archivo donde se guardarán los datos.
	private String filename;

	// Constructor que recibe el nombre del archivo
	// Este constructor inicializa el nombre del archivo donde se guardarán los datos.
	public FileDataSource(String filename) {
		this.filename = filename;
	}

	// Método que escribe datos en el archivo
	// Este método escribe los datos proporcionados en el archivo especificado.
	@Override
	public void writeData(String data) {
		File file = new File(filename);
		FileOutputStream fos = new FileOutputStream(file);
		fos.write(data.getBytes());
		fos.close();
	}

	// Método que lee datos del archivo
	// Este método lee los datos del archivo especificado y los devuelve como una cadena.
	@Override
	public String readData() {
		File file = new File(filename);
		FileInputStream fis = new FileInputStream(file);
		byte[] data = new byte[(int) file.length()];
		fis.read(data);
		fis.close();
		return new String(data);
	}
}

public class Base64DataSource implements DataSource {

	// Atributo que representa la fuente de datos envuelta
	// Este atributo almacena la fuente de datos original que se está envolviendo.
	private DataSource wrapped;

	// Constructor que recibe una fuente de datos
	// Este constructor inicializa la fuente de datos envuelta.
	public Base64DataSource(DataSource wrapped) {
		this.wrapped = wrapped;
	}

	// Método que escribe datos codificados en Base64
	@Override
	public void writeData(String data) {
		String encodedData = Base64.getEncoder().encodeToString(data.getBytes());
		wrapped.writeData(encodedData);
	}

	// Método que lee datos decodificados desde Base64
	@Override
	public String readData() {
		String encodedData = wrapped.readData();
		return new String(Base64.getDecoder().decode(encodedData));
	}
}

