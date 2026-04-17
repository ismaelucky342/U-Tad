package com.example.unidad2proyecto

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.unidad2proyecto.databinding.ActivityMainBinding
import com.example.unidad2proyecto.fragments.FavoritesFragment
import com.example.unidad2proyecto.fragments.LoginFragment
import com.example.unidad2proyecto.fragments.ProductListFragment
import com.example.unidad2proyecto.fragments.RegisterFragment

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        showLogin()
    }

    fun showLogin() {
        supportFragmentManager.beginTransaction()
            .replace(binding.fragmentContainer.id, LoginFragment())
            .commit()
    }

    fun showRegister() {
        supportFragmentManager.beginTransaction()
            .replace(binding.fragmentContainer.id, RegisterFragment())
            .addToBackStack(null)
            .commit()
    }

    fun showProducts() {
        supportFragmentManager.beginTransaction()
            .replace(binding.fragmentContainer.id, ProductListFragment())
            .commit()
    }

    fun showFavorites() {
        supportFragmentManager.beginTransaction()
            .replace(binding.fragmentContainer.id, FavoritesFragment())
            .addToBackStack(null)
            .commit()
    }
}
