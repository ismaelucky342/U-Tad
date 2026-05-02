# AEC1 - Rediseño Inclusivo

## 1. Introducción y Web Elegida

Para esta práctica se nos pedía analizar una página pública en busca de oportunidades de mejora en su interfaz. 

Como estudiante universitario no he podido evitar elegir como página de referencia el portal de Becas y Ayudas al Estudio del Ministerio de Educación que es uno de los recursos digitales públicos de mayor impacto social en España, se estima que más de 1,3 millones de estudiantes solicitan algún tipo de beca o ayuda cada año a través de este sistema.

A pesar de su enorme relevancia, la interfaz presenta deficiencias graves y sistemáticas que comprometen directamente la experiencia del usuario y, en muchos casos, el acceso efectivo a un derecho reconocido. Además de por experiencia personal la elección de este sitio responde a tres criterios que considero objetivos:

**1.1 — Relevancia social e impacto real**

El portal no es un servicio opcional: para miles de familias, completar correctamente una solicitud de beca representa la diferencia entre poder costear o no los estudios de sus hijos. Un diseño deficiente en este contexto no es solo un problema de usabilidad, sino una barrera de acceso a derechos. Esto convierte el rediseño en un ejercicio con consecuencias éticas reales, lo que eleva la exigencia del análisis.

**1.2 — Densidad de problemas de usabilidad verificables**

Una primera exploración del sitio permite identificar violaciones heurísticas en prácticamente cada sección: menús de navegación con más de doce ítems de primer nivel sin agrupación lógica, formularios sin validación en tiempo real, textos legales sin jerarquía visual, ausencia de feedback ante errores del usuario y una arquitectura de información que no refleja los modelos mentales de sus usuarios reales (estudiantes y familias, no funcionarios).

**1.3 — Perfiles de usuario con alta diversidad funcional**

El público objetivo del portal es extremadamente heterogéneo: estudiantes universitarios nativos digitales, familias con bajo nivel de alfabetización digital, personas mayores que gestionan becas de sus hijos, usuarios con discapacidad visual o cognitiva, y ciudadanos cuya lengua materna no es el español. Esta diversidad hace que el sitio sea un escenario idóneo para aplicar principios de diseño universal e inclusivo.

### tabla de su estado actual (mi impresión previa al analisis)

| Dimensión | Estado actual |
|---|---|
| Diseño visual | Anticuado, sin sistema de diseño coherente |
| Arquitectura de información | Desestructurada, con solapamiento de categorías |
| Accesibilidad | Incumple criterios WCAG 2.1 nivel AA en múltiples puntos |
| Navegación por teclado | Parcialmente rota en los formularios |
| Responsive / Mobile | Adaptación deficiente en pantallas pequeñas |
| Feedback al usuario | Inexistente o tardío (solo al enviar el formulario) |
| Contraste de color | Insuficiente en textos secundarios y botones de acción |

---

## 2. Auditoría Heurística (Nielsen)

Aquí he identificado cinco violaciones de los 10 Heurísticos de Nielsen. Para cada una se especifica si constituye una brecha de ejecución (el sistema no permite al usuario realizar lo que quiere hacer) o una brecha de evaluación (el usuario no puede interpretar correctamente el estado o respuesta del sistema).

---

### Violación 1 — Heurístico #1: Visibilidad del estado del sistema
**Brecha de evaluación**

**Descripción del problema:**  Durante el proceso de solicitud de beca, el formulario consta de múltiples pasos (datos personales, datos académicos, datos económicos, documentación adjunta). Sin embargo, en ningún momento se muestra al usuario en qué paso se encuentra ni cuántos quedan por completar. No existe ningún indicador de progreso (stepper, barra de progresión, breadcrumb de pasos).

**Impacto:**  El usuario no sabe si está al principio o al final del proceso, lo que genera ansiedad y abandono prematuro. En estudios de usabilidad de formularios gubernamentales, la ausencia de indicador de progreso es una de las principales causas de abandono antes de la finalización.

**Evidencia:**  Al iniciar la solicitud el sistema muestra un formulario largo sin contextualizar cuántas secciones componen el proceso completo. Solo al hacer scroll al final de la página se intuye que hay más secciones.

**Propuesta de mejora:** Implementar un componente *stepper* horizontal visible en la parte superior de cada paso, con el número total de etapas, el nombre de cada una y el estado (completado / activo / pendiente). Reforzado con texto del tipo *"Paso 2 de 5: Datos económicos de la unidad familiar"*.

---

### Violación 2 — Heurístico #4: Consistencia y estándares
**Brecha de ejecución**

