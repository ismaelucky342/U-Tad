1. Obtener todas las películas en las que ha actuado Tom Cruise y mostrar sus
títulos.

MATCH (a:person)-[:ACTED_IN]->(m:movie)
WHERE a.name = 'Tom Cruise'
RETURN m.title as movie

2. Obtener toda la gente nacida en los años 70 y mostrar sus nombres y años
de nacimiento

MATCH (a:person)
WHERE a.born >= 1970 AND a.born <= 1980
RETURN a.name as Name, a.born as 'Year Born'

3. Obtener todos los actores cuyo nombre empieza con “James”. Mostrar solo
los nombres y apellidos

MATCH (a:Person)-[ACTED_IN]->(m:Movie)
WHERE a.name STARTS WITH 'James'
RETURN a.name

4. Obtener todos los actores y una lista con las películas en las que han
actuado.

MATCH (a:Person)-[ACTED_IN]->(m:Movie)
RETURN p.name as actor, collect(m.title) AS 'movie_list'

5. Obtener todas las películas en las que el título de la misma sea el papel de
alguno de los actores. Mostrar el título de la película y el nombre del actor

MATCH (a:Person)-[r:ACTED_IN]->(m:Movie)
WHERE m.title in r.roles
RETURN m.title as Movie, a.name as Actor