const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const User = require('./User');

const Book = sequelize.define('Book', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  title: {
    type: DataTypes.STRING(200),
    allowNull: false,
  },
  author: {
    type: DataTypes.STRING(150),
    allowNull: false,
  },
  isbn: {
    type: DataTypes.STRING(20),
    allowNull: false,
    unique: true,
  },
  genre: {
    type: DataTypes.STRING(100),
    allowNull: false,
  },
  publicationYear: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  pages: {
    type: DataTypes.INTEGER,
    allowNull: false,
    validate: {
      min: 1,
    },
  },
  available: {
    type: DataTypes.BOOLEAN,
    defaultValue: true,
  },
  synopsis: {
    type: DataTypes.TEXT,
    allowNull: true,
  },
  userId: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: {
      model: User,
      key: 'id',
    },
  },
}, {
  tableName: 'books',
  timestamps: true,
});

// Asociaciones
User.hasMany(Book, { foreignKey: 'userId', as: 'booksAdded' });
Book.belongsTo(User, { foreignKey: 'userId', as: 'creator' });

module.exports = Book;
