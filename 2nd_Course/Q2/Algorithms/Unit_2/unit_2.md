# Capítulo 2: Algoritmos Recursivos

## Definición de Recursividad

Los algoritmos recursivos suponen una herramienta fundamental en la programación y el diseño de algoritmos. Se basan en la idea de resolver un problema dividiéndolo en subproblemas más pequeños de la misma naturaleza que el problema original. La recursividad se caracteriza por el hecho de que una función se llama a sí misma directa o indirectamente durante su ejecución. Es decir, un algoritmo es recursivo cuando el propio algoritmo se llama a sí mismo en algún punto (o varios puntos) de su código. 

Esa llamada se llama “llamada recursiva”. La recursividad es una forma más natural que la iteratividad de ver muchos algoritmos. Este método puede simplificar notablemente la solución de problemas complejos al dividirlos en casos más simples y manejables. En general, diremos que un objeto es recursivo si forma parte o se define a sí mismo (por ejemplo, animaciones o imágenes recursivas).

Dependiendo de cómo se realiza la auto-llamada (llamada recursiva), la recursión se clasifica en dos tipos: directa e indirecta.

### **Recursión Directa**

- La recursión directa ocurre cuando una función se llama a sí misma explícitamente dentro de su propio cuerpo.
    - Es la forma más sencilla y directa de recursión.
    - La función recursiva continúa llamándose a sí misma con un nuevo conjunto de argumentos hasta que se alcanza una condición de terminación o caso base, momento en el cual las llamadas recursivas comienzan a desenrollarse.
    - Ejemplo de recursión directa. Ver imagen.
    - En este ejemplo, la función factorial se llama a sí misma con el argumento n - 1, lo cual es un caso clásico de recursión directa.

![image.png](attachment:d3ffea83-0aa2-435d-a849-e458f008fbab:image.png)

### **Recursión indirecta**

- La recursión indirecta ocurre cuando una función se llama a sí misma pero no de manera directa, sino a través de una o varias funciones intermedias. Es decir, una función A llama a otra función B, que a su vez llama a la función A (o posiblemente a través de una cadena más larga de llamadas a funciones), creando un ciclo de llamadas entre las funciones.
    - Ejemplo de recursión indirecta. Ver imagen.
    - En este ejemplo, funcionA llama a funcionB, y funcionB a su vez llama a funcionA con un nuevo conjunto de argumentos. Este intercambio de llamadas entre funcionA y funcionB ilustra la recursión indirecta.

![image.png](attachment:f219905d-6c15-47b6-a04f-d198258717fd:image.png)

### Divide y vencerás

La recursividad sigue la estrategia de divide y vencerás para resolve problemas: 

- Se divide un problema en 2 o mas subproblemas y así sucesivamente
- Cada subproblema es de naturaleza similar al problema inicial pero cada subprolema es de tamaño menor que el inicial
- Se resuelve cada subproblema por separado y una vez resuelto combinan sus resultados para producir una solución común.

A menudo es más fácil realizar un programa recursivo que su equivalente iterativo porque muchas definiciones y problemas son de naturaleza recursiva, y, por lo tanto, convertirlos en un algoritmo recursivo es inmediato y sencillo.

Hay ciertas estructuras de datos que se definen recursivamente, como las listas, los árboles, o los grafos. Al ser recursivas, se manipulan muy fácilmente con algoritmos recursivos, por ejemplo, se puede ordenar una lista ordenando cada mitad por separado y luego juntando los resultados (algoritmo de ordenación quicksort).

El tipo de problemas que se pueden resolver es bastante amplio, y en general abarca a la gran mayoría de problemas de dimensión grande cuya solución se pueda plantear como la combinación de las soluciones de una serie de subproblemas similares al original. Por ejemplo:

