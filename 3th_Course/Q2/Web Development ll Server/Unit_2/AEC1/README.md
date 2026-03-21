# AEC 1 - BurgerPrince

## Introducción
Para esta actividad he construido un mini sistema de gestion de pedidos pensado como base para una futura API y app movil. El foco es simular el flujo real de un pedido (recepcion, validacion, pago y confirmacion) usando **eventos** y **asincronia** en Node.js. Queria que el flujo se entendiera bien en consola, pero sin perder el enfoque tecnico.

## Módulos  
- **EventEmitter**: es el motor de eventos de Node. Me permite registrar callbacks y dispararlos cuando ocurre algo, lo que encaja perfecto con un flujo de pedidos por estados.
- **Patron pub/sub**: una forma de desacoplar partes del sistema. El que emite no necesita conocer al que escucha, y eso hace el flujo mas flexible.
- **Promesa**: un objeto que representa algo que pasa mas tarde (exito o error). En este caso, el pago.
- **async/await**: una sintaxis que deja el flujo secuencial y legible sin perder la asincronia.
- **Estado de pedido**: una etiqueta que indica en que punto del ciclo se encuentra un pedido. Es clave para depurar y para futuras integraciones.

## Como funciona el flujo
1. **nuevoPedido**: recibo el pedido y calculo el total con el menu.
2. **validarPedido**: compruebo items, cantidades y stock disponible.
3. **procesarPago**: espero 2 segundos simulando pasarela de pago.
4. **confirmarPedido**: cierro el pedido si el pago sale bien.
5. **cancelarPedido**: si algo falla, libero stock y dejo el motivo.

La idea es que cada evento tenga una responsabilidad clara y el pedido vaya cambiando de estado con un rastro facil de seguir.


## Estructura del proyecto
```
AEC1/
├── index.js            # Flujo principal y simulacion del pedido
├── gestorEventos.js    # Clase que extiende EventEmitter
├── package.json        # Dependencias y scripts
└── README.md           # Este documento
```

## Añadidos
- **Menu + stock**: cada item tiene precio y cantidad disponible.
- **Validacion previa**: evita pedidos vacios o productos inexistentes.
- **Reserva y liberacion de stock**: se reserva antes del pago y se libera si falla.
- **Pago probabilistico**: 80% de exito para simular escenarios medianamente reales.

## Como ejecutar
1. Instalar dependencias:
   npm install
2. Ejecutar la simulacion:
   npm start


## Extra
Quise que el proyecto no se quedara corto, asi que he añadido alguna freature extra para que sirva como una base decente en futuras actividades. 

![alt text](image.png)