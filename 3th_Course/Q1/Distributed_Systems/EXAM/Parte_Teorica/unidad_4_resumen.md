# Parte Teórica - Sistemas Distribuidos (Unidad 4) — Resumen corto

## Definiciones clave (las que “caen”) 

- **Migración de procesos**: mover el **estado** de un proceso (CPU/regs + memoria + contexto) a otro nodo para que continúe ejecutándose.
- **Hipervisor**: software que gestiona VMs.
  - **Tipo 1 (bare metal)**: corre sobre el hardware (más rendimiento/aislamiento). Ej: AWS/EC2.
  - **Tipo 2 (hosted)**: corre sobre un SO host (más cómodo, más overhead). Ej: VirtualBox.
- **Virtualización completa**: el invitado no se modifica; el hipervisor **emula/virtualiza** el hardware (más compatible, más lenta si es por software).
- (Extra) A veces se acelera con **traducción dinámica**, pero hoy domina **VT-x/AMD-V**.
- **Virtualización asistida por HW**: usa Intel VT-x / AMD-V para acelerar y aislar (lo habitual hoy).
- **Paravirtualización**: el invitado “sabe” que está virtualizado y usa **hiperllamadas/drivers** (ej. Guest Additions).
- **Contenedores (virtualización a nivel de SO)**: aislan procesos compartiendo **kernel** (ligeros, arranque rápido).
- **Kubernetes**: orquestador de contenedores.
  - **Contenedor → Pod → Deployment**.

---

## Migración de procesos 🔁 (idea + por qué)

**Motivaciones típicas:**
- **Equilibrado de carga**: mover procesos de nodos saturados a nodos libres.
- **Reducir coste de comunicación**: juntar procesos que se hablan mucho para bajar latencia.
- **Alta disponibilidad/mantenimiento**: mover procesos críticos antes de apagar nodos.
- **Acceso a recursos**: mover a nodo con GPU/almacenamiento/hardware específico.

**Quién decide:**
- Suele ser el **SO/monitor** (balanceo), o la **aplicación** si está diseñada para ello (buscar recursos).

---

## Tipos de migración (chuleta)

| Tipo | Qué hace | Pro | Contra |
|------|----------|-----|--------|
| **Stop-and-copy** | pausa → copia todo → reanuda | simple | parada grande si hay mucha RAM |
| **Pre-copiado** | copia RAM mientras corre; pausa final corta | poca parada | complejidad: páginas “sucias” |
| **Working set conocido** | copia CPU + páginas “necesarias” | menos datos | origen mantiene el resto |
| **Bajo demanda** | copia CPU; RAM se trae cuando se usa | arranque rápido | fallos de página remotos (parones) |

Notas rápidas:
- **Migración de VM**: mueve *todo el entorno* (SO+memoria+dispositivos virtuales) → más pesado.
- **Ficheros**: moverlos es caro; a veces se dejan en origen y se acceden remoto (latencia; se mitiga con caché).

Ejemplos de implementación (1 línea):
- **IBM AIX**: migración iniciada por el **programa**.
- **Charlotte**: “starters” monitorizan y acuerdan migración para **balanceo**.

---

## Virtualización vs contenedores 🧩

| Tema | VMs | Contenedores |
|------|-----|--------------|
| Kernel | propio | compartido con host |
| Arranque | más lento | muy rápido |
| Aislamiento | más fuerte | bueno pero depende del kernel |
| Overhead | mayor | menor |

**Copy-on-write (Docker)**: varias instancias comparten capas de la imagen; al escribir se crea copia. Si quieres persistencia real → volúmenes/commit.

---

## Kubernetes en 6 ideas ☸️

- Orquesta contenedores en un clúster: **despliegue + escalado + autoreparación**.
- **Service discovery + balanceo**.
- **Rolling updates + rollback**.
- **Pods**: 1+ contenedores que comparten red y storage.
- **Deployments**: gestionan réplicas de pods.
- **Persistencia**: los pods son efímeros; se usan **volúmenes**.
