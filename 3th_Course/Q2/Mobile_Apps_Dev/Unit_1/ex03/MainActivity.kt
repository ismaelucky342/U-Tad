package com.ejercicio.ex03

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.app.AppCompatDelegate
import com.ejercicio.ex03.databinding.ActivityMainBinding

// Ejercicio 03 — Internacionalización
// La app carga strings según el idioma del sistema sin ningún código extra.
// Prueba: cambia el idioma del emulador (Settings > System > Language) y relanza la app.
//
// Estructura de recursos necesaria:
//   res/values/strings.xml         → inglés (por defecto)
//   res/values-es/strings.xml      → español
//   res/values-night/themes.xml    → tema oscuro
//
// Los strings se referencian en XML con @string/nombre
// y en código con getString(R.string.nombre)

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // mostrar el idioma actual en tiempo de ejecución
        val locale = resources.configuration.locales[0]
        binding.textoLocale.text = "Locale activo: ${locale.displayName}"

        binding.botonOscuro.setOnClickListener {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)
        }

        binding.botonClaro.setOnClickListener {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
        }

        binding.botonSistema.setOnClickListener {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_FOLLOW_SYSTEM)
        }
    }
}
