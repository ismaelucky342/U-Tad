# Parte Teórica - Sistemas Distribuidos (Unidad 2) — Resumen corto

## Definiciones clave

- **Memoria distribuida (multicomputador)**: cada nodo es “independiente”, con su SO y memoria local; **no hay memoria compartida**.
- **Paso de mensajes**: comunicación entre procesos/máquinas mediante `send/receive` (la red es lo lento).
- **Middleware**: capa que oculta heterogeneidad (SO, librerías, red) y da **portabilidad**.
- **Cliente–Servidor**: cliente pide, servidor ofrece recursos/servicios.
- **Maestro–Esclavo**: maestro reparte trabajo; esclavos ejecutan y devuelven resultado.
- **RPC**: llamada remota “como si fuese” una función local (middleware oculta la red).

---

## Memoria distribuida: ideas que importan

- Cada nodo debe ser **autónomo** ⇒ minimizar accesos a red.
- Compartir recursos (ficheros, BD, etc.) requiere **protocolos de coordinación** (más complejo que mutex de memoria compartida).

---

## Modelos de programación

### Cliente–Servidor

- **Ventaja**: simple y común (web, BD).
- **Problema típico**: **cuello de botella** en el servidor cuando crecen los clientes.

Variantes típicas (1 línea):
- **Host-based** (cliente tonto), **Server-based** (cliente UI + algo de lógica), **Client-based** (casi todo en cliente), **Cooperativo/P2P**.

### Maestro–Esclavo

- **Ventaja**: fácil de paralelizar.
- **Problema**: **desequilibrio de carga** (maestro puede quedar infrautilizado).

---

## Middleware (3 funciones)

1. **Uniformidad**: mismo programa en nodos distintos.
2. **Acceso unificado a datos**: da “ilusión” de local.
3. **Portabilidad**: aísla del hardware/SO.

Ejemplos típicos: **QT**, **JVM (Java)**, intérpretes (Python), servicios del SO.

## Clusters (muy resumido)

- Factores: **HW barato**, **red rápida**, **herramientas de admin**.
- Configuración: **FS compartido** (barato pero cuello) vs **almacenamiento distribuido paralelo** (más complejo, más rendimiento).

---

## Paso de mensajes (chuleta)

- **Fiable**: llega sí o sí (ej. **TCP**). Más overhead.
- **No fiable**: puede perderse (ej. **UDP**). Más rápido.

### Bloqueante vs no bloqueante

- **Bloqueante**: la llamada espera a terminar (simple, pero “para” el programa).
- **No bloqueante**: devuelve control y luego compruebas/recibes (mejor solapamiento).

---

## RPC (qué es y por qué)

- Convierte: *llamada local* → **mensaje por red** → ejecución en servidor → respuesta.
- Objetivo: separar **interfaz/cliente** del **núcleo/servidor**.
- Ventajas típicas:
      - Interfaces claras (nombres y tipos).
      - Código reutilizable/generable (stubs/proxies según tecnología).

---

## Comparativas rápidas

| Tema | Cliente–Servidor | Maestro–Esclavo |
|---|---|---|
| Rol central | servidor | maestro |
| Riesgo | servidor se satura | carga mal repartida |
| Uso | servicios/datos | cómputo paralelo |

| Tema | TCP | UDP |
|---|---|---|
| Entrega | fiable | no garantizada |
| Latencia/overhead | mayor | menor |
