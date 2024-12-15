package astralis;

import java.util.Scanner;

public class JuegoEstrategia {
    private Jugador jugador;
    private int turnosRestantes;
	private String[] tiposNaves;

    // Constructor del juego, inicializando con un jugador y un número de turnos
    public JuegoEstrategia(int turnosIniciales) {
        this.jugador = new Jugador();
        this.turnosRestantes = turnosIniciales;
    }

    // Método para iniciar el juego
    public void iniciarJuego() {
        Scanner scanner = new Scanner(System.in);
        
        // Mensaje de bienvenida
        System.out.println("¡Bienvenido al juego de estrategia Astralis!");
        System.out.println("Tienes " + turnosRestantes + " turnos para gestionar tu base.");
        
        // Bucle principal del juego
        while (turnosRestantes > 0) {
            System.out.println("\nTurno " + (11 - turnosRestantes) + ":");
            mostrarMenu();
            try {
                // Solicitar al jugador que elija una opción
                int opcion = scanner.nextInt();
                
                // Ejecutar la acción elegida
                if (opcion == 3) {
                    // Si el jugador elige atacar, preguntar qué tipo de nave usar
                    System.out.println("Elige una nave para atacar:");
                    System.out.println("1. Carguero (Poder de ataque: 5, Counter: Caza)");
                    System.out.println("2. Acorazado (Poder de ataque: 15, Counter: Corveta)");
                    System.out.println("3. Corbeta (Poder de ataque: 10, Counter: Carguero)");
                    System.out.println("4. Caza (Poder de ataque: 8, Counter: Acorazado)");

                    int tipoNave = scanner.nextInt();
                    Nave naveSeleccionada = null;
                    switch (tipoNave) {
                        case 1:
                            naveSeleccionada = new Nave("Carguero", 5, "Caza");
                            break;
                        case 2:
                            naveSeleccionada = new Nave("Acorazado", 15, "Corveta");
                            break;
                        case 3:
                            naveSeleccionada = new Nave("Corbeta", 10, "Carguero");
                            break;
                        case 4:
                            naveSeleccionada = new Nave("Caza", 8, "Acorazado");
                            break;
                        default:
                            System.out.println("Selección inválida.");
                            continue;
                    }
                    jugador.agregarNave(naveSeleccionada);
                    System.out.println("Nave seleccionada: " + naveSeleccionada.getTipo());
                    
                    // Simulación de combate con el enemigo
                    simularCombate(jugador, naveSeleccionada);
                } else {
                    jugador.ejecutarAccion(opcion, null, null);
                }
                
                // Mostrar el estado del jugador al final de cada turno
                jugador.mostrarEstado();
                
                // Verificar si el juego ha terminado
                if (jugador.getDefensas() <= 0) {
                    System.out.println("¡Tu base ha sido destruida! El juego ha terminado.");
                    break;
                }
                if (jugador.getRecursos() <= 0) {
                    System.out.println("¡Se te han agotado los recursos! El juego ha terminado.");
                    break;
                }
            } catch (AccionInvalidaException e) {
                System.out.println("Error: " + e.getMessage());
            } catch (RecursoInsuficienteException e) {
                System.out.println("Error: " + e.getMessage());
            } catch (Exception e) {
                System.out.println("Ocurrió un error inesperado: " + e.getMessage());
            }
            
            // Reducir el número de turnos restantes
            turnosRestantes--;
        }
        
        // Fin del juego
        if (turnosRestantes == 0) {
            System.out.println("Se han agotado los turnos. El juego ha terminado.");
        }
        
        // Cerrar el scanner
        scanner.close();
    }

    // Método para mostrar las opciones del menú
    private void mostrarMenu() {
        System.out.println("Elige tu acción:");
        System.out.println("1. Recolectar recursos");
        System.out.println("2. Construir defensas");
        System.out.println("3. Atacar al enemigo");
        System.out.print("Elige tu acción (1-3): ");
    }
    
 // Método para simular el combate con el enemigo
    private void simularCombate(Jugador jugador, Nave naveSeleccionada) {
        // Generar una nave enemiga
        Nave enemigo = generarNaveEnemiga();

        // Mostrar detalles del combate
        System.out.println("Tu nave: " + naveSeleccionada.getTipo() + " (Poder de ataque: " + naveSeleccionada.getPoderDeAtaque() + ")");
        System.out.println("Nave enemiga: " + enemigo.getTipo() + " (Poder de ataque: " + enemigo.getPoderDeAtaque() + ")");

        // Determinar si el ataque tiene éxito
        if (naveSeleccionada.getCounter().equals(enemigo.getTipo())) {
            System.out.println("¡Tu nave es eficaz contra la nave enemiga!");
            // El jugador inflige daño
            enemigo.setPoderDeAtaque(enemigo.getPoderDeAtaque() - naveSeleccionada.getPoderDeAtaque());
            if (enemigo.getPoderDeAtaque() <= 0) {
                System.out.println("¡Has destruido la nave enemiga!");
            } else {
                System.out.println("La nave enemiga ha sobrevivido con poder de ataque: " + enemigo.getPoderDeAtaque());
            }
        } else {
            System.out.println("Tu nave no es eficaz contra la nave enemiga.");
            System.out.println("El enemigo lanza un contraataque...");
            // El enemigo inflige daño a la base del jugador
            jugador.setDefensas(jugador.getDefensas() - enemigo.getPoderDeAtaque());
            System.out.println("¡La base ha recibido " + enemigo.getPoderDeAtaque() + " de daño!");
        }

        // Agregar un mensaje para describir la acción del enemigo
        System.out.println("El enemigo ha analizado tu estrategia y ha elegido la nave: " + enemigo.getTipo() + 
            ". Su intención es " + (enemigo.getPoderDeAtaque() > 10 ? "dominar el campo de batalla con su poder ofensivo." : "resistir y contraatacar."));
    }

    // Método para generar una nave enemiga aleatoria
    private Nave generarNaveEnemiga() {
        setTiposNaves(new String[] {"Carguero", "Acorazado", "Corbeta", "Caza"});
        int tipoAleatorio = (int) (Math.random() * 4);
        
        switch (tipoAleatorio) {
            case 0:
                return new Nave("Carguero", 5, "Caza");
            case 1:
                return new Nave("Acorazado", 15, "Corveta");
            case 2:
                return new Nave("Corbeta", 10, "Carguero");
            case 3:
                return new Nave("Caza", 8, "Acorazado");
            default:
                return new Nave("Carguero", 5, "Caza");
        }
    }

	public String[] getTiposNaves() {
		return tiposNaves;
	}

	public void setTiposNaves(String[] tiposNaves) {
		this.tiposNaves = tiposNaves;
	}
}
