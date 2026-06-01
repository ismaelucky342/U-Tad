const Book = require('../models/Book');
const User = require('../models/User');

// GET /books — Obtener todos los libros (público)
const getAllBooks = async (req, res) => {
  try {
    const books = await Book.findAll({
      include: [{
        model: User,
        as: 'creator',
        attributes: ['id', 'username', 'fullName'],
      }],
      order: [['createdAt', 'DESC']],
    });
    return res.status(200).json(books);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// GET /books/:id — Obtener libro por ID (público)
const getBookById = async (req, res) => {
  const { id } = req.params;
  try {
    const book = await Book.findByPk(id, {
      include: [{
        model: User,
        as: 'creator',
        attributes: ['id', 'username', 'fullName'],
      }],
    });
    if (!book) {
      return res.status(404).json({ error: `Libro con ID ${id} no encontrado.` });
    }
    return res.status(200).json(book);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// POST /books — Crear nuevo libro (solo admin)
const createBook = async (req, res) => {
  const { title, author, isbn, genre, publicationYear, pages, available, synopsis } = req.body;

  try {
    const existingBook = await Book.findOne({ where: { isbn } });
    if (existingBook) {
      return res.status(409).json({ error: 'Ya existe un libro con ese ISBN.' });
    }

    const newBook = await Book.create({
      title,
      author,
      isbn,
      genre,
      publicationYear,
      pages,
      available: available !== undefined ? available : true,
      synopsis,
      userId: req.user.id,
    });

    return res.status(201).json({
      message: 'Libro creado correctamente.',
      data: newBook,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// PUT /books/:id — Actualizar libro (solo admin)
const updateBook = async (req, res) => {
  const { id } = req.params;
  const { title, author, isbn, genre, publicationYear, pages, available, synopsis } = req.body;

  try {
    const book = await Book.findByPk(id);
    if (!book) {
      return res.status(404).json({ error: `Libro con ID ${id} no encontrado.` });
    }

    if (isbn && isbn !== book.isbn) {
      const existing = await Book.findOne({ where: { isbn } });
      if (existing) {
        return res.status(409).json({ error: 'Ya existe un libro con ese ISBN.' });
      }
    }

    const updateData = {};
    if (title !== undefined) updateData.title = title;
    if (author !== undefined) updateData.author = author;
    if (isbn !== undefined) updateData.isbn = isbn;
    if (genre !== undefined) updateData.genre = genre;
    if (publicationYear !== undefined) updateData.publicationYear = publicationYear;
    if (pages !== undefined) updateData.pages = pages;
    if (available !== undefined) updateData.available = available;
    if (synopsis !== undefined) updateData.synopsis = synopsis;

    await book.update(updateData);

    return res.status(200).json({
      message: 'Libro actualizado correctamente.',
      data: book,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// DELETE /books/:id — Eliminar libro (solo admin)
const deleteBook = async (req, res) => {
  const { id } = req.params;

  try {
    const book = await Book.findByPk(id);
    if (!book) {
      return res.status(404).json({ error: `Libro con ID ${id} no encontrado.` });
    }

    await book.destroy();
    return res.status(200).json({ message: `Libro con ID ${id} eliminado correctamente.` });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

module.exports = {
  getAllBooks,
  getBookById,
  createBook,
  updateBook,
  deleteBook,
};
