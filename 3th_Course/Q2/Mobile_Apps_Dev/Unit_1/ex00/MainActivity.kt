package com.ejercicio.ex00

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.ejercicio.ex00.databinding.ActivityMainBinding

// Ejercicio 00 — Hola Mundo con eventos
// Campo de texto + botón + resultado. Si el campo está vacío, Toast de error.

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.botonSaludar.setOnClickListener {
            val nombre = binding.campoNombre.text.toString().trim()
            if (nombre.isEmpty()) {
                Toast.makeText(this, "Escribe un nombre", Toast.LENGTH_SHORT).show()
            } else {
                binding.textoSaludo.text = "¡Hola, $nombre!"
            }
        }

        binding.botonLimpiar.setOnClickListener {
            binding.campoNombre.text.clear()
            binding.textoSaludo.text = ""
        }
    }
}