- Factorial de un número: Un ejemplo clásico es el cálculo del factorial de un número, donde el factorial de n (denotado como n!) es el producto de todos los números enteros positivos desde 1 hasta n.
- Búsqueda binaria: Un algoritmo que divide el conjunto de búsqueda a la mitad en cada paso, buscando un elemento en una lista ordenada.
- Recorrido de estrucutras de datos:Los algoritmos para recorrer árboles (como el recorrido en preorden, inorden y postorden) o para explorar grafos (como la búsqueda en profundidad) se expresan de manera natural mediante recursividad.

### Ventajas de la Recursividad

El uso de recursividad en nuestros algoritmos plantea una serie de ventajas, como lo son:

- Simplicidad: La recursividad puede simplificar el código necesario para resolver problemas complejos, haciendo que sea más fácil de entender y mantener.
- Naturalidad en la solución: Muchos problemas, especialmente aquellos relacionados con estructuras de datos como árboles y grafos, se pueden describir y resolver de manera más natural con algoritmos recursivos.
- Facilidad de comprensión: Gracias a la recursividad, se pueden reducir algoritmos complejos a pocas líneas que son más fáciles de comprender por alguien externo a su desarrollo.

No obstante, también trae consigo algunas desventajas:

- Eficiencia: La recursividad puede ser menos eficiente en términos de uso de memoria y velocidad de ejecución en comparación con los enfoques iterativos, debido al overhead asociado con las llamadas de función.
- Riesgo de desbordamiento de pila: Si la profundidad de la recursión es demasiado grande, existe el riesgo de agotar el espacio disponible en la pila de llamadas de la función, lo que podría llevar a un desbordamiento de pila y, en consecuencia, a la terminación del programa.

### Esquema Básico

Los algoritmos recursivos siempre cuentan con una serie de características clave a identificar que lo definen. Estas son:

- Caso base: Todo algoritmo recursivo debe tener al menos un caso base, que es una condición que detiene la recursión. El caso base define el escenario más simple posible para el problema, para el cual se conoce la solución sin necesidad de más divisiones o llamadas recursivas.
- Llamada recursiva: Además del caso base, un algoritmo recursivo realiza una o más llamadas a sí mismo con diferentes argumentos, acercándose al caso base en cada iteración. Estas llamadas tienen el objetivo de descomponer el problema original en subproblemas más pequeños.
- Reducción del problema: En cada llamada recursiva, el tamaño del problema debe reducirse de alguna manera, acercándose al caso base. Esto asegura que la recursión eventualmente terminará, evitando ciclos infinitos.

Entonces, siguiendo estas características, podemos decir que un algoritmo recursivo siempre sigue un esquema similar:

- Primero, una condición «si...». Es la condición que decide si hacemos una llamada recursiva o salimos del apartado de la recursividad.
- Salida del algoritmo en el caso trivial, o lo que es lo mismo, cuando ya no necesitamos hacer una llamada recursiva para resolver el problema.
- En el caso no trivial, se «simplifica» el problema y se llama de nuevo al algoritmo con el problema simplificado como entrada.
- Primero, una condición «si...». Es la condición que decide si hacemos una llamada recursiva o salimos del apartado de la recursividad.
- Salida del algoritmo en el caso trivial, o lo que es lo mismo, cuando ya no necesitamos hacer una llamada recursiva para resolver el problema.ç
- En el caso no trivial, se «simplifica» el problema y se llama de nuevo al algoritmo con el problema simplificado como entrada.

Veamos de manera visual como quedaría el esquema general de un algoritmo recursivo:

![image.png](attachment:b5d72de7-e04b-42c0-8981-3d1f4247f251:image.png)

EJEMPLO 1: 

Cálculo del valor máximo y mínimo de un conjunto de elementos implementado por medio de un array de N elementos. Enfoque clásico:

![image.png](attachment:84405c6f-c910-46fe-acb9-0ea140dc041d:image.png)

Para poder pasar del enfoque clásico a la recursividad, tenemos que:

- Identificar el tamaño del problema resoluble:
- Si sólo tenemos 2 números a comparar, el máximo será el mayor y el mínimo el menor.
- Si sólo tenemos 1 número, éste será tanto el máximo como el mínimo.
- Determinar cómo dividir el problema original y en cuántas partes.
- Podemos dividir el array en 2 subarrays de “igual” tamaño.
- Combinar las soluciones parciales para obtener la solución total.
    - El máximo será el mayor valor de los máximos de ambos subarrays.
    - El mínimo será el menor valor de los mínimos de ambos subarrays.
