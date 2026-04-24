package com.example.aec1.model

data class Product(
    val id: Int = 0,
    val title: String = "",
    val price: Double = 0.0,
    val description: String = "",
    val category: String = "",
    val image: String = ""
) {
    // Required for Firebase
    constructor() : this(0, "", 0.0, "", "", "")
}