# Test Unidad 5: Análisis de Redes Sociales con Python

## 1. Teoría de Grafos

**1.** ¿Qué es un grafo?
 A) Una representación visual de datos
 B) Un par (V, E) donde V son nodos y E son aristas
 C) Un tipo de base de datos
 D) Un archivo de imagen

**2.** ¿Qué es un nodo en teoría de grafos?
 A) Un error
 B) Una conexión entre elementos
 C) Un vértice o entidad individual
 D) Un archivo

**3.** ¿Qué es una arista?
 A) Un tipo de gráfico
 B) Una conexión o relación entre dos nodos
 C) Una unidad de medida
 D) Un tipo de dato

**4.** ¿Qué es una red social?
 A) Solo Facebook e Instagram
 B) Un grafo donde nodos son actores y aristas son relaciones
 C) Un servidor
 D) Un protocolo de internet

**5.** ¿Por qué es importante Social Network Analysis (SNA) en ingeniería de software?
 A) No es importante
 B) Permite modelar interacciones complejas y detectar patrones
 C) Solo para marketing
 D) Para crear redes sociales

**6.** ¿Cuál es una aplicación práctica de SNA?
 A) Crear sitios web
 B) Identificar influencers, detectar anomalías, sistemas de recomendación
 C) Compilar código
 D) Gestionar bases de datos

**7.** ¿Qué es la Teoría de Grafos?
 A) El estudio de datos visualles
 B) Rama matemática que modela relaciones con nodos y aristas
 C) Un tipo de compilador
 D) Un protocolo

**8.** ¿Cuáles son los componentes principales de un grafo?
 A) Solo nodos
 B) Nodos y aristas
 C) Dirección y peso
 D) Nombre y descripción

**9.** ¿Cómo se representa un arista no dirigida?
 A) (u,v) con dirección
 B) (u,v) sin dirección; la relación es bidireccional
 C) Solo u
 D) Una línea punteada

**10.** ¿Cómo se representa una arista dirigida?
 A) (u,v) bidireccional
 B) <u,v> indicando dirección de u a v
 C) Una línea recta
 D) Un círculo

---

## 2. Tipos de Redes

**11.** ¿Qué es una red no dirigida?
 A) Una red que no tiene inicio
 B) Relaciones bidireccionales (como amistades en Facebook)
 C) Una red rota
 D) Una red sin estructura

**12.** ¿Qué es una red dirigida?
 A) Una red con dirección física
 B) Relaciones con sentido específico (como seguir en Twitter)
 C) Una red ordenada
 D) Una red con GPS

**13.** ¿Qué es una red ponderada?
 A) Una red pesada
 B) Aristas con pesos que representan intensidad de relación
 C) Una red con mucha datadensidad
 D) Una red sin conexiones

**14.** ¿Qué es una red bipartita?
 A) Una red con 2 nodos
 B) Nodos divididos en 2 conjuntos disjuntos, conexiones solo entre grupos
 C) Una red repartida
 D) Una red duplicada

**15.** ¿Cuál es un ejemplo de red bipart​ita?
 A) Amistades en Facebook
 B) Usuarios y productos en e-commerce
 C) Seguidores en Twitter
 D) Correos en Enron

**16.** ¿Qué es multigrafo?
 A) Múltiples grafos separados
 B) Un grafo con múltiples aristas entre los mismos nodos
 C) Un grafo muy grande
 D) Un grafo sin estructura

**17.** ¿Qué es un grafo conexo?
 A) Un grafo conectado al internet
 B) Existe un camino entre cualquier par de nodos
 C) Un grafo organizado
 D) Un grafo pequeño

**18.** ¿Qué es un componente desconectado?
 A) Un nodo sin conexión
 B) Un subgrafo donde nodos están conectados pero aislados del resto
 C) Una red rota
 D) Un archivo perdido

**19.** ¿Qué es un ciclo en un grafo?
 A) Una vuelta en el tiempo
 B) Un camino que comienza y termina en el mismo nodo
 C) Una conexión circular
 D) Un tipo de error

**20.** ¿Qué es un árbol en teoría de grafos?
 A) Una estructura biológica
 B) Un grafo conexo y acíclico
 C) Un tipo de archivo
 D) Una planta

---

## 3. Propiedades de Redes

**21.** ¿Qué es el grado de un nodo?
 A) Su importancia en la red
 B) El número de conexiones que tiene
 C) Su ubicación
 D) Su edad

