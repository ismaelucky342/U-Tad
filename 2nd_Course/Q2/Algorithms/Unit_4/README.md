# Algoritmos Sencillos de Ordenación

Aunque sencillos en su implementación, los siguientes algoritmos que se presentan son fundamentales para resolver casos sencillos de ordenación de datos. Nos permiten comprender los principios subyacentes de la ordenación de datos y establecer una base sólida para abordar los algoritmos más complejos que veremos en las secciones posteriores.

El objetivo principal es familiarizarnos con tres algoritmos de ordenación clásicos: Inserción, Selección y Burbuja. Para cada uno de ellos seguiremos el mismo guion: 

- Son iterativos empleando dos bucles anidados
- Logran ordenar listas contiguas en un tiempo de complejidad O(n`2)
- En el caso de las listas no contiguas el tiempo de ejecución intuitivamente sería O3 pero podemos reducirlo a O2
- Su complejidad es constante O1 independientemente del tipo de lista que estemos ordenando


## Algoritmo de Inserción

El algoritmo de inserción es uno de los algoritmos de ordenación más simples. Su enfoque se asemeja a la manera en que comúnmente ordenamos cartas de una baraja en nuestras manos: insertamos cada elemento en su posición correcta en relación con los elementos ya ordenados.

*“Este algoritmo es ideal para pequeñas cantidades de datos o para listas que ya están parcialmente ordenadas a un proceso creador.”*

Veamos a continuación como sería paso a paso el funcionamiento del algoritmo:

- Comenzamos con el segundo elemento de la lista y lo consideramos como el primer elemento “ordenado”.
- Luego, tomamos el siguiente elemento y lo “insertamos” en la parte ordenada de la lista, desplazando los elementos mayores hacia la derecha para hacer espacio.
- Continuamos este proceso hasta que todos los elementos estén en su lugar correcto.

Veamos con un ejemplo cuales serían los pasos:

- Consideremos la lista [5, 2, 4, 6, 1, 3]:
- Empezamos con el segundo elemento, el 2, y lo insertamos en su posición correcta entre el 5 y el 2.
- El siguiente elemento es el 4. Lo insertamos entre el 2 y el 5, obteniendo [2, 4, 5, 6, 1, 3].
- Procedemos de manera similar con los siguientes elementos hasta que la lista esté completamente ordenada.

**Pseudocódigo:**

```agda
Para i desde 1 hasta longitud(lista) - 1:
    valor_actual = lista[i]
    j = i - 1
    Mientras j sea mayor o igual a 0 y lista[j] sea mayor que valor_actual:
        lista[j + 1] = lista[j]
        j = j - 1
    Fin mientras
    lista[j + 1] = valor_actual
Fin para
```

**Implementación (Código en C):**

```c
#include <stdio.h>

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        /* Mover los elementos del array arr[0..i-1], que son
           mayores que el valor de la llave, 
           a una posición adelante de su posición actual */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
```

### **Eficiencia Temporal**

El algoritmo de inserción tiene una complejidad temporal de O(n^2) en el peor caso y en el caso promedio. Esto se debe a que, en el peor escenario, cuando la lista está en orden inverso, cada elemento debe ser comparado y movido hasta su posición correcta, lo que lleva a un número total de comparaciones y movimientos proporcional a la suma de los primeros n números naturales.

En el mejor caso, cuando la lista ya está ordenada, el algoritmo requiere solo O(n) comparaciones y ningún movimiento, ya que cada elemento es mayor que el elemento que le precede.

### **Eficiencia Espacial**

El algoritmo de inserción tiene una eficiencia espacial constante, O(1). Esto se debe a que la cantidad de espacio adicional requerido no depende del tamaño de la entrada, sino que es constante y depende únicamente de la cantidad de variables adicionales utilizadas por el algoritmo, que en este caso son variables enteras y un arreglo.

El algoritmo de inserción es simple y eficiente en términos de espacio, pero puede ser ineficiente para listas grandes en términos de tiempo debido a su complejidad cuadrática. Sin embargo, para listas pequeñas o parcialmente ordenadas, puede ser una opción viable debido a su simplicidad y su eficiencia lineal en el mejor caso.

## Algoritmo de Selección

El algoritmo de selección es otro método simple pero efectivo para ordenar una lista de elementos. Su enfoque se basa en seleccionar repetidamente el elemento más pequeño (o más grande, dependiendo del orden deseado) de la lista no ordenada y colocarlo al principio (o al final) de la lista ordenada.

*“Aunque puede no ser tan eficiente como algunos otros algoritmos para grandes conjuntos de datos, es fácil de entender y de implementar.”*

### **Funcionamiento**

Veamos a continuación como sería paso a paso el funcionamiento del algoritmo:

- Seleccionamos el elemento más pequeño (o más grande) de la lista no ordenada.
- Intercambiamos este elemento con el primer elemento de la lista no ordenada.
- Repetimos este proceso para el resto de la lista, excluyendo los elementos ya ordenados.

### **Ejemplo**

Veamos con un ejemplo cuales serían los pasos:

- Consideremos la lista [5, 2, 4, 6, 1, 3]:
- Buscamos el elemento más pequeño, que es 1, y lo colocamos al principio de la lista: [1, 2, 4, 6, 5, 3].
- Luego, encontramos el siguiente elemento más pequeño, que es 2, y lo colocamos en la segunda posición: [1, 2, 4, 6, 5, 3].
- Continuamos este proceso hasta que todos los elementos estén ordenados.

**Pseudocódigo**: 

```agda
Para i desde 0 hasta longitud(lista) - 1:
    minimo_index = i
    Para j desde i + 1 hasta longitud(lista) - 1:
        Si lista[j] < lista[minimo_index]:
            minimo_index = j
    Fin para
    Si minimo_index != i:
        Intercambiar(lista[i], lista[minimo_index])
Fin para
```

**C:** 

```c
#include <stdio.h>

void swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionSort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        swap(&arr[min_idx], &arr[i]);
    }
}
```

El algoritmo de selección tiene una complejidad temporal de O(n^2) en todos los casos, ya que siempre debe recorrer toda la lista para encontrar el elemento mínimo en cada iteración.

### **Eficiencia Temporal**

El algoritmo de selección realiza n-1 comparaciones en la primera iteración, n-2 comparaciones en la segunda iteración, y así sucesivamente hasta la penúltima iteración. Esto da como resultado un total de (n-1) + (n-2) + ... + 2 + 1 = n(n-1)/2 comparaciones en el peor caso, lo que resulta en una complejidad temporal de O(n^2).

Aunque el número de comparaciones no cambia en los diferentes casos, el número de intercambios puede variar:

- En el peor caso, puede haber n-1 intercambios.
- En el mejor caso puede no haber intercambios (cuando la lista ya está ordenada).

### **Eficiencia Espacial**

El algoritmo de selección realiza todas sus operaciones en el mismo array de entrada, sin utilizar estructuras de datos adicionales. Por lo tanto, su complejidad espacial es constante y pequeña, es decir, O(1). Esto significa que no importa cuán grande sea el tamaño de la entrada, el algoritmo de selección siempre requerirá la misma cantidad de memoria adicional.

Aunque el algoritmo de selección no es tan eficiente como algunos otros algoritmos de ordenación, tiene la ventaja de ser simple y fácil de implementar. Es útil en situaciones donde la claridad del código es prioritaria sobre la eficiencia temporal (fácil mantenimiento). Además, para conjuntos de datos pequeños o parcialmente ordenados, el rendimiento del algoritmo de selección puede ser aceptable. Aunque tiene una complejidad temporal cuadrática, su complejidad espacial constante lo hace atractivo en ciertas situaciones.

## Algoritmo de Burbuja

El algoritmo de burbuja es uno de los algoritmos de ordenación sencillos más conocidos. Su nombre proviene del hecho de que los elementos más grandes "burbujean" gradualmente hacia la parte superior de la lista como lo harían las burbujas en un líquido en ebullición. Aunque no es eficiente en términos de tiempo para grandes conjuntos de datos, es útil para enseñar conceptos básicos de algoritmos de ordenación y para listas de tamaño pequeño o parcialmente ordenadas.

### **Funcionamiento**

Veamos a continuación como sería paso a paso el funcionamiento del algoritmo:

- Comparamos cada par adyacente de elementos en la lista y los intercambiamos si están en el orden incorrecto.
- Repetimos este proceso hasta que no haya más intercambios necesarios, lo que indica que la lista está ordenada.

### **Ejemplo**

Veamos con un ejemplo cuales serían los pasos:

- Consideremos la lista [5, 2, 4, 6, 1, 3]:
- Comenzamos comparando 5 y 2. Como 5 es mayor que 2, los intercambiamos: [2, 5, 4, 6, 1, 3].
- Continuamos comparando y moviendo elementos hasta que la lista esté completamente ordenada.

**Pseudocódigo:** 

```agda
Para i desde 0 hasta longitud(lista) - 1:
    Para j desde 0 hasta longitud(lista) - i - 1:
        Si lista[j] > lista[j + 1]:
            Intercambiar(lista[j], lista[j + 1])
