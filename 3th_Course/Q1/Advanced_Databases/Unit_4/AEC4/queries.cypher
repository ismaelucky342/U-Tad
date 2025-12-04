//====================================================================================================//
//                                                                                                    //
//                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        //
//      AEC4 - ABDB                                ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       //
//                                                        ██║   ██║█████╗██║   ███████║██║  ██║       //
//      created:        03/12/2025  -  01:35:10           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       //
//      last change:    04/12/2025  -  11:34:43           ╚██████╔╝      ██║   ██║  ██║██████╔╝       //
//                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        //
//                                                                                                    //
//      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             //
//                                                                                                    //
//      Github:                                           https://github.com/ismaelucky342            //
//                                                                                                    //
//====================================================================================================// 

// 1. Obtener todos los nodos Person.
MATCH (p:Person)
RETURN p;

// 2. Obtener todas las películas (nodos Movie) estrenadas en 2003.
MATCH (m:Movie {released: 2003})
RETURN m;

// 3. Obtener toda la gente que escribió la película "Speed Racer".
MATCH (p:Person)-[:WROTE]->(m:Movie {title: 'Speed Racer'})
RETURN p;

// 4. Obtener todas las películas conectadas con Tom Hanks.
MATCH (tom:Person {name: 'Tom Hanks'})--(m:Movie)
RETURN DISTINCT m;

// 5. Obtener información sobre los papeles que ha hecho Tom Hanks.
MATCH (tom:Person {name: 'Tom Hanks'})-[r:ACTED_IN]->(m:Movie)
RETURN m.title AS Movie, r.roles AS Roles;

// 6. Obtener los actores que actuaron en la película "The Matrix" nacidos después de 1960. Mostrar sus nombres y años de nacimiento.
MATCH (p:Person)-[:ACTED_IN]->(m:Movie {title: 'The Matrix'})
WHERE p.born > 1960
RETURN p.name AS Name, p.born AS Born;

// 7. Obtener toda la gente que ha escrito películas. Utilizar para ello la relación entre 2 nodos. Mostrar los nombres de las personas junto con los títulos de las películas.
MATCH (p:Person)-[:WROTE]->(m:Movie)
RETURN p.name AS Writer, m.title AS Movie;

// 8. Obtener toda la gente del grafo que no cuenta con la propiedad born. Mostrar sus nombres.
MATCH (p:Person)
WHERE p.born IS NULL
RETURN p.name AS Name;

// 9. Obtener toda la gente relacionada con películas donde la relación cuenta con la propiedad rating. Mostrar sus nombres, título de la película y valoración (rating).
MATCH (p:Person)-[r:REVIEWED]->(m:Movie)
WHERE r.rating IS NOT NULL
RETURN p.name AS Reviewer, m.title AS Movie, r.rating AS Rating;

// 10. Obtener toda la gente que ha producido una película pero que no ha dirigido ninguna. Mostrar sus nombres y los títulos de las películas.
MATCH (p:Person)-[:PRODUCED]->(m:Movie)
WHERE NOT (p)-[:DIRECTED]->(:Movie)
RETURN p.name AS Producer, m.title AS Movie;

// 11. Obtener las películas y los actores donde uno de los actores también dirigió la película. Mostrar el nombre de los actores, el nombre del director y el título de la película.
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(director:Person)
WHERE actor = director
RETURN actor.name AS ActorDirector, director.name AS Director, m.title AS Movie;

// 12. Obtener todas las películas estrenadas en los años 2000, 2004 y 2008. Mostrar sus títulos y años de estreno.
MATCH (m:Movie)
WHERE m.released IN [2000, 2004, 2008]
RETURN m.title AS Title, m.released AS Year;

// 13. Obtener todas las películas en las que ha actuado Gene Hackman, junto con el director de las mismas. Además, obtener el nombre de los actores que han actuado junto con Gene Hackman. Mostrar el nombre de la película, el nombre del director y el nombre de los actores.
MATCH (gene:Person {name: 'Gene Hackman'})-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(director:Person)
MATCH (coactor:Person)-[:ACTED_IN]->(m)
WHERE coactor <> gene
RETURN m.title AS Movie, director.name AS Director, COLLECT(coactor.name) AS Coactors;

