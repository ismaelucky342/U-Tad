public class Calculadora {
    public int sumar(int a, int b) {
        return a + b;
    }

    public double sumar(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        System.out.println(calc.sumar(2, 3)); // Llama al método con enteros
        System.out.println(calc.sumar(2.5, 3.5)); // Llama al método con dobles
    }
}