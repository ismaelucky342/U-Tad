## Introducción a las Listas

En programación definimos las listas como una secuencia finita que puede contener cero o más elementos, todos pertenecientes a un mismo tipo, inicialmente consideramos a todas las listas como homogéneas lo cual implica que todos sus elementos comparten el mismo tipo de datos. Aunque existe la posibilidad de trabajar con listas heterogéneas lo que puede permitir listas dentro de listas.

El tamaño de una lista se denota como n y representa la cantidad de elementos que contiene, además ocasionalmente hacemos referencia a la capacidad de la lista que indica el tamaño máximo que esta puede llegar a alcanzar.  

### Implementación y Tipos de Lista

La implementación de una lista puede seguir dos enfoques principales, por un lado la forma contigua que consiste en almacenar los elementos uno detrás de otro en la memoria con lo cual la capacidad puede ser estática o dinámica, conocemos a estas listas contiguas normalmente como arrays o vectores.

```cpp
    int arr[5] = {1, 2, 3, 4, 5};
```

Por otra parte tenemos las listas no contiguas basadas en los punteros, en las cuales cada elemento contiene un puntero al siguiente elemento en la secuencia permitiendo una estructura no contigua de memoria. Estas listas son conocidas como listas enlazadas y su capacidad no es relevante puesto que puede acomodar elementos sin restricciones.  

```cpp
struct Node {
    int data;
    Node* next;
};
```

Las representaciones enlazadas tienen una desventaja principal que radica en su acceso indexado pero a su vez presentan una ventaja en operaciones de modificación siempre y cuando se posicione el punto adecuado sin requerir desplazar elementos. 

Este enfoque implica que aunque el acceso a elementos específicos pueda ser menos eficiente en comparación a los arrays, la capacidad de realizar de manera eficaz modificaciones es crucial en ciertos escenarios. 

## Listas Contiguas

En las listas contiguas, los elementos se almacenan de manera consecutiva en la memoria, organizados según su posición en la secuencia. Al emplear punteros en lugar de arrays estáticos, se obtiene la capacidad de modificar dinámicamente el tamaño de la lista, ya sea ampliándolo o reduciéndolo según sea necesario. Este ajuste dinámico en la memoria reservada para la lista se puede lograr mediante la función `realloc()` en el lenguaje de programación C.

Esta capacidad de reconfiguración dinámica es una característica distintiva de las listas contiguas, permitiendo una gestión más flexible y eficiente del espacio en memoria utilizado por la estructura de datos.

El mecanismo de ampliación o disminución de memoria reservada, implementado a través de la función “realloc”, se desglosa en tres casos específicos:

### Caso 1 (Mejor Caso) - Ampliación con Memoria Disponible

Si hay memoria libre contigua a la ya reservada, el sistema simplemente amplía la zona de memoria existente sin necesidad de copiar los datos. Este es el caso más eficiente.

**Ejemplo en C++ usando `std::vector`:**

```cpp
cpp

#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.reserve(7);  // Se intenta ampliar sin reubicar si hay espacio contiguo disponible

    std::cout << "Capacidad después de reservar: " << vec.capacity() << 
    std::endl;
    return 0;
}
```

- **Complejidad Temporal:** O(1) si la ampliación es contigua.
- **Complejidad Espacial:** No se usa memoria extra, solo se extiende.

---

### Caso 2 (Peor Caso) - Ampliación sin Memoria Disponible

Si no hay memoria libre contigua, el sistema asigna una nueva zona, copia los datos y libera la anterior, lo que implica un mayor costo.

**Ejemplo en C++:**

```cpp
cpp

#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.reserve(1000);  // Si no hay espacio contiguo, se copia a una nueva ubicación

    std::cout << "Capacidad después de reservar: " << vec.capacity() << 
    std::endl;
    return 0;
}
```

- **Complejidad Temporal:** O(n) en el peor caso (se copian todos los elementos).
- **Complejidad Espacial:** Puede requerir hasta el doble de memoria temporalmente.

---

### Caso 3 - Disminución de Memoria

Reducir la memoria reservada es una operación eficiente, ya que solo indica al sistema que la memoria reservada ahora termina antes.

**Ejemplo en C++:**

```cpp
cpp

#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.shrink_to_fit();  // Reduce la capacidad al tamaño actual

    std::cout << "Capacidad después de reducir: " << vec.capacity() << std::endl;
    return 0;
}  
```

- **Complejidad Temporal:** O(1).
- **Complejidad Espacial:** O(1), ya que solo se reduce la memoria utilizada.

