package com.ejercicio.ex02

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.ejercicio.ex02.databinding.ActivityFormularioBinding

// Ejercicio 02 — Paso de datos entre Activities (pantalla 1 de 2)
// Recoge nombre y edad, valida que no estén vacíos y abre ResumenActivity con los datos.

class FormularioActivity : AppCompatActivity() {
    private lateinit var binding: ActivityFormularioBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityFormularioBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.botonEnviar.setOnClickListener {
            val nombre = binding.campoNombre.text.toString().trim()
            val edadStr = binding.campoEdad.text.toString().trim()
            val curso = binding.campoCurso.text.toString().trim()

            when {
                nombre.isEmpty() -> mostrarError("Escribe tu nombre")
                edadStr.isEmpty() -> mostrarError("Escribe tu edad")
                edadStr.toIntOrNull() == null -> mostrarError("La edad debe ser un número")
                curso.isEmpty() -> mostrarError("Escribe tu curso")
                else -> {
                    val intent = Intent(this, ResumenActivity::class.java).apply {
                        putExtra("NOMBRE", nombre)
                        putExtra("EDAD", edadStr.toInt())
                        putExtra("CURSO", curso)
                    }
                    startActivity(intent)
                }
            }
        }
    }

    private fun mostrarError(msg: String) {
        Toast.makeText(this, msg, Toast.LENGTH_SHORT).show()
    }
}
