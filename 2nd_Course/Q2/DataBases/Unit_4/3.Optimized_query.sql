-- Crear la base de datos
CREATE DATABASE cine_db;
USE cine_db;

-- Tablas
CREATE TABLE PELICULAS (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100),
  genero VARCHAR(50),
  duracion INT,
  estreno DATE
) ENGINE=InnoDB;

CREATE TABLE DIRECTORES (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  nacionalidad VARCHAR(50)
) ENGINE=InnoDB;

CREATE TABLE DIRIGE (
  id_pelicula INT,
  id_director INT,
  PRIMARY KEY (id_pelicula, id_director),
  FOREIGN KEY (id_pelicula) REFERENCES PELICULAS(id),
  FOREIGN KEY (id_director) REFERENCES DIRECTORES(id)
) ENGINE=InnoDB;

-- Índices
CREATE INDEX idx_genero ON PELICULAS(genero);
CREATE INDEX idx_estreno ON PELICULAS(estreno);
CREATE INDEX idx_nombre_nacionalidad ON DIRECTORES(nombre, nacionalidad);

-- Consulta optimizada
EXPLAIN SELECT p.titulo, d.nombre
FROM PELICULAS p
JOIN DIRIGE di ON p.id = di.id_pelicula
JOIN DIRECTORES d ON d.id = di.id_director
WHERE p.genero = 'Drama' AND YEAR(p.estreno) = 2022;
