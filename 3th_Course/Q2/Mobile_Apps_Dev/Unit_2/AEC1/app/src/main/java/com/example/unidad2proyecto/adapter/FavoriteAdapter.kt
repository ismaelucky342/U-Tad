package com.example.unidad2proyecto.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.example.unidad2proyecto.databinding.ItemFavoriteBinding
import com.example.unidad2proyecto.model.FavoriteItem

class FavoriteAdapter : ListAdapter<FavoriteItem, FavoriteAdapter.FavoriteViewHolder>(FavoriteDiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): FavoriteViewHolder {
        val binding = ItemFavoriteBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return FavoriteViewHolder(binding)
    }

    override fun onBindViewHolder(holder: FavoriteViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class FavoriteViewHolder(private val binding: ItemFavoriteBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(item: FavoriteItem) {
            binding.titleText.text = item.title
            binding.priceText.text = "€${item.price}"
        }
    }
}

class FavoriteDiffCallback : DiffUtil.ItemCallback<FavoriteItem>() {
    override fun areItemsTheSame(oldItem: FavoriteItem, newItem: FavoriteItem) = oldItem.id == newItem.id
    override fun areContentsTheSame(oldItem: FavoriteItem, newItem: FavoriteItem) = oldItem == newItem
}
