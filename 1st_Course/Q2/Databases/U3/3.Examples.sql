--1.)

SELECT * FROM pedido;

-- This selects all columns from the table called "pedido".

--2.)

SELECT AVG(saldo_cl), ciudad_cl FROM cliente GROUP BY ciudad_cl;

-- This calculates the average "saldo_cl" (balance) for each city in the "cliente" table.

--3.)

SELECT id_proveedor_almacen, COUNT(id_articulo_almacen) FROM almacén GROUP BY id_proveedor_almacen;

--This counts the number of articles each provider has in the warehouse and groups them by the provider's ID.

--4.)

SELECT * FROM cliente WHERE descuento IN (10, 25, 3);

--This selects all columns from the "cliente" table where the discount is either 10, 25, or 3.

--5.)
SELECT id_pedido_detalles FROM detalles_pedido ORDER BY cantidad_articulo_pedido LIMIT 1;

--This selects the ID of the order details (id_pedido_detalles) from the "detalles_pedido" table, ordering them by the quantity of the ordered items and selecting only the first result.

--6.) 

SELECT DISTINCT descuento_cl FROM cliente;

--This selects unique discount values from the "cliente" table.

--7.)

SELECT ciudad_cl, SUM(credito_cl) FROM cliente GROUP BY ciudad_cl;

--This calculates the total credit for each city in the "cliente" table.

--8.)

SELECT DISTINCT direccion_envio FROM pedido WHERE direccion_envio LIKE ‘%Antonio%’;

--This selects unique shipping addresses from the "pedido" table where the address contains the string 'Antonio'.

--9.)

SELECT id_articulo_almacen FROM almacén WHERE stock_articulo_almacen > 49 ORDER BY stock_articulo_almacen;

--This selects the ID of the articles in the warehouse where the stock is greater than 49, ordering them by stock amount.

--10.)

SELECT id_articulo_almacen FROM almacén WHERE stock_articulo_almacen >= 49 ORDER BY stock_articulo_almacen;

--Similar to the previous one, but including cases where the stock is exactly 49.

--11.)
SELECT id_articulo_almacen FROM almacen WHERE stock_articulo_almacen < 49 ORDER BY stock_articulo_almacen;

--This selects the ID of articles in the warehouse where the stock is less than 49, ordering them by stock amount.

--12.)

SELECT id_articulo_almacen FROM almacen WHERE stock_articulo_almacen <= 49 ORDER BY stock_articulo_almacen;

--Similar to the previous one, but including cases where the stock is exactly 49.

--13.) 

SELECT id_articulo_almacen FROM almacen WHERE stock_articulo_almacen BETWEEN 1 AND 49 ORDER BY stock_articulo_almacen;

--This selects the ID of articles in the warehouse where the stock is between 1 and 49, inclusive, ordering them by stock amount.