package com.ejercicio.ex02

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.ejercicio.ex02.databinding.ActivityResumenBinding

// Ejercicio 02 — Paso de datos entre Activities (pantalla 2 de 2)
// Recibe los datos del intent y los muestra. finish() vuelve a la pantalla anterior.

class ResumenActivity : AppCompatActivity() {
    private lateinit var binding: ActivityResumenBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityResumenBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val nombre = intent.getStringExtra("NOMBRE") ?: "Desconocido"
        val edad   = intent.getIntExtra("EDAD", 0)
        val curso  = intent.getStringExtra("CURSO") ?: "—"

        binding.textoResumen.text = """
            Nombre: $nombre
            Edad:   $edad años
            Curso:  $curso
        """.trimIndent()

        // determinar si es mayor de edad para mostrar un mensaje extra
        binding.textoExtra.text = if (edad >= 18) "✓ Mayor de edad" else "✗ Menor de edad"

        binding.botonVolver.setOnClickListener {
            finish()  // destruye esta Activity y vuelve a la del backstack
        }
    }
}
