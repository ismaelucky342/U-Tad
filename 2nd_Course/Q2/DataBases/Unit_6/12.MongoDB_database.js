// Crear una colección llamada productos
db.createCollection("productos");

// Insertar un documento en la colección productos
db.productos.insertOne({
    nombre: "Camiseta",
    categoria: "Ropa",
    precio: 19.99,
    stock: 100
  });

  