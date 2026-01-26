EJEMPLO 1: Crear nodos y relaciones
Enunciado

Crear un usuario llamado Ismael que vive en Madrid.

CREATE (u:usuario {nombre: "Ismael", edad: 28})
CREATE (c:ciudad {nombre: "Madrid"})
CREATE (u)-[:vive_en]->(c)



EJEMPLO 2: Buscar un nodo por propiedad
Enunciado

Obtener el usuario llamado Ismael.

MATCH (u:Usuario {nombre: "Ismael"})
RETURN u



EJEMPLO 3: Seguir una relación
Enunciado

Saber en qué ciudad vive Ismael.

MATCH (u:Usuario {nombre: "Ismael"})-[:vive_en]->(c:ciudad)
RETURN c.nombre



EJEMPLO 4: Relaciones entre usuarios
Enunciado

Saber quiénes son amigos de Ismael.

MATCH (u:usuario {nombre: "Ismael"})-[amigo_de]->(amigo:Usuario)
Return amigo.nombre



EJEMPLO 5: Filtro por propiedad
Enunciado

Obtener usuarios mayores de 30 años.

MATCH (u:Usuario)
WHERE u.edad > 30
RETURN u.nombre, u.edad



EJEMPLO 6: Contar relaciones
Enunciado

Contar cuántos amigos tiene cada usuario.

MATCH (u:Usuario)-[:AMIGO_DE]->()
RETURN u.nombre, COUNT(*) AS totalAmigos



EJEMPLO 7: Camino entre nodos (clave de Neo4j)
Enunciado

Saber si Ismael está conectado con Ana (directa o indirectamente).


MATCH path = (u1:Usuario {nombre: "Ismael"})-[:AMIGO_DE*]-(u2:Usuario {nombre: "Ana})
RETURN path



EJEMPLO 8: Camino con límite
Enunciado

Buscar amigos de amigos (máximo 2 saltos).

MATCH (u:Usuario {nombre: "Ismael"})-[:AMIGO_DE*1..2]-(otro:Usuario)
RETURN DISTINCT otro.nombre



EJEMPLO 9: Relación con propiedades 

Enunciado 

Guardar desde cuándo Ismael trabaja en una empresa. 

MATCH (u:Usuario {nombre: "Ismael"}), (e:Empresa {nombre: "ACME"})
CREATE (u)-[:TRABAJA_EN {desde: 2022}]->(e)



EJEMPLO 10: Ranking (top N)

Enunciado

Obtener las ciudades con más usuarios viviendo en ellas.

MATCH (:Usuario)-[:VIVE_EN]->(c:Ciudad)
RETURN c.nombre, COUNT(*) AS total
ORDER BY total DESC
LIMIT 3