// 14. Obtener todos los nodos con los que James Thompson tiene directamente una relación FOLLOWS en cualquier dirección.
MATCH (james:Person {name: 'James Thompson'})-[:FOLLOWS]-(other)
RETURN other;

// 15. Modificar la consulta anterior para obtener únicamente los nodos que están exactamente a 3 pasos.
MATCH (james:Person {name: 'James Thompson'})-[:FOLLOWS*3]-(other)
RETURN DISTINCT other;

// 16. Obtener toda la gente que ha revisado (review) una película. Mostrar la lista de revisores y el número que hay.
MATCH (p:Person)-[:REVIEWED]->(m:Movie)
RETURN COLLECT(DISTINCT p.name) AS Reviewers, COUNT(DISTINCT p) AS NumberOfReviewers;

// 17. Mostrar todos los revisores, sus películas y la gente que ha actuado en las películas. Mostrar el nombre del director, el número de actores que han trabajado en la película y la lista de los actores.
MATCH (reviewer:Person)-[:REVIEWED]->(m:Movie)<-[:ACTED_IN]-(actor:Person)
RETURN reviewer.name AS Reviewer, m.title AS Movie, COUNT(actor) AS NumberOfActors, COLLECT(actor.name) AS Actors
ORDER BY NumberOfActors DESC;

// 18. Obtener todos los actores que han actuado exactamente en 5 películas. Mostrar el nombre del actor junto con una lista de las películas en las que ha trabajado.
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)
WITH actor, COLLECT(m.title) AS movies
WHERE SIZE(movies) = 5
RETURN actor.name AS Actor, movies AS Movies;

// 19. Obtener las películas que tienen al menos 2 directores, y de manera opcional (OPTIONAL) el nombre de la gente que ha revisado la película.
MATCH (m:Movie)<-[:DIRECTED]-(director:Person)
WITH m, COLLECT(director.name) AS directors
WHERE SIZE(directors) >= 2
OPTIONAL MATCH (reviewer:Person)-[:REVIEWED]->(m)
RETURN m.title AS Movie, directors AS Directors, COLLECT(reviewer.name) AS Reviewers;

// 20. Obtener las 5 mejores valoraciones y las películas asociadas. Mostrar el título de la película y la puntuación.
MATCH (p:Person)-[r:REVIEWED]->(m:Movie)
RETURN m.title AS Movie, r.rating AS Rating
ORDER BY r.rating DESC
LIMIT 5;

// 21. Obtener todos los actores que han actuado en películas y los productores de esas películas. Durante la consulta recopila el nombre de los actores y el nombre de los productores. Mostrar los títulos de las películas, junto con la lista de actores y productores de la misma, asegurando que no haya duplicados. Ordenar los resultados en función del tamaño de la lista de actores.
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)<-[:PRODUCED]-(producer:Person)
WITH m, COLLECT(DISTINCT actor.name) AS actors, COLLECT(DISTINCT producer.name) AS producers
RETURN m.title AS Movie, actors AS Actors, producers AS Producers
ORDER BY SIZE(actors) DESC;

// 22. Obtener los actores que han actuado en más de 5 películas. Mostrar el nombre del actor junto con la lista de películas.
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)
WITH actor, COLLECT(m.title) AS movies
WHERE SIZE(movies) > 5
RETURN actor.name AS Actor, movies AS Movies;

// 23. Modificar la consulta anterior de tal manera que antes de terminar se utilice el comando UNWIND sobre la lista. Mostrar el nombre de los actores junto con la película asociada.
MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)
WITH actor, COLLECT(m.title) AS movies
WHERE SIZE(movies) > 5
UNWIND movies AS movie
RETURN actor.name AS Actor, movie AS Movie;

// 24. Obtener todas las películas en las que ha actuado Tom Hanks. Mostrar el título de la película, el año de estreno y la edad que tenía Tom cuando la película fue estrenada.
MATCH (tom:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie)
RETURN m.title AS Movie, m.released AS Year, m.released - tom.born AS AgeAtRelease
ORDER BY m.released;

// 25. Crear un nodo Movie para una película con el título "Forrest Gump".
CREATE (fg:Movie {title: 'Forrest Gump'});

// 26. Crear un nodo Person para una persona de nombre Robin Wright.
CREATE (rw:Person {name: 'Robin Wright'});

