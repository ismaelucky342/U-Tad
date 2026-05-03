package com.example.aec1.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.aec1.adapter.ProductAdapter
import com.example.aec1.databinding.FragmentFavoritesBinding
import com.example.aec1.model.Product
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.*

class FavoritesFragment : Fragment() {

    private var _binding: FragmentFavoritesBinding? = null
    private val binding get() = _binding!!
    private lateinit var adapter: ProductAdapter
    private val favoriteProducts = mutableListOf<Product>()
    private val databaseUrl = "https://aec1-8a207-default-rtdb.europe-west1.firebasedatabase.app"

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentFavoritesBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        adapter = ProductAdapter(favoriteProducts, { product ->
            removeFromFavorites(product)
        }, null)
        binding.rvFavorites.layoutManager = LinearLayoutManager(context)
        binding.rvFavorites.adapter = adapter

        loadFavorites()
    }

    private fun loadFavorites() {
        val userId = FirebaseAuth.getInstance().currentUser?.uid
        if (userId != null) {
            val ref = FirebaseDatabase.getInstance(databaseUrl).getReference("favorites").child(userId)
            ref.addValueEventListener(object : ValueEventListener {
                override fun onDataChange(snapshot: DataSnapshot) {
                    favoriteProducts.clear()
                    for (child in snapshot.children) {
                        val product = child.getValue(Product::class.java)
                        if (product != null) {
                            favoriteProducts.add(product)
                        }
                    }
                    adapter.updateData(favoriteProducts)
                }

                override fun onCancelled(error: DatabaseError) {
                    if (isAdded) Toast.makeText(context, "Error al cargar: ${error.message}", Toast.LENGTH_SHORT).show()
                }
            })
        }
    }

    private fun removeFromFavorites(product: Product) {
        val userId = FirebaseAuth.getInstance().currentUser?.uid
        if (userId != null) {
            FirebaseDatabase.getInstance(databaseUrl).getReference("favorites").child(userId).child(product.id.toString())
                .removeValue()
                .addOnSuccessListener {
                    if (isAdded) Toast.makeText(context, "Eliminado de favoritos", Toast.LENGTH_SHORT).show()
                }
                .addOnFailureListener { e ->
                    if (isAdded) Toast.makeText(context, "Error al eliminar: ${e.message}", Toast.LENGTH_SHORT).show()
                }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}