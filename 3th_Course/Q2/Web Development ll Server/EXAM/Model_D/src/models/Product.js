const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const User = require('./User');
const Product = sequelize.define('Product', {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  name: { type: DataTypes.STRING(200), allowNull: false },
  description: { type: DataTypes.TEXT, allowNull: true },
  price: { type: DataTypes.FLOAT, allowNull: false, validate: { min: 0 } },
  stock: { type: DataTypes.INTEGER, allowNull: false, validate: { min: 0 } },
  category: { type: DataTypes.STRING(100), allowNull: false },
  brand: { type: DataTypes.STRING(100), allowNull: false },
  imageUrl: { type: DataTypes.STRING(500), allowNull: true },
  weight: { type: DataTypes.FLOAT, allowNull: false, validate: { min: 0 } },
  registeredDate: { type: DataTypes.DATEONLY, allowNull: false },
  registeredBy: { type: DataTypes.INTEGER, allowNull: false, references: { model: User, key: 'id' } },
}, { tableName: 'products', timestamps: true });
User.hasMany(Product, { foreignKey: 'registeredBy', as: 'productsRegistered' });
Product.belongsTo(User, { foreignKey: 'registeredBy', as: 'registrant' });
module.exports = Product;