**22.** ¿Qué es in-degree?
 A) El grado hacia adentro
 B) El número de aristas que llegan a un nodo
 C) Un tipo de medicación
 D) Una medida de latitud

**23.** ¿Qué es out-degree?
 A) Fuera del grado
 B) El número de aristas que salen de un nodo
 C) Un equivalente a in-degree
 D) Una medida de altitud

**24.** ¿Qué es densidad de una red?
 A) Peso total de la red
 B) Proporción de conexiones posibles que existen
 C) Número total de nodos
 D) Tamaño físico

**25.** ¿Cuál es la fórmula básica de densidad?
 A) n/(n-1)
 B) m/(n*(n-1)/2) para no dirigidas
 C) n + m
 D) sqrt(m/n)

**26.** ¿Qué significa una densidad cercana a 1?
 A) La red está muy dispersa
 B) La red está muy interconectada
 C) La red tiene un nodo
 D) Error en cálculo

**27.** ¿Qué es el diámetro de un grafo?
 A) Su tamaño físico
 B) La máxima distancia (número de saltos) entre cualquier par de nodos
 C) El número de aristas
 D) El número de nodos

**28.** ¿Qué es distancia entre nodos?
 A) La distancia física
 B) El número mínimo de aristas para ir de un nodo a otro
 C) Una medida de disimilitud
 D) El peso total

**29.** ¿Qué es centralidad de grado?
 A) El grado de un nodo
 B) Una medida de importancia basada en número de conexiones
 C) La ubicación central
 D) El promedio de grados

**30.** ¿Qué es centralidad de intermediación?
 A) Estar en el medio
 B) Medida de cuán importante es un nodo como "puente" entre otros
 C) Un tipo de cálculo
 D) Una medida de distancia

---

## 4. El Caso Enron

**31.** ¿Qué fue Enron?
 A) Un banco
 B) Una empresa energética que colapsó por fraude contable
 C) Un software
 D) Un protocolo

**32.** ¿Cuándo se declaró Enron en bancarrota?
 A) 1995
 B) 2000
 C) Diciembre 2001
 D) 2005

**33.** ¿Por qué es importante el dataset de Enron?
 A) No es importante
 B) Contiene correos reales que permiten analizar redes corporativas
 C) Es un caso de éxito
 D) Demuestra fraude positivo

**34.** ¿Qué información contiene el dataset de Enron?
 A) Transacciones bancarias
 B) Correos electrónicos internos entre empleados
 C) Contabilidad
 D) Documentos legales

**35.** ¿Cuál es el valor académico del caso Enron?
 A) Enseña matemáticas
 B) Permite estudiar dinámicas de comunicación en una empresa real
 C) Es entretenimiento
 D) No tiene valor

**36.** ¿Cómo se puede modelar Enron como red?
 A) Solo tablas
 B) Nodos = empleados, aristas = comunicación por email
 C) Como una sola línea
 D) No es posible

**37.** ¿Qué insights se pueden obtener del caso Enron?
 A) El color de los uniformes
 B) Patrones comunicacionales, identificar clusters de empleados
 C) La ubicación física
 D) Nada importante

**38.** ¿Dónde se obtiene el dataset de Enron?
 A) En Enron.com
 B) En Kaggle u otros repositorios públicos
 C) Solo en papers académicos
 D) No es público

**39.** ¿Qué limpieza se requiere en los datos de Enron?
 A) Ninguna
 B) Extraer remitente, destinatario, fecha; tratar valores nulos
 C) Solo cambiar formato
 D) Dividir en partes

**40.** ¿Cómo se construye el grafo del caso Enron?
 A) Aleatoriamente
 B) Nodos del DataFrame de emails, aristas del remitente-destinatario
 C) De la base de datos original
 D) Manualmente

---

## 5. Librería NetworkX

**41.** ¿Qué es NetworkX?
 A) Una red de telecomunicaciones
 B) Una librería Python para crear y analizar grafos
 C) Un navegador
 D) Un protocolo

**42.** ¿Cómo se instala NetworkX?
 A) pip install net-x
 B) pip install networkx
 C) pip install graphs
 D) pip install network

**43.** ¿Cómo se crea un grafo vacío en NetworkX?
 A) G = networkx.Graph()
 B) G = nx.Graph()
 C) Ambas
 D) G = create_graph()

