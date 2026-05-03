═══════════════════════════════════════════════════════════════════════════════
GUIÓN DE GRABACIÓN - INICIALIZACIÓN DEL REPOSITORIO EVENTLINK FRONTEND
═══════════════════════════════════════════════════════════════════════════════

Duración estimada: 10-12 minutos
Presentador: Ismael Hernández
Fecha: 3 de mayo de 2026

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 1] INTRODUCCIÓN - 1 minuto
───────────────────────────────────────────────────────────────────────────────

Hola, soy Ismael Hernández, y voy a presentar el trabajo que realicé en la fase 
inicial del proyecto EventLink. Específicamente, quiero mostrarles cómo configuré 
el repositorio del frontend para que todo el equipo tuviera una base común y 
estandarizada desde el principio.

EventLink es un marketplace de dos lados que conecta creadores de eventos con 
patrocinadores. Somos un equipo de seis desarrolladores, y para poder trabajar 
todos en paralelo sin conflictos, necesitábamos establecer una base sólida con 
las mismas herramientas, las mismas dependencias y, lo más importante, los mismos 
estándares de desarrollo.

Mi tarea fue: Como equipo de desarrollo, quiero tener un repositorio configurado 
con React, TypeScript, Vite, CSS y las dependencias necesarias, para que todos 
los miembros puedan comenzar a desarrollar sobre una base común y estandarizada.

Completé seis subtareas para hacer esto realidad. Voy a mostrarles cada una.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 2] PANTALLA 1: JIRA - EL TABLERO CON LAS SUBTAREAS - 2 minutos
───────────────────────────────────────────────────────────────────────────────

[INIDICACIÓN: Abre Jira o tu gestor de tareas y muestra el épica/issue EVB-102 
o similar con las 6 subtareas. Mantén la pantalla visible mientras hablas]

Primero, voy a mostrarles el tablero de Jira donde está toda la información de 
mi tarea. Aquí pueden ver la historia de usuario principal con más lado seis 
subtareas que completé al cien por cien.

Cada subtarea representa un paso específico en la configuración:

EVB-97: Crear repositorio en la plataforma de control de versiones. Esto era 
inicializar el repositorio en GitHub con la estructura base.

EVB-96: Configurar proyecto base con Vite, React y TypeScript. El scaffold inicial 
usando Vite como bundler, React como librería de UI, y TypeScript como lenguaje 
tipado.

EVB-98: Instalar dependencias esenciales del proyecto. Aquí instalé todas las 
librerías necesarias: React Router para navegación, Material UI para componentes, 
ESLint y Prettier para code quality.

EVB-99: Agregar y configurar soporte para CSS. Decidimos usar una mezcla de 
Material UI theming con estilos CSS modulares para cada componente.

EVB-100: Configurar scripts de desarrollo y build. Aquí creé los comandos npm 
para levantar el servidor local, buildear para producción, linting y preview.

EVB-101: Configurar archivo .gitignore y convenciones básicas. Establecer qué 
archivos ignora Git y definir reglas básicas para los commits usando Conventional 
Commits.

Todas las subtareas están marcadas como Done. Voy a mostrarles ahora cómo quedó 
el repositorio.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 3] PANTALLA 2: REPOSITORIO - ESTRUCTURA DEL PROYECTO - 2.5 minutos
───────────────────────────────────────────────────────────────────────────────

[INDICACIÓN: Abre VS Code o un terminal. Muestra la estructura del proyecto. 
Puedes usar 'tree' o simplemente abrir el explorador de archivos en VS Code]

Aquí está el repositorio. Voy a mostrarles la estructura que quedó después de 
la configuración inicial.

[MUESTRA la carpeta raíz del proyecto]

Tenemos varios archivos de configuración en la raíz:

Primero, vite.config.ts. Este es el corazón de la build. Aquí configuré Vite 
para que use el plugin de React y establecí un alias de imports. Con eso podemos 
escribir 'import desde @/components' en lugar de '../../../components'. Es más 
limpio y escalable.

[MUESTRA el contenido de vite.config.ts sobre la marcha, o mantén el panel 
visible]

Tenemos tsconfig.json y tsconfig.app.json que configura cómo TypeScript compila 
el código. Es importante para que todos tengamos las mismas reglas de tipo.

También está .eslintrc.json y .prettierrc, que son reglas de linting y formato 
automático de código. Así cuando hace un commit, el código se formatea 
automáticamente.

