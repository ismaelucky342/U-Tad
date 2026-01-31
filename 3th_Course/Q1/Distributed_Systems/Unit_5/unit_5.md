# Unidad 5. Introducción a Cloud y Servicios

## Introducción y objetivos

En esta unidad exploraremos el paradigma del **Cloud Computing** (Computación en la Nube), que ha revolucionado la forma en que las empresas y usuarios consumen recursos tecnológicos. El objetivo es comprender qué es la nube, por qué se utiliza, sus fundamentos técnicos, modelos de servicio y despliegue.

Además, nos centraremos en **Amazon Web Services (AWS)**, el proveedor líder del mercado actual y la herramienta que utilizaremos a lo largo de la asignatura para la realización de prácticas. Esta unidad servirá de base teórica para ampliar los conocimientos sobre los servicios disponibles que usaremos en los ejercicios.

### Objetivos:
*   Definir qué es el Cloud Computing y sus características esenciales.
*   Diferenciar entre los distintos modelos de servicio (IaaS, PaaS, SaaS).
*   Entender los modelos de despliegue (Pública, Privada, Híbrida).
*   Conocer conceptos clave como elasticidad, escalabilidad, SLA y las garantías de servicio.
*   Comprender las implicaciones legales y de seguridad asociadas a la localización de los datos.
*   Desmitificar el concepto de "nube" entendiendo la infraestructura física subyacente.
*   Identificar los servicios principales de AWS y sus casos de uso.

---

## 1. Introducción al cloud computing

### Introducción

La computación en la nube ("Cloud Computing") es un modelo tecnológico que permite el acceso ubicuo, conveniente y bajo demanda a un conjunto compartido de recursos informáticos configurables (por ejemplo, redes, servidores, almacenamiento, aplicaciones y servicios) que pueden ser aprovisionados y liberados rápidamente con un mínimo esfuerzo de gestión o interacción con el proveedor del servicio.

En términos sencillos, es la entrega de servicios informáticos (servidores, almacenamiento, bases de datos, redes, software, análisis, inteligencia, etc.) a través de Internet ("la nube"), ofreciendo una innovación más rápida, recursos flexibles y economías de escala.

### Beneficios de usar sistemas cloud

La adopción de la nube ofrece ventajas significativas frente a los centros de datos tradicionales "on-premise":

1.  **Coste**: Elimina la inversión de capital (CapEx) necesaria para comprar hardware y software y configurar centros de datos (racks, electricidad, refrigeración, expertos TI). Se pasa a un modelo de gasto operativo (OpEx), pagando solo por lo que se usa.
2.  **Velocidad y Agilidad**: Los recursos se pueden aprovisionar en minutos con unos pocos clics, lo que permite a las organizaciones responder rápidamente a los cambios del mercado y experimentar con nuevas ideas sin grandes riesgos.
3.  **Escala Global**: Permite escalar elásticamente. Esto significa entregar la cantidad correcta de recursos de TI (más o menos potencia de cálculo, almacenamiento, ancho de banda) justo cuando se necesitan y desde la ubicación geográfica adecuada.
4.  **Productividad**: Elimina la necesidad de muchas tareas de gestión de hardware ("undifferentiated heavy lifting"), como el apilamiento de servidores o parcheado de software, permitiendo a los equipos de TI centrarse en objetivos de negocio.
5.  **Rendimiento**: Los servicios se ejecutan en una red mundial de centros de datos seguros, actualizados regularmente con el hardware más rápido y eficiente.
6.  **Fiabilidad**: Facilita la copia de seguridad de datos, la recuperación ante desastres y la continuidad del negocio, ya que los datos se pueden duplicar en múltiples sitios redundantes en la red del proveedor.

### Desventajas de los sistemas cloud

A pesar de sus beneficios, existen desafíos y desventajas que deben considerarse:

1.  **Dependencia de Internet**: El acceso a los servicios depende enteramente de la conexión a Internet. Si la conexión falla, se pierde el acceso a los recursos.
2.  **Vendor Lock-in (Cautividad del proveedor)**: Puede ser difícil migrar aplicaciones o servicios de un proveedor de nube a otro debido a diferencias en plataformas, API y formatos de datos.
3.  **Seguridad y Privacidad**: Aunque los proveedores invierten masivamente en seguridad, confiar datos sensibles a un tercero genera preocupaciones sobre la privacidad y el cumplimiento normativo (GDPR, etc.). El modelo de responsabilidad compartida implica que el usuario sigue siendo responsable de la seguridad "en" la nube.
4.  **Costes ocultos o impredecibles**: Si no se gestiona correctamente, el modelo de pago por uso puede resultar en facturas inesperadamente altas debido a un sobreaprovisionamiento o falta de control de recursos.
5.  **Control Limitado**: El usuario tiene control sobre sus aplicaciones y datos, pero no sobre la infraestructura física subyacente, que es gestionada opacamente por el proveedor.