**44.** ¿Cuál es la diferencia entre Graph y DiGraph en NetworkX?
 A) No hay diferencia
 B) Graph no dirigido; DiGraph dirigido
 C) DiGraph es más pequeño
 D) Graph solo para números

**45.** ¿Cómo se agrega un nodo en NetworkX?
 A) G.node_add(n)
 B) G.add_node(n)
 C) G.append(n)
 D) G.node(n)

**46.** ¿Cómo se agregan múltiples nodos?
 A) G.add_nodes([n1, n2, ...])
 B) G.add_nodes_from(list)
 C) Ambas
 D) G.add_multiple(nodes)

**47.** ¿Cómo se agrega una arista?
 A) G.add_edge(u, v)
 B) G.connect(u, v)
 C) G.link(u, v)
 D) G.edge(u, v)

**48.** ¿Cómo se agrega peso a una arista?
 A) G.add_edge(u, v, weight=0.5)
 B) G.add_weighted_edge(u, v, 0.5)
 C) G.set_weight(u, v, 0.5)
 D) G.edge_weight(u, v, 0.5)

**49.** ¿Cómo se obtienen los nodos de un grafo?
 A) G.nodes()
 B) list(G.nodes())
 C) G.get_nodes()
 D) G.node_list()

**50.** ¿Cómo se obtienen las aristas de un grafo?
 A) G.edges()
 B) list(G.edges())
 C) G.get_edges()
 D) G.edge_list()

---

## 6. Análisis de Métricas

**51.** ¿Qué calcula degree_centrality()?
 A) El grado promedio
 B) La importancia de cada nodo basada en su grado
 C) La distancia
 D) El peso total

**52.** ¿Cuál es el rango de degree centrality?
 A) Cualquier número
 B) 0 a 1
 C) Negativo a positivo
 D) 0 a 100

**53.** ¿Qué calcula betweenness_centrality()?
 A) El grado
 B) Importancia como "puente" entre otros nodos
 C) La distancia promedio
 D) El peso

**54.** ¿Qué calcula closeness_centrality()?
 A) Cuán cerca está de todos
 B) Importancia basada en proximidad promedio a otros
 C) El grado
 D) El peso

**55.** ¿Qué calcula eigenvector_centrality()?
 A) El vector propio
 B) Importancia considerando vecinos importantes
 C) Un autovalor
 D) Una matriz

**56.** ¿Qué es average_shortest_path_length()?
 A) La ruta más corta
 B) Distancia promedio entre todos los pares de nodos
 C) El diámetro
 D) La densidad

**57.** ¿Qué es clustering_coefficient()?
 A) El grado de agrupación
 B) Medida de cuán agrupados están los vecinos de un nodo
 C) El número de clústers
 D) Un tipo de dato

**58.** ¿Qué es transitivity()?
 A) Cualidad de ser temporal
 B) Probabilidad de que amigos de un nodo sean amigos entre sí
 C) Una propiedad matemática
 D) Un tipo de relación

**59.** ¿Cómo se calcula el número de nodos en NetworkX?
 A) G.node_count()
 B) len(G) o G.number_of_nodes()
 C) G.nodes_count
 D) count(G.nodes())

**60.** ¿Cómo se calcula el número de aristas?
 A) G.edge_count()
 B) G.number_of_edges()
 C) len(G.edges())
 D) Todas

---

## 7. Análisis de Comunidades

**61.** ¿Qué es community detection?
 A) Detectar comunidades en internet
 B) Identificar subgrupos cohesivos dentro de una red
 C) Encontrar policías
 D) Clasificar mensajes

**62.** ¿Por qué es importante detectar comunidades?
 A) No es importante
 B) Revela estructura subyacente y agrupa actores similares
 C) Solo para redes sociales
 D) Para dividir el grafo

**63.** ¿Qué es el algoritmo Louvain?
 A) Un lugar en Francia
 B) Un algoritmo de detección de comunidades que maximiza modularidad
 C) Un tipo de red
 D) Un protocolo

**64.** ¿Cómo se instala la librería community?
 A) pip install community-detection
 B) pip install python-louvain
 C) pip install community
 D) Viene con NetworkX

**65.** ¿Qué es modularidad?
 A) Que se puede modular
 B) Una medida de la calidad de partición comunitaria
 C) Una modularidad de sonido
 D) Un tipo de software

**66.** ¿Cuál es el rango de modularidad?
 A) 0 a 1
 B) -1 a 1
 C) -0.5 a 1
 D) Cualquier número

