package com.example.unidad2proyecto.firebase

import com.example.unidad2proyecto.model.FavoriteItem
import com.example.unidad2proyecto.model.Product
import com.google.firebase.firestore.FirebaseFirestore

object FirestoreManager {
    private val firestore = FirebaseFirestore.getInstance()

    fun saveFavorite(product: Product, completion: (Boolean, String) -> Unit) {
        val userId = FirebaseAuthManager.currentUserId()
        if (userId == null) {
            completion(false, "Usuario no autenticado")
            return
        }
        val favorite = FavoriteItem(product.id, product.title, product.price)
        firestore.collection("users")
            .document(userId)
            .collection("favorites")
            .document(product.id.toString())
            .set(favorite)
            .addOnSuccessListener {
                completion(true, "Añadido a favoritos")
            }
            .addOnFailureListener { error ->
                completion(false, error.localizedMessage ?: "Error guardando favorito")
            }
    }

    fun fetchFavorites(completion: (List<FavoriteItem>?, String?) -> Unit) {
        val userId = FirebaseAuthManager.currentUserId()
        if (userId == null) {
            completion(null, "Usuario no autenticado")
            return
        }
        firestore.collection("users")
            .document(userId)
            .collection("favorites")
            .get()
            .addOnSuccessListener { querySnapshot ->
                val favorites = querySnapshot.documents.mapNotNull { it.toObject(FavoriteItem::class.java) }
                completion(favorites, null)
            }
            .addOnFailureListener { error ->
                completion(null, error.localizedMessage ?: "Error obteniendo favoritos")
            }
    }
}
