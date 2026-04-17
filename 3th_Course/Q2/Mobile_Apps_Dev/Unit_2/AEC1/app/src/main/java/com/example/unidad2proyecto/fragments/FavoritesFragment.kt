package com.example.unidad2proyecto.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.unidad2proyecto.MainActivity
import com.example.unidad2proyecto.adapter.FavoriteAdapter
import com.example.unidad2proyecto.databinding.FragmentFavoritesBinding
import com.example.unidad2proyecto.firebase.FirebaseAuthManager
import com.example.unidad2proyecto.firebase.FirestoreManager

class FavoritesFragment : Fragment() {
    private var _binding: FragmentFavoritesBinding? = null
    private val binding get() = _binding!!
    private lateinit var adapter: FavoriteAdapter

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentFavoritesBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        adapter = FavoriteAdapter()
        binding.favoritesRecyclerView.layoutManager = LinearLayoutManager(requireContext())
        binding.favoritesRecyclerView.adapter = adapter

        binding.backButton.setOnClickListener {
            (activity as? MainActivity)?.showProducts()
        }

        binding.logoutButton.setOnClickListener {
            FirebaseAuthManager.signOut()
            (activity as? MainActivity)?.showLogin()
        }

        loadFavorites()
    }

    private fun loadFavorites() {
        FirestoreManager.fetchFavorites { favorites, error ->
            if (error != null) {
                Toast.makeText(requireContext(), error, Toast.LENGTH_SHORT).show()
                return@fetchFavorites
            }
            adapter.submitList(favorites ?: emptyList())
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