- Veámoslo en imágenes:

![image.png](attachment:b6f5f72b-4545-41b0-a3cb-6e814dabbef8:image.png)

SOLUCIÓN: 

![image.png](attachment:b26daa9e-9a8e-4d4b-9f92-4bb824ae4457:image.png)

## Funcionamiento de la recursividad

Cuando desarrollamos un algoritmo que incluye recursividad, probar, demostrar o asegurarse de que funciona es sencillo. Basta con asegurarse de que se cumple todo lo siguiente:

- Tiene que existir una salida no recursiva del algoritmo (caso trivial)
    
    En el ejemplo anterior del factorial, cuando n es 0
    
    - En el ejemplo anterior del factorial, cuando n es 0
- Cada llamada recursiva se refiere a un problema más simple
    - La llamada recursiva se hace con n-1, más simple que si la hiciéramos con n. Si no, estaríamos generando un problema irresoluble después de varias llamadas recursivas…
- Suponiendo que las llamadas recursivas funcionan, el algoritmo debe de funcionar
    - En el factorial, si la llamada recursiva funciona y devuelve (n-1)!, entonces el algoritmo devuelve n!

### Programación Dinámica

La programación dinámica es otra técnica de diseño de algoritmos que se utiliza para resolver problemas de optimización. De manera similar a la recursividad, la programación dinámica se caracteriza por descomponer un problema complejo en subproblemas más pequeños. La diferencia radica en que la programación dinámica soluciona cada uno de estos subproblemas solo una vez, mientras que en la recursividad es complicado conseguir esto. Para hacerlo, en programación dinámica se van almacenando las soluciones a los subproblemas generalmente en una tabla o matriz para evitar el trabajo repetido. Esta estrategia es especialmente útil en problemas donde se observa una superposición de subproblemas, es decir, situaciones donde diferentes caminos para resolver el problema incluyen resolver los mismos subproblemas. La programación dinámica se basa en dos principios clave:

- **Optimalidad de subestructura**: Un problema exhibe una subestructura óptima si una solución al problema puede ser construida de manera eficiente a partir de soluciones de sus subproblemas. 
Esto implica que el problema puede ser dividido en subproblemas más pequeños, resolver estos subproblemas de manera independiente, y combinar sus soluciones para formar la solución al problema original.
- **Superposición de subproblemas:** Un problema tiene una superposición de subproblemas si al descomponer el problema en subproblemas, estos subproblemas no son independientes, es decir, se repiten múltiples veces. La programación dinámica almacena las soluciones de estos subproblemas en una estructura de datos (como una tabla) para que cada subproblema se resuelva una sola vez, ahorrando así una cantidad significativa de cálculo.

Tiene múltiples aplicaciones, como, por ejemplo:

- **PROBLEMA DE LA MOCHILA:** Dado un conjunto de ítems, cada uno con un peso y un valor, determinar la combinación de ítems a incluir en una mochila para que el valor total sea máximo y el peso no supere la capacidad de la mochila.
- **CAMINO MÍNIMO EN UN GRÁFICO:** Encontrar el camino de costo mínimo entre dos nodos en un gráfico, especialmente útil en redes de transporte o telecomunicaciones.
- **SECUENCIA COMÚN MÁS LARGA:** Determinar la longitud de la secuencia común más larga entre dos secuencias, una tarea común en bioinformática para comparar secuencias de ADN.

Existen dos enfoques principales en la programación dinámica:

- Top Down: Este enfoque sigue una estrategia recursiva pero almacena los resultados de los subproblemas en una estructura de datos (por ejemplo, un arreglo o un diccionario) para evitar cálculos repetidos.
- Bottom-up: Este enfoque llena una tabla de manera iterativa, resolviendo primero los subproblemas más pequeños y utilizando sus soluciones para construir soluciones a problemas más grandes. La tabulación comienza desde el caso base y avanza hasta llegar al problema original, asegurándose de que todos los subproblemas necesarios ya se hayan resuelto en el momento en que se necesiten.

