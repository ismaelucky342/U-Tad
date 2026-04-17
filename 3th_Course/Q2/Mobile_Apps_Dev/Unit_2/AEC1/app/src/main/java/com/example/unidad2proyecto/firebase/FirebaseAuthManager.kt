package com.example.unidad2proyecto.firebase

import com.google.firebase.auth.FirebaseAuth

object FirebaseAuthManager {
    private val auth: FirebaseAuth = FirebaseAuth.getInstance()

    fun register(email: String, password: String, completion: (Boolean, String) -> Unit) {
        auth.createUserWithEmailAndPassword(email, password)
            .addOnCompleteListener { task ->
                if (task.isSuccessful) {
                    completion(true, "Registro correcto")
                } else {
                    completion(false, task.exception?.localizedMessage ?: "Error al registrar")
                }
            }
    }

    fun signIn(email: String, password: String, completion: (Boolean, String) -> Unit) {
        auth.signInWithEmailAndPassword(email, password)
            .addOnCompleteListener { task ->
                if (task.isSuccessful) {
                    completion(true, "Login correcto")
                } else {
                    completion(false, task.exception?.localizedMessage ?: "Error al iniciar sesión")
                }
            }
    }

    fun signOut() {
        auth.signOut()
    }

    fun currentUserId(): String? = auth.currentUser?.uid
}