### Insertar, eliminar e implementar

**1. Problema del solapamiento de memoria**

Cuando se copian datos en memoria que se solapan, el uso de `memcpy()` puede provocar corrupción de datos, ya que no maneja correctamente la superposición.

**Ejemplo de problema con `memcpy()`**

```cpp
cpp

#include <iostream>
#include <cstring>

int main() {
    char str[] = "123456";
    std::memcpy(str + 1, str, 5);  // No maneja solapamiento correctamente
    std::cout << str << std::endl; // Salida inesperada
    return 0;
}
```

Esto puede producir resultados erróneos, ya que `memcpy()` no previene la sobreescritura de datos antes de copiarlos.

**2. Uso de `memmove()` para manejar solapamiento**

La función `memmove()` maneja el solapamiento copiando primero los datos a una ubicación temporal.

**Ejemplo con `memmove()`**

```cpp
cpp

#include <iostream>
#include <cstring>

int main() {
    char str[] = "123456";
    std::memmove(str + 1, str, 5);  // Maneja solapamiento correctamente
    std::cout << str << std::endl; // Salida esperada: "112345"
    return 0;
}
```

Aquí, `memmove()` evita el problema copiando de manera segura.

---

**Insertar un elemento en la posición `i` en un array dinámico**

Al insertar un elemento, pueden ocurrir dos casos:

1. **Ampliación de la capacidad** (caso peor: `O(n)`)
2. **Desplazamiento de elementos a la derecha** (`O(n)`)
3. **Inserción del nuevo elemento** (`O(1)`)

**Ejemplo de inserción en un `std::vector` (maneja memoria automáticamente)**

```cpp
cpp

#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.insert(vec.begin() + 2, 99);  // Insertar 99 en la posición 2

    for (int num : vec) {
        std::cout << num << " ";
    }
    return 0;
}
// Salida: 1 2 99 3 4 5
```

**Ejemplo con un array dinámico manual**

```cpp
cpp

#include <iostream>
#include <cstring>

void insertar(int*& arr, int& capacidad, int& size, int i, int valor) {
    if (size == capacidad) { // Necesita redimensionar
        int nuevaCapacidad = capacidad * 2;
        int* nuevoArr = new int[nuevaCapacidad];
        std::memcpy(nuevoArr, arr, size * sizeof(int));
        delete[] arr;
        arr = nuevoArr;
        capacidad = nuevaCapacidad;
    }

    std::memmove(arr + i + 1, arr + i, (size - i) * sizeof(int));
    arr[i] = valor;
    size++;
}

int main() {
    int capacidad = 5, size = 5;
    int* arr = new int[capacidad]{1, 2, 3, 4, 5};

    insertar(arr, capacidad, size, 2, 99);  // Insertar 99 en la posición 2

    for (int i = 0; i < size; i++)
        std::cout << arr[i] << " ";

    delete[] arr;
    return 0;
}
// Salida: 1 2 99 3 4 5
```

---

**Eliminar un elemento en la posición `i`**

Cuando se elimina un elemento, los elementos a la derecha deben desplazarse a la izquierda.

1. **Desplazamiento a la izquierda** (`O(n)`)
2. **Disminución de la capacidad** (`O(1)`)

**Ejemplo con `std::vector`**

```cpp
cpp

#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.erase(vec.begin() + 2);  // Eliminar el elemento en la posición 2

    for (int num : vec) {
        std::cout << num << " ";
    }
    return 0;
}
// Salida: 1 2 4 5
```

**Ejemplo con array dinámico**

```cpp
cpp

#include <iostream>
#include <cstring>

void eliminar(int*& arr, int& size, int i) {
    std::memmove(arr + i, arr + i + 1, (size - i - 1) * sizeof(int));
    size--;
}

int main() {
    int size = 5;
    int* arr = new int[size]{1, 2, 3, 4, 5};

    eliminar(arr, size, 2);  // Eliminar el elemento en la posición 2

    for (int i = 0; i < size; i++)
        std::cout << arr[i] << " ";

    delete[] arr;
    return 0;
}
// Salida: 1 2 4 5
```

---

**Acceso a un elemento en la posición `i`** (`O(1)`)

El acceso es directo y tiene una complejidad constante.

```cpp
cpp

#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = {10, 20, 30, 40, 50};

    int i = 2;
    std::cout << "Elemento en la posición " << i << ": " << vec[i] << std::endl;

    return 0;
}
// Salida: Elemento en la posición 2: 30
```