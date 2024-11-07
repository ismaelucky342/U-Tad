public class Example_operators {
    public static void main(String[] args) {
        // Operadores aritméticos
        int a = 10;
        int b = 5;
        int suma = a + b;
        int producto = a * b;
        
        // Operadores relacionales y lógicos
        boolean esMayor = a > b;  // true
        boolean esIgual = (a == b) || (a == 10);  // true

        // Operador unario
        int negativo = -a;  // -10

        // Operadores de asignación
        a += 2;  // a = a + 2, ahora a = 12

        // Operador condicional
        String resultado = (a > b) ? "a es mayor" : "b es mayor";  // "a es mayor"

        // Operador instanceof
        String texto = "Hola";
        boolean esString = texto instanceof String;  // true

        // Incremento
        int i = 0;
        int preIncremento = ++i;  // preIncremento = 1, i = 1
        int postIncremento = i++;  // postIncremento = 1, i = 2

        // Imprimir resultados
        System.out.println("Suma: " + suma);
        System.out.println("Producto: " + producto);
        System.out.println("Es mayor: " + esMayor);
        System.out.println("Es igual: " + esIgual);
        System.out.println("Valor negativo: " + negativo);
        System.out.println("Resultado: " + resultado);
        System.out.println("¿Es String?: " + esString);
        System.out.println("Pre-incremento: " + preIncremento);
        System.out.println("Post-incremento: " + postIncremento);
    }
}
