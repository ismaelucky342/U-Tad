# Model A

### **1. Tabla con los 10 patrones vistos (1 punto)**

**¿Qué te van a pedir?**

Una tabla como esta, donde tú clasifiques **diez patrones de diseño** de entre los vistos en clase según su tipo: **Creación, Estructura, Comportamiento**.

**Cómo se ve en el examen:**

Te dan algo así:

| Creación | Estructural | Comportamiento |
| --- | --- | --- |
| Singleton | Facade | Template Method |
| Factory Method | Adapter (objeto/clase) | Strategy |
| Abstract Factory | Decorator | State |
|  |  | Observer |

---

### **2. Tipos de uso del patrón Observer (0.5 puntos)**

**¿Qué te van a pedir?**

Redactar en una o dos frases **cuándo usarías el patrón Observer**.

**Cómo se ve en el examen:**

> Explica dos situaciones donde sea apropiado usar el patrón Observer.
> 

**Solución esperada:**

1. Cuando necesitas **monitorizar cambios en un modelo de datos** (por ejemplo, interfaz gráfica que se actualiza cuando cambia el modelo).
2. Cuando un objeto cambia su estado y otros objetos **dependen de ese cambio** pero **sin que el sujeto conozca quiénes son** (desacoplamiento).

---

### **3. Diagrama UML con patrón Decorator simple (2.5 puntos)**

**¿Qué te van a pedir?**

Un **diagrama de clases UML** para una situación concreta, aplicando el patrón **Decorator**.

**Cómo se ve en el examen:**

Te dan un contexto como:

> “Queremos una clase que represente un número, y otra que añada funcionalidades como comprobar si es primo.”
> 

**Solución esperada (ejemplo de clases en UML):**

```

          <<interface>>
        NumberComponent
               ^
               |
   -------------------------
   |                       |
NumberBaseComponent  <<abstract>>
                      NumberDecorator
                              ^
                              |
                 PrimeNumberDecorator

```

Debes mostrar la relación de herencia y composición del patrón Decorator.

---

### **4. Código a partir de clases UML (4 puntos)**

**¿Qué te van a pedir?**

A partir de un UML dado (por ejemplo, el de arriba), implementar desde cero algunas clases. Te pedirán que **hagas el código real** en Java (o el lenguaje que usen), siguiendo el patrón.

**Cómo se ve en el examen:**

1. Implementar **NumberBaseComponent** completa.
2. Implementar **parte de PrimeNumberDecorator**.
3. Implementar **parte del main** (instanciar decoradores, usar los métodos, etc.).


```java
// Clase base que representa un número simple
public class NumberBaseComponent {
    private int number;

    public NumberBaseComponent(int number) {
        this.number = number;
    }

    public int getNumber() {
        return number;
    }
}
```

---

```java
public class PrimeNumberDecorator {
    private NumberBaseComponent baseComponent;

    public PrimeNumberDecorator(NumberBaseComponent baseComponent) {
        this.baseComponent = baseComponent;
    }

    public int getNumber() {
        return baseComponent.getNumber();
    }

    // Método que verifica si el número es primo
    public boolean isPrime() {
        int num = baseComponent.getNumber();
        if (num < 2) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
```

---

```java
public class Main {
    public static void main(String[] args) {
        NumberBaseComponent number = new NumberBaseComponent(13);
        PrimeNumberDecorator primeNumber = new PrimeNumberDecorator(number);

        System.out.println("Número: " + primeNumber.getNumber());
        System.out.println("¿Es primo?: " + primeNumber.isPrime());
    }
}
```

### **5. Ejercicio sobre Adapter (2 puntos)**

**¿Qué te van a pedir?**

Te dan una clase **con errores o incompleta** que debería implementar el patrón **Adapter**. Tienes que:

- **Refactorizar** un método que ya está mal hecho.
- **Completar el código** para que el patrón Adapter funcione correctamente.

**Cómo se ve en el examen:**

Te dan algo como esto:

```java
public class OldSystem {
    public void doSomethingOld() {
        System.out.println("Doing it the old way");
    }
}

// Incompleto
public class Adapter {
    private OldSystem oldSystem;

    public void execute() {
        // ???
    }
}
```

Y tú tienes que:

1. Agregar constructor.
2. Implementar el método `execute()` correctamente.
3. Asegurarte de que el patrón Adapter esté bien aplicado.

**Solución esperada:**

```java
public class Adapter implements NewSystem {
    private OldSystem oldSystem;

    public Adapter(OldSystem oldSystem) {
        this.oldSystem = oldSystem;
    }

    @Override
    public void execute() {
        oldSystem.doSomethingOld();
    }
}
```