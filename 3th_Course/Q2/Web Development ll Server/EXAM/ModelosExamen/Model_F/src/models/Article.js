const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const User = require('./User');
const Article = sequelize.define('Article', {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  title: { type: DataTypes.STRING(300), allowNull: false },
  subtitle: { type: DataTypes.STRING(300), allowNull: true },
  body: { type: DataTypes.TEXT, allowNull: false },
  category: { type: DataTypes.STRING(100), allowNull: false },
  publishedDate: { type: DataTypes.DATE, allowNull: false },
  authorId: { type: DataTypes.INTEGER, allowNull: false, references: { model: User, key: 'id' } },
  featuredImageUrl: { type: DataTypes.STRING(500), allowNull: true },
  tags: { type: DataTypes.JSON, allowNull: true },
  status: { type: DataTypes.ENUM('borrador', 'publicado'), defaultValue: 'borrador', allowNull: false },
}, { tableName: 'articles', timestamps: true });
User.hasMany(Article, { foreignKey: 'authorId', as: 'articlesAuthored' });
Article.belongsTo(User, { foreignKey: 'authorId', as: 'author' });
module.exports = Article;