Para ilustrar lo que es la programación dinámica, veamos el algoritmo recursivo para calcular el elemento i-ésimo de la sucesión de Fibonacci:

La sucesión de Fibonacci es una secuencia de números en la que cada número es la suma de los dos anteriores. Comienza con los números 0 y 1, y a partir de ahí, cada elemento de la secuencia se calcula como la suma de los dos elementos previos. Matemáticamente, se define de la siguiente manera:

- F(0)=0
- F(1)=1
- F(n)=F(n−1)+F(n−2) para n>1

Por lo tanto, los primeros términos de la sucesión de Fibonacci son:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Entonces, la versión recursiva surge de manera natural con la definición…

![image.png](attachment:3a640292-6110-450e-a1af-54df57f934ae:image.png)

Árbol de llamadas recursivas del cálculo recursivo del séptimo elemento de la serie de Fibonacci:

![image.png](attachment:11bdf521-7e8c-4a8e-b30b-0233bed9c351:image.png)

En el árbol de llamadas recursivas vemos que los mismos valores se calculan multitud de veces de forma redundante. Por lo tanto, la programación recursiva de Fibonacci es el ejemplo más típico de cuando no utilizar la recursión, ya que se calcula varias veces el mismo valor. Se soluciona con la “programación dinámica”:

- una vez calculada una solución, guardarla para su posible uso posterior
- Evitar calcular varias veces el mismo resultado, manteniendo una tabla de resultados conocidos

## Eficiencia de Algoritmos Recursivos

En los algoritmos no recursivos, el cálculo de la eficiencia de algoritmos es crucial para entender cómo su rendimiento afecta a las aplicaciones en términos de tiempo de ejecución y uso de memoria.

La eficiencia de un algoritmo se evalúa comúnmente a través de su complejidad temporal y espacial, que indica, respectivamente, cuánto tiempo tarda y cuánta memoria utiliza en función del tamaño de la entrada. Al analizar algoritmos recursivos, estos cálculos se vuelven especialmente necesarios debido a la naturaleza de las llamadas recursivas. 

Entonces, sabemos que, para estos algoritmos, igual que para los no recursivos, tendremos que estudiar la Complejidad Temporal (con su función de tiempo T(n)) y su Complejidad Espacial (con su función de memoria M(n)).

Tanto la T(n) como la M(n) de un algoritmo recursivo es una función/ecuación en recurrencia: 

- Una función en recurrencia es aquella que se incluye a si misma en su definición.
- Todas las funciones recurrentes tienen una o varias condiciones iniciales.

## Función de tiempo en algoritmos recursivos

La complegidad temporal de un algoritmo se refiere a como el tiempo de ejecucion cambia dependiendo del tamaño de entrada, para lo cual debemos considerar: 

- Número de llamadas recursivas: Cuántas veces el algoritmo se llama a sí mismo.
- Trabajo realizado en cada llamada: El tiempo que toma ejecutar el código dentro de la función antes de hacer la llamada recursiva y después de que la llamada recursiva retorna.
- Caso base: El tiempo que toma manejar el caso base, que no involucra ninguna llamada recursiva.

En el ejemplo clásico del cálculo recursivo del factorial de un número n:

![image.png](attachment:3812d81d-845a-4274-b15e-d47470f1b710:image.png)

Para el calculo de la complejidad temporal de este algoritmo observamos lo siguiente: 

Tenemos un **caso base:** cuando n es 0 o 1 tiene una complejidad constante, O(1) ya que devuelve un valor sin realizar ninguna operación adicional. 

Las **llamadas recursivas** por su parte funcionan de la siguiente forma, para cualquier otro valor de n el algoritmo realiza una única llamada recursiva con n - 1 y adicionalmente una multiplicación que también es O(1) en términos de complejidad temporal. 

