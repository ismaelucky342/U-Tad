package com.example.aec1.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
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
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.FirebaseDatabase
import org.json.JSONArray

class HomeFragment : Fragment() {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!
    private lateinit var adapter: ProductAdapter
    private val products = mutableListOf<Product>()

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        adapter = ProductAdapter(products) { product ->
            addToFavorites(product)
        }
        binding.rvProducts.layoutManager = LinearLayoutManager(context)
        binding.rvProducts.adapter = adapter

        binding.btnGoToFavorites.setOnClickListener {
            findNavController().navigate(R.id.action_homeFragment_to_favoritesFragment)
        }

        fetchProducts()
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
                    Toast.makeText(context, "Error fetching products: ${error.message}", Toast.LENGTH_SHORT).show()
                }
            }
        )
        queue.add(jsonArrayRequest)
    }

    private fun parseResponse(response: JSONArray) {
        val newProducts = mutableListOf<Product>()
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
                newProducts.add(product)
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
        products.clear()
        products.addAll(newProducts)
        adapter.updateData(ArrayList(products))
    }

    private fun addToFavorites(product: Product) {
        val user = FirebaseAuth.getInstance().currentUser
        if (user != null) {
            try {
                val database = FirebaseDatabase.getInstance()
                val ref = database.getReference("favorites").child(user.uid).child(product.id.toString())
                ref.setValue(product).addOnCompleteListener { task ->
                    if (isAdded) {
                        if (task.isSuccessful) {
                            Toast.makeText(context, "Added to favorites", Toast.LENGTH_SHORT).show()
                        } else {
                            Toast.makeText(context, "Failed: ${task.exception?.message}", Toast.LENGTH_SHORT).show()
                        }
                    }
                }
            } catch (e: Exception) {
                Toast.makeText(context, "Database error: ${e.message}", Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}