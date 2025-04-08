public class Projector {
    public void on() {
        System.out.println("Projector ON");
    }

    public void off() {
        System.out.println("Projector OFF");
    }
}

public class Screen {
    public void down() {
        System.out.println("Screen down");
    }

    public void up() {
        System.out.println("Screen up");
    }
}

public class SoundSystem {
    public void on() {
        System.out.println("Sound system ON");
    }

    public void setVolume(int level) {
        System.out.println("Volume set to " + level);
    }

    public void off() {
        System.out.println("Sound system OFF");
    }
}

public class VideoPlayer {
    public void play(String movie) {
        System.out.println("Playing movie: " + movie);
    }

    public void stop() {
        System.out.println("Stopping movie");
    }
}

public class HomeTheaterFacade {
    private Projector projector;
    private Screen screen;
    private SoundSystem sound;
    private VideoPlayer player;

    public HomeTheaterFacade(Projector projector, Screen screen, SoundSystem sound, VideoPlayer player) {
        this.projector = projector;
        this.screen = screen;
        this.sound = sound;
        this.player = player;
    }

    public void watchMovie(String movie) {
        System.out.println("Preparing to watch a movie...");
        screen.down();
        projector.on();
        sound.on();
        sound.setVolume(20);
        player.play(movie);
    }

    public void endMovie() {
        System.out.println("Shutting down movie...");
        player.stop();
        sound.off();
        projector.off();
        screen.up();
    }
}

public class Main {
    public static void main(String[] args) {
        // Crear los subsistemas
        Projector projector = new Projector();
        Screen screen = new Screen();
        SoundSystem sound = new SoundSystem();
        VideoPlayer player = new VideoPlayer();

        // Crear la fachada
        HomeTheaterFacade homeTheater = new HomeTheaterFacade(projector, screen, sound, player);

        // Usar la fachada
        homeTheater.watchMovie("The Matrix");
        System.out.println("... enjoying the movie 🍿");
        homeTheater.endMovie();
    }
}