Fin para
```

**C:**

```c
#include <stdio.h>

void swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(int arr[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        // Ultimos i elementos ya están en su lugar correcto
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}
```

El algoritmo de burbuja tiene una complejidad temporal de O(n^2) en el peor caso, donde n es el número de elementos en la lista. Esto se debe a que, en el peor escenario, se deben hacer comparaciones y posiblemente intercambios para cada par de elementos en la lista.

### **Eficiencia Temporal**

El algoritmo de burbuja tiene una complejidad temporal de O(n^2) en el peor caso, el caso promedio y el mejor caso. Esto se debe a que el algoritmo debe comparar y posiblemente intercambiar cada par de elementos en la lista en cada una de las n-1 iteraciones externas.

En cada iteración, el algoritmo recorre la lista desde el primer elemento hasta el último elemento no ordenado, lo que implica n-1, n-2, n-3, ..., 1 comparaciones e intercambios respectivamente. La suma de estos números es igual a (n-1)(n-2)/2, lo cual resulta en una complejidad cuadrática.

Aunque el algoritmo de burbuja tiene una complejidad temporal cuadrática, puede ser eficiente para pequeños conjuntos de datos y para listas que ya están casi ordenadas, ya que requiere menos intercambios en esos casos.

### **Eficiencia Espacial**

El algoritmo de burbuja realiza todas sus operaciones en el mismo arreglo de entrada, sin requerir estructuras de datos adicionales. Por lo tanto, su complejidad espacial es constante y pequeña, es decir, O(1). Esto significa que no importa cuán grande sea el tamaño de la entrada, el algoritmo de burbuja siempre requerirá la misma cantidad de memoria adicional.

A pesar de su simplicidad y facilidad de implementación, el algoritmo de burbuja no es eficiente para grandes conjuntos de datos debido a su complejidad temporal cuadrática. Sin embargo, como con el resto de los algoritmos sencillos vistos en este apartado de la unidad, puede ser útil en situaciones donde el tamaño de los datos es pequeño o cuando se necesita un algoritmo simple.

## Otros algoritmos simples

Aunque pueden no ser tan conocidos como los algoritmos básicos que hemos discutido antes, los que se presentan en este apartado son igualmente efectivos y pueden ser una herramienta valiosa en el arsenal de un programador. Nos centraremos simplemente en introducirlos y describirlos para disponer de una “navaja suiza” más amplia:

**Ordenación por sacudida (Cocktail Sort)**

El algoritmo de ordenación por sacudida es una variante del algoritmo de burbuja que busca minimizar el número de pasadas a través del arreglo. Funciona de manera similar al algoritmo de burbuja, pero en lugar de mover el elemento más grande hacia arriba en cada pasada y el más pequeño hacia abajo, el algoritmo de sacudida realiza pasadas alternas hacia adelante y hacia atrás a través del arreglo, intercambiando los elementos que están fuera de lugar.

**Ordenación por inserción binaria**

Este algoritmo mejora el algoritmo de inserción tradicional al utilizar una búsqueda binaria para encontrar la posición correcta de cada elemento que se inserta en la lista ordenada. Esto reduce la cantidad de comparaciones necesarias en comparación con el algoritmo de inserción tradicional, lo que puede conducir a una mejora significativa en la eficiencia, especialmente para listas grandes.

**Ordenación por montículos (Heap Sort)**

El algoritmo de ordenación por montículos utiliza una estructura de datos llamada montículo (heap) para organizar los elementos de la lista. Aunque es más complejo de entender e implementar que los algoritmos de inserción, selección y burbuja, tiene una complejidad temporal similar de O(n log n) y puede ser más eficiente en la práctica para grandes conjuntos de datos.

# Algoritmos de Ordenación Avanzados

Se presentan los que serán los dos algoritmos principales, MergeSort y QuickSort, que ofrecen una mejora significativa en términos de eficiencia temporal en comparación con sus contrapartes más simples.

Hablaremos sobre el funcionamiento interno de estos algoritmos, comprendiendo cómo aprovechan diferentes estrategias y técnicas para lograr una ordenación rápida y a la vez más eficiente que los algoritmos ya vistos. Exploraremos también sus complejidades temporales y espaciales, así como sus fortalezas y limitaciones en diferentes escenarios de aplicación.

## MergeSort

El algoritmo MergeSort es un método de ordenación basado en el principio de dividir para hacer el problema más pequeño (¿te suena eso a algo de las unidades pasadas…?). Es un algoritmo conocido por su eficiencia y estabilidad en la clasificación de grandes conjuntos de datos.

*"MergeSort divide repetidamente la lista no ordenada en mitades iguales hasta que cada sublista contenga un solo elemento, luego fusiona estas sublistas en orden ascendente hasta obtener la lista ordenada completa.”*

### **Funcionamiento**

Veamos a continuación como sería paso a paso el funcionamiento del algoritmo:

- Se divide la lista original en dos sublistas de tamaño parecido
- Se ordena cada sublista por separado (recursividad)
- Se mezclan/combinan las dos sublistas (cada una de ellas ya está ordenada).
    - Mezclar o combinar es:
        - Comparar el primer elemento de la primera sublista con el primer elemento de la segunda sublista.
        - El menor de los dos lo ponemos en la lista resultado y lo quitamos de la sublista en donde lo hemos encontrado.
        - Repetimos los tres pasos anteriores hasta que una de las sublistas quede vacía.
- Finalmente copiamos en el resultado lo que queda en la sublista no vacía.

A la hora de mezclar listas contiguas hay dos opciones:

- Espacio adicional O(n) para guardar la lista resultado en una lista temporal en cada paso, tiempo O(n).
- Espacio adicional O(1), tiempo O(n). Intentamos ahorrarnos el crear una lista resultado temporal. Esto se puede hacer, pero el resultado sería un algoritmo bastante complicado que no siempre tiene sentido

Si estamos aplicando el MergeSort sobre una lista enlazada, su mezcla tiene una complejidad espacial de O(1) y la temporal es O(n).

- La complejidad espacial es O(1) porque cada vez que ponemos un nodo más en la lista resultado, lo hemos quitado de una de las sublistas de origen. Gracias a esto no necesitamos espacio adicional, lo que hace al MergeSort un buen algoritmo en términos de eficiencia para ordenar listas enlazadas.

### **Ejemplo**

Veamos con un ejemplo cuales serían los pasos:

- Consideremos la lista [38, 27, 43, 3, 9, 82, 10]:
- Dividimos la lista en dos mitades: [38, 27, 43] y [3, 9, 82, 10].
- Recursivamente, ordenamos cada mitad: [27, 38, 43] y [3, 9, 10, 82].
- Seguiríamos dividiendo hasta solo tener un elemento…
- Fusionamos las dos mitades ordenadas: [3, 9, 10, 27, 38, 43, 82].

### **Pseudocódigo:**

```agda
algoritmo ordenar
entrada lista l
salida lista l

si longitud(l) > 1 entonces
    dividir l en dos sublistas l1 y l2
    ordenar l1
    ordenar l2
    combinar l1 y l2 en l
```

**C:**

```c
#include <stdio.h>
#include <stdlib.h>

// Función para combinar dos subarreglos ordenados en un solo arreglo ordenado
void merge(int arr[], int l, int m, int r) {
    int i, j, k; // Índices para recorrer los subarreglos y el arreglo combinado
    int n1 = m - l + 1; // Tamaño del primer subarreglo
    int n2 = r - m;     // Tamaño del segundo subarreglo

    // Crear arreglos temporales para almacenar los subarreglos
    int L[n1], R[n2];

    // Copiar los datos de los subarreglos alos arreglos temporales L[] y R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Mezclar los arreglos temporales L[] y R[] en el arreglo original arr[]
    i = 0; // Índice inicial del primer subarreglo
    j = 0; // Índice inicial del segundo subarreglo
    k = l; // Índice inicial del arreglo combinado

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copiar los elementos restantes del primer subarreglo, si hay alguno
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copiar los elementos restantes del segundo subarreglo, si hay alguno
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Función principal de ordenamiento por mezcla (merge sort)
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        // Encontrar el punto medio del arreglo
        int m = l + (r - l) / 2;

        // Ordenar recursivamente la primera mitad
        mergeSort(arr, l, m);
        // Ordenar recursivamente la segunda mitad
        mergeSort(arr, m + 1, r);

        // Mezclar las dos mitades ordenadas
        merge(arr, l, m, r);
    }
}
```

### **Complejidad Temporal**

El algoritmo MergeSort tiene una complejidad temporal de O(n log n) en todos los casos (peor caso, mejor caso y caso promedio). Esta complejidad temporal se debe a la naturaleza del algoritmo, que divide recursivamente la lista en mitades hasta que cada sublista contiene un solo elemento, y luego fusiona estas sublistas en orden ascendente.

- División en mitades: Cada vez que el algoritmo divide la lista en dos mitades, toma O(log n) operaciones, ya que el tamaño de la lista se reduce a la mitad en cada iteración.
- Fusión de sublistas: La fusión de dos sublistas ordenadas toma O(n) operaciones, ya que se comparan y se colocan los elementos de ambas sublistas en la lista final.
- La complejidad temporal de O(n log n) de MergeSort lo convierte en uno de los algoritmos de ordenación más eficientes, especialmente para grandes conjuntos de datos.

Veamos paso a paso como llegamos aquí:

- Partir la lista es simplemente calcular su punto medio: O(1) en contiguas y O(n) en enlazadas.
- Tenemos que ordenar cada parte de forma recursiva, por lo tanto, tardamos 2 veces T(n/2).
- La mezcla es O(n)
- Por lo tanto, tenemos que MergeSort tiene una función de tiempo:
    - T(n) = 1 + 2*T(n/2) + n +1 en contiguas
    - T(n) = n + 2*T(n/2) + n +1 en enlazadas
- Operando, nos queda O(n·logn) en ambas.

### **Complejidad Espacial**

MergeSort requiere espacio adicional para almacenar las sublistas durante el proceso de división y fusión. En el peor caso, esta complejidad espacial es O(n), donde n es el número de elementos en la lista, debido a las llamadas recursivas y la creación de sublistas temporales durante la fusión. Vamos paso a pasa para ver como llegamos a esto:

- Partir la lista es O(1) en cualquier tipo de lista:
    1. En contiguas sólo hay que recordar dónde acaba el primer trozo y donde empieza el segundo.
    2. En enlazadas tenemos que mover los nodos de un lugar a otro. Para ello, cada vez que insertemos un elemento en una sublista, lo eliminamos de la lista original.
- Hacemos dos llamadas recursivas. Como cuando hacemos la segunda ya hemos terminado la primera, la máxima memoria que necesitamos es M(n/2)
- Combinar:
    - En listas contiguas es O(1) o O(n), respectivamente con mezcla eficiente (necesitamos un algoritmo de mezcla más complejo) o mezcla sencilla usando memoria adicional.
    - En listas enlazadas es siempre O(1) porque movemos los nodos de un lugar a otro. De nuevo, cada vez que insertemos un elemento desde una sublista a la lista total, lo eliminamos de la sublista de origen.
- Por lo tanto:
    - En listas contiguas con mezcla eficiente: M(n)=1+M(n/2)+n E O(n)
    - En listas contiguas sin mezcla eficiente: M(n)=1+M(n/2) E O(lgn)
    - En listas enlazadas M(n)=1+M(n/2) E O(lgn)

Aunque MergeSort es menos eficiente en términos de espacio que algunos otros algoritmos de ordenación, es más estable y predecible, lo que lo hace ideal para grandes conjuntos de datos y aplicaciones en tiempo real. Su complejidad temporal de O(n log n) lo convierte en una opción atractiva para aplicaciones donde la eficiencia es importante.

## Algoritmo de QuickSort

El algoritmo QuickSort es otro método de ordenación basado en la estrategia de "dividir para conquistar" (ahora sabemos que esto significa recursividad ¿no?). Es conocido por su eficiencia y amplio uso en la práctica debido a su rendimiento promedio muy rápido y su implementación sencilla.

### **Funcionamiento**

La diferencia entre MergeSort y QuickSort es cómo se divide la lista y cómo se mezcla.

**¿Cómo se divide la lista en dos?**

- Se toma un elemento como pivote. Veremos cómo elegirlo. De momento, podemos pensar que el pivote es un elemento cualquiera (el primero, el del medio, etc.).
- Se reparten el resto de elementos en dos listas, una con los menores que el pivote y otra con los mayores que el pivote.
- También discutiresmos que hacer cuando los números son iguales.

Por lo tanto, mezclar (una vez ordenada cada sublista) es sólo poner una sublista a continuación de otra, pues todos los elementos de la primera son menores que todos los elementos de la segunda.

### **Ejemplo**

Veamos con un ejemplo cuales serían los pasos:

- Consideremos la lista [38, 27, 43, 3, 9, 82, 10]:
- Seleccionamos el pivote, por ejemplo, 27.
- Reorganizamos la lista de manera que los elementos menores que 27 estén antes y los mayores después, obteniendo [9, 3, 10, 27, 38, 43, 82].
- Aplicamos recursivamente QuickSort en las sublistas antes y después del pivote hasta que toda la lista esté ordenada.

**Pseudocódigo:** 

```agda
función quickSort(arreglo, bajo, alto):
    si bajo < alto entonces:
        // Particionar el arreglo y obtener el índice del pivote
        pivote = particionar(arreglo, bajo, alto)

        // Ordenar recursivamente las sublistas izquierda y derecha
        quickSort(arreglo, bajo, pivote - 1)
        quickSort(arreglo, pivote + 1, alto)
    fin si