// 27. Añadir la etiqueta OlderMovie a las películas estrenadas antes de 2010.
MATCH (m:Movie)
WHERE m.released < 2010
SET m:OlderMovie;

// 28. Obtener todas las películas antiguas para comprobar que la etiqueta se ha añadido correctamente.
MATCH (m:OlderMovie)
RETURN m.title AS Title, m.released AS Year;

// 29. Añadir las siguientes propiedades a la película "Forrest Gump": released: 1994, tagline: Life is like a box of chocolates… you never know what you're gonna get., lengthInMinutes: 142
MATCH (m:Movie {title: 'Forrest Gump'})
SET m.released = 1994,
    m.tagline = 'Life is like a box of chocolates… you never know what you\'re gonna get.',
    m.lengthInMinutes = 142
RETURN m;

// 30. Eliminar la propiedad lengthInMinutes de la película "Forrest Gump".
MATCH (m:Movie {title: 'Forrest Gump'})
REMOVE m.lengthInMinutes
RETURN m;

// 31. Crear la relación ACTED_IN entre los actores Robin Wright, Tom Hanks y Gary Sinise y la película "Forrest Gump".
MATCH (m:Movie {title: 'Forrest Gump'})
MATCH (rw:Person {name: 'Robin Wright'})
MATCH (th:Person {name: 'Tom Hanks'})
MATCH (gs:Person {name: 'Gary Sinise'})
CREATE (rw)-[:ACTED_IN {roles: ['Jenny Curran']}]->(m)
CREATE (th)-[:ACTED_IN {roles: ['Forrest Gump']}]->(m)
CREATE (gs)-[:ACTED_IN {roles: ['Lieutenant Dan Taylor']}]->(m)
RETURN m, rw, th, gs;

// 32. Crear la relación DIRECTED entre Robert Zemeckis y la película "Forrest Gump".
MATCH (rz:Person {name: 'Robert Zemeckis'})
MATCH (m:Movie {title: 'Forrest Gump'})
CREATE (rz)-[:DIRECTED]->(m)
RETURN rz, m;

// 33. Crear la relación HELPED desde Tom Hanks a Gary Sinise.
MATCH (th:Person {name: 'Tom Hanks'})
MATCH (gs:Person {name: 'Gary Sinise'})
CREATE (th)-[:HELPED]->(gs)
RETURN th, gs;

// 34. Añadir la propiedad research a la relación HELPED entre Tom Hanks y Gary Sinise con el valor "war history".
MATCH (th:Person {name: 'Tom Hanks'})-[h:HELPED]->(gs:Person {name: 'Gary Sinise'})
SET h.research = 'war history'
RETURN th, h, gs;

// 35. Eliminar la propiedad creada en la consulta anterior.
MATCH (th:Person {name: 'Tom Hanks'})-[h:HELPED]->(gs:Person {name: 'Gary Sinise'})
REMOVE h.research
RETURN th, h, gs;

// 36. Eliminar la relación HELPED del grafo.
MATCH (th:Person {name: 'Tom Hanks'})-[h:HELPED]->(gs:Person {name: 'Gary Sinise'})
DELETE h;

// 37. Hacer una consulta en el grafo para comprobar que la relación ya no existe.
MATCH (th:Person {name: 'Tom Hanks'})-[h:HELPED]->(gs:Person {name: 'Gary Sinise'})
RETURN h;

// 38. Eliminar el nodo "Forrest Gump" junto con sus relaciones.
MATCH (m:Movie {title: 'Forrest Gump'})
DETACH DELETE m;

// 39. Utilizar MERGE para crear (ON CREATE) un nodo de tipo Movie con título "Forrest Gump". Si se crea, fijar la fecha de estreno a 1994.
MERGE (m:Movie {title: 'Forrest Gump'})
ON CREATE SET m.released = 1994
RETURN m;

// 40. Utiliza MERGE para actualizar un nodo de tipo Movie con título "Forrest Gump". Si se encuentra, dar el valor "Life is like a box of chocolates… you never know what you're gonna get." a la propiedad tagline.
MERGE (m:Movie {title: 'Forrest Gump'})
ON MATCH SET m.tagline = 'Life is like a box of chocolates… you never know what you\'re gonna get.'
RETURN m;
