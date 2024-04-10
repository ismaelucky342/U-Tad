INSERT INTO usuario (email, nombre_usuario, contraseña_usuario, ciudad_residencia) VALUES 
('u1@gmail.com', 'Luis', '', 'Madrid'),
('u2@gmail.com', 'Felipe', '', 'Barcelona'),
('u3@gmail.com', 'Carlos', '', 'Lugo'),
('u4@gmail.com', 'Ana', '', 'Madrid'),
('u5@gmail.com', 'Maria', '', 'Soria'),
('u6@gmail.com', 'Monica', '', 'Madrid');

INSERT INTO contenido (id_user_cont, fecha_cont, visualizaciones, nombre_fichero, puntuacion, nombre_contenido) VALUES
(1, '2010-10-10', 100, '/home/foto.jpg', 3, 'Foto Vacaciones'),
(2, '2010-10-10', 10, '/home/video.mp4', 0, 'Video Playa'),
(3, '2010-11-10', 500, '/home/mitexto.txt', 9, 'Documento 1'),
(4, '2011-01-10', 20, '/home/video2.mp4', 2, 'Video Cena'),
(4, '2013-01-10', 20, '/home/foto3.jpg', 1, 'Foto Familia'),
(4, '2014-01-10', 20, '/home/video2.mp4', 0, 'Video Tutorial'),
(4, '2014-01-10', 35, '/home/foto4.jpg', 6, 'Foto montaña'),
(4, '2014-01-10', 12, '/home/otrafoto.jpg', 4, 'Foto trabajo'),
(2, '2010-10-10', 10, '/home/video.mp4', 3, 'Video Casa'),
(2, '2013-10-23', 10, '/home/video.mp4', 3, 'Video2'),
(3, '2020-07-15', 3, '/home/mivideo.mp4', 5, 'General');

INSERT INTO comentario (id_user_coment, id_contenido_coment, comentario) VALUES
(2, 3, 'Como mola este video'),
(2, 3, 'Me encanta la cancion'),
(2, 1, 'Me reucerda cuando yo era pequeña'),
(2, 4, 'No soporto los videos como este'),
(1, 3, 'Vaya postureo'),
(5, 4, 'jajajajaja'),
(5, 4, 'Nada que decir'),
(1, 1, 'Puede que me sume a este reto'),
(1, 4, 'Me encanta');

INSERT INTO voto_contenido (id_usu_voto_cont, id_cont_voto_cont, valor_voto_cont, fecha_voto_cont) VALUES
(3, 4, 1, '2021-02-02'),
(4, 4, -1, '2019-07-05'),
(2, 3, 1, '2021-11-04'),
(1, 3, -1, '2020-05-05'),
(2, 2, 1, '2019-12-01'),
(4, 5, 1, '2021-07-03'),
(2, 6, 1, '2020-01-04'),
(4, 6, -1, '2021-03-15');

INSERT INTO voto_comment (id_usu_voto_comment, id_com_voto_comment, valor_voto_comment, fecha_voto_commet) VALUES
(4, 3, 1, '2020-07-02'),
(1, 2, 0, '2019-01-01'),
(3, 4, 1, '2019-01-05'),
(4, 2, 0, '2021-10-07'),
(2, 1, 0, '2020-12-03');

PRIMARY KEY (`id_usuario`)

UNIQUE KEY `voto_contenido_un` (`id_usu_voto_cont`,`id_cont_voto_cont`)

CONSTRAINT `Voto_Contenido_FK` FOREIGN KEY (`id_usu_voto_cont`) REFERENCES `usuario` (`id_usuario`)
