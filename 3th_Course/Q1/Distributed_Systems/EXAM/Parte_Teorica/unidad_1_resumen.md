# Parte Teórica - Sistemas Distribuidos (Unidad 1) — Resumen corto

## Definiciones clave

- **Sistema distribuido**: nodos de cómputo conectados por una red que cooperan.
- **Nodo**: máquina con autonomía mínima para ejecutar órdenes.
- **Red**: envío/recepción de datos entre nodos.
- **Cluster**: conjunto de máquinas en red que trabajan coordinadas; escalado horizontal (añadir nodos).
- **Grid computing**: recursos distribuidos entre instituciones para un **proyecto común**.
- **Cloud computing**: recursos/servicios ofrecidos al **gran público** bajo **pago por uso**.
- **HPC**: aplicaciones que requieren muchos recursos (clusters/datacenters).

---

## Línea histórica (lo más preguntable)

- **Años 50 — Grosch**: separación mainframe–terminal + *time sharing* + visión de centros distribuidos.
- **Años 60 — McCarthy**: computación como servicio (visión “pagar por uso”).
- **1966 — Parkhill**: “Computer Utility” (computación como electricidad/agua).
- **Años 80–90**: PC + Internet → viabiliza clusters.
- **2000+**: Grid (colaborativo) vs Cloud (comercial). **2006: EC2** como hito del cloud moderno.

---

## Clusters: idea central

- **Pros**: escalan fácil añadiendo nodos (CPU/RAM/almacenamiento).
- **Contras**: la **red** y el **acceso a datos** se convierten en cuellos de botella.

Detalles que suelen preguntar:
- **Multi-CPU vs cluster**: multi-CPU complica bus/memoria/cachés (coherencia); cluster escala barato pero depende de red.
- **Gestión/energía**: nodos infrautilizados = gasto; migrar cargas para **apagar nodos** (o cores en PCs).

Regla de oro:
> **Mejor 1 nodo al 100% que 2 nodos al 50%** (si no hay otras restricciones).

---

## Grid vs Cloud (tabla rápida)

| Aspecto | Grid | Cloud |
|---|---|---|
| Objetivo | proyecto colaborativo | servicio comercial |
| Usuarios | instituciones/centros | cualquiera que pague |
| Modelo | cooperación | pago por uso |
| Ejemplos | proyectos científicos | AWS / Azure / GCP |

---

## Ejemplos típicos de HPC

- **Ciencia/ingeniería**: simulaciones grandes.
- **Medicina**: simulación molecular (GPU + red rápida).
- **E-commerce**: disponibilidad/transacciones.
- **Finanzas**: baja latencia.
