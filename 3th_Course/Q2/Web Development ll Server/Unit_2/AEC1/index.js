/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC1 - PWIC                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        17/03/2026  -  01:07:13           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    21/03/2026  -  12:49:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

const chalk = require("chalk");
const GestorEventos = require("./gestorEventos");

const gestor = new GestorEventos();

const menu = {
  clasica: { nombre: "Burger Clasica", precio: 6.5 },
  doble: { nombre: "Burger Doble", precio: 8.5 },
  vegana: { nombre: "Burger Vegana", precio: 7.5 },
  patatas: { nombre: "Patatas", precio: 2.5 },
  refresco: { nombre: "Refresco", precio: 1.8 },
};

const inventario = {
  clasica: 10,
  doble: 6,
  vegana: 4,
  patatas: 20,
  refresco: 30,
};

const pedido = {
  id: "BP-1001",
  cliente: "Cliente Demo",
  items: [
    { codigo: "doble", cantidad: 1 },
    { codigo: "patatas", cantidad: 1 },
    { codigo: "refresco", cantidad: 1 },
  ],
  estado: "creado",
};

/**
 * Sumo el total del pedido a partir de los items y el menu.
 */
function calcularTotal(items) {
  return items.reduce((total, item) => {
    const producto = menu[item.codigo];
    return total + producto.precio * item.cantidad;
  }, 0);
}

/**
 * Aqui valido lo basico para no procesar pedidos rotos y mantener el flujo limpio.
 */
function validarPedido(pedidoActual) {
  const errores = [];

  if (!pedidoActual.items || pedidoActual.items.length === 0) {
    errores.push("El pedido no tiene productos");
  }

  for (const item of pedidoActual.items || []) {
    if (!menu[item.codigo]) {
      errores.push(`Producto no existe: ${item.codigo}`);
      continue;
    }

    if (item.cantidad <= 0) {
      errores.push(`Cantidad invalida para ${item.codigo}`);
    }

    if ((inventario[item.codigo] || 0) < item.cantidad) {
      errores.push(`Sin stock suficiente de ${item.codigo}`);
    }
  }

  return errores;
}

/**
 * Reservo stock antes de pagar, asi simulo un flujo realista.
 */
function reservarStock(items) {
  for (const item of items) {
    inventario[item.codigo] -= item.cantidad;
  }
}

/**
 * Si algo falla, devuelvo el stock para no dejar el inventario inconsistente.
 */
function liberarStock(items) {
  for (const item of items) {
    inventario[item.codigo] += item.cantidad;
  }
}

/**
 * Simulo la pasarela de pago con un timeout y un porcentaje de fallo.
 */
function procesarPedido(pedidoActual) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const pagoExitoso = Math.random() < 0.8;

      if (pagoExitoso) {
        resolve({
          ...pedidoActual,
          estado: "confirmado",
          transaccionId: "TX-" + Date.now(),
        });
      } else {
        reject(new Error("Pago rechazado por el banco"));
      }
    }, 2000);
  });
}

/**
 * Inicio el flujo: recibo pedido, calculo total y paso a validar.
 */
gestor.on("nuevoPedido", (pedidoActual) => {
  const pedidoConTotal = {
    ...pedidoActual,
    total: calcularTotal(pedidoActual.items),
    estado: "recibido",
  };

  console.log(chalk.blue("Pedido recibido:"), pedidoConTotal);
  gestor.emit("validarPedido", pedidoConTotal);
});

/**
 * Valido, reservo stock y mando el pedido al pago.
 */
gestor.on("validarPedido", (pedidoActual) => {
  const errores = validarPedido(pedidoActual);

  if (errores.length > 0) {
    gestor.emit("cancelarPedido", {
      ...pedidoActual,
      estado: "fallido",
      motivo: errores.join(" | "),
    });
    return;
  }

  reservarStock(pedidoActual.items);
  gestor.emit("procesarPago", { ...pedidoActual, estado: "pago_en_proceso" });
});

/**
 * Aqui controlo el pago con async/await para que el flujo se vea ordenado.
 */
gestor.on("procesarPago", async (pedidoActual) => {
  console.log(chalk.yellow("Procesando pago..."));

  try {
    const resultado = await procesarPedido(pedidoActual);
    gestor.emit("confirmarPedido", resultado);
  } catch (error) {
    liberarStock(pedidoActual.items);
    console.log(chalk.red("Pedido fallido:"), error.message);
    gestor.emit("cancelarPedido", {
      ...pedidoActual,
      estado: "fallido",
      motivo: error.message,
    });
  }
});

/**
 * Confirmo el pedido si todo ha salido bien.
 */
gestor.on("confirmarPedido", (pedidoActual) => {
  console.log(chalk.green("Pedido confirmado:"), pedidoActual);
});

/**
 * Si falla algo, dejo el motivo y cierro el pedido.
 */
gestor.on("cancelarPedido", (pedidoActual) => {
  console.log(chalk.red("Pedido cancelado:"), {
    id: pedidoActual.id,
    estado: pedidoActual.estado,
    motivo: pedidoActual.motivo,
  });
});

// Simulacion del flujo 
gestor.emit("nuevoPedido", pedido);