fin función

función particionar(arreglo, bajo, alto):
    // Seleccionar el último elemento como pivote
    pivote = arreglo[alto]

    // Inicializar el índice del elemento más pequeño
    i = bajo - 1

    // Iterar a través del arreglo desde 'bajo' hasta 'alto - 1'
    para j desde bajo hasta alto - 1 hacer:
        // Si el elemento actual es menor o igual que el pivote
        si arreglo[j] <= pivote entonces:
            // Incrementar el índice del elemento más pequeño
            i = i + 1

            // Intercambiar arreglo[i] y arreglo[j]
            intercambiar(arreglo[i], arreglo[j])
        fin si
    fin para

    // Intercambiar el pivote con el elemento en la posición correcta
    intercambiar(arreglo[i + 1], arreglo[alto])

    // Devolver el índice del pivote
    devolver i + 1
fin función

función intercambiar(a, b):
    temporal = a
    a = b
    b = temporal
fin función
```

**C:** 

```c
#include <stdio.h>

// Función para intercambiar dos elementos de un arreglo
void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// Función para dividir el arreglo y poner el pivote en su posición correcta
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // seleccionamos el último elemento como pivote
    int i = (low - 1); // indice del elemento más pequeño

    for (int j = low; j <= high - 1; j++) {
        // Si el elemento actual es más pequeño o igual que el pivote
        if (arr[j] <= pivot) {
            i++; // incrementamos el índice del elemento más pequeño
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

// Función recursiva que implementa el algoritmo QuickSort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Particionamos el arreglo
        int pi = partition(arr, low, high);

        // Ordenamos las sublistas recursivamente
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

QuickSort es un algoritmo de ordenación eficiente y ampliamente utilizado debido a su rendimiento promedio muy rápido y su implementación simple. Aunque tiene una complejidad temporal de peor caso de O(n^2), este escenario raramente se presenta en la práctica y se puede mitigar con estrategias de selección de pivote inteligentes. Veamos un estudio detallado de su eficiencia temporal y espacial.

### **Complejidad Temporal**

El análisis de la eficiencia temporal del algoritmo QuickSort se divide en tres casos: el mejor caso, el caso promedio y el peor caso.

- Mejor caso: En el mejor caso, QuickSort tiene una complejidad temporal de O(n log n). Esto ocurre cuando en cada partición el pivote divide el arreglo en dos subarreglos de igual tamaño.
- Caso promedio: En el caso promedio, QuickSort también tiene una complejidad temporal de O(n log n). Esto se debe a que, en promedio, el pivote divide el arreglo en subarreglos de tamaño proporcional.
- Peor caso: En el peor caso, QuickSort puede tener una complejidad temporal de O(n^2). Esto ocurre cuando en cada partición el pivote seleccionado es el elemento más pequeño o grande, dividiendo el arreglo en un subarreglo de tamaño n-1 y otro de tamaño 0, lo que hace que el algoritmo se convierta en una versión ineficiente de sí mismo similar al algoritmo de ordenamiento por inserción. Sin embargo, este escenario es poco probable con una implementación adecuada y selección inteligente del pivote, como seleccionar un pivote aleatorio o el método de la mediana de tres.

Veamos un estudio detallado de esto:

- En el mejor caso: el pivote elegido siempre reparte equitativamente los elementos en dos sublistas de igual tamaño:
    - T(n) = 2T(n/2) + n + 1 si elegir pivote es O(1)
    - T(n) = 2T(n/2) + 2n + 1 si elegir pivote es O(n)
    - El resultado en ambos es O(nlogn)
- En el peor caso: el pivote elegido siempre reparte mal los elementos: una sublista se queda con un elemento (y por lo tanto no hace falta ordenarla), y la otra con n-1. Entonces:
    - T(n) = T(n-1) + n + 1 si elegir pivote es O(1)
    - T(n) = T(n-1) + 2n + 1 si elegir pivote es O(n)
    - El resultado en ambos es O(n2)

En el caso medio (no lo calculamos), QuickSort es O(nlogn)

### **Complejidad Espacial**

En cuanto a la eficiencia espacial, QuickSort requiere un espacio adicional para almacenar el estado de la recursión en la pila de llamadas. La complejidad espacial del algoritmo QuickSort es O(log n) en el peor caso, donde n es el número de elementos en el arreglo. Esto se debe a que la profundidad máxima de la pila de llamadas recursivas es logarítmica en relación con el tamaño del arreglo.

Veamos un estudio detallado paso a paso de la eficiencia temporal:

- Elegir el pivote es siempre O(1)
- Partición es O(1) siempre:
    - En listas contiguas, con el algoritmo que vimos
    - En listas enlazadas, porque movemos los nodos a una sublista o a otra. Cada vez que insertemos un elemento en una sublista, lo eliminamos de la lista origen.
- Las llamadas recursivas:
    - Usan M(n/2) en el mejor caso (las dos sublistas tienen el mismo tamaño), igual que en MergeSort.
    - Usan M(n-1) en el peor caso (una de las sublistas tiene n-1 elementos y la otra 1).
- La combinación es O(1)
- Por lo tanto, tenemos:
    - Mejor caso: M(n)=1+M(n/2) E O(lgn) (como en MergeSort)
    - Peor caso: M(n)=1+M(n-1) E O(n)
- En el caso medio (no lo calculamos), es O(lgn)

Aunque QuickSort requiere un espacio adicional en la pila de llamadas debido a la recursión, este espacio adicional es mínimo y no depende directamente del tamaño del arreglo. En general, la eficiencia espacial del algoritmo QuickSort es muy buena.

- QuickSort es un algoritmo de ordenamiento muy eficiente con un rendimiento promedio y en el mejor caso de O(n log n), lo que lo hace adecuado para una amplia gama de aplicaciones.
- Aunque en el peor caso QuickSort puede tener una complejidad temporal de O(n^2), este escenario es poco probable con una implementación adecuada y selección inteligente del pivote.
- En cuanto a la eficiencia espacial, QuickSort requiere un espacio adicional en la pila de llamadas debido a la recursión, pero este espacio es mínimo y no depende directamente del tamaño del arreglo.

## **Comparación cuantitativa de los dos algoritmos**

Tiempo en el peor caso:

- MergeSort es O(nlogn)
- QuickSort es O(n2)

Tiempo en el mejor caso:

- MergeSort es O(nlogn)
- QuickSort es O(nlogn), con constantes ocultas mejores que las del MergeSort (no lo calculamos) si la elección del pivote es O(1) y si n es muy grande
- Cuando n es pequeño, QuickSort es peor que MergeSort e incluso peor que los algoritmos básicos de ordenación (insercción, selección, burbuja, etc.)

Tiempo en el caso medio:

- MergeSort es O(nlogn)
- QuickSort es O(nlogn), con constantes ocultas mejores que las del MergeSort (no lo calculamos) si la elección del pivote es O(1) y si n es muy grande
- Cuando n es pequeño, QuickSort es peor que MergeSort e incluso peor que los algoritmos básicos de ordenación (insercción, selección, burbuja, etc.)

Por lo tanto, en cuestión de eficiencia temporal, QuickSort es el mejor algoritmo general de ordenación de todos los que existen, para el caso medio y cuando n es grande.

# Otros algoritmos de ordenación

Además de los algoritmos básicos y avanzados que ya hemos discutido, existen otras técnicas y estrategias de ordenación que vale la pena conocer y comprender.

Examinaremos algunos algoritmos menos convencionales, pero igualmente relevantes, incluyendo aquellos que se basan en principios de paralelismo y técnicas de ordenación con rango. Se presentarán varios algoritmos, aunque no entraremos en tanto detalle como en los algoritmos ya presentados en esta unidad.

## Ordenación paralela

El paralelismo es una técnica que permite ejecutar partes de un algoritmo simultáneamente para acelerar su procesamiento. Los algoritmos de ordenación paralela aprovechan esta técnica para distribuir la carga de trabajo entre múltiples procesadores, lo que puede resultar en una ordenación mucho más rápida. No todos los algoritmos se pueden paralelizar, pero MergeSort es un ejemplo de un algoritmo que se puede paralelizar. La fórmula de tiempo de ejecución de MergeSort cambia cuando se paraleliza, lo que indica una mejora en la eficiencia.

**Algoritmo de Ordenación Paralela Bitonic**

El algoritmo de ordenación paralela Bitonic es un método eficiente para ordenar elementos en paralelo. Se basa en la idea de realizar una serie de comparaciones "bitónicas" en una secuencia de elementos. A través de un proceso de fusión iterativo, los elementos son comparados y reordenados de acuerdo con un patrón predefinido. El algoritmo Bitonic es particularmente adecuado para implementaciones en hardware paralelo, como GPUs.

**Algoritmo de Ordenación Paralela Odd-Even Transposition**

El algoritmo de ordenación paralela Odd-Even Transposition es otro enfoque eficiente para la ordenación de datos en paralelo. Este algoritmo divide la lista en sublistas de tamaño fijo y realiza operaciones de intercambio de elementos en paralelo en sublistas adyacentes. A través de una serie de fases de comparación e intercambio, los elementos son gradualmente ordenados en la lista.

**Algoritmo de Ordenación Paralela de Malla**

El algoritmo de ordenación paralela de malla, también conocido como algoritmo de ordenación de malla bidimensional, organiza los elementos en una estructura de malla y utiliza múltiples procesadores para realizar operaciones de comparación e intercambio en paralelo a lo largo de las filas y columnas de la malla. Este enfoque distribuido permite una alta eficiencia en sistemas paralelos.

## Ordenación por rango

El algoritmo de ordenación por rango, también conocido como Bucket Sort, divide el rango de valores posibles en un número finito de contenedores (buckets) y luego distribuye cada elemento del arreglo original en el bucket correspondiente. Una vez que todos los elementos han sido asignados a los buckets, se aplica un algoritmo de ordenación adicional (generalmente un algoritmo de ordenación por inserción) para ordenar los elementos dentro de cada bucket. 

Finalmente, los elementos ordenados en cada bucket se combinan para obtener el arreglo finalmente ordenado.

### **Veamos un ejemplo de aplicación práctica de esto:**

Ordenar los 10 elementos de la lista (1, 3, 5, 4, 1, 3, 3, 1, 5, 3), sabiendo que cada uno de sus elementos estarán en el rango [0,5].

- Creamos el array “contadores”, con tamaño 6 (amplitud del rango).
    1. Tiempo O(1)
    2. Espacio O(n)
- Inicializamos cada posición de “contadores” a 0. Nos queda contadores = (0, 0, 0, 0, 0, 0)
    1. Tiempo O(1) porque el array siempre mide 5, independientemente de lo grande que sea n
    2. Espacio O(1)
- Contamos las veces que cada número aparece en la lista y lo anotamos en “contadores”. Para ello recorremos la lista, y cada vez que, por ejemplo, veamos un “3”, incrementaremos en una unidad la posición 3 de “contadores”. Por tanto, “contadores” queda con (0, 3, 0, 4, 1, 2).
    1. Tiempo O(n), porque estamos recorriendo la lista y haciendo operaciones elementales por cada elemento.
    2. Espacio O(1).
- Recorremos “contadores” y vamos poniendo en la lista original tantos números iguales como nos diga cada casilla de contadores. Por lo tanto, la lista queda con (1, 1, 1, 3, 3, 3, 3, 4, 5, 5)
    1. Tiempo O(n), porque recorremos la lista para modificar cada elemento de esta según lo que nos vaya diciendo “contadores”.
    2. Espacio O(1)

### **¿Cuándo podemos usar este tipo de ordenación y por lo tanto conseguir la estupenda complejidad temporal de O(n)?**

Cuando se cumplan todos los requisitos siguientes:

- Cada componente de la lista a ordenar está comprendido en un rango definido.
- Además, el rango tiene que ser discreto. Es decir, la cantidad de posibles números dentro del rango tiene que ser finita. Por ejemplo, no puede ser un rango de números reales.
- Cuando nos sobran grandes porciones de memoria contigua, para poder reservar el array “contadores”.

La ordenación por rango es particularmente efectiva cuando los elementos del conjunto original están uniformemente distribuidos dentro de un rango limitado de valores. Además, este enfoque es altamente paralelizable, lo que lo hace adecuado para su implementación en sistemas distribuidos y paralelos. Bucket Sort se utiliza a menudo como un paso previo en algoritmos más complejos de ordenación externa y en técnicas de ordenación distribuida.

## Listas ordenadas

Las **listas ordenadas** son estructuras de datos fundamentales que **mantienen sus elementos en un orden específico**, ya sea **ascendente o descendente**. A diferencia de otras estructuras como arreglos o listas enlazadas, una lista ordenada **garantiza** que los elementos estén siempre dispuestos según un criterio de ordenación definido.

### **Implementaciones de Listas Ordenadas**

Existen diversas maneras de implementar una lista ordenada, cada una con características y ventajas particulares. Las más comunes son:

**a) Lista enlazada ordenada**

- Utiliza nodos enlazados para almacenar los elementos de manera ordenada.
- La búsqueda es **O(n)** porque se realiza de forma secuencial.
- La inserción es **O(n)** porque hay que recorrer la lista para encontrar la posición adecuada.
- Es eficiente si hay muchas **búsquedas** y pocas **inserciones/eliminaciones**.

**b) Árbol de búsqueda binaria (BST - Binary Search Tree)**