---

## 2. Fundamentos del cloud

### Introducción

Para entender cómo funciona la nube, es vital comprender los conceptos fundamentales que la diferencian de la infraestructura tradicional. Estos conceptos definen la "naturaleza" de la nube.

### Elasticidad y escalabilidad

A menudo se usan indistintamente, pero tienen matices diferentes:
*   **Escalabilidad**: Es la capacidad del sistema para manejar una carga creciente de trabajo agregando recursos. Puede ser **Vertical** (o *Scale Up*: añadir más CPU/RAM a una máquina existente) o **Horizontal** (o *Scale Out*: añadir más máquinas al clúster). La escalabilidad suele ser una planificación a medio/largo plazo.
*   **Elasticidad**: Es la capacidad de *adaptarse automáticamente* a los cambios en la carga de trabajo en tiempo real. Un sistema elástico aprovisiona recursos cuando la demanda sube y los libera ("de-provisiona") cuando la demanda baja. Esto es clave para el ahorro de costes en la nube, ya que evita pagar por recursos ociosos.

### Auto-abastecimiento de servicios (On-demand Self-service)

Es la característica que permite a un consumidor aprovisionarse de capacidades informáticas, como tiempo de servidor y almacenamiento de red, de forma automática y unilateral, sin requerir interacción humana con el personal del proveedor de servicios. Esto se realiza habitualmente a través de un portal web o consola de gestión.

### Interfaces de programación estándar (APIs)

Los servicios en la nube no solo son accesibles por humanos, sino también (y principalmente) por máquinas. Los proveedores exponen **APIs (Application Programming Interfaces)** estandarizadas y documentadas que permiten gestionar la infraestructura mediante código. Esto habilita la **Infraestructura como Código (IaC)**, donde servidores y redes se definen en scripts (como Terraform o CloudFormation) en lugar de configurarse manualmente, facilitando la automatización, repetibilidad y control de versiones.

### Pago de servicios (Pay-as-you-go)

El modelo económico de la nube se basa en el consumo medido. Los recursos se monitorean, controlan y reportan, proporcionando transparencia.
*   **Pago por uso**: Se factura por unidad de tiempo (segundos, horas), por almacenamiento usado (GB/TB) o por solicitudes realizadas.
*   **Modelos de precios**: Incluyen instancias bajo demanda (precio estándar), instancias reservadas (descuentos por compromiso de uso a 1-3 años) y Spot (uso de capacidad excedente con grandes descuentos pero con riesgo de interrupción).

### Calidad de servicio (QoS)

La Calidad de Servicio en la nube se refiere a la capacidad del proveedor para garantizar cierto nivel de rendimiento, disponibilidad y fiabilidad. Dado que los recursos son compartidos (multi-tenancy), el proveedor debe utilizar mecanismos para asegurar que el uso intensivo de un cliente ("vecino ruidoso") no degrade el rendimiento de otros. Incluye métricas como ancho de banda garantizado, latencia máxima y IOPS (operaciones de entrada/salida por segundo) en almacenamiento.

### Service Level Agreements (SLA)

Un **Acuerdo de Nivel de Servicio (SLA)** es un contrato entre el proveedor y el cliente que define el nivel de servicio esperado.
*   **Disponibilidad (Uptime)**: Generalmente expresado en "nueves". Por ejemplo, un SLA del 99.99% permite menos de 52 minutos de caída al año.
*   **Penalizaciones/Compensaciones**: El SLA define qué sucede si no se cumple el nivel de servicio (normalmente, créditos de servicio para el cliente).
*   **Métricas**: Incluye tiempos de respuesta, resolución de incidentes y disponibilidad de la infraestructura.

### Aspectos Legales y Soberanía de Datos

Aunque la nube parezca etérea, los datos residen físicamente en discos duros ubicados en centros de datos específicos. Esto tiene importantes implicaciones legales:
*   **Soberanía del Dato**: Los datos están sujetos a las leyes del país donde se encuentran físicamente almacenados. Por ejemplo, datos alojados en EE.UU. pueden estar sujetos a la *CLOUD Act*, mientras que en Europa rige el RGPD (GDPR).
*   **Cumplimiento (Compliance)**: Es imprescindible ser consciente de las leyes y regulaciones que aplican a tu sector (bancario, sanitario, gubernamental) y elegir una región de nube que cumpla con estos requisitos. Un proveedor puede mover datos entre centros de datos para optimizar, pero el contrato debe garantizar dónde permanecen los datos sensibles.

