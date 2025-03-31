-- ============================================================
-- **Exercise 4: Relational Algebra Expressions**
-- ============================================================

-- 🔹 **A) Customers from Zaragoza who have purchased more than 10 units of a product**

-- 1️⃣ Filter customers from Zaragoza
CustomersZaragoza ← σ_{city='Zaragoza'}(CUSTOMERS)

-- 2️⃣ Filter sales with quantity greater than 10
SalesGreaterThan10 ← σ_{quantity > 10}(SALES)

-- 3️⃣ Join the filtered tables to get customers from Zaragoza who purchased more than 10 units
ResultA ← π_{customer_id, name} (CustomersZaragoza ⨝ SalesGreaterThan10)

---

-- 🔹 **B) Products priced above €2000 and sold more than 10 times**

-- 1️⃣ Filter products priced above €2000
ExpensiveProducts ← σ_{price > 2000}(PRODUCTS)

-- 2️⃣ Group sales by product and calculate the total quantity sold
SalesByProduct ← γ_{product_id, SUM(quantity) → total_sold}(SALES)

-- 3️⃣ Filter products sold more than 10 times
SalesGreaterThan10 ← σ_{total_sold > 10}(SalesByProduct)

-- 4️⃣ Join expensive products with the filtered sales
ResultB ← π_{product_id, description} (ExpensiveProducts ⨝ SalesGreaterThan10)

---

-- 🔹 **C) Customers who have purchased exactly 5 distinct products**

-- 1️⃣ Group sales by customer and count distinct products purchased
ProductsByCustomer ← γ_{customer_id, COUNT(DISTINCT product_id) → num_products}(SALES)

-- 2️⃣ Filter customers who purchased exactly 5 distinct products
Customers5Products ← σ_{num_products = 5}(ProductsByCustomer)

-- 3️⃣ Join with the CUSTOMERS table to get their names
ResultC ← π_{customer_id, name} (Customers5Products ⨝ CUSTOMERS)

---

-- 🔹 **D) Product IDs that have not been purchased by more than 5 customers**

-- 1️⃣ Count the number of distinct customers who purchased each product
CustomersByProduct ← γ_{product_id, COUNT(DISTINCT customer_id) → num_customers}(SALES)

-- 2️⃣ Filter products not purchased by more than 5 customers
ProductsNotMoreThan5 ← σ_{num_customers ≤ 5}(CustomersByProduct)

-- 3️⃣ Select only the product IDs
ResultD ← π_{product_id} (ProductsNotMoreThan5)

---

-- 🔹 **E) Products priced the same as the product with the lowest price**

-- 1️⃣ Get the minimum price of the products
MinPrice ← γ_{MIN(price) → min_price}(PRODUCTS)

-- 2️⃣ Select products with that price
ProductsSamePrice ← σ_{price = min_price} (PRODUCTS × MinPrice)

-- 3️⃣ Get the product ID and description
ResultE ← π_{product_id, description} (ProductsSamePrice)

---

-- 🔹 **F) Customers who have purchased products from more than 2 different categories**

-- 1️⃣ Join sales with the products table to get the categories
SalesWithCategories ← SALES ⨝ PRODUCTS

-- 2️⃣ Count distinct categories per customer
CategoriesByCustomer ← γ_{customer_id, COUNT(DISTINCT category) → num_categories}(SalesWithCategories)

-- 3️⃣ Filter customers with more than 2 different categories
CustomersMoreThan2 ← σ_{num_categories > 2}(CategoriesByCustomer)

-- 4️⃣ Join with CUSTOMERS to get their names
ResultF ← π_{customer_id, name} (CustomersMoreThan2 ⨝ CUSTOMERS)
