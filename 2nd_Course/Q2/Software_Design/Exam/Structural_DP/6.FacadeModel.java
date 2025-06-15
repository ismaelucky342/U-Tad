/*
### Variante 3.7 – **Facade: Reproductor multimedia**

**Enunciado:**

Tenemos un sistema de reproducción multimedia con múltiples subsistemas: decodificador, procesador de audio, renderizador de video, etc. Queremos ofrecer una interfaz simple con el patrón **Facade**.

**Componentes requeridos:**

- `MediaPlayerFacade`: única clase expuesta al cliente.
- Subsistemas: `AudioProcessor`, `VideoRenderer`, `FileDecoder`.

**Tarea:**

Dibuja el **diagrama UML** de este diseño usando el patrón Facade.
 */

public class MediaPlayerFacade {
	private AudioProcessor audioProcessor;
	private VideoRenderer videoRenderer;
	private FileDecoder fileDecoder;

	public MediaPlayerFacade() {
		this.audioProcessor = new AudioProcessor();
		this.videoRenderer = new VideoRenderer();
		this.fileDecoder = new FileDecoder();
	}

	public void play(String fileName) {
		String decodedFile = fileDecoder.decode(fileName);
		audioProcessor.processAudio(decodedFile);
		videoRenderer.renderVideo(decodedFile);
	}
}