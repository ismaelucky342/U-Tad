package com.example.aec1.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.aec1.adapter.ProductAdapter
import com.example.aec1.databinding.FragmentCartBinding
import com.example.aec1.model.Product
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.*

class CartFragment : Fragment() {

    private var _binding: FragmentCartBinding? = null
    private val binding get() = _binding!!
    private lateinit var adapter: ProductAdapter
    private val cartProducts = mutableListOf<Product>()
    private val databaseUrl = "https://aec1-8a207-default-rtdb.europe-west1.firebasedatabase.app"

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCartBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        adapter = ProductAdapter(cartProducts, { product ->
            // Acción al pulsar estrella en el carrito (opcional)
        }, null)
        binding.rvCart.layoutManager = LinearLayoutManager(context)
        binding.rvCart.adapter = adapter

        binding.btnClearCart.setOnClickListener {
            clearCart()
        }

        loadCart()
    }

    private fun loadCart() {
        val userId = FirebaseAuth.getInstance().currentUser?.uid ?: return
        val ref = FirebaseDatabase.getInstance(databaseUrl).getReference("cart").child(userId)
        ref.addValueEventListener(object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                cartProducts.clear()
                var total = 0.0
                for (child in snapshot.children) {
                    val product = child.getValue(Product::class.java)
                    if (product != null) {
                        cartProducts.add(product)
                        total += (product.price * product.quantity)
                    }
                }
                adapter.updateData(cartProducts)
                if (isAdded) {
                    binding.tvTotal.text = "Total: ${String.format("%.2f", total)} €"
                }
            }

            override fun onCancelled(error: DatabaseError) {
                if (isAdded) Toast.makeText(context, "Error: ${error.message}", Toast.LENGTH_SHORT).show()
            }
        })
    }

    private fun clearCart() {
        val userId = FirebaseAuth.getInstance().currentUser?.uid ?: return
        FirebaseDatabase.getInstance(databaseUrl).getReference("cart").child(userId)
            .removeValue()
            .addOnSuccessListener {
                if (isAdded) Toast.makeText(context, "Carrito vaciado", Toast.LENGTH_SHORT).show()
            }
            .addOnFailureListener { e ->
                if (isAdded) Toast.makeText(context, "Error: ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}