### Sistemas cloud públicos, privados e híbridos

Son los modelos de despliegue ("Deployment Models"):
1.  **Nube Pública**: La infraestructura es propiedad de un proveedor de servicios (AWS, Azure, Google Cloud) que la vende al público general. Los recursos son compartidos entre múltiples clientes (multi-tenant) y accesibles vía Internet. Es el modelo más común para reducir costes y mantenimiento.
2.  **Nube Privada**: La infraestructura es dedicada exclusivamente a una sola organización. Puede estar alojada en el centro de datos de la propia empresa (on-premise) o gestionada por un tercero. Ofrece mayor control y seguridad, ideal para entidades gubernamentales o financieras con regulaciones estrictas.
3.  **Nube Híbrida**: Combina nubes públicas y privadas, unidas por tecnología que permite compartir datos y aplicaciones entre ellas. Permite a las empresas mantener datos sensibles en su nube privada y usar la nube pública para escalar capacidad (Cloud Bursting) o para aplicaciones menos críticas.
4.  **Multi-Cloud**: Uso de múltiples proveedores de nube pública (ej. usar AWS para almacenamiento y Google Cloud para Machine Learning) para evitar el vendor lock-in y optimizar servicios.

### Tipos de servicios

Se conocen como modelos de servicio (SPI: SaaS, PaaS, IaaS) y definen qué gestiona el proveedor y qué gestiona el usuario:

1.  **IaaS (Infrastructure as a Service)**:
    *   **Definición**: Provee recursos informáticos fundamentales (procesamiento, almacenamiento, redes). Es como "alquilar hardware virtual".
    *   **Gestión**: El proveedor gestiona virtualización, servidores, almacenamiento y red. El usuario gestiona el Sistema Operativo, aplicaciones y datos.
    *   **Ejemplos**: Amazon EC2, Google Compute Engine, Azure Virtual Machines.

2.  **PaaS (Platform as a Service)**:
    *   **Definición**: Provee una plataforma que permite a los clientes desarrollar, ejecutar y gestionar aplicaciones sin la complejidad de construir y mantener la infraestructura infraestructural.
    *   **Gestión**: El proveedor gestiona hasta el Sistema Operativo y el Runtime. El usuario solo gestiona la aplicación y los datos.
    *   **Ejemplos**: AWS Elastic Beanstalk, Google App Engine, Heroku.

3.  **SaaS (Software as a Service)**:
    *   **Definición**: El proveedor entrega aplicaciones de software completas a través de Internet.
    *   **Gestión**: El proveedor gestiona absolutamente todo. El usuario solo configura y usa la aplicación.
    *   **Ejemplos**: Gmail, Dropbox, Salesforce, Microsoft 365, Zoom.

---

## 3. Arquitectura cloud

### Introducción

La arquitectura cloud se refiere a cómo se diseñan los componentes tecnológicos para aprovechar las ventajas de la nube. Difiere de la arquitectura tradicional en que abraza el fallo ("Design for Failure"), utiliza componentes desacoplados y microservicios.

### Infraestructura

Es fundamental desmitificar el concepto de "nube": no es algo mágico, sino enormes instalaciones industriales de hardware. La infraestructura de un sistema cloud se basa en grandes centros de datos físicos conectados globalmente.
*   **Centros de Datos (Data Centers)**: Edificios físicos con miles de servidores en racks, sistemas de refrigeración industrial, generadores de energía de respaldo y seguridad física estricta. Aquí es donde realmente ocurre el cómputo y se guardan los datos.
*   **Regiones**: Áreas geográficas físicas (ej. "us-east-1" en N. Virginia, "eu-south-2" en España). Una región es un cluster de centros de datos.
*   **Zonas de Disponibilidad (AZs)**: Dentro de cada región, hay múltiples AZs aisladas entre sí por kilómetros de distancia para evitar que un desastre (incendio, inundación) afecte a toda la región.
*   **Red Global**: Fibra óptica propietaria que conecta estos centros de datos alrededor del mundo para mover datos a alta velocidad.

### Capas de un sistema cloud

