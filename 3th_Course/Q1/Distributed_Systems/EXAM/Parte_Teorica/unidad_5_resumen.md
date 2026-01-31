# Parte Teórica - Sistemas Distribuidos (Unidad 5) — Resumen corto

## Definiciones clave

- **Cloud Computing**: pago por uso de recursos IT a través de internet (luz/agua). Modelo **OpEx** (gasto operativo) vs **CapEx** (inversión inicial).
- **IaaS (Infraestructura)**: alquilas "hierro" virtual (CPU, RAM). Tú gestionas el SO. Ej: EC2.
- **PaaS (Plataforma)**: alquilas el entorno de ejecución. Tú pones el código/datos. Ej: RDS, Elastic Beanstalk.
- **SaaS (Software)**: usas la aplicación final. Ej: Gmail, Dropbox.
- **FaaS (Function as a Service)**: subes funciones sueltas, sin gestionar servidor. Ej: Lambda.

---

## Escalabilidad vs Elasticidad (Pregunta trampa típica)

- **Escalabilidad**: capacidad de crecer/decrecer (planificado).
  - *Vertical (Scale Up)*: +RAM/CPU a la misma máquina.
  - *Horizontal (Scale Out)*: +máquinas al cluster.
- **Elasticidad**: adaptación **automática** a la demanda en tiempo real (sube y baja solo). Clave para ahorrar €.

---

## Modelos de Despliegue

| Modelo | Descripción | ¿Para quién? |
|---|---|---|
| **Pública** | Multi-tenant (compartido), internet. Ej: AWS. | Startups, uso general. |
| **Privada** | Infra dedicada (on-premise o hosteada). | Banca, gobierno (seguridad extrema). |
| **Híbrida** | Conecta pública + privada. | Bursting (picos de carga a la pública). |

---

## Infraestructura Física (Desmitificando la nube)

- **Región**: Área geográfica (ej: `us-east-1`). Conjunto de Data Centers.
- **AZ (Availability Zone)**: Data Center (o grupo de ellos) aislado físicamente dentro de una región. Fallo en una AZ no afecta a otra.
- **Soberanía del dato**: Los datos residen en discos físicos en un país concreto.
  - **GDPR**: Europa.
  - **CLOUD Act**: EE.UU (pueden pedir datos).
  - *Ojo*: Elegir región implica elegir jurisdicción legal.

---

## Conceptos de Servicio

- **SLA (Service Level Agreement)**: contrato de uptime. Se mide en "nueves" (99.9% vs 99.999%). Si no cumplen -> devuelven dinero (créditos).
- **Responsabilidad Compartida**:
  - AWS protege la nube (físico, red global).
  - Tú proteges lo que pones EN la nube (datos, cifrado, firewall de SO).

---

## Servicios AWS "a fuego"

- **EC2**: Máquina virtual (IaaS).
- **RDS**: Base de datos SQL gestionada (PaaS). Backups y parches solos.
- **S3**: Almacenamiento de objetos (archivos). Súper duradero.
- **Lambda**: Ejecutar código sin servidor (FaaS).