**Descripción del problema:** El portal utiliza simultáneamente un total tres estilos visuales distintos en diferentes secciones la página de inicio hereda estilos del portal general del Ministerio, el apartado de convocatorias usa una maquetación diferente con tablas HTML sin estilo, y el acceso al formulario de solicitud carga una aplicación con una interfaz completamente distinta (otro sistema, otra paleta, otra tipografía). El usuario experimenta tres interfaces distintas en un mismo flujo de tarea.

**Impacto:**  La inconsistencia rompe la confianza del usuario, que puede interpretar que ha abandonado el sitio oficial o que algo ha ido mal. Es especialmente desorientador para usuarios mayores o con baja experiencia digital.

**Evidencia:**  Al hacer clic en *"Solicitar beca"*, el usuario es redirigido a `sede.educacion.gob.es` con un cambio brusco de apariencia visual sin transición ni aviso previo. El logotipo, la tipografía y los colores cambian completamente.

**Propuesta de mejora:**  Unificar el sistema de diseño (tokens de color, tipografía, componentes) entre el portal informativo y la sede electrónica. Como mínimo, mantener el header institucional y la identidad visual de forma consistente en todas las pantallas del flujo.

---

### Violación 3 — Heurístico #6: Reconocer antes que recordar
**Brecha de ejecución**

**Descripción del problema:**  En el formulario de solicitud, varios campos requieren que el usuario introduzca códigos específicos: código del centro educativo, código de la titulación, código de la provincia de residencia habitual. Estos códigos no son conocidos por el usuario promedio, y el sistema no ofrece ningún mecanismo de búsqueda o autocompletado. El usuario debe salir del formulario, buscar el código en otra fuente, y volver.

**Impacto:**  Se genera una carga cognitiva innecesaria y elevada. El usuario debe recordar o anotar externamente información que el sistema podría proveer. Esta violación provoca errores frecuentes (código incorrecto) y abandono del proceso.

**Evidencia:**  El campo *"Código del centro"* muestra únicamente un input de texto libre con el placeholder *"Introduzca el código del centro"*, sin buscador, sin enlace a un directorio de centros, sin validación en tiempo real del código introducido.

**Propuesta de mejora:**  Sustituir los campos de código por selectores con búsqueda en tiempo real (*autocomplete*): el usuario escribe el nombre del centro o titulación y el sistema sugiere las opciones válidas. Esto elimina la necesidad de memorizar o buscar externamente cualquier código.

---

### Violación 4 — Heurístico #9: Ayudar a los usuarios a reconocer, diagnosticar y recuperarse de errores
**Brecha de evaluación**

**Descripción del problema:**  Cuando el usuario comete un error en el formulario (campo obligatorio vacío, formato incorrecto, fechas incoherentes), el sistema no muestra el mensaje de error hasta que intenta pasar al siguiente paso o enviar el formulario. En ese momento, aparece un listado genérico de errores en la parte superior de la página, sin resaltar visualmente los campos afectados y con mensajes técnicos poco comprensibles para el usuario general.

**Ejemplo de mensaje:**  *"Error: El campo NIF/NIE no cumple el formato requerido. Verifique que ha introducido correctamente su número de identificación fiscal según el modelo definido en el RD 338/1990."*

**Impacto:**  El usuario no sabe qué campo está mal ni cómo corregirlo. La referencia a normativa legal en el mensaje de error es completamente inútil desde el punto de vista de la usabilidad. Esto provoca frustración y reenvíos múltiples del formulario.

**Propuesta de mejora:**  Implementar validación en tiempo real campo a campo (al perder el foco). Los mensajes de error deben aparecer inmediatamente debajo del campo afectado, en lenguaje claro y accionable: *"El NIF debe tener 8 números seguidos de una letra. Ejemplo: 12345678A"*. Acompañar con icono de error y borde en color rojo con suficiente contraste.

---

### Violación 5 — Heurístico #2: Coincidencia entre el sistema y el mundo real
**Brecha de evaluación**

**Descripción del problema:**  La sección de convocatorias organiza las becas utilizando la nomenclatura administrativa interna del Ministerio, no el lenguaje que usan los ciudadanos para referirse a sus estudios. Se encuentran categorías como *"Enseñanzas Postobligatorias No Universitarias (EPNU)"*, *"Ciclos Formativos de Grado Superior (CFGS) — Régimen General"* o *"Másteres Universitarios Habilitantes"*, sin ninguna aclaración ni equivalencia en lenguaje cotidiano.

**Impacto:**  Un estudiante de bachillerato no sabe si su tipo de estudios corresponde a la categoría *"Enseñanzas Postobligatorias"* o a otra. La brecha entre el vocabulario del sistema y el modelo mental del usuario obliga a la lectura reiterada y genera errores de selección de convocatoria.

