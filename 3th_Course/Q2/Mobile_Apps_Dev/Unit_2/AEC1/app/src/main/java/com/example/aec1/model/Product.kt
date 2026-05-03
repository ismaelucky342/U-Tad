package com.example.aec1.model

data class Product(
    var id: Int = 0,
    var title: String = "",
    var price: Double = 0.0,
    var description: String = "",
    var category: String = "",
    var image: String = "",
    var quantity: Int = 1
) {
    // Required for Firebase
    constructor() : this(0, "", 0.0, "", "", "", 1)
}