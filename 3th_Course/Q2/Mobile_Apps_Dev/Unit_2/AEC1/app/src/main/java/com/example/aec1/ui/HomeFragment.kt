package com.example.aec1.ui

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.appcompat.app.AppCompatDelegate
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import com.android.volley.Request
import com.android.volley.toolbox.JsonArrayRequest
import com.android.volley.toolbox.Volley
import com.example.aec1.R
import com.example.aec1.adapter.ProductAdapter
import com.example.aec1.databinding.FragmentHomeBinding
import com.example.aec1.model.Product
import com.google.android.material.chip.Chip
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.*
import org.json.JSONArray

class HomeFragment : Fragment() {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!
    private lateinit var adapter: ProductAdapter
    private val allProducts = mutableListOf<Product>()
    
    private val databaseUrl = "https://aec1-8a207-default-rtdb.europe-west1.firebasedatabase.app"

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        adapter = ProductAdapter(
            mutableListOf(),
            { product -> addToFavorites(product) },
            { product -> addToCart(product) }
        )
        binding.rvProducts.layoutManager = LinearLayoutManager(context)
        binding.rvProducts.adapter = adapter

        binding.btnGoToFavorites.setOnClickListener {
            findNavController().navigate(R.id.action_homeFragment_to_favoritesFragment)
        }

        binding.fabCart.setOnClickListener {
            findNavController().navigate(R.id.action_homeFragment_to_cartFragment)
        }

        binding.btnThemeToggle.setOnClickListener {
            val currentMode = AppCompatDelegate.getDefaultNightMode()
            if (currentMode == AppCompatDelegate.MODE_NIGHT_YES) {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
            } else {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
            }
        }

        checkDatabaseConnection()
        fetchProducts()
    }

    private fun checkDatabaseConnection() {
        Log.d("FIREBASE", "Intentando conectar a: $databaseUrl")
        val connectedRef = FirebaseDatabase.getInstance(databaseUrl).getReference(".info/connected")
        connectedRef.addValueEventListener(object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                val connected = snapshot.getValue(Boolean::class.java) ?: false
                if (connected) {
                    Log.d("FIREBASE", "¡Conexión establecida correctamente!")
                } else {
                    Log.w("FIREBASE", "Esperando conexión a $databaseUrl...")
                }
            }
            override fun onCancelled(error: DatabaseError) {
                Log.e("FIREBASE", "Error de conexión: ${error.message} - ${error.details}")
            }
        })
    }

    private fun fetchProducts() {
        val currentContext = context ?: return
        binding.progressBar.visibility = View.VISIBLE
        val url = "https://fakestoreapi.com/products"
        val queue = Volley.newRequestQueue(currentContext)

        val jsonArrayRequest = JsonArrayRequest(Request.Method.GET, url, null,
            { response ->
                _binding?.let {
                    it.progressBar.visibility = View.GONE
                    parseResponse(response)
                }
            },
            { error ->
                _binding?.let {
                    it.progressBar.visibility = View.GONE
                    Toast.makeText(context, "Error API: ${error.message}", Toast.LENGTH_SHORT).show()
                }
            }
        )
        queue.add(jsonArrayRequest)
    }

    private fun parseResponse(response: JSONArray) {
        allProducts.clear()
        val categories = mutableSetOf<String>()
        categories.add("Todas")

        for (i in 0 until response.length()) {
            try {
                val obj = response.getJSONObject(i)
                val product = Product(
                    obj.optInt("id"),
                    obj.optString("title"),
                    obj.optDouble("price"),
                    obj.optString("description"),
                    obj.optString("category"),
                    obj.optString("image")
                )
                allProducts.add(product)
                categories.add(product.category)
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
        setupCategories(categories.toList())
        filterProducts("Todas")
    }

    private fun setupCategories(categories: List<String>) {
        binding.cgCategories.removeAllViews()
        categories.forEach { category ->
            val chip = Chip(context)
            chip.text = category
            chip.isCheckable = true
            chip.setOnClickListener { filterProducts(category) }
            if (category == "Todas") chip.isChecked = true
            binding.cgCategories.addView(chip)
        }
    }

    private fun filterProducts(category: String) {
        val filtered = if (category == "Todas") {
            allProducts
        } else {
            allProducts.filter { it.category == category }
        }
        adapter.updateData(ArrayList(filtered))
        binding.rvProducts.scheduleLayoutAnimation()
    }

    private fun addToFavorites(product: Product) {
        val user = FirebaseAuth.getInstance().currentUser
        if (user == null) {
            Toast.makeText(context, "Debes iniciar sesión", Toast.LENGTH_SHORT).show()
            return
        }

        FirebaseDatabase.getInstance(databaseUrl)
            .getReference("favorites")
            .child(user.uid)
            .child(product.id.toString())
            .setValue(product)
            .addOnSuccessListener {
                if (isAdded) Toast.makeText(context, "⭐ Añadido a favoritos", Toast.LENGTH_SHORT).show()
            }
            .addOnFailureListener { e ->
                if (isAdded) Toast.makeText(context, "Error: ${e.message}", Toast.LENGTH_LONG).show()
            }
    }

    private fun addToCart(product: Product) {
        val user = FirebaseAuth.getInstance().currentUser
        if (user == null) {
            Toast.makeText(context, "Inicia sesión para comprar", Toast.LENGTH_SHORT).show()
            return
        }

        val ref = FirebaseDatabase.getInstance(databaseUrl)
            .getReference("cart")
            .child(user.uid)
            .child(product.id.toString())
            
        // Usamos addListenerForSingleValueEvent que es más fiable que .get() para escrituras rápidas
        ref.addListenerForSingleValueEvent(object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                if (snapshot.exists()) {
                    val existing = snapshot.getValue(Product::class.java)
                    existing?.let {
                        it.quantity += 1
                        ref.setValue(it)
                    }
                } else {
                    product.quantity = 1
                    ref.setValue(product)
                }
                if (isAdded) Toast.makeText(context, "🛒 Añadido al carrito", Toast.LENGTH_SHORT).show()
            }

            override fun onCancelled(error: DatabaseError) {
                if (isAdded) Toast.makeText(context, "Error: ${error.message}", Toast.LENGTH_LONG).show()
            }
        })
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}