Una arquitectura cloud típica se puede visualizar en capas:
1.  **Hardware Físico**: Servidores, almacenamiento, dispositivos de red (Gestionado por el proveedor).
2.  **Capa de Virtualización**: Hipervisores (Xen, KVM) que crean abstracciones de los recursos físicos (Gestionado por el proveedor).
3.  **Capa IaaS**: Servicios básicos de cómputo, red y almacenamiento expuestos vía API (EC2, S3, VPC).
4.  **Capa PaaS/Servicios Gestionados**: Bases de datos gestionadas, colas de mensajes, balanceadores de carga, servicios de IA.
5.  **Capa de Aplicación (SaaS)**: El software final que consume el usuario o cliente.

### Cloud Toolkit

El "Cloud Toolkit" se refiere al conjunto de herramientas que permiten a desarrolladores y administradores interactuar, desarrollar y operar en la nube. No es una única herramienta, sino un ecosistema que incluye:
*   **Consola de Gestión**: Interfaz web gráfica (GUI) para gestionar recursos manualmente.
*   **CLI (Command Line Interface)**: Herramientas de línea de comandos (ej. `aws cli`) para scripting y automatización.
*   **SDKs (Software Development Kits)**: Librerías para lenguajes de programación (Python con Boto3, Java, Node.js) para integrar aplicaciones con servicios cloud.
*   **IDE Toolkits**: Plugins para entornos de desarrollo (VS Code, IntelliJ, Eclipse) que permiten desplegar y depurar aplicaciones en la nube directamente desde el editor (ej. AWS Toolkit for VS Code).
*   **Herramientas IaC**: Terraform, AWS CloudFormation, Ansible.

---

## 4. Ejemplo cloud AWS

### Introducción

**Amazon Web Services (AWS)** es la plataforma que utilizaremos en los ejercicios prácticos. A continuación, exploraremos ejemplos concretos que cubren las capas de Infraestructura, Plataforma, Software y Almacenamiento:

### EC2 (Elastic Compute Cloud) - Infraestructura (IaaS)
*   **Descripción**: Servicio web que proporciona capacidad informática segura y redimensionable en la nube. Son "máquinas virtuales" puras donde el usuario gestiona desde el sistema operativo hacia arriba.
*   **Características clave**:
    *   Permite elegir el Sistema Operativo (Linux, Windows, MacOS).
    *   Variedad de "Tipos de Instancia" optimizados para diferentes tareas (cómputo, memoria, almacenamiento, gráficos).
    *   Control total a nivel de root.

### RDS (Relational Database Service) - Plataforma (PaaS)
*   **Descripción**: Servicio de base de datos relacional gestionado. AWS se encarga de la infraestructura, el sistema operativo y el software de base de datos, mientras tú gestionas las tablas y los datos.
*   **Motores soportados**: Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, SQL Server.
*   **Características clave**:
    *   **Alta Disponibilidad (Multi-AZ)**: Réplica síncrona en otra zona de disponibilidad.
    *   Copias de seguridad y parches automáticos.

### S3 (Simple Storage Service) - Almacenamiento
*   **Descripción**: Almacenamiento de objetos diseñado para ofrecer una durabilidad del 99,999999999% (11 nueves).
*   **Concepto de Objeto**: Los archivos se guardan como objetos en "buckets".
*   **Uso típico**: Hosting de webs estáticas, backups, datalakes.

### Lambda - Computación sin servidor (FaaS) y Software
*   **Descripción**: Permite ejecutar código sin aprovisionar servidores. A menudo se utiliza para construir lógica de backend de aplicaciones (Software) de forma totalmente gestionada.
*   **Características clave**:
    *   **Event-driven**: Se ejecuta en respuesta a eventos.
    *   **Pago por uso**: Solo pagas por los milisegundos de ejecución.

> **Nota sobre SaaS en AWS**: Aunque AWS es conocido por IaaS/PaaS, también ofrece servicios SaaS puros como **Amazon WorkMail** (correo) o **Amazon Chime** (reuniones), donde el servicio se consume directamente como un producto final.

---

## Conclusiones de la unidad

En esta unidad hemos establecido las bases teóricas del Cloud Computing. Hemos visto que la nube no es una entidad abstracta, sino una vasta red de centros de datos físicos sujetos a leyes y regulaciones específicas (Soberanía de Datos).

La distinción entre IaaS, PaaS y SaaS es fundamental para comprender la responsabilidad compartida en seguridad y gestión. AWS será nuestra herramienta de trabajo práctica; servicios como EC2, S3 y RDS serán piezas clave en los ejercicios de las siguientes unidades, permitiéndonos desplegar arquitecturas complejas con agilidad y escalabilidad, pagando solo por lo que usamos.
