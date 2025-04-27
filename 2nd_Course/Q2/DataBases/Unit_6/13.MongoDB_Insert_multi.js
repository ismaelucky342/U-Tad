// Insertar varios productos
db.productos.insertMany([
    {
      nombre: "Pantalón",
      categoria: "Ropa",
      precio: 39.99,
      stock: 50
    },
    {
      nombre: "Zapatos",
      categoria: "Calzado",
      precio: 59.99,
      stock: 200
    },
    {
      nombre: "Gorra",
      categoria: "Accesorios",
      precio: 14.99,
      stock: 150
    }
  ]);
  