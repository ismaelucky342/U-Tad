-- Crear keyspace y tabla de ejemplo
CREATE KEYSPACE IF NOT EXISTS test_keyspace WITH REPLICATION = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

USE test_keyspace;

CREATE TABLE IF NOT EXISTS users (
  pk text,
  ck text,
  name text,
  age int,
  email text,
  city text,
  PRIMARY KEY (pk, ck)
);

-- Insertar datos de ejemplo
INSERT INTO users (pk, ck, name, age) VALUES ('pk1', 'ck1', 'John', 30);
INSERT INTO users (pk, ck, email) VALUES ('pk2', 'ck2', 'john@example.com');
INSERT INTO users (pk, ck, city) VALUES ('pk3', 'ck3', 'Madrid');

-- Queries de ejemplo para simular lecturas
SELECT * FROM users WHERE pk = 'pk1' AND ck = 'ck1';
SELECT * FROM users WHERE pk = 'pk2' AND ck = 'ck2';
SELECT * FROM users WHERE pk = 'pk3' AND ck = 'ck3';