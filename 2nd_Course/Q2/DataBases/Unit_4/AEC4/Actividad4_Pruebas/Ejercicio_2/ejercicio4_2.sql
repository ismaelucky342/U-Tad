-- ejercicio4_2.sql

USE Unidad4;

CREATE TABLE libros (
    id INT PRIMARY KEY,
    titulo VARCHAR(255)
) ENGINE=InnoDB
  ROW_FORMAT=DYNAMIC
  FILE_PER_TABLE=1;


CREATE TABLE libros_tbs (
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(50),
    año_publicacion INT
) TABLESPACE tbs_libros STORAGE DISK ENGINE=InnoDB;

SELECT TABLE_NAME, ENGINE, ROW_FORMAT
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'Unidad4';

SELECT * FROM information_schema.FILES
WHERE FILE_TYPE = 'DATAFILE';

-- Crear nuevo tablespace
CREATE TABLESPACE tbs_nuevo
    ADD DATAFILE '/var/lib/mysql/tbs_nuevo.ibd'
    ENGINE=InnoDB;

-- Mover tabla (requiere ALTER con DISCARD/IMPORT)
ALTER TABLE libros_tbs TABLESPACE tbs_nuevo;

SELECT TABLE_NAME, ENGINE, ROW_FORMAT
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'Unidad4';

-- Primero elimina la tabla del tablespace si aún existe
DROP TABLE IF EXISTS libros_tbs;

-- Luego elimina el tablespace
DROP TABLESPACE tbs_libros;