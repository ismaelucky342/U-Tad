-- Insertar datos en la tabla Usuario
INSERT INTO Usuario (email, nombre_usuario, contraseña_usuario, ciudad_residencia) 
VALUES 
('usuario1@example.com', 'Usuario 1', 'contraseña1', 'Ciudad 1'),
('usuario2@example.com', 'Usuario 2', 'contraseña2', 'Ciudad 2'),
('usuario3@example.com', 'Usuario 3', 'contraseña3', 'Ciudad 3'),
('usuario4@example.com', 'Usuario 4', 'contraseña4', 'Ciudad 4'),
('usuario5@example.com', 'Usuario 5', 'contraseña5', 'Ciudad 5');

-- Insertar datos en la tabla Contenido
INSERT INTO Contenido (id_user_cont, fecha_cont, visualizaciones, nombre_fichero, puntuacion, nombre_contenido)
VALUES 
(1, '2023-01-01', 100, '/ruta/a/archivo1.mp4', 4, 'Contenido 1'),
(2, '2023-01-02', 200, '/ruta/a/archivo2.mp4', 3, 'Contenido 2'),
(3, '2023-01-03', 150, '/ruta/a/archivo3.mp4', 5, 'Contenido 3'),
(4, '2023-01-04', 120, '/ruta/a/archivo4.mp4', 2, 'Contenido 4'),
(5, '2023-01-05', 180, '/ruta/a/archivo5.mp4', 4, 'Contenido 5');

-- Insertar datos en la tabla Comentario
INSERT INTO Comentario (id_user_coment, id_contenido_coment, comentario)
VALUES 
(1, 1, '¡Genial!'),
(2, 1, 'Me encantó'),
(3, 2, 'Interesante'),
(4, 3, 'Buen trabajo'),
(5, 3, 'Excelente contenido');

-- Insertar datos en la tabla Voto_Comment
INSERT INTO Voto_Comment (id_usu_voto_comment, id_com_voto_comment, valor_voto_comment, fecha_voto_commet)
VALUES 
(1, 1, 1, '2023-01-01'),
(2, 1, 1, '2023-01-02'),
(3, 2, 1, '2023-01-03'),
(4, 3, -1, '2023-01-04'),
(5, 4, 1, '2023-01-05');

-- Insertar datos en la tabla Voto_Contenido
INSERT INTO Voto_Contenido (id_usu_voto_cont, id_cont_voto_cont, valor_voto_cont, fecha_voto_cont)
VALUES 
(1, 1, 1, '2023-01-01'),
(2, 1, 1, '2023-01-02'),
(3, 2, 1, '2023-01-03'),
(4, 3, -1, '2023-01-04'),
(5, 4, 1, '2023-01-05');


PRIMARY KEY (`id_usuario`)

UNIQUE KEY `voto_contenido_un` (`id_usu_voto_cont`,`id_cont_voto_cont`)

CONSTRAINT `Voto_Contenido_FK` FOREIGN KEY (`id_usu_voto_cont`) REFERENCES `usuario` (`id_usuario`)


-- Crear tabla Usuario
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    nombre_usuario VARCHAR(100) NOT NULL,
    contraseña_usuario VARCHAR(100) NOT NULL,
    ciudad_residencia VARCHAR(100)
);

-- Crear tabla Comentario
CREATE TABLE Comentario (
    id_comentario INT AUTO_INCREMENT PRIMARY KEY,
    id_user_coment INT,
    id_contenido_coment INT,
    comentario VARCHAR(100),
    FOREIGN KEY (id_user_coment) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_contenido_coment) REFERENCES Contenido(id_contenido)
);

-- Crear tabla Contenido
CREATE TABLE Contenido (
    id_contenido INT AUTO_INCREMENT PRIMARY KEY,
    id_user_cont INT,
    fecha_cont DATE,
    visualizaciones INT,
    nombre_fichero VARCHAR(100) NOT NULL,
    puntuacion INT,
    nombre_contenido VARCHAR(100),
    FOREIGN KEY (id_user_cont) REFERENCES Usuario(id_usuario)
);

-- Crear tabla Voto_Comment
CREATE TABLE Voto_Comment (
    id_voto_comment INT AUTO_INCREMENT PRIMARY KEY,
    id_usu_voto_comment INT,
    id_com_voto_comment INT,
    valor_voto_comment INT,
    fecha_voto_commet DATE,
    UNIQUE KEY Voto_Comment_UN (id_usu_voto_comment, id_com_voto_comment),
    FOREIGN KEY (id_usu_voto_comment) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_com_voto_comment) REFERENCES Comentario(id_comentario)
);

-- Crear tabla Voto_Contenido
CREATE TABLE Voto_Contenido (
    id_voto_cont INT AUTO_INCREMENT PRIMARY KEY,
    id_usu_voto_cont INT,
    id_cont_voto_cont INT,
    valor_voto_cont INT,
    fecha_voto_cont DATE,
    UNIQUE KEY voto_contenido_un (id_usu_voto_cont, id_cont_voto_cont),
    FOREIGN KEY (id_usu_voto_cont) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_cont_voto_cont) REFERENCES Contenido(id_contenido)
);
