# Parte Teórica - Sistemas Distribuidos (Unidad 3) — Resumen corto

## Definiciones clave

- **sshfs**: montar un directorio remoto como si fuera local usando **SSH** (seguro). Se apoya en **FUSE**.
- **Thread / multithread**: ejecución en paralelo dentro de un proceso (comparten memoria).
- **Mutex / exclusión mutua**: evita que 2 threads toquen a la vez una región crítica.
- **RPC**: llamadas remotas entre cliente y servidor (como función local) mediante mensajes.
- **Proxy / Stub**: piezas de middleware.
  - **Proxy (cliente)**: empaqueta y envía la petición.
  - **Stub (servidor)**: desempaqueta, ejecuta y responde.
- **Broker de objetos**: intermediario que conoce servidores disponibles y ayuda a balancear/asignar.

---

## Administración básica de cluster (idea)

- En AWS, los **Security Groups** controlan puertos y conexiones.
- Para compartir carpeta entre máquinas sin NFS/Samba: **sshfs**.

---

## Programación paralela (lo esencial)

- **Joinable**: esperas al hilo (`join`) para sincronizar/recoger resultado.
- **Detached**: el hilo va “a su bola” (no esperas).

### Regiones críticas

- Si varios threads comparten una variable ⇒ necesitas **mutex/semáforo/condición**.
- Regla: *lock → trabajo → unlock*.

Primitivas (chuleta):
- **Mutex/candado**: 1 hilo dentro.
- **Semáforo**: contador (hasta N hilos).
- **Condición**: hilos “duermen” hasta que se cumpla algo.

---

## RPC aplicado a objetos (Persona)

Idea clave: **no cambia el `main` del usuario**; cambia la implementación por un proxy remoto.

- El cliente llama métodos “normales” → el proxy los convierte en mensajes.
- El servidor mantiene las instancias reales (ej. `map<ID, Persona*>`).
- Cada objeto remoto suele tener un **ID remoto** asignado por el servidor.

### Protocolo (2 reglas)

1. **Enum/Tipo de mensaje** para indicar la operación.
2. Para strings: enviar **tamaño + bytes** (sin terminador) y leer en el mismo orden.

---

## Escalado: broker

- Si hay **varios servidores**, el cliente no sabe a cuál conectarse.
- El **broker** mantiene lista/estado de servidores y devuelve el “mejor” según carga/recursos.

---

## Chuleta de fallos típicos

- Desalinear orden de *write/read* ⇒ corrupción/bloqueos.
- Olvidar sincronización en servidor multi-hilo ⇒ condiciones de carrera.
- Guardar ficheros desde RPC ⇒ el fichero se crea **en el servidor**, no en el cliente.
