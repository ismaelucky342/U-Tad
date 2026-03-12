package com.ejercicio.ex04

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.ejercicio.ex04.databinding.ActivityIntentsBinding

// Ejercicio 04 — Intents implícitos
// Demuestra los distintos tipos de intents implícitos:
//   - Abrir URL en el navegador
//   - Compartir texto con la hoja nativa
//   - Componer email con cliente de correo
//   - Marcar un número en el teléfono
//   - Abrir ubicación en Google Maps
//
// Con resolveActivity() verificamos antes de lanzar que hay alguna app
// que pueda manejar el intent — sin eso, hay riesgo de crash.

class IntentsActivity : AppCompatActivity() {
    private lateinit var binding: ActivityIntentsBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityIntentsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // 1. Abrir URL en el navegador
        binding.botonNavegador.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
            lanzarSiPosible(intent, "No hay navegador instalado")
        }

        // 2. Compartir texto con la hoja nativa de Android
        binding.botonCompartir.setOnClickListener {
            val intent = Intent(Intent.ACTION_SEND).apply {
                type = "text/plain"
                putExtra(Intent.EXTRA_TEXT, "Aprendiendo intents en Android 🚀")
            }
            // createChooser siempre muestra el menú aunque haya solo una app compatible
            startActivity(Intent.createChooser(intent, "Compartir con..."))
        }

        // 3. Componer email
        binding.botonEmail.setOnClickListener {
            val intent = Intent(Intent.ACTION_SENDTO).apply {
                data = Uri.parse("mailto:profesor@utad.es")
                putExtra(Intent.EXTRA_SUBJECT, "Duda Unidad 1")
                putExtra(Intent.EXTRA_TEXT, "Hola, tengo una duda sobre...")
            }
            lanzarSiPosible(intent, "No hay cliente de email instalado")
        }

        // 4. Marcar número (ACTION_DIAL no requiere permiso; ACTION_CALL sí)
        binding.botonTelefono.setOnClickListener {
            val intent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:+34600000000"))
            lanzarSiPosible(intent, "No hay app de teléfono")
        }

        // 5. Abrir ubicación en Maps
        binding.botonMaps.setOnClickListener {
            // geo:lat,lon?q=query abre Maps centrado en la ubicación
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("geo:40.4168,-3.7038?q=Madrid"))
            lanzarSiPosible(intent, "No hay app de mapas instalada")
        }
    }

    private fun lanzarSiPosible(intent: Intent, mensajeError: String) {
        if (intent.resolveActivity(packageManager) != null) {
            startActivity(intent)
        } else {
            Toast.makeText(this, mensajeError, Toast.LENGTH_SHORT).show()
        }
    }
}
