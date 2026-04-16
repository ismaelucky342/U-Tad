
# AEC 2 - BurgerPrince API (Pedidos)

Proyecto: API REST simple para gestionar pedidos (CRUD) basada en la práctica AEC1.

Resumen:
- Endpoint `/orders` con operaciones Create, Read, Update, Delete.
- Datos en memoria (array) durante la ejecución.
- Middlewares de validación y manejo de errores.
- Respuestas JSON estructuradas con códigos HTTP adecuados.

Estructura principal:
```
AEC2/
├── package.json
├── .gitignore
├── src/
│   ├── index.js
│   ├── routes/
│   │   └── orders.js
│   ├── controllers/
│   │   └── ordersController.js
│   ├── middlewares/
│   │   ├── validateOrder.js
│   │   └── errorHandler.js
│   └── data/
│       └── ordersData.js
└── tests/
		└── orders.test.js
```

Instalación y ejecución:

1. Instalar dependencias:

```bash
npm install
```

2. Ejecutar la API:

```bash
npm start
```

Endpoints (ejemplos con `curl`):

- Listar pedidos:

```bash
curl -sS http://localhost:3000/orders | jq
```

- Crear pedido:

```bash
curl -sS -X POST http://localhost:3000/orders \
	-H 'Content-Type: application/json' \
	-d '{"paymentMethod":"cash","price":8.5,"ingredients":{"bun":"sesame","patty":"beef","cheese":true}}' | jq
```

- Obtener pedido por ID:

```bash
curl -sS http://localhost:3000/orders/1 | jq
```

- Actualizar pedido:

```bash
curl -sS -X PUT http://localhost:3000/orders/1 \
	-H 'Content-Type: application/json' \
	-d '{"paymentMethod":"card","price":9.5,"ingredients":{"bun":"sesame","patty":"veggie","cheese":false}}' | jq
```

- Eliminar pedido:

```bash
curl -sS -X DELETE http://localhost:3000/orders/1 | jq
```

Pruebas manuales:
- Se puede usar Postman o `curl` con los ejemplos anteriores. Las respuestas devuelven JSON con `success` y `data` o `message`.

Notas:
- No incluir `node_modules` en la entrega.
- Hay un conjunto básico de tests en `tests/orders.test.js` que usa `jest` y `supertest`.
