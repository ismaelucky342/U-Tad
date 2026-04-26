
# AEC2 - API de pedidos

Este proyecto consiste en una variante del que realicé en la AEC1 en el que añadimos una API para gestionar pedidos de hamburguesería. la idea es poder gestionar acciones concretas de local como crear pedidos, listarlos, actualizarlos y borrarlos mientras el servidor está en marcha.

## Cómo está organizado el proyecto

El proyecto está distribuído de la siguiente forma: 

```
├── package.json
├── package-lock.json
├── README.md
├── .gitignore
├── src
│   ├── controllers
│   │   └── ordersController.js
│   ├── data
│   │   └── ordersData.js
│   ├── index.js
│   ├── middlewares
│   │   ├── errorHandler.js
│   │   ├── logger.js
│   │   ├── validateId.js
|   │   └── validateOrder.js
│   └── routes
│       └── orders.js
└── tests
    └── orders.test.js
```

- `package.json`: dependencias y scripts.
- `package-lock.json`: versiones exactas de las dependencias.
- `.gitignore`: evita subir `node_modules` y archivos temporales.
- `src/index.js`: arranca el servidor y aplica los middlewares.
- `src/routes/orders.js`: define las rutas del endpoint `/orders`.
- `src/controllers/ordersController.js`: contiene la lógica de los pedidos.
- `src/middlewares/`: valida peticiones, comprueba IDs y gestiona errores.
- `src/data/ordersData.js`: almacena los pedidos en memoria.
- `tests/orders.test.js`: cubre las rutas con pruebas automáticas.

## Flujo 

He implementado una API de pedidos con rutas completas para crear, listar, actualizar y eliminar pedidos. El proyecto valida los datos que recibe antes de guardarlos, comprueba que los IDs sean correctos en las rutas con parámetros, y usa un middleware global para devolver errores claros cuando algo falla. También añadí un logger básico para ver las peticiones entrantes, respuestas JSON consistentes con códigos HTTP adecuados y un almacenamiento temporal en memoria. Para cerrar el ciclo, cubrí el comportamiento principal con pruebas automáticas usando `jest` y `supertest`.

## Test

Solo hay que instalar dependencias:

```bash
npm install
```

Y arrancar el servidor con:

```bash
npm start
```

La API queda en `http://localhost:3000`.

## Comandos disponibles

```bash
npm start      # arranca la API
npm test       # ejecuta los tests
npm run dev    # arranca la API con nodemon
```

## Rutas implementadas

- `GET /orders` : Devuelve todos los pedidos en memoria.

- `GET /orders/:id`: Busca un pedido por su ID y lo devuelve.

- `POST /orders`: Crea un pedido nuevo.

- `PUT /orders/:id`: Actualiza los campos de un pedido.

- `DELETE /orders/:id`: Elimina un pedido.

## Ejemplo de pedido

```json
{
  "paymentMethod": "cash",
  "price": 8.5,
  "ingredients": {
    "bun": "brioche",
    "patty": "carnesita",
    "cheese": true
  }
}
```

## ejemplos que he hecho usando con curl

Listar pedidos:

```bash
curl -sS http://localhost:3000/orders | jq
```

Crear un pedido:

```bash
curl -sS -X POST http://localhost:3000/orders \
  -H 'Content-Type: application/json' \
  -d '{"paymentMethod":"cash","price":8.5,"ingredients":{"bun":"sesame","patty":"beef","cheese":true}}' | jq
```

Ver un pedido por ID:

```bash
curl -sS http://localhost:3000/orders/1 | jq
```

Actualizar un pedido:

```bash
curl -sS -X PUT http://localhost:3000/orders/1 \
  -H 'Content-Type: application/json' \
  -d '{"paymentMethod":"card","price":9.5,"ingredients":{"bun":"sesame","patty":"veggie","cheese":false}}' | jq
```

Eliminar un pedido:

```bash
curl -sS -X DELETE http://localhost:3000/orders/1 | jq
```

## Errores que he probado

Probé el caso de enviar datos inválidos y la API devuelve un 400 con un mensaje claro.

Ejemplo:

```bash
curl -sS -X POST http://localhost:3000/orders \
  -H 'Content-Type: application/json' \
  -d '{"price":-5,"ingredients":{}}' | jq
```

La respuesta:

```json
{
  "success": false,
  "message": "Validation failed",
  "errors": [
    "paymentMethod is required and must be a non-empty string",
    "price is required and must be a non-negative number",
    "ingredients object must include at least one ingredient"
  ]
}
```

También comprobé que un ID inválido devuelve un 400:

```bash
curl -sS http://localhost:3000/orders/abc | jq
```

Y que un pedido no existente devuelve un 404.

## Pruebas manuales realizadas

- `GET /orders` para ver la lista inicial
- `POST /orders` para crear un pedido
- `GET /orders/:id` para recuperar ese pedido
- `PUT /orders/:id` para actualizarlo
- `DELETE /orders/:id` para borrarlo
- respuestas 400 cuando envío datos malos
- respuestas 404 cuando no existe el pedido

## Tests automáticos

he añadido unos tests automáticos que se ejecutan con:

```bash
npm test
```

donde se cubre: 

- listado de pedidos
- creación de pedido válido
- lectura por ID
- actualización
- eliminación
- errores de validación
- IDs inválidos
- pedidos inexistentes

## Extras

Este proyecto me ha servido para practicar cómo estructurar una API pequeña con rutas claras, validaciones y manejo de errores sin usar base de datos. Me ha permitido ver lo útil que es separar rutas, controladores y middlewares, y confirmar que incluso un proyecto sencillo gana calidad con pruebas automáticas y una documentación clara.



