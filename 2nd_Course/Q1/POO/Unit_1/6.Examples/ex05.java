import java.util.Scanner; 

public class ex05 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in); 
        char respuesta = 's'; 
        while (respuesta == 's') {
                System.out.print("Introduce un numero entero positivo: \n");
                int n = scanner.nextInt();
                int suma = 0; 
                for(int i = 1; i <= n; i++){
                    suma += i; 
                }
                System.out.println("la suma de los primeros " + n + " numeros enteros es " + suma); 
                System.out.print("desea continuar?: (s/n): \n");
                respuesta = scanner.next().charAt(0); 

            }
            scanner.close();
        }
    }


