#!/bin/bash

# Script de configuración e importación de datos
# Restaurantes de Nueva York

echo "============================================"
echo "Importando datos de restaurantes..."
echo "============================================"

# Importar datos JSON a MongoDB
mongoimport --db restaurantesNY --collection restaurants --file restaurants.json --jsonArray

echo "============================================"
echo "Datos importados exitosamente"
echo "Total de documentos:"
mongosh restaurantesNY --eval "db.restaurants.countDocuments()"
echo "============================================"

# Crear índices para mejorar el rendimiento
echo "Creando índices..."
mongosh restaurantesNY --eval "db.restaurants.createIndex({ borough: 1 })"
mongosh restaurantesNY --eval "db.restaurants.createIndex({ cuisine: 1 })"
mongosh restaurantesNY --eval "db.restaurants.createIndex({ 'grades.grade': 1 })"
mongosh restaurantesNY --eval "db.restaurants.createIndex({ 'address.zipcode': 1 })"

echo "¡Configuración completada!"