**67.** ¿Qué indica modularidad cercana a 1?
 A) Comunidades débiles
 B) Comunidades muy fuertes y bien definidas
 C) Sin comunidades
 D) Error

**68.** ¿Cómo se ejecuta el algoritmo Louvain?
 A) best_partition(G)
 B) community.best_partition(G)
 C) G.communities()
 D) louvain(G)

**69.** ¿Qué retorna best_partition()?
 A) Un gráfico
 B) Un diccionario {nodo: comunidad_id}
 C) Una lista de comunidades
 D) Un número

**70.** ¿Cuál es una limitación de Louvain?
 A) Es tan rápido
 B) No garantiza solución óptima; sensible a orden de procesamiento
 C) Solo funciona con 2 comunidades
 D) No tiene limitaciones

---

## 8. Visualización de Redes

**71.** ¿Por qué es importante visualizar redes?
 A) No es importante
 B) Permite comprender estructura y patrones visualmente
 C) Para decorar
 D) Para imprimir

**72.** ¿Cuál es una herramienta de visualización popular?
 A) Excel
 B) Gephi
 C) Word
 D) Photoshop

**73.** ¿Cómo se visualiza un grafo en NetworkX con matplotlib?
 A) nx.draw(G)
 B) plt.plot(G)
 C) draw_network(G)
 D) G.visualize()

**74.** ¿Qué es un spring layout?
 A) Una primavera
 B) Un algoritmo que posiciona nodos como fuerzas de repulsión/atracción
 C) Un tipo de gráfico
 D) Un mes

**75.** ¿Cómo se usa spring_layout en NetworkX?
 A) pos = nx.spring_layout(G)
 B) pos = nx.layout.spring(G)
 C) pos = spring(G)
 D) G.spring_layout()

**76.** ¿Qué es Gephi?
 A) Una fruta
 B) Una herramienta especializada para visualización de grafos
 C) Un programa
 D) Una ciudad

**77.** ¿Cuál es una ventaja de Gephi vs matplotlib?
 A) Gephi es más programático
 B) Gephi es más interactivo y visual; mejor para grafos complejos
 C) matplotlib es mejor
 D) Son iguales

**78.** ¿Qué formato usa Gephi?
 A) .gph
 B) .graphml o GEXF
 C) .xlsx
 D) .json

**79.** ¿Cómo se exporta un grafo de NetworkX a formato legible por Gephi?
 A) nx.write_graphml(G, 'file.graphml')
 B) nx.write_gexf(G, 'file.gexf')
 C) Ambas
 D) No es posible

**80.** ¿Cuáles son los parámetros principales de nx.draw()?
 A) node_color, node_size, edge_color
 B) pos, with_labels
 C) Todos
 D) G

---

## 9. Aplicaciones Avanzadas

**81.** ¿Cómo se detecta fraude con SNA?
 A) No es posible
 B) Identificar patrones anómalos, transacciones inusuales
 C) Revisión manual
 D) Por suerte

**82.** ¿Qué es detección de anomalías en redes?
 A) Encontrar nodos o aristas que no encajan con patrones normales
 B) Errores de cálculo
 C) Componentes dañados
 D) No existe

**83.** ¿Cómo se usa SNA en sistemas de recomendación?
 A) No se usa
 B) Recomendar basándose en proximidad en la red (usuarios similares)
 C) Recomendaciones aleatorias
 D) No funciona

**84.** ¿Qué es análisis de influencers?
 A) Analizar influenciadores
 B) Identificar nodos más importantes para difusión de información
 C) Ver seguidores
 D) Contar likes

**85.** ¿Cómo se identifica un influencer en SNA?
 A) Por número de seguidores
 B) Por centralidad (grado, intermediación, etc.)
 C) Popularity
 D) Random

**86.** ¿Qué es propagación en redes?
 A) Difundir información incorrecta
 B) Cómo la información se difunde a través de la red
 C) Reproducción
 D) Contagio

**87.** ¿Cuál es un modelo de propagación?
 A) Linear
 B) Susceptible-Infected-Recovered (SIR)
 C) Quadratic
 D) Exponential puro

**88.** ¿Cómo se analiza colaboración en equipos de software?
 A) No se puede
 B) Nodos = desarrolladores, aristas = colaboración; analizar clusters
 C) Solo con resultados
 D) Manualmente