**Propuesta de mejora:**  Reorganizar las convocatorias usando el lenguaje del usuario: *"Estoy en Bachillerato"*, *"Estoy en la FP"*, *"Estoy en la Universidad"*, *"Tengo un máster"*. 

---

## 3. Benchmarking de Accesibilidad

Aqui he analizado tres portales competidores o equivalentes funcionales al Becas MEC, evaluando su nivel de conformidad WCAG 2.1, el uso de textos alternativos en imágenes y la navegación por teclado.

### Metodología

- **Herramientas usadas:** WAVE (WebAIM), axe DevTools, Lighthouse (Chrome), inspección manual con teclado
- **Criterios evaluados:** Nivel de conformidad declarado y verificado, calidad de textos alternativos, operabilidad por teclado (Tab, Shift+Tab, Enter, Escape, flechas), presencia de skip links, contraste de color
- **Navegadores usados para el test de teclado:** Chrome 124 y Firefox 126


### Competidor 1 — Agència de Gestió d'Ajuts Universitaris (AGAUR) — Generalitad de Cataluña
**URL:** [https://agaur.gencat.cat](https://agaur.gencat.cat)

| Criterio | Resultado |
|---|---|
| Conformidad WCAG declarada | Nivel AA |
| Conformidad WCAG verificada | Nivel AA parcial (algunos fallos en nivel A que menciono abajo) |
| Textos alternativos | Correctos en imágenes de contenido; decorativas marcadas con alt="" |
| Navegación por teclado | Funcional en su mayor parte; skip link al contenido principal presente |
| Contraste de color | Cumple en textos principales; falla en algunos textos sobre fondo gris claro |
| Idioma del documento | Declarado correctamente (lang="ca" / lang="es") |
| Formularios | Labels asociados correctamente a sus inputs en la mayoría de campos |

**mi valoración:**  AGAUR es para mi un referente sólido. Lo conocí por un familiar y sin duda creo que su portal cumple los criterios esenciales de nivel AA con pequeñas excepciones. La navegación por teclado permite completar las tareas principales sin ratón, aunque algunos modales de información no tienen gestión correcta del foco (el foco no se desplaza al modal al abrirlo). El skip link al contenido principal es funcional, algo que el portal MEC no implementa.

**punto diferencial positivo:** Ofrece la opción de cambiar el tamaño del texto desde la propia interfaz, sin depender de las preferencias del navegador.

---

### Competidor 2 — Becas del Santander
**URL:** [https://www.becas-santander.com](https://www.becas-santander.com)

| Criterio | Resultado |
|---|---|
| Conformidad WCAG declarada | Nivel AA (declaración genérica) |
| Conformidad WCAG verificada | Nivel A en la mayoría de criterios; AA no verificable sin login |
| Textos alternativos | Irregulares: imágenes de portada sin alt, imágenes de convocatorias con alt genérico ("imagen") |
| Navegación por teclado | Parcialmente funcional; el menú principal desplegable no es operable con teclado |
| Contraste de color | Falla en botones secundarios (texto rojo sobre fondo rosa claro: ratio ~2.8:1, por debajo del mínimo 4.5:1) |
| Idioma del documento | Declarado correctamente |
| Formularios | Labels presentes pero algunos inputs de filtro sin label accesible |

**valoración:**  El portal de Becas Santander también conocido por muchos estudiantes (en mi caso suado para idiomas) presenta una imagen visual más moderna que el MEC, pero sus problemas de accesibilidad son más graves en algunas áreas específicas. La navegabilidad por teclado está rota en el menú principal desplegable: al pulsar Tab sobre una categoría del menú, el submenú se despliega pero no puede navegarse con flechas ni con Tab, lo que obliga al usuario a usar el ratón. Los textos alternativos de las imágenes de convocatorias son genéricos e inútiles para un usuario de lector de pantalla.

**diferenciador:** El diseño responsive es notablemente mejor que el MEC en dispositivos móviles y se notan mas actualizaciones frecuentes.

---

### Competidor 3 — Ministerio de Educación de Portugal (DGEstE)
**URL:** [https://www.dgeste.mec.pt](https://www.dgeste.mec.pt)

| Criterio | Resultado |
|---|---|
| Conformidad WCAG declarada | Nivel AA (obligatorio por ley portuguesa desde 2019) |
| Conformidad WCAG verificada | Nivel AA con algunas excepciones documentadas |
| Textos alternativos | Bien implementados; imágenes decorativas correctamente omitidas del árbol de accesibilidad |
| Navegación por teclado | Buena: skip links presentes, orden de foco lógico, todos los controles interactivos alcanzan foco |
| Contraste de color | Cumple en todos los elementos principales verificados |
| Idioma del documento | Declarado correctamente, con opción de inglés |
| Formularios | Excelente: todos los campos con label, descripción de error en tiempo real, instrucciones previas al formulario |

**valoración :**  
El portal portugués es el más accesible de los tres analizados. La legislación portuguesa es bastante estricta y exige a todos los organismos públicos cumplir WCAG 2.1 AA con un mecanismo de reporte público de conformidad, lo que incentiva el cumplimiento real. La gestión del foco en los formularios es ejemplar: cuando aparece un error, el foco se desplaza automáticamente al primer campo con error, con un mensaje descriptivo leído por los lectores de pantalla. Es el modelo de referencia más cercano a lo que debería ser el portal MEC.

**punto diferencial:** Publica un informe anual de accesibilidad con los puntos pendientes de mejora, demostrando un compromiso real con el proceso.

---

## 4. User Personas e Inclusión

### Persona 1 — Ismael Frenandez

**Datos demográficos**
- **Edad:** 22 años
- **Localización:** Madrid, España
- **Estudios:** 1º de Grado en Software, Universidad de tecnología y arte digital 
- **Ocupación:** Estudiante a tiempo completo; emprendedor
- **Dispositivo principal:** Smartphone Android (Xiaomi Redmi Note 12); accede a internet principalmente desde el móvil
- **Experiencia digital:** Alta en redes sociales y apps móviles; media-baja en webs institucionales y trámites administrativos

**Situación personal**  
Ismael es el mayor de sus hermanos y por tanto el primero en ir a la universidad en esta era digital. Sus padres trabajan en el sector sanitario; Ismael ha decidido que quiere hacerse cargo del coste de sus estudios por lo que la beca general del MEC es imprescindible para que el pueda costear los desplazamientos, los materiales y las tasas universitarias. Es el quien gestiona el trámite de la solicitud, sin ayuda de nadie del entorno familiar. 

**Metas**
- Solicitar la beca antes de que se cierre el plazo sin cometer errores que la invaliden
- Entender qué documentación tiene que presentar y en qué formato
- Saber en qué punto está su solicitud una vez enviada
- Recibir la resolución con tiempo suficiente para planificar el año académico

**Frustraciones actuales con el portal**
- La web no está bien adaptada al móvil: los formularios desbordan la pantalla y algunos botones no son pulsables
- No entiende en qué convocatoria debe solicitar (terminología administrativa incomprensible)
- No sabe qué documentos necesita hasta que llega al paso final del formulario
- El formulario no guarda el progreso: si se cierra accidentalmente, pierde todo lo introducido

**Cita representativa:**  
*"Llevo dos horas intentando enviar la solicitud y al final me dijo que había un error pero no me decía dónde. Al día siguiente lo intenté desde el ordenador del instituto y ya pude, pero no sé qué hice diferente."*

**Conexión con el rediseño:**  
Ismael representa al usuario mayoritario real del portal: joven, mobile-first, con alfabetización digital asimétrica (alta en entornos familiares, baja en contextos institucionales) y con mucho en juego. El rediseño debe priorizar el diseño responsive, el lenguaje claro, la indicación de documentación necesaria al inicio del proceso y el guardado automático del formulario.

---

### Persona 2 — Manuel Ortega

**Datos demográficos**
- **Edad:** 58 años
- **Localización:** Navaluenga, avila, municipio rural de ~10.000 habitantes
- **Ocupación:** Agricultor, jubilado anticipado por incapacidad parcial
- **Estudios:** Graduado escolar
- **Dispositivo principal:** Ordenador de sobremesa compartido con su mujer, conexión ADSL con velocidad irregular
- **Experiencia digital:** Baja, usa el correo electrónico y WhatsApp, nunca ha realizado un trámite online sin ayuda
- **Discapacidad:** Baja visión severa (agudeza visual del 20% en ambos ojos tras una retinopatía diabética). Usa el magnificador de Windows al 200% y en ocasiones el lector de pantalla NVDA, aunque no tiene formación específica en su uso

**Situación personal**  
Manuel gestiona la solicitud de beca de su hija Carmen, que estudia un Ciclo Formativo de Grado Superior de Administración en la capital de provincia. La familia no tiene recursos para contratar a un gestor y el único servicio de atención presencial está en la delegación provincial, a 40 km de su pueblo. Manuel intenta hacer la solicitud desde casa, ampliando la pantalla al máximo y ayudándose de su mujer para leer los textos.

**Metas**
- Completar la solicitud de beca de su hija sin tener que desplazarse a la ciudad
- Entender qué se le está pidiendo en cada paso del formulario
- Asegurarse de que el trámite ha quedado registrado correctamente
- No tener que repetir el proceso por errores que no comprende

**Necesidades de accesibilidad**
- Textos con tamaño mínimo de 16px, ampliables sin pérdida de maquetación
- Contraste alto en todos los elementos (mínimo 7:1 para nivel AAA)
- Sin dependencia del color como único canal de información
- Compatible con magnificador de pantalla sin desbordes horizontales
- Compatible con NVDA: etiquetas en formularios, anuncio de errores, orden de lectura lógico
- Sin límites de tiempo en el formulario (o con posibilidad de extenderlos)
- Sin animaciones ni elementos que destellen (riesgo de distorsión visual)

**Frustraciones actuales con el portal**
- Al ampliar la pantalla al 200%, el layout se rompe y el texto se superpone
- Los mensajes de error son en color rojo sin icono ni texto alternativo descriptivo
- El formulario tiene un *timeout* de sesión de 20 minutos sin aviso previo
- El NVDA no lee correctamente los campos del formulario: no anuncia si son obligatorios ni el formato requerido

**Cita representativa:**  
*"Me fui a buscar la documentación del banco y cuando volví me había cerrado la sesión. Perdí todo. Llamé al teléfono de atención y me dijeron que tenía que volver a empezar. Eso no puede ser."*

**Conexión con el rediseño:**  
Manuel representa a un segmento de usuarios frecuentemente ignorado en el diseño de portales públicos: edad media-alta, baja alfabetización digital, necesidades de accesibilidad visual y contexto rural con limitaciones de conectividad y acceso presencial. Su perfil justifica directamente decisiones de diseño universal como el alto contraste, la compatibilidad con tecnologías de apoyo, la eliminación de timeouts agresivos, el guardado automático del progreso y el uso de iconos junto al color para comunicar estados.

---

## 5. Arquitectura y Leyes de UX

### 5.1 Diagnóstico de la arquitectura actual

La estructura de navegación actual del portal presenta los siguientes problemas estructurales:

- El menú principal contiene 14 ítems de primer nivel sin agrupación jerárquica clara
- Existen rutas duplicadas: la misma convocatoria puede encontrarse a través de tres caminos diferentes
- La sección *"Preguntas frecuentes"* está enterrada en el quinto nivel de navegación
- El flujo de solicitud mezcla información, documentación y formulario en páginas distintas sin conexión explícita
- No existe un flujo guiado: el usuario debe descubrir por sí mismo los pasos necesarios

### 5.2 Aplicación de las Leyes de UX


**Ley de Hick — Reducción de opciones para acelerar la decisión**

> *"El tiempo que se tarda en tomar una decisión aumenta con el número y la complejidad de las opciones disponibles."* — William Edmund Hick, 1952

**Problema actual:** El menú de primer nivel presenta 14 opciones simultáneas. A esto se suma que la sección de convocatorias lista todas las becas disponibles (universitarias, no universitarias, másters, doctorados, educación especial, idiomas, movilidad…) sin ningún filtro o segmentación previa. El usuario debe procesar toda la oferta para encontrar la que le corresponde.

**Aplicación en el rediseño:**  La nueva arquitectura comienza con una pregunta de segmentación que reduce drásticamente el espacio de decisión antes de mostrar opciones:

```
¿Qué tipo de estudios estás cursando?

[ Bachillerato / FP Básica ]    [ FP Grado Medio o Superior ]
[ Universidad — Grado ]         [ Universidad — Máster ]
[ Educación Especial ]          [ Otra situación ]
```

Esta pantalla de entrada reduce 14 ítems de menú a 6 opciones mutuamente excluyentes. Una vez seleccionada, el sistema muestra únicamente las convocatorias relevantes para ese perfil. El menú principal queda simplificado a 4 secciones: *Solicitar*, *Mi solicitud*, *Información* y *Ayuda*.


**Ley de Fitts — Tamaño y posición de los objetivos interactivos**

> *"El tiempo necesario para alcanzar un objetivo es función de la distancia al objetivo y de su tamaño."* — Paul Fitts, 1954

**Problema actual:** Los botones de acción principal (*"Solicitar beca"*, *"Acceder a mi solicitud"*) son elementos de tamaño reducido, mal posicionados y en ocasiones desplazados por elementos de menor relevancia. En mobile, los botones no cumplen el mínimo de 44x44px recomendado por las guías de accesibilidad táctil de Apple y Google. Los formularios contienen campos de selección (dropdowns, checkboxes) con áreas de toque mínimas.

**Aplicación en el rediseño:**  
- Botón de acción principal siempre visible, con un tamaño mínimo de 48x48px en mobile y 36px de altura en desktop
- Botones de acción primaria diferenciados visualmente de los secundarios mediante tamaño, no solo color
- En formularios, los labels clicables amplían el área de toque al campo completo (no solo al input)
- La CTA *"Solicitar ahora"* aparece fija en la parte inferior de la pantalla en mobile (patrón *sticky bottom bar*)
- Elementos destructivos (*"Cancelar solicitud"*, *"Borrar datos"*) ubicados lejos de los de confirmación y con tamaño reducido deliberadamente

**Ley de Miller — Límite de la memoria de trabajo**

> *"La capacidad de la memoria de trabajo humana está limitada a aproximadamente 7 elementos (±2)."* — George Miller, 1956

**Problema actual:** El formulario de solicitud presenta hasta 23 campos en una misma pantalla sin agrupación visual. La sección de documentación exige adjuntar hasta 11 archivos distintos listados en un solo bloque de texto. El usuario debe mantener en mente qué ha completado, qué le falta y qué ha enviado, sin ningún apoyo externo del sistema.

**Aplicación en el rediseño:**  
- El formulario se divide en pasos temáticos de no más de 6-7 campos cada uno, agrupados por proximidad semántica (datos personales / datos académicos / datos económicos / documentación / revisión y envío)
- Cada grupo de campos se presenta en una tarjeta visual delimitada con un título claro
- La sección de documentación organiza los archivos requeridos en categorías de no más de 4 documentos por grupo, con checkboxes de estado (adjunto / pendiente)
- En la pantalla de revisión final se muestra un resumen estructurado de toda la información introducida, organizado en las mismas categorías que el formulario, para facilitar la verificación antes del envío

### 5.3 Nueva estructura de navegación propuesta

```
PORTAL BECAS MEC — mi propuesta

INICIO
   - Segmentador de perfil (¿Qué estudios cursa?)
   - Convocatorias abiertas (filtradas por perfil)
   - Acceso rápido: Mi solicitud / Estado de resolución
SOLICITAR BECA
   - Paso 1: ¿Qué beca me corresponde? (asistente de selección)
   - Paso 2: Documentación necesaria (lista previa al formulario)
   - Paso 3: Formulario de solicitud (dividido en 5 sub-pasos)
   - Paso 4: Confirmación y número de registro
- MI SOLICITUD
- Estado actual (con indicador visual claro)
   - Documentación enviada y pendiente
   - Resolución y notificaciones
   - Reclamaciones y subsanaciones
INFORMACIÓN
   - ¿Quién puede solicitar? (por tipo de estudios)
   - Cuantías y criterios económicos
   - Plazos de convocatoria
   - Preguntas frecuentes
AYUDA
   - Chat de ayuda (o asistente virtual)
   - Teléfono y email de contacto
   - Cita previa presencial
   - Guías y tutoriales en vídeo
```

---

## 6. Rediseño Visual y Técnico

### 6.1 Sistema de diseño 

**Paleta de colores**

| Token | Color | Hexacecimal | Uso | contraste|
|---|---|---|---|---|
| `--color-primary` | Azul institucional | `#0057A8` | Botones primarios, enlaces, CTA | 7.2:1  AAA |
| `--color-primary-dark` | Azul oscuro | `#003D7A` | Hover estados, texto sobre fondo claro | 10.1:1  AAA |
| `--color-secondary` | Verde confirmación | `#1A7A3C` | Estados completados, éxito | 5.8:1  AA |
| `--color-warning` | Naranja alerta | `#B45309` | Advertencias, plazos próximos | 4.8:1  AA |
| `--color-error` | Rojo error | `#B91C1C` | Errores de validación | 5.9:1  AA |
| `--color-neutral-100` | Gris muy claro | `#F5F7FA` | Fondos de sección, tarjetas | — |
| `--color-neutral-700` | Gris texto | `#374151` | Texto cuerpo | 10.7:1  AAA |
| `--color-neutral-900` | Casi negro | `#111827` | Títulos, texto principal | 18.4:1  AAA |

> **principio aplicado:** Ningún estado del sistema se comunica únicamente mediante color. Todos los estados de error, éxito y advertencia van acompañados de un icono y un texto descriptivo. Esto cumple el criterio WCAG 2.1 — 1.4.1 Uso del color (Nivel A).

---

**Tipografía**

| Rol | Fuente | Peso | Tamaño base |
|---|---|---|---|
| Títulos | `IBM Plex Sans` | 700 | 32px (H1) / 24px (H2) / 20px (H3) |
| Cuerpo | `IBM Plex Sans` | 400 | 16px (mínimo) |
| UI / Labels | `IBM Plex Sans` | 500 | 14px (mínimo en labels) |
| Código / Referencias | `IBM Plex Mono` | 400 | 14px |

> ¿Porque aplico esto? IBM Plex Sans es una fuente Sans Serif diseñada para alta legibilidad en pantalla, open source (sin coste de licencia para el sector público), con excelente soporte de caracteres especiales y diacríticos del español, y disponible en Google Fonts. Cumple el criterio WCAG de fuente legible y evita los problemas de accesibilidad asociados a fuentes decorativas o con trazos muy finos.

---

**Grid y espaciado**

- Sistema de 12 columnas con gutters de 24px en desktop y 16px en mobile
- Unidad base de espaciado: 8px (múltiplos: 8, 16, 24, 32, 48, 64)
- Contenedor máximo: 1200px centrado
- Padding lateral en mobile: 16px
- Área de contenido principal en desktop: 8 columnas (máx. 768px) para mejorar la legibilidad de textos largos

---

### 6.2 Componentes rediseñados — Descripción

**Formulario de solicitud — Stepper**  
Es un componente de navegación horizontal en la parte superior que muestra los 5 pasos del formulario. El paso activo se indica mediante: 
- (1) color primario de relleno
- (2) texto en negrita
- (3) icono de paso activo. 

Los pasos completados muestran un icono de check. Los pasos pendientes están en gris neutro. En mobile, el stepper se adapta a una versión compacta que muestra el paso actual y el siguiente.

**Campos de formulario**  
- Label siempre visible encima del campo (nunca dentro como placeholder que desaparece)
- Texto de ayuda opcional debajo del campo en gris neutro, tamaño 14px
- Estado de error: borde rojo + icono de alerta + mensaje de error debajo del campo
- Estado de éxito: borde verde + icono de check
- Los campos obligatorios se indican con asterisco rojo Y con texto "(obligatorio)" para no depender únicamente del símbolo

**Tarjetas de convocatoria**  
Cada beca se presenta en una tarjeta con: (1) título de la convocatoria en lenguaje claro, (2) tipo de estudios aplicable, (3) fecha límite destacada con icono de calendario, (4) estado (abierta / cerrada / próximamente) con badge de color + icono, (5) botón de acción con CTA clara. Las tarjetas son completamente navegables por teclado y tienen un foco visible claramente definido.

**Sistema de notificaciones de estado**  
El estado de la solicitud se presenta mediante un componente de línea de tiempo vertical que muestra las etapas del proceso (recibida / en revisión / resuelta favorablemente / resuelta desfavorablemente / abonada). Cada etapa tiene un icono, un color de estado y una fecha. El estado actual se resalta visualmente. El componente es compatible con lectores de pantalla y anuncia el estado actual al cargar la página.

---

### 6.3 Mejoras en arquitectura de la información

- **Documentación requerida al inicio:** Antes de acceder al formulario, el usuario ve una lista de los documentos que necesitará adjuntar, con formato requerido y ejemplos. Esto elimina el abandono a mitad del proceso por falta de documentación.
- **Guardado automático:** El formulario guarda automáticamente el progreso cada vez que el usuario pasa de campo. Si la sesión expira, los datos se recuperan al volver a autenticarse.
- **Aviso de timeout:** 5 minutos antes de que expire la sesión, el sistema muestra un modal de aviso con botón para extender la sesión.
- **Resumen previo al envío:** La última pantalla muestra un resumen completo de todos los datos introducidos, organizado por secciones, antes de confirmar el envío. Permite editar cualquier sección directamente desde el resumen.
- **Confirmación con número de registro:** Tras el envío, se muestra una pantalla de confirmación con el número de registro, la fecha y hora, y un enlace para descargar el resguardo en PDF. Se envía también un correo de confirmación.

---

## 7. Validación de Usabilidad

### 7.1 Dimensión Objetiva — Métricas de eficiencia

Para la dimensión objetiva de la usabilidad hago referencia a la capacidad del sistema para permitir al usuario completar tareas con eficacia, eficiencia y sin errores. Se evalúa mediante métricas cuantificables.

| Métrica | Web actual (estimación) | Propuesta rediseño | Mejora |
|---|---|---|---|
| Tiempo medio en completar solicitud | ~45-60 min | ~20-25 min | ~60% de reducción |
| Tasa de abandono estimada en el formulario | ~35% | ~15% | -20 pp |
| Número de clics hasta iniciar el formulario | 7-9 clics | 3-4 clics | ~55% de reducción |
| Ítems de menú primer nivel | 14 | 4 | -71% |
| Campos por pantalla (máximo) | 23 | 7 | -70% |
| Compatibilidad con teclado | Parcial (~40% de flujo) | Completa (100% de flujo) | +60 pp |
| Contraste mínimo verificado | ~2.8:1 (falla AA) | 4.8:1 (cumple AA) | Cumplimiento normativo |
| Errores de validación anunciados a lector pantalla | 0% | 100% | +100 pp |
| Pasos hasta la pantalla de confirmación | Sin indicador | 5 pasos visibles | Nuevo |

**Análisis de la mejora objetiva:**  
La reducción más significativa la veo en la carga cognitiva durante el formulario. Pasar de 23 campos en pantalla a un máximo de 7 por paso no solo reduce el tiempo de cumplimentación, sino que también reduce drásticamente la tasa de error: los usuarios cometen más errores cuando deben gestionar muchos elementos simultáneamente (efecto directo de la Ley de Miller). La reducción del menú principal de 14 a 4 ítems, apoyada por el segmentador inicial de perfil, aplica la Ley de Hick y reduce el tiempo de orientación inicial del usuario.

---

### 7.2 Dimensión Subjetiva — Satisfacción y confianza percibida

La dimensión subjetiva hace referencia a la experiencia emocional del usuario durante la interacción: la confianza que le genera el sistema, la sensación de control, la ausencia de ansiedad y la satisfacción al completar la tarea.

**Factores de mejora subjetiva en el rediseño:**

**Confianza y credibilidad:**  
El diseño actual mezcla identidades visuales de distintos sistemas, lo que genera desconfianza en usuarios no expertos (¿estoy en el sitio oficial?). El rediseño unifica la identidad visual en todo el flujo, usa el escudo institucional de forma consistente y mantiene el color azul institucional como elemento de reconocimiento. El usuario sabe en todo momento que está en un portal del Ministerio.

**Sensación de control y progreso:**  
La ausencia de stepper en el formulario actual genera angustia: el usuario no sabe cuánto le queda. El rediseño, con su indicador de progreso en 5 pasos claramente nombrados, transforma la experiencia de un proceso opaco e interminable en un camino estructurado con final visible.

**Tolerancia al error y recuperación:**  
En el sistema actual, un error en el formulario puede suponer empezar desde cero (por timeout de sesión o por error de validación al final). Esta posibilidad genera ansiedad durante todo el proceso de cumplimentación. El guardado automático, los mensajes de error en tiempo real y el aviso de timeout eliminan esta fuente de estrés, haciendo que el usuario se sienta más seguro para tomarse el tiempo que necesita.

**Lenguaje y tono:**  
El cambio de terminología administrativa a lenguaje ciudadano tiene un impacto subjetivo directo: el usuario siente que el portal está pensado para él, no para los funcionarios que lo gestionan. Esto mejora la percepción de cercanía institucional y reduce la sensación de exclusión que experimentan especialmente usuarios con menor nivel educativo o digital.

**Inclusión real como mejora subjetiva:**  
Para Manuel (Persona 2), el rediseño supone la diferencia entre poder realizar el trámite de forma autónoma desde su domicilio o tener que desplazarse 40km o pedir ayuda externa. La compatibilidad con su magnificador de pantalla y con el lector NVDA no es solo un requisito técnico de accesibilidad: es la condición necesaria para que este usuario experimente el portal como un recurso al que tiene derecho y no como una barrera.

---

### 7.3 Conclusión comparativa

El rediseño que he propuesto no supone únicamente una mejora estética o de modernización visual. Representa un cambio estructural en la relación entre la institución y el ciudadano a través de su interfaz digital. Las mejoras en accesibilidad, arquitectura de información y lenguaje transforman un portal que actualmente excluye a parte de su público objetivo en uno que puede ser usado de forma autónoma por la diversidad real de usuarios que dependen de él.

La aplicación sistemática de las leyes de Hick, Fitts y Miller creo que no es para nada decorativa cada decisión de diseño (número de ítems en menú, tamaño de botones, agrupación de campos) tiene una justificación en la psicología cognitiva y un impacto medible en la eficiencia y la satisfacción del usuario. El cumplimiento de WCAG 2.1 AA, además de ser un requisito legal para los portales de la Administración General del Estado desde el RD 1112/2018, es una condición de equidad: una beca pública debe ser solicitada por todos los ciudadanos que tienen derecho a ella, independientemente de sus capacidades o su nivel de experiencia digital.

---

## Referencias

- Nielsen, J. (1994). *10 Usability Heuristics for User Interface Design*. Nielsen Norman Group.
- Hick, W. E. (1952). On the rate of gain of information. *Quarterly Journal of Experimental Psychology*, 4(1), 11–26.
- Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. *Journal of Experimental Psychology*, 47(6), 381–391.
- Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97.
- W3C Web Accessibility Initiative. (2018). *Web Content Accessibility Guidelines (WCAG) 2.1*. https://www.w3.org/TR/WCAG21/
- Real Decreto 1112/2018, de 7 de septiembre, sobre accesibilidad de los sitios web y aplicaciones para dispositivos móviles del sector público. *BOE* núm. 227, de 18 de septiembre de 2018.
- WebAIM. (2024). *WAVE Web Accessibility Evaluation Tool*. https://wave.webaim.org/
- Norman, D. A. (2013). *The Design of Everyday Things* (Revised ed.). Basic Books.

---

![alt text](image.png)