El archivo más importante es package.json. Aquí están todas las dependencias que 
instalé. React 19, React DOM, React Router DOM para navegación entre páginas, 
Material UI y Emotion para los componentes y estilos, y todas las herramientas 
de desarrollo necesarias.

[MUESTRA package.json, esp. la sección de scripts]

Aquí están los scripts que configuré:

'npm run dev' levanta el servidor local en modo desarrollo. Vite hace hot module 
replacement, así que cada vez que cambio código, se recarga automáticamente sin 
perder el estado.

'npm run build' crea la versión optimizada y minificada para producción.

'npm run lint' ejecuta ESLint para validar que el código siga las reglas.

'npm run preview' te muestra cómo se ve el build de producción en local.

Aquí está el .gitignore. Básicamente ignoramos node_modules porque eso se instala 
con npm, la carpeta dist porque es generada, variables de entorno locales, y 
archivos del IDE.

[MUESTRA la carpeta src]

Dentro de src es donde está todo el código de la aplicación. Tenemos módulos por 
features:

- auth: Autenticación, login, registro, logout
- creators: Todo lo relacionado con creadores de eventos
- sponsors: Panel de patrocinadores
- chat: La sala de negociación, el deal room donde patrocinadores y creadores 
  negocian
- events: Componentes compartidos relacionados con eventos
- shared: Utilidades comunes, landing page, componentes reutilizables
- theme: La configuración del tema de Material UI

App.tsx es el componente raíz donde están las rutas principales de la aplicación. 
Main.tsx es el entry point, donde se monta React en el DOM.

Esta estructura permite que seis personas trabajen en paralelo en diferentes 
features sin pisarse.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 4] PANTALLA 3: LEVANTANDO EL SERVIDOR - 1.5 minutos
───────────────────────────────────────────────────────────────────────────────

[INDICACIÓN: Abre una terminal en la carpeta del proyecto. Ejecuta 'npm run dev']

Ahora voy a levantar el servidor de desarrollo para que vean la aplicación 
funcionando.

[ESCRIBE en la terminal]

npm run dev

[ESPERA a que Vite inicie. Deberías ver algo como:]
"VITE v8.0.1  ready in 245 ms
  ➜  Local:   http://localhost:5173/"

La velocidad aquí es importante. Vite levanta en menos de 300 milisegundos. Con 
Webpack tardaríamos 5 o 10 segundos. Eso es la diferencia entre tener una buena 
experiencia de desarrollo y estar viendo una pantalla de carga cada vez que haces 
un cambio.

Ahora abro el navegador en localhost:5173.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 5] PANTALLA 4: FRONTEND FUNCIONANDO - SPONSOR VIEW - 2 minutos
───────────────────────────────────────────────────────────────────────────────

[INDICACIÓN: El navegador debería mostrar la app de EventLink. Si la app tiene 
una landing page o login, muéstralo. Si tienes un feed de eventos para patrocinadores, 
navega a eso. Si no, muestra lo que haya]

Aquí está la aplicación funcionando. Vemos la interfaz del feed de descubrimiento 
donde los patrocinadores pueden ver eventos.

[MUESTRA la pantalla. Explica lo que ves]

Tienen eventos listados con imágenes, títulos, fechas, ubicaciones. Debajo de 
cada evento, pueden ver los paquetes de patrocinio disponibles. Cuando un 
patrocinador está interesado, puede enviar una propuesta.

Toda esta interfaz está hecha con Material UI. Los botones, las tarjetas, los 
iconos. Todo consiste usado componentes pre-construidos de MUI, pero 
personalizados con nuestro tema.

La razón por la que usamos Material UI es que en un equipo pequeño no tenemos 
tiempo para estar reinventando componentes. MUI nos proporciona componentes 
testeados, accesibles, y con documentación excelente. Eso nos permite enfocarnos 
en la lógica del negocio, no en pasar horas diseñando un botón que funcione bien 
en todos los navegadores.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 6] PANTALLA 5: FRONTEND FUNCIONANDO - CREATOR VIEW - 1.5 minutos
───────────────────────────────────────────────────────────────────────────────

[INDICACIÓN: Navega a la vista de creadores. Muestra el dashboard, la lista de 
eventos, el formulario de crear evento, o lo que sea que haya]

Ahora cambiamos al panel de creadores. Aquí está su dashboard donde pueden ver 
los eventos que han creado o crear nuevos.

[MUESTRA la pantalla]

Pueden listar los eventos, ver propuestas que han recibido de patrocinadores, 
aceptarlas, rechazarlas, o hacer contrapropuestas.

