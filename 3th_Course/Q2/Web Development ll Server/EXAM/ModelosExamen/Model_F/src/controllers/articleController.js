const Article = require('../models/Article');
const User = require('../models/User');
const getAllArticles = async (req, res) => {
  try {
    const articles = await Article.findAll({ include: [{ model: User, as: 'author', attributes: ['id', 'username', 'fullName'] }], where: { status: 'publicado' }, order: [['publishedDate', 'DESC']] });
    return res.status(200).json(articles);
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const getArticleById = async (req, res) => {
  const { id } = req.params;
  try {
    const article = await Article.findByPk(id, { include: [{ model: User, as: 'author', attributes: ['id', 'username', 'fullName'] }] });
    if (!article || article.status !== 'publicado') return res.status(404).json({ error: 'No encontrado.' });
    return res.status(200).json(article);
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const createArticle = async (req, res) => {
  const { title, subtitle, body, category, publishedDate, featuredImageUrl, tags, status } = req.body;
  try {
    const newArticle = await Article.create({ title, subtitle, body, category, publishedDate, featuredImageUrl, tags, status: status || 'borrador', authorId: req.user.id });
    return res.status(201).json({ message: 'Artículo creado.', data: newArticle });
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const updateArticle = async (req, res) => {
  const { id } = req.params;
  const { title, subtitle, body, category, publishedDate, featuredImageUrl, tags, status } = req.body;
  try {
    const article = await Article.findByPk(id);
    if (!article) return res.status(404).json({ error: 'No encontrado.' });
    const updateData = {};
    if (title !== undefined) updateData.title = title;
    if (subtitle !== undefined) updateData.subtitle = subtitle;
    if (body !== undefined) updateData.body = body;
    if (category !== undefined) updateData.category = category;
    if (publishedDate !== undefined) updateData.publishedDate = publishedDate;
    if (featuredImageUrl !== undefined) updateData.featuredImageUrl = featuredImageUrl;
    if (tags !== undefined) updateData.tags = tags;
    if (status !== undefined) updateData.status = status;
    await article.update(updateData);
    return res.status(200).json({ message: 'Actualizado.', data: article });
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const deleteArticle = async (req, res) => {
  const { id } = req.params;
  try {
    const article = await Article.findByPk(id);
    if (!article) return res.status(404).json({ error: 'No encontrado.' });
    await article.destroy();
    return res.status(200).json({ message: 'Eliminado.' });
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
module.exports = { getAllArticles, getArticleById, createArticle, updateArticle, deleteArticle };
