Explora la BBDD listingsAndReviews (adjunta) que contiene información sobre alojamientos en Airbnb y sus reseñas. Se proponen las siguientes consultas:

Ejercicio 1: Encuentra el precio por noche del primer registro de la colección.

db.listingsAndReviews.find().price()

Ejercicio 2: Obtén todos los documentos con listing_url, name, bedrooms,
cleaning_fee, y price de la colección donde el campo cleaning_fee
no sea null.

db.listingsAndReviews.find(
    { cleaning_fee: {$ne: null}}, 
    { 
      listing_url: 1,
      name: 1,
      bedrooms: 1,
      cleaning_fee: 1,
      price: 1    
    }
);

Ejercicio 3: Encuentra todos los alojamientos con listing_url, name, amenities,
host de la colección que tengan un host con una verificación de Jumio y una
sección about.

db.listingsAndReviews.find(
  {
    "host.host_verifications": "jumio",
    "host.host_about": { $exists: true, $ne: "" }
  },
  {
    listing_url: 1,
    name: 1,
    amenities: 1,
    host: 1,
    _id: 0
  }
);


Ejercicio 4: Encuentra los anuncios con listing_url, name, address and
amenities, price, review_scores de la colección que tienen los
precios por noche más altos.

db.listingsAndReviews.find(
    {price: {$exist: TRUE}}, 
    {
        listing_url: 1,
        name: 1,
        address: 1,
        amenities: 1,
        price: 1 ,
        review_score: 1
    }
).sort({"price":1}).limit(1)

Ejercicio 5: Encuentra todos los anuncios con listing_url, name, address,
reviews de la colección que tienen al menos una reseña.

db.listingsAndReviews.find(
    {reviews: {$exist: true}, $not: {$size: 0}},
    {
        listing_url: 1,
        name: 1,
        address: 1,
        reviews: 1
    }
);