**89.** ¿Qué es análisis de repositorios como red?
 A) Visualizar archivos
 B) Nodos = archivos, aristas = dependencias; detectar módulos
 C) Estadísticas de commits
 D) Historial git

**90.** ¿Cómo se usa SNA en ciberseguridad?
 A) No se usa
 B) Detectar comportamiento anómalo, ataques coordinados
 C) Cambiar contraseñas
 D) Solo firewalls

---

## 10. Casos Prácticos Integrados

**91.** ¿Qué es un pipeline completo de SNA?
 A) Una tubería
 B) Extracción de datos → Construcción de grafo → Análisis → Visualización
 C) Solo análisis
 D) Solo visualización

**92.** ¿Cuál es el primer paso en un análisis?
 A) Visualización
 B) Recolección e importación de datos
 C) Interpretación
 D) Reportes

**93.** ¿Cómo se valida un análisis de redes?
 A) No se valida
 B) Comparar distribuciones, propiedades, benchmarks
 C) Intuición
 D) Adivinar

**94.** ¿Qué es un grafo de prueba sintético?
 A) Un grafo falso
 B) Un grafo generado para testear algoritmos
 C) Un grafo pequeño
 D) Un grafo real

**95.** ¿Cómo se generan grafos sintéticos?
 A) Random, Scale-free (Barabási-Albert), Small-world (Watts-Strogatz)
 B) Solo aleatoriamente
 C) Manualmente
 D) Descargando

**96.** ¿Cómo se escala SNA a grafos muy grandes?
 A) No es posible
 B) Sampling, paralelización, algoritmos aproximados
 C) Usar más memoria
 D) Esperar

**97.** ¿Qué es graph sampling?
 A) Muestreo de grafos
 B) Seleccionar subconjunto representativo para análisis eficiente
 C) Copiar el grafo
 D) Hacer backup

**98.** ¿Cómo se reportan resultados de SNA?
 A) Solo números
 B) Gráficos, tablas, visualizaciones, interpretaciones
 C) Solo fotos
 D) No se reportan

**99.** ¿Cuál es una limitación del SNA?
 A) No tiene limitaciones
 B) Datos incompletos, atribución causal difícil, cambios temporales
 C) Solo para redes pequeñas
 D) Requiere GPU

**100.** ¿Cuál es el futuro del SNA?
 A) Va a desaparecer
 B) Análisis dinámico, multimodalidad, interpretabilidad, aplicaciones emergentes
 C) Solo análisis estático
 D) Sin cambios

---

## SOLUCIONARIO

| Pregunta | Respuesta | Pregunta | Respuesta | Pregunta | Respuesta |
|----------|-----------|----------|-----------|----------|-----------|
| 1 | B | 34 | B | 67 | B |
| 2 | C | 35 | B | 68 | B |
| 3 | B | 36 | B | 69 | B |
| 4 | B | 37 | B | 70 | B |
| 5 | B | 38 | B | 71 | B |
| 6 | B | 39 | B | 72 | B |
| 7 | B | 40 | B | 73 | A |
| 8 | B | 41 | B | 74 | B |
| 9 | B | 42 | B | 75 | A |
| 10 | B | 43 | C | 76 | B |
| 11 | B | 44 | B | 77 | B |
| 12 | B | 45 | B | 78 | B |
| 13 | B | 46 | C | 79 | C |
| 14 | B | 47 | A | 80 | C |
| 15 | B | 48 | A | 81 | B |
| 16 | B | 49 | A | 82 | A |
| 17 | B | 50 | A | 83 | B |
| 18 | B | 51 | B | 84 | B |
| 19 | B | 52 | B | 85 | B |
| 20 | B | 53 | B | 86 | B |
| 21 | B | 54 | B | 87 | B |
| 22 | B | 55 | B | 88 | B |
| 23 | B | 56 | B | 89 | B |
| 24 | B | 57 | B | 90 | B |
| 25 | B | 58 | B | 91 | B |
| 26 | B | 59 | B | 92 | B |
| 27 | B | 60 | D | 93 | B |
| 28 | B | 61 | B | 94 | B |
| 29 | B | 62 | B | 95 | A |
| 30 | B | 63 | B | 96 | B |
| 31 | B | 64 | B | 97 | B |
| 32 | C | 65 | B | 98 | B |
| 33 | B | 66 | B | 99 | B |
| | | | | 100 | B |
