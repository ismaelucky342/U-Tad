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
  
// Mostrar todos los productos
db.productos.find().pretty();

// Mostrar solo los productos de la categoría "Ropa"
db.productos.find({ categoria: "Ropa" }).pretty();

// Mostrar solo los productos con un precio menor a 30
db.productos.find({ precio: { $lt: 30 } }).pretty();