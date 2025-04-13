-- ejercicio4_1.sql

DROP DATABASE IF EXISTS Unidad4;
CREATE DATABASE Unidad4;
USE Unidad4;

CREATE TABLE libros (
    id_libro INT NOT NULL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    año_publicacion INT NOT NULL CHECK (año_publicacion <= 2025),
    genero VARCHAR(20) NOT NULL
);