El número de total de llamadas recursivas que se realizarán para calcular n! es n ya que cada llamada reduce el problema en una unidad (n - 1)(n -2)… hasta que alcanzamos el caso base. Por tanto podemos modelar la complejidad temporal del algoritmo como la suma de n operaciones de tiempo constante mas el tiempo constante del caso base. O(n). 

## Función de memoria en Algoritmos Recursivos

La **complejidad espacial** se refiere a la cantidad de memoria que utiliza un algoritmo durante su ejecución. En algoritmos recursivos, la complejidad espacial no solo incluye el espacio para las variables y datos utilizados sino también el espacio adicional en la pila de llamadas debido a las llamadas recursivas pendientes. 

Para ello tenemos en cuenta ciertos factores: 

- Profundidad de la Recursión: Siendo este el máximo numero de llamadas recursivas pendientes en cualquier momento.
- Espacio usado en cada llamada: Esto incluye tanto las variables locales como el espacio adicional necesario para la información de control de la llamada.

Cuánta memoria adicional usa el algoritmo recursivo para calcular el factorial de un número “n”?  Un algoritmo recursivo que realiza llamadas en profundidad lineal (n) tiene una complejidad espacial de O(n) debido al espacio necesario para cada llamada en la pila.

![image.png](attachment:facf84c6-8267-4999-9bdd-b380fe10e53f:image.png)

Para el calcular la complejidad espacial se observan los siguientes componentes, por un lado el Espacio para variables locales y parámetros siendo el espacio necesario para la variable local n y el espacio para el propio contexto de la llamada, que son contantes. Por otro lado el espacio en la pila de llamadas donde se almacena cada valor de n en cada llamada recursiva, habiendo un total de n + 1 llamadas en la pila en el peor de los casos.  

Por tanto la complejidad espacial del algoritmo se debe principalmente al espacio utilizado en la pila debido a llamadas de recursión dado que este espacio necesitamos q sea constante en cada llamada recursiva hay n + 1 llamadas en total para calcular n!. 

### Ejemplo 1 - Algoritmo Torres de Hanoi

![image.png](attachment:4283f0fc-99de-40ae-b0fe-657350fde9b0:image.png)

**Función de tiempo**

(Suponemos que mover un disco de un poste a otro es una operación elemental):

- Para analizar la complejidad temporal, observemos cómo crece el número de movimientos con respecto al número de discos n.
- En el paso 1, necesitamos mover n−1 discos al poste auxiliar. Esto se hace mediante una llamada recursiva y el número de movimientos necesarios para esto es T(n−1).
- El paso 2 implica un solo movimiento, por lo que es O(1).
- En el paso 3, necesitamos mover n−1 discos del poste auxiliar al poste destino. Esto también se realiza mediante una llamada recursiva y el número de movimientos necesarios es T(n−1) nuevamente.
- Por lo tanto, la relación de recurrencia para el número total de movimientos T(n) es:
    - T(n)=2T(n−1)+1 para n>=1

**Función de memoria adicional**

El análisis de la complejidad espacial para este algoritmo se centra en el uso de la pila de llamadas, ya que es el principal consumidor de memoria. Veamos los componentes principales que contribuyen a la complejidad espacial:

- Llamadas Recursivas: Cada llamada recursiva al algoritmo para mover los discos consume espacio en la pila. Este espacio se utiliza para almacenar los parámetros de la función (como el número de discos a mover y los postes de origen, destino y auxiliar), así como la dirección de retorno.
- Profundidad de la Recursión: La profundidad de la recursión, es decir, el número de llamadas recursivas activas en la pila en un momento dado, es un factor crítico en el uso de memoria. Para este problema, la profundidad de la recursión alcanza su máximo cuando se mueve el último disco, lo que implica una serie de llamadas recursivas para mover n-1 discos.
- Dado que el algoritmo resuelve el problema mediante la división en subproblemas más pequeños (mover n-1 discos primero al poste auxiliar, luego un disco al destino, y finalmente n-1 discos al destino), la profundidad máxima de la pila de llamadas corresponde a mover todos los discos, lo cual es n.
- M(0)=1
- M(n)=M(n-1)+1 para n>=1.

