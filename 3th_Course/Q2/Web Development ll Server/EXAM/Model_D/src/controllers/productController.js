const Product = require('../models/Product');
const User = require('../models/User');
const getAllProducts = async (req, res) => {
  try {
    const products = await Product.findAll({
      include: [{ model: User, as: 'registrant', attributes: ['id', 'username', 'fullName'] }],
      order: [['registeredDate', 'DESC']],
    });
    return res.status(200).json(products);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const getProductById = async (req, res) => {
  const { id } = req.params;
  try {
    const product = await Product.findByPk(id, {
      include: [{ model: User, as: 'registrant', attributes: ['id', 'username', 'fullName'] }],
    });
    if (!product) return res.status(404).json({ error: `Producto con ID ${id} no encontrado.` });
    return res.status(200).json(product);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const createProduct = async (req, res) => {
  const { name, description, price, stock, category, brand, imageUrl, weight, registeredDate } = req.body;
  try {
    const newProduct = await Product.create({
      name, description, price, stock, category, brand, imageUrl, weight, registeredDate, registeredBy: req.user.id,
    });
    return res.status(201).json({ message: 'Producto creado correctamente.', data: newProduct });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const updateProduct = async (req, res) => {
  const { id } = req.params;
  const { name, description, price, stock, category, brand, imageUrl, weight, registeredDate } = req.body;
  try {
    const product = await Product.findByPk(id);
    if (!product) return res.status(404).json({ error: `Producto con ID ${id} no encontrado.` });
    const updateData = {};
    if (name !== undefined) updateData.name = name;
    if (description !== undefined) updateData.description = description;
    if (price !== undefined) updateData.price = price;
    if (stock !== undefined) updateData.stock = stock;
    if (category !== undefined) updateData.category = category;
    if (brand !== undefined) updateData.brand = brand;
    if (imageUrl !== undefined) updateData.imageUrl = imageUrl;
    if (weight !== undefined) updateData.weight = weight;
    if (registeredDate !== undefined) updateData.registeredDate = registeredDate;
    await product.update(updateData);
    return res.status(200).json({ message: 'Producto actualizado correctamente.', data: product });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const deleteProduct = async (req, res) => {
  const { id } = req.params;
  try {
    const product = await Product.findByPk(id);
    if (!product) return res.status(404).json({ error: `Producto con ID ${id} no encontrado.` });
    await product.destroy();
    return res.status(200).json({ message: `Producto con ID ${id} eliminado correctamente.` });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
module.exports = { getAllProducts, getProductById, createProduct, updateProduct, deleteProduct };
