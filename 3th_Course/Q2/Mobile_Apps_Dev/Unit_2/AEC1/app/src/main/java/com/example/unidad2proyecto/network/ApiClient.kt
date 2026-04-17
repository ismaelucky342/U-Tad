package com.example.unidad2proyecto.network

import android.content.Context
import com.android.volley.Request
import com.android.volley.toolbox.JsonArrayRequest
import com.android.volley.toolbox.Volley
import com.example.unidad2proyecto.Constants
import com.example.unidad2proyecto.model.Product
import org.json.JSONException

object ApiClient {

    fun fetchProducts(context: Context, completion: (List<Product>?, String?) -> Unit) {
        val queue = Volley.newRequestQueue(context)
        val request = JsonArrayRequest(Request.Method.GET, Constants.PRODUCTS_API_URL, null,
            { response ->
                try {
                    val products = mutableListOf<Product>()
                    for (i in 0 until response.length()) {
                        val item = response.getJSONObject(i)
                        val product = Product(
                            id = item.getInt("id"),
                            title = item.getString("title"),
                            price = item.getDouble("price"),
                            description = item.getString("description"),
                            image = item.getString("image")
                        )
                        products.add(product)
                    }
                    completion(products, null)
                } catch (e: JSONException) {
                    completion(null, "Error parseando productos")
                }
            },
            { error ->
                completion(null, error.message ?: "Error de red")
            }
        )
        queue.add(request)
    }
}
