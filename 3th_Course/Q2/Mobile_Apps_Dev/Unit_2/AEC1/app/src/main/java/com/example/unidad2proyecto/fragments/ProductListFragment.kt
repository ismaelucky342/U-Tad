package com.example.unidad2proyecto.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.unidad2proyecto.MainActivity
import com.example.unidad2proyecto.adapter.ProductAdapter
import com.example.unidad2proyecto.databinding.FragmentProductListBinding
import com.example.unidad2proyecto.firebase.FirebaseAuthManager
import com.example.unidad2proyecto.firebase.FirestoreManager
import com.example.unidad2proyecto.model.Product
import com.example.unidad2proyecto.network.ApiClient

class ProductListFragment : Fragment() {
    private var _binding: FragmentProductListBinding? = null
    private val binding get() = _binding!!
    private lateinit var adapter: ProductAdapter

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentProductListBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        adapter = ProductAdapter { product ->
            FirestoreManager.saveFavorite(product) { success, message ->
                Toast.makeText(requireContext(), message, Toast.LENGTH_SHORT).show()
            }
        }
        binding.productsRecyclerView.layoutManager = LinearLayoutManager(requireContext())
        binding.productsRecyclerView.adapter = adapter

        binding.favoritesButton.setOnClickListener {
            (activity as? MainActivity)?.showFavorites()
        }

        binding.logoutButton.setOnClickListener {
            FirebaseAuthManager.signOut()
            (activity as? MainActivity)?.showLogin()
        }

        loadProducts()
    }

    private fun loadProducts() {
        ApiClient.fetchProducts(requireContext()) { products, error ->
            if (error != null) {
                Toast.makeText(requireContext(), error, Toast.LENGTH_SHORT).show()
                return@fetchProducts
            }
            adapter.submitList(products ?: emptyList())
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