### Ejemplo 2 - Algoritmo de Fibonacci

![image.png](attachment:74b96b0b-1b59-42be-a997-69fb2031f8c7:image.png)

**Función del tiempo**

La relación de recurrencia para el tiempo de ejecución T(n) del cálculo recursivo de Fibonacci se puede definir como:

- **Caso base:** T(0)=T(1)=O(1), ya que obtener F(0) o F(1) es directo y no requiere llamadas recursivas adicionales.
- **Relación de recurrencia:** Para n>1, cada llamada a F(n) requiere dos llamadas a F(n−1) y F(n−2), más el tiempo para sumar los resultados de esas dos llamadas. Si asumimos que el tiempo para realizar la suma es constante, la relación de recurrencia se puede expresar como T(n)=T(n−1)+T(n−2)+O(1). Para comprender cómo crece T(n), podemos observar que:
    - Para n=2, hay dos llamadas a F(1) y F(0), por lo tanto, T(2)=2O(1)+O(1).
    - Para n=3, se requieren llamadas a F(2) y F(1), lo que implica T(3)=T(2)+T(1)+O(1).
    - Siguiendo esta relación de recurrencia, es evidente que el número de llamadas crece exponencialmente con n. Esto se debe a la naturaleza de la definición de Fibonacci, donde el cálculo de F(n) depende del cálculo de todos los términos anteriores hasta F(1) y F(0).
    - Dada la relación de recurrencia T(n)=T(n-1)+T(n-2)+O(1), es claro que el tiempo de ejecución crece exponencialmente. Sin resolver explícitamente la relación de recurrencia, podemos decir que T(n) es de orden exponencial, específicamente O(2n), lo cual indica que el tiempo de ejecución dobla con cada incremento unitario de n.

**Función de memoria adicional**

El análisis se centra en el número máximo de llamadas a la función que están activas al mismo tiempo en la pila de llamadas:

- **Caso Base:** Para n=0 o n=1, la función no realiza llamadas recursivas y solo ocupa un espacio constante en la pila de llamadas para esa única llamada.
- **Llamadas Recursivas:** Para n>1, cada llamada a la función **Fibonacci(n)** produce dos llamadas recursivas adicionales: una para **Fibonacci(n-1)** y otra para **Fibonacci(n-2).** Sin embargo, es crucial notar que estas llamadas no se expanden en paralelo. Es decir, la función **Fibonacci(n-1)** se ejecuta y completa, devolviendo su resultado antes de que se ejecute **Fibonacci(n-2).** Esto significa que la complejidad espacial no se duplica con cada paso. En cambio, la complejidad espacial está dictada por la longitud de la "rama" más larga de la recursión, que corresponde a la secuencia de llamadas desde **Fibonacci(n)** hasta llegar al caso base. La profundidad máxima de la pila de llamadas recursivas, por lo tanto, es proporcional a n, ya que la "ruta" más larga desde la llamada inicial hasta el caso base involucra hacer una serie de llamadas decrecientes hasta llegar a 0 o 1. Entonces, podemos concluir:
    - M(0)=1
    - M(1)=1
    - M(n)=M(n-1) para n>=2 y suponiendo que M(n-1) >= M(n-2)

## Cálculo de la **complejidad**

La obtención de la complejidad de un algoritmo recursivo, al igual que hacemos con los algoritmos no recursivos, implica analizar cómo el tiempo de ejecución (complejidad temporal) o el uso de memoria (complejidad espacial) cambia en función del tamaño de la entrada. No obstante, este proceso puede ser más complejo que el análisis de algoritmos no recursivos debido a la naturaleza de las llamadas recursivas. De una función en recurrencia no siempre podemos obtener directamente su complejidad, por lo cual tenemos que convertirla en una función no recurrente:

- Es decir, una función que no dependa de sí misma
- A partir de la función no recurrente equivalente ya podríamos obtener su O(…) según las reglas vistas.