- Los nodos están organizados de manera que el valor de un nodo es mayor que el de su hijo izquierdo y menor que el de su hijo derecho.
- La búsqueda, inserción y eliminación tienen un tiempo medio de **O(log n)** si el árbol está equilibrado.
- Puede volverse ineficiente si el árbol se desbalancea, llegando a **O(n)** en el peor caso.

**c) Árbol AVL**

- Es un tipo de BST que **se equilibra automáticamente** para evitar que la profundidad crezca demasiado.
- Asegura que la búsqueda, inserción y eliminación siempre sean **O(log n)**.
- Es más eficiente que un BST simple, pero requiere operaciones adicionales para mantener el balance.

### **Operaciones en Listas Ordenadas**

Las listas ordenadas admiten diversas operaciones, manteniendo el orden de los elementos.

**a) Búsqueda**

- Si la lista es **contigua (array ordenado)**, se puede usar **búsqueda binaria** con complejidad **O(log n)**.
- Si la lista es **enlazada**, la búsqueda debe ser **secuencial**, con complejidad **O(n)**.

**b) Inserción**

- **Lista contigua desordenada**: Insertar un elemento toma **O(n)** porque puede ser necesario desplazar elementos.
- **Lista contigua ordenada**:
    - **Búsqueda de la posición correcta**: **O(log n)** (búsqueda binaria).
    - **Inserción en la posición encontrada**: **O(n)** (desplazamiento de elementos).
    - **Tiempo total**: **O(n)**, aunque con mayores constantes ocultas que en una lista desordenada.
