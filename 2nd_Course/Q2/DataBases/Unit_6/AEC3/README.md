## **Ejercicio 1 – MongoDB**

### Crear una base de datos llamada **"tienda"**

Primero, abrí la terminal y ejecuté `mongosh` para entrar a la consola de MongoDB. Luego, usé el comando:

```bash
use tienda
```

Con eso seleccioné (o creé si no existía) la base de datos "tienda". MongoDB automáticamente trabaja con ella después de ese comando.

---

### Crear una colección llamada **"productos"**

Después de entrar en la base de datos, creé la colección llamada "productos" con:

```jsx
db.createCollection("productos")
```

Esto genera una colección vacía donde luego insertaría los productos.

---

### Insertar documentos en la colección **"productos"**

Añadí varios productos usando `insertMany`, que me permite insertar varios documentos a la vez:

```jsx
db.productos.insertMany([
  { nombre: "Camiseta", categoria: "Ropa", precio: 15.99, stock: 100 },
  { nombre: "Laptop", categoria: "Electrónica", precio: 599.99, stock: 30 },
  { nombre: "Auriculares", categoria: "Electrónica", precio: 29.99, stock: 150 },
  { nombre: "Zapatos", categoria: "Ropa", precio: 49.99, stock: 50 },
  { nombre: "Mochila", categoria: "Accesorios", precio: 25.99, stock: 80 }
])
```

Los productos se guardaron correctamente en la colección.

---

### Consultar todos los productos en la colección

Para ver todo lo que tenía guardado en la colección "productos", ejecuté:

```jsx
db.productos.find()
```

Esto me mostró todos los productos que había insertado.

### Consultar productos con precio mayor a 50

Filtré los productos por precio con:

```jsx
db.productos.find({ precio: { $gt: 50 } })
```

Así obtuve, por ejemplo, el producto "Laptop", que cuesta más de 50.

### Actualizar el precio de los productos de categoría "Ropa"

Luego, decidí aumentar el precio de todos los productos de la categoría "Ropa". Usé:

```jsx
db.productos.updateMany(
  { categoria: "Ropa" },
  { $set: { precio: 59.99 } }
)
```

Con esto, todos los productos de "Ropa" ahora tienen el mismo precio actualizado.

### Insertar un nuevo producto **"Smartwatch"**

Agregué otro producto, esta vez de tipo "Electrónica":

```jsx
db.productos.insertOne({
  nombre: "Smartwatch",
  categoria: "Electrónica",
  precio: 199.99,
  stock: 60
})
```

---

### Eliminar productos con stock menor a 50

Decidí eliminar los productos que tenían poco stock, menos de 50 unidades:

```jsx
db.productos.deleteMany({ stock: { $lt: 50 } })
```

Esto eliminó, por ejemplo, la "Laptop", que solo tenía 30 en stock.

### Mostrar productos de categoría **"Electrónica"** con stock mayor a 50

Para comprobar los productos electrónicos con buen stock, escribí:

```jsx
db.productos.find({ categoria: "Electrónica", stock: { $gt: 50 } })
```

Aquí apareció, por ejemplo, el "Smartwatch" y los "Auriculares".

### Crear una colección llamada **"clientes"**

Continué con la parte de clientes y creé una nueva colección:

```jsx
db.createCollection("clientes")
```

## **Exercise 1 – MongoDB**

### Create a database called **"store"**

First, I opened the terminal and ran `mongosh` to enter the MongoDB console. Then, I used the command:

```bash
use store
```

With that, I selected (or created if it didn't exist) the "store" database. MongoDB automatically works with it after that command.

---

### Create a collection called **"products"**

After entering the database, I created the collection called "products" with:

```jsx
db.createCollection("products")
```

This generates an empty collection where I would then insert the products.

---

### Insert documents into the **"products" collection**

I added multiple products using `insertMany`, which allows me to insert multiple documents at once:

```jsx
db.products.insertMany([
{ name: "T-shirt", category: "Clothing", price: 15.99, stock: 100 },
{ name: "Laptop", category: "Electronics", price: 599.99, stock: 30 },
{ name: "Headphones", category: "Electronics", price: 29.99, stock: 150 },
{ name: "Shoes", category: "Clothing", price: 49.99, stock: 50 },
{ name: "Backpack", category: "Accessories", price: 25.99, stock: 80 }
])
```

The products were successfully saved to the collection.

---

### Query all products in the collection

To see everything I had saved in the "products" collection, I ran:

```jsx
db.productos.find()
```

This showed me all the products I had inserted.

### Query products with prices greater than 50

I filtered the products by price with:

```jsx
db.productos.find({ price: { $gt: 50 } })
```

This gave me, for example, the product "Laptop," which costs more than 50.

### Update the price of products in the "Clothing" category

Then, I decided to increase the price of all products in the "Clothing" category. I used:

```jsx
db.products.updateMany(
{ category: "Clothing" },
{ $set: { price: 59.99 } }
)
```

With this, all "Clothing" products now have the same updated price.

### Insert a new product **"Smartwatch"**

I added another product, this time of type "Electronics":

```jsx
db.productos.insertOne({
name: "Smartwatch",
category: "Electronics",
price: 199.99,
stock: 60
})
```

---

### Delete products with less than 50 in stock

I decided to delete the products that had low stock, less than 50 units:

```jsx
db.productos.deleteMany({ stock: { $lt: 50 } })
```

This eliminated, for example, the "Laptop", which only had 30 in stock.

### Display products from the **"Electronics"** category with stock greater than 50

To check for electronic products with good stock, I wrote:

```jsx
db.products.find({ category: "Electronics", stock: { $gt: 50 } })
```

Here, for example, the "Smartwatch" and "Earphones" appeared.

### Create a collection called **"customers"**

I continued with the customers section and created a new collection:

```jsx
db.createCollection("customers")
```