TypeScript aquí juega un papel importante. Cada acción que hacemos, cada click 
en un botón, cada dato que enviamos al servidor, está tipado. Si intento hacer 
algo que no debería, TypeScript me lo detiene en el editor rojo como un error. 
Eso previene bugs que de otro modo llegarían a producción.

React Router es lo que permite navegar entre estas vistas. Puedo cambiar entre 
el panel de sponsor y el panel de creador sin que se recargue toda la página. 
Solo actualiza la parte que cambió. Eso es lo que hace que se sienta como una 
aplicación desktop, no como un sitio web.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 7] PANTALLA 6: DEAL ROOM / CHAT - 1 minuto
───────────────────────────────────────────────────────────────────────────────

[INDICACIÓN: Si existe, navega a una vista de deal room o chat para mostrar 
cómo se ve. Si no existe, describe lo que habrá]

Y aquí está el deal room, la sala de negociación. Cuando un patrocinador envía 
una propuesta y un creador la acepta, abren en este espacio para comunicarse.

[MUESTRA la vista]

Es un chat threaded donde pueden negociar términos, hablar sobre beneficios, 
precios, todo en contexto de la propuesta específica. Material UI nos ayuda aquí 
también con componentes para mensajes, avatares, y UI responsiva.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 8] PANTALLA 7: CÓDIGO - TYPESCRIPT EN ACCIÓN - 1 minuto
───────────────────────────────────────────────────────────────────────────────

[INDICACIÓN: Abre un archivo .tsx o .ts del proyecto en el editor. Muestra 
algún componente o hook con tipos. Haz autocompletar para mostar cómo TypeScript 
ayuda]

Aquí está el código. Este es un componente React en TypeScript. 

[MUESTRA el archivo]

Ven como cada props está tipado. Cada función sabe qué tipo de datos recibe. Si 
intento pasar un tipo incorrecto, TypeScript me lo marca inmediatamente.

Si hago autocompletar, TypeScript me sugiere automáticamente qué propiedades 
puedo acceder en este objeto. Eso acelera mucho el desarrollo.

Comparenlo con JavaScript puro: estarías escribiendo sin ayuda, haciendo pruebas 
en el navegador, y descubriendo errores cuando el usuario los encuentra.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 9] PANTALLA 8: VOLVEMOS A JIRA - RESUMEN DE LO COMPLETADO - 1 minuto
───────────────────────────────────────────────────────────────────────────────

[INDICACIÓN: Vuelve a mostrar Jira con las subtareas]

Recapitulando, estas fueron las seis subtareas que completé:

EVB-97: Crear repositorio ✓
EVB-96: Configurar Vite, React y TypeScript ✓
EVB-98: Instalar dependencias ✓
EVB-99: Configurar CSS ✓
EVB-100: Configurar scripts de desarrollo y build ✓
EVB-101: Configurar .gitignore y convenciones ✓

Todo al cien por cien.

El resultado es que el equipo tiene:
- Un repositorio limpio y organizado
- Herramientas modernas y rápidas
- TypeScript para seguridad de tipos
- Componentes reutilizables de Material UI
- Reglas de code quality automáticas
- Scripts listos para desarrollar, buildear y deployar

Ahora cualquier nuevo desarrollador puede clonar el repo, hacer 'npm install', 
'npm run dev', y estar contribuyendo en cinco minutos. Eso es lo que era el objetivo.

───────────────────────────────────────────────────────────────────────────────
[SECCIÓN 10] CIERRE - 0.5 minutos
───────────────────────────────────────────────────────────────────────────────

Esta fase inicial no es glamurosa, pero es fundamental. Sin ella, tendríamos seis 
personas trabajando con configuraciones diferentes, conflictos de versiones, y 
nadie sabría cómo hacer la build funcionar.

Con Everything confgurado aquí, podemos enfocarnos en lo que realmente importa: 
features, bugs, valor para el usuario.

Eso fue todo. Cualquier pregunta, me avisan.

═══════════════════════════════════════════════════════════════════════════════
FIN DEL GUIÓN
═══════════════════════════════════════════════════════════════════════════════

TIEMPO TOTAL: ~12 minutos (dentro del rango 7-15 requerido)

CLAVES PARA GRABAR:
- Habla naturalmente, no leas mecanicamente
- Haz pausas cuando muestres algo importante (3-5 seg)
- La calidad de audio es más importante que la de video
- Ten listo localhost:5173 antes de empezar
- Si algo falla en la demo, tienes screenshots de backup
- Mantén la cámara/micrófono enfocado en ti (si te ves) o solo en pantalla
