public class Coche {
    private Motor motor;
    public Coche() {
        motor = new Motor();
    }
    
    class Motor {
        public void encender() {
            System.out.println("Motor encendido");
        }
    }
    public void arrancar() {
        motor.encender();
        System.out.println("Coche en marcha");
    }
    public static void main(String[] args) {
        Coche miCoche = new Coche();
        miCoche.arrancar();
    }
}