-- 1) Mostrar el contenido con más votos
SELECT c.id_contenido, c.nombre_contenido, COUNT(vc.id_voto_cont) AS num_votos
FROM Contenido c
INNER JOIN Voto_Contenido vc ON c.id_contenido = vc.id_cont_voto_cont
GROUP BY c.id_contenido, c.nombre_contenido
ORDER BY num_votos DESC
LIMIT 1;

+--------------+------------------+-----------+
| id_contenido | nombre_contenido | num_votos |
+--------------+------------------+-----------+
|            1 | Contenido 1      |         2 |
+--------------+------------------+-----------+
1 row in set (0.000 sec)




-- 2) Mostrar el contenido con más puntuación
SELECT id_contenido, nombre_contenido, MAX(puntuacion) AS max_puntuacion
FROM Contenido
GROUP BY id_contenido, nombre_contenido
ORDER BY max_puntuacion DESC
LIMIT 1;

+--------------+------------------+----------------+
| id_contenido | nombre_contenido | max_puntuacion |
+--------------+------------------+----------------+
|            3 | Contenido 3      |              5 |
+--------------+------------------+----------------+
1 row in set (0.000 sec)


-- 3) Mostrar el comentario más largo, muestra también su longitud
SELECT id_comentario, comentario, LENGTH(comentario) AS longitud
FROM Comentario
ORDER BY longitud DESC
LIMIT 1;

+---------------+---------------------+----------+
| id_comentario | comentario          | longitud |
+---------------+---------------------+----------+
|             5 | Excelente contenido |       19 |
+---------------+---------------------+----------+
1 row in set (0.000 sec)



-- 4) Muestra los identificadores y la fecha de los contenidos subidos después de 2010 y antes de 2015
SELECT id_contenido, fecha_cont
FROM Contenido
WHERE fecha_cont > '2010-01-01' AND fecha_cont < '2015-01-01';

Empty set (0.000 sec)


-- 5) Mostrar id del Usuario, nombre y email del usuario que tiene mayor número de contenidos
SELECT u.id_usuario, u.nombre_usuario, u.email
FROM Usuario u
INNER JOIN (
    SELECT id_user_cont, COUNT(*) AS num_contenidos
    FROM Contenido
    GROUP BY id_user_cont
    ORDER BY num_contenidos DESC
    LIMIT 1
) c ON u.id_usuario = c.id_user_cont;

+------------+----------------+----------------------+
| id_usuario | nombre_usuario | email                |
+------------+----------------+----------------------+
|          1 | Usuario 1      | usuario1@example.com |
+------------+----------------+----------------------+
1 row in set (0.000 sec)


-- 6) id Usuario y nombre del usuario que ha hecho más comentarios indicando cuantos son
SELECT u.id_usuario, u.nombre_usuario, COUNT(*) AS num_comentarios
FROM Usuario u
INNER JOIN Comentario c ON u.id_usuario = c.id_user_coment
GROUP BY u.id_usuario, u.nombre_usuario
ORDER BY num_comentarios DESC
LIMIT 1;

+------------+----------------+-----------------+
| id_usuario | nombre_usuario | num_comentarios |
+------------+----------------+-----------------+
|          4 | Usuario 4      |               1 |
+------------+----------------+-----------------+
1 row in set (0.000 sec)



-- 7) Mostar el id del Contenido menos visualizado así como su número de visualizaciones
SELECT id_contenido, nombre_contenido, MIN(visualizaciones) AS min_visualizaciones
FROM Contenido;

+--------------+------------------+---------------------+
| id_contenido | nombre_contenido | min_visualizaciones |
+--------------+------------------+---------------------+
|            1 | Contenido 1      |                 100 |
+--------------+------------------+---------------------+
1 row in set (0.000 sec)


-- 8) Mostrar el id Usuario y nombre del usuario que ha votado mayor número de contenidos indicando cuantos son
SELECT u.id_usuario, u.nombre_usuario, COUNT(*) AS num_votos
FROM Usuario u
INNER JOIN Voto_Contenido vc ON u.id_usuario = vc.id_usu_voto_cont
GROUP BY u.id_usuario, u.nombre_usuario
ORDER BY num_votos DESC
LIMIT 1;


+------------+----------------+-----------+
| id_usuario | nombre_usuario | num_votos |
+------------+----------------+-----------+
|          4 | Usuario 4      |         1 |
+------------+----------------+-----------+
1 row in set (0.000 sec)


-- 9) Mostrar el id Usuario del usuario con mayor número de votos positivos indicando cuantos son
SELECT id_usu_voto_cont, COUNT(*) AS num_votos_positivos
FROM Voto_Contenido
WHERE valor_voto_cont > 0
GROUP BY id_usu_voto_cont
ORDER BY num_votos_positivos DESC
LIMIT 1;

+------------------+---------------------+
| id_usu_voto_cont | num_votos_positivos |
+------------------+---------------------+
|                1 |                   1 |
+------------------+---------------------+
1 row in set (0.000 sec)


-- 10) Mostrar el día en el que más vídeos subió el usuario '2' indicando cuantos videos subió
SELECT DATE(fecha_cont) AS fecha_subida, COUNT(*) AS num_videos_subidos
FROM Contenido
WHERE id_user_cont = 2
GROUP BY DATE(fecha_cont)
ORDER BY num_videos_subidos DESC
LIMIT 1;


+--------------+--------------------+
| fecha_subida | num_videos_subidos |
+--------------+--------------------+
| 2023-01-02   |                  1 |
+--------------+--------------------+
1 row in set (0.000 sec)