const mongoose = require('mongoose');

const ProductSchema = new mongoose.Schema({
  title: { type: String, required: true },
  price: { type: Number, required: true },
  url: { type: String, required: true },
  specs: { type: String }, // JSON string
  rating: { type: String },
  rating_distribution: { type: String }, // JSON string
  score: { type: Number },
  explanation: { type: String },
  n_reviews: { type: String },
  image_url: { type: String },
  created_at: { type: Date, default: Date.now },
  category: { type: String }
});

module.exports = mongoose.model('Product', ProductSchema);