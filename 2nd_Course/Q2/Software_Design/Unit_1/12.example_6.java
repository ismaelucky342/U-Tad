/**7.a To design the previous musical instruments, we want to increase the abstraction of the Instrument class by changing it from an abstract class to an interface. Apply the change to the affected elements and verify that the MusicTest class still works. */

public abstract class Instrument {
	abstract void play(Note n);
	abstract String what(){
		return "Instrument";
	}
	abstract void adjust();
}

public interface Instrument {
	void play(Note n);
	String what();
	void adjust();
}

public class Wind implements Instrument {
	public void play(Note n) {
		System.out.println("Wind.play() " + n);
	}

	public String what() {
		return "Wind";
	}

	public void adjust() {
		System.out.println("Adjusting Wind");
	}
}

public class Percussion implements Instrument {
	public void play(Note n) {
		System.out.println("Percussion.play() " + n);
	}

	public String what() {
		return "Percussion";
	}

	public void adjust() {
		System.out.println("Adjusting Percussion");
	}
}

public class Stringed implements Instrument {
	public void play(Note n) {
		System.out.println("Stringed.play() " + n);
	}

	public String what() {
		return "Stringed";
	}

	public void adjust() {
		System.out.println("Adjusting Stringed");
	}
}
