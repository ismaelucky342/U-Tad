package com.ejercicio.ex01

import android.os.Bundle
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.ejercicio.ex01.databinding.ActivityContadorBinding

// Ejercicio 01 — Contador con ciclo de vida
// El valor del contador sobrevive a rotaciones de pantalla gracias a ViewModel.
// Prueba: incrementa el contador y rota el emulador — el valor no debe resetearse.

class ContadorViewModel : ViewModel() {
    private val _valor = MutableLiveData(0)
    val valor: LiveData<Int> = _valor  // solo lectura desde fuera del ViewModel

    fun incrementar() {
        _valor.value = (_valor.value ?: 0) + 1
    }

    fun decrementar() {
        val actual = _valor.value ?: 0
        if (actual > 0) _valor.value = actual - 1
    }

    fun reset() {
        _valor.value = 0
    }
}

class ContadorActivity : AppCompatActivity() {
    private lateinit var binding: ActivityContadorBinding
    private val vm: ContadorViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityContadorBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // observe: cada vez que el valor cambia, actualiza el TextView
        vm.valor.observe(this) { valor ->
            binding.textoContador.text = valor.toString()
            // botón de restar deshabilitado si el contador está a 0
            binding.botonRestar.isEnabled = valor > 0
        }

        binding.botonSumar.setOnClickListener { vm.incrementar() }
        binding.botonRestar.setOnClickListener { vm.decrementar() }
        binding.botonReset.setOnClickListener { vm.reset() }
    }
}
