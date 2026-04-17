package com.example.unidad2proyecto.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.example.unidad2proyecto.MainActivity
import com.example.unidad2proyecto.databinding.FragmentLoginBinding
import com.example.unidad2proyecto.firebase.FirebaseAuthManager

class LoginFragment : Fragment() {
    private var _binding: FragmentLoginBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentLoginBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.loginButton.setOnClickListener {
            val email = binding.emailEditText.text.toString().trim()
            val password = binding.passwordEditText.text.toString().trim()
            if (email.isEmpty() || password.isEmpty()) {
                Toast.makeText(requireContext(), "Introduce email y contraseña", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            FirebaseAuthManager.signIn(email, password) { success, message ->
                if (success) {
                    (activity as? MainActivity)?.showProducts()
                } else {
                    Toast.makeText(requireContext(), message, Toast.LENGTH_SHORT).show()
                }
            }
        }

        binding.registerText.setOnClickListener {
            (activity as? MainActivity)?.showRegister()
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
