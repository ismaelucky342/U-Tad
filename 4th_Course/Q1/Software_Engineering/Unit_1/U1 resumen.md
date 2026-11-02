# U1 · Resumen · Introducción a la Ingeniería del Software

> Repaso rápido. Detalle y ejemplos en el temario denso (los enlaces `→` te llevan a cada sección). ⚠️ marca puntos donde el material y las fuentes externas discrepan: **en el examen, usa el criterio del profesor**.

---

## 1. Key concepts

**Software y calidad** → [→ §1](U1_temario_denso.md#1-el-software-qué-es-y-cómo-es)
- Software = **programas + estructuras de datos + documentos + configuraciones** (no solo código).
- Rasgos (Pressman): se **desarrolla** (no se fabrica), **no se desgasta pero se degrada**, suele ser **a medida**, **coste de réplica ≈ 0**.
- Atributos de calidad / NFR: confiabilidad, mantenibilidad, eficiencia, usabilidad (+ seguridad, cumplimiento, escalabilidad, accesibilidad…).
- No existe una metodología universal: cada tipo de sistema pide la suya.

**Origen y retos** → [→ §3](U1_temario_denso.md#3-origen-de-la-ingeniería-del-software-y-sus-retos)
- Retos: plazos, costes, calidad, adecuación al cliente, mantenimiento, medición del progreso.
- **Conferencia de 1968** (NATO, Garmisch) = punto de partida. Fracasos actuales: exigencias crecientes + desarrollo sin principios de ingeniería.

**Definición** → [→ §4](U1_temario_denso.md#4-definición-y-alcance)
- **Bauer 1972**: principios de ingeniería → software rentable, fiable, en máquinas reales.
- **IEEE 610.12**: enfoque **sistemático, disciplinado y cuantificable** al desarrollo, operación y mantenimiento.
- La esencia del ingeniero: **análisis y diseño**; lo demás es contingente.
- Predictivo/cascada → más análisis y diseño; ágil (XP) → más proceso de desarrollo.

**Teoría de Sistemas y actividades** → [→ §5](U1_temario_denso.md#5-teoría-de-sistemas-y-actividades-fundamentales)
- 4 principios: especializado = menos adaptable; grande = más mantenimiento; sistemas dentro de sistemas; los sistemas crecen.
- 6 pasos de análisis: problema → comprender → alternativas → elegir → implantar → evaluar impacto.
- **4 actividades siempre presentes:** especificación, desarrollo, validación, evolución/mantenimiento.

**Procesos del ciclo de vida** → [→ §6](U1_temario_denso.md#6-campo-de-acción-procesos-del-ciclo-de-vida)
- **PMI:** 10 áreas de conocimiento, 5 grupos de procesos (inicio, planificación, ejecución, monitoreo y control, cierre), 3 dominios PMP.
- **ISO/IEC 12207:** 17 procesos = **5 principales + 8 de soporte + 4 organizativos**.
- Proceso de **Desarrollo**: 9 actividades (requisitos sistema → requisitos software → arquitectura → diseño detallado → construcción → integración → pruebas → instalación → aceptación).

**Industrialización** → [→ §7](U1_temario_denso.md#7-industrialización-del-software)
- Aplicar principios industriales al **proceso** (automatizar, estandarizar, medir): CI/CD, pruebas automáticas, gestión de configuración, roles.
- Incluye requisitos de **operación**: manuales, recuperación, backups, logs, indicadores y alarmas.
- Coste: dependencia de herramientas y procesos que exigen inversión y formación.

**TCO** → [→ §9](U1_temario_denso.md#9-total-cost-of-ownership-tco)
- Coste directo + indirecto durante **todo el ciclo de vida**. Decisión: **comprar, adaptar, construir** (o descartar).
- **Iceberg:** los costes ocultos superan a los visibles.
- Alta inversión inicial puede compensarse con bajos costes recurrentes, y al revés.

**Tipología, integración y SaaS** → [→ §10](U1_temario_denso.md#10-tipología-de-aplicaciones), [→ §11](U1_temario_denso.md#11-integración-de-sistemas), [→ §12](U1_temario_denso.md#12-saas)
- 10 tipos de aplicaciones; 3 modelos de provisión: a medida, cerrada, abierta.
- Integrar cuando: no se puede cubrir todo con una app, integrar cuesta menos que desarrollar, obligación legal, y hay tecnología.
- **SaaS:** aplicación y datos alojados por un tercero, acceso por Internet; el proveedor opera y da soporte. Modelos IDC: *hosted AM* y *software on demand*.

---

## 2. Fórmulas esenciales

| Concepto | Fórmula | Símbolos | Ejemplo |
|---|---|---|---|
| **TCO** | $\text{TCO} = C_0 + \sum_{t=1}^{n} \dfrac{C_t}{(1+r)^t}$ | $C_0$ coste inicial; $C_t$ coste del año $t$; $r$ tasa de descuento (0 si no se descuenta); $n$ años | $135.000 + 5\cdot105.000 = 660.000$ € → [→ §9.5](U1_temario_denso.md#95-ejemplo-resuelto-) |
| **TCO sin descuento, costes constantes** | $\text{TCO} = C_0 + n\cdot C_a$ | $C_a$ coste anual | Paquete: $220.000+5\cdot94.000=690.000$ € |
| **Punto de equilibrio entre dos opciones** | $n^* = \dfrac{C_{0,X}-C_{0,Y}}{C_{a,Y}-C_{a,X}}$ | X: más inversión inicial, menor coste anual | $\dfrac{150.000-10.000}{72.000-35.000}\approx 3{,}78$ años → [→ §14](U1_temario_denso.md#14-ejercicios) |
| **Conexiones punto a punto** | $\binom{n}{2}=\dfrac{n(n-1)}{2}$ | $n$ sistemas | $n=8\Rightarrow 28$ (con *hub*: 8) → [→ §11.4](U1_temario_denso.md#114-motivos-de-integración) |

---

## 3. Cuándo usar qué

| Situación | Opción | Por qué |
|---|---|---|
| Nadie ofrece lo que se necesita, o es ventaja competitiva única | **A medida** | Adaptación total; coste inicial y riesgo altos |
| Necesidad estándar, quiero previsibilidad y soporte del fabricante | **Cerrada / propietaria** | Soporte, rapidez; *lock-in* y licencias |
| Quiero control, evitar licencias y tengo perfiles técnicos | **Abierta (open source)** | Flexibilidad; coste en implantación y personal |
| Empezar rápido, poca inversión, no quiero operar infraestructura | **SaaS** | Opex, el proveedor opera; riesgo de dependencia y subidas |
| Horizonte corto (1-2 años) | Suele ganar la opción de **menor coste inicial** | El coste recurrente pesa poco |
| Horizonte largo (5+ años) | Suele ganar la de **menor coste recurrente** | La inversión inicial se amortiza |
| Varias apps deben compartir datos | **Integración** | Evita cuellos de botella manuales |
| Muchos sistemas conectados entre sí | **Hub / bus de integración** | Evita crecimiento cuadrático de interfaces |

| Para… | Usa |
|---|---|
| Gestionar un proyecto (alcance, plazos, costes, riesgos) | **PMI / PMBOK** |
| Ver qué procesos componen el ciclo de vida del software | **ISO/IEC 12207** |
| Comparar el coste completo de alternativas | **TCO** |

---

## 4. Checklist "debo saber…"

- [ ] Los 4 componentes del software y las 4 características de Pressman.
- [ ] Definir confiabilidad, mantenibilidad, eficiencia, usabilidad.
- [ ] Los retos que justifican la disciplina y qué fue la conferencia de 1968.
- [ ] Las definiciones de Bauer, Boehm, IEEE 610.12 y Navarro.
- [ ] Por qué la esencia del trabajo es el análisis y el diseño.
- [ ] Los 4 principios de la Teoría de Sistemas y los 6 pasos de análisis.
- [ ] Las 4 actividades fundamentales del proceso.
- [ ] Qué es el PMI, el PMBOK, la PMP; las 10 áreas y los 5 grupos.
- [ ] La estructura 5 + 8 + 4 de ISO/IEC 12207 y las 9 actividades del proceso de Desarrollo.
- [ ] Qué es la industrialización y la tabla industrial frente a académico.
- [ ] Definir TCO y calcularlo; explicar el iceberg.
- [ ] Clasificar aplicaciones por tipología y por modelo (medida/cerrada/abierta).
- [ ] Cuándo integrar y los 5 grupos de problemas de integración.
- [ ] Definir SaaS, hosted AM y software on demand.

---

## 5. Errores típicos de examen

1. Definir software como "programas" (olvidar datos, documentos, configuración).
2. Confundir *confiabilidad* con *cumplir la especificación*.
3. Decir que el software "no envejece": no se **desgasta**, pero se **degrada**.
4. Citar la definición IEEE como "610-12 de 1993": es **610.12, 1990** ⚠️.
5. Pensar que ágil "no diseña".
6. Confundir las **áreas de conocimiento** (10) con los **grupos de procesos** (5).
7. ⚠️ Mezclar la estructura 5 + 8 + 4 con la de ediciones posteriores de ISO 12207; en la unidad es 5 + 8 + 4 = 17.
8. Comparar alternativas solo por el precio de adquisición.
9. Creer que open source es "gratis" o que SaaS elimina costes de operación e integración.
10. Confundir *enterprise software* (procesos de toda la organización) con *enterprise infrastructure* (la plataforma).
11. Equiparar industrialización con burocracia.
12. Olvidar los requisitos de **operación** (backups, logs, alarmas) al hablar de software profesional.

---

## 6. Preguntas de autoevaluación

1. ¿Qué cuatro componentes forman el software?
2. ¿Por qué se dice que el software "no se desgasta" pero sí se degrada?
3. Enumera cuatro atributos de calidad y pon un ejemplo de dominio donde cada uno sea prioritario.
4. ¿Qué retos dieron origen a la Ingeniería del Software y qué ocurrió en 1968?
5. Resume la definición de la IEEE e identifica sus tres adjetivos clave.
6. ¿Qué es la parte "esencial" y cuál la "contingente" del trabajo de un ingeniero del software?
7. Nombra las cuatro actividades fundamentales del proceso y qué responde cada una.
8. ¿Cuántas áreas de conocimiento y cuántos grupos de procesos define el PMBOK (6.ª ed.), y cuáles son los grupos?
9. ¿Cuántos procesos tiene la estructura de ISO/IEC 12207 de la unidad y cómo se reparten?
10. Nombra las 9 actividades del proceso de Desarrollo en orden.
11. Cita cuatro diferencias entre software industrializado y programación académica.
12. ¿Qué es el TCO y qué muestra el "iceberg"?
13. Una opción cuesta 150.000 € de inicio y 35.000 €/año; otra, 10.000 € de inicio y 72.000 €/año. ¿Cuál es más barata a 3 y a 5 años, y cuándo se igualan?
14. ¿Cuándo conviene integrar sistemas? Da las cuatro condiciones.
15. Define SaaS y diferencia *hosted AM* de *software on demand*.

<details>
<summary><strong>Respuestas</strong></summary>

1. Instrucciones (programas), estructuras de datos, documentos y configuraciones/parametrizaciones.
2. Es intangible y no sufre fatiga ni caducidad física; pero cada cambio puede introducir defectos y el entorno evoluciona, de modo que su calidad interna empeora (degradación).
3. Por ejemplo: seguridad (sistema bancario), interactividad/eficiencia (videojuego), confiabilidad (dispositivo médico), mantenibilidad (sistema que cambia a menudo por normativa), usabilidad (aplicación para el público general).
4. Retrasos, sobrecostes, fallos de calidad, resultado distinto de lo esperado, mantenimiento costoso y dificultad para medir el progreso. En 1968 se celebró la conferencia (NATO, Garmisch) que se toma como punto de partida de la disciplina.
5. "Aplicación de un enfoque sistemático, disciplinado y cuantificable al desarrollo, operación y mantenimiento del software". Claves: sistemático, disciplinado, cuantificable.
6. Esencial: analizar necesidades y especificar el sistema (análisis y diseño). Contingente: lenguaje, máquina, despliegue.
7. Especificación (¿qué hacer?), desarrollo (¿cómo construirlo?), validación (¿es lo correcto?), evolución/mantenimiento (¿sigue siendo útil?).
8. 10 áreas y 5 grupos: inicio, planificación, ejecución, monitoreo y control, cierre.
9. 17: 5 principales, 8 de soporte y 4 organizativos.
10. Análisis de requisitos del sistema; análisis de requisitos del software; diseño de la arquitectura; diseño detallado; construcción (codificación); integración; pruebas; instalación; aceptación.
11. Por ejemplo: objetivo (valor al cliente frente a aprender), escalabilidad (alta frente a baja), automatización (extensa frente a mínima), clientes reales (sí frente a no), entorno de explotación (real frente a simulado), documentación (exhaustiva frente a opcional), reutilización (alta frente a baja).
12. Método para determinar costes directos e indirectos (y beneficios) de un producto durante su ciclo de vida completo. El iceberg indica que los costes ocultos exceden con mucho a los visibles.
13. A 3 años: 255.000 € frente a 226.000 € (gana la segunda). A 5 años: 325.000 € frente a 370.000 € (gana la primera). Se igualan en $140.000/37.000 \approx 3{,}78$ años.
14. Cuando no se puede cubrir la funcionalidad con una sola aplicación; cuando desarrollar cuesta más que integrar, gestionar y evolucionar la integración; cuando hay obligaciones externas (legales o regulatorias); y existe tecnología que permita integrar.
15. SaaS: modelo en el que las aplicaciones y los datos del cliente se alojan en servidores de un tercero, accedidos por Internet, y el proveedor se encarga de mantenimiento, operación y soporte. *Hosted AM*: el proveedor instala software comercial en sus servidores y lo ofrece por Internet (similar a ASP). *Software on demand*: el proveedor ofrece acceso por red a una copia de una aplicación creada específicamente para distribución SaaS.

</details>