- **Lista enlazada desordenada**:
    - **Buscar la posición**: **O(n)** (recorrido de la lista).
    - **Insertar el nodo**: **O(1)** (ajuste de punteros).
    - **Tiempo total**: **O(n)**.
- **Lista enlazada ordenada**:
    - **Buscar la posición**: **O(n)** (recorrido secuencial).
    - **Insertar el nodo**: **O(1)** (ajuste de punteros).
    - **Tiempo total**: **O(n)**, con constantes ocultas similares a la versión desordenada.

**c) Eliminación**

- Similar a la inserción, ya que es necesario buscar el elemento antes de eliminarlo.
- En una **lista contigua ordenada**, es **O(n)** debido al desplazamiento de elementos.
- En una **lista enlazada ordenada**, es **O(n)** debido a la búsqueda secuencial, pero la eliminación en sí toma **O(1)**.

### **Ventajas y Desventajas de Mantener una Lista Ordenada**

**¿Cuándo es útil una lista ordenada?**

- Si recorremos la lista **frecuentemente** para **imprimir sus elementos en orden**.
- Si necesitamos encontrar el **mínimo o el máximo rápidamente** (por ejemplo, en una **cola de prioridad**).
- Si hacemos **muchas búsquedas y pocas inserciones/eliminaciones**, porque la búsqueda en una lista ordenada puede ser más rápida que en una desordenada.

**Comparación de complejidades**

| Tipo de lista | Búsqueda en ordenada | Búsqueda en desordenada |
| --- | --- | --- |
| **Lista contigua (array)** | **O(log n)** | **O(n)** |
| **Lista enlazada** | **O(n)** | **O(n)** |

A cambio de mantener el orden, **las inserciones y eliminaciones requieren más trabajo** en listas ordenadas, especialmente en listas contiguas.

### **Aplicaciones y Casos de Uso**

Las listas ordenadas son fundamentales en diversas áreas de la informática:

**a) Bases de datos**

- Mantener los **índices** de las tablas ordenados para **acelerar las consultas**.

**b) Algoritmos de búsqueda y ordenación**

- Se utilizan como **paso intermedio** en algoritmos de búsqueda y ordenación eficientes.

**c) Implementación de estructuras de datos avanzadas**

- Se usan en la implementación de **conjuntos y mapas ordenados**, optimizando la búsqueda y recuperación de elementos.