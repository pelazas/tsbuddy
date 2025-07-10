const express = require('express');
const router = express.Router();
const Product = require('../models/Product');

// 1. GET /products/:productId - Fetch a product by its ID
router.get('/:productId', async (req, res) => {
  try {
    const product = await Product.findById(req.params.productId);
    if (!product) return res.status(404).json({ message: 'Product not found' });
    res.json(product);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
});

// 2. GET /products - For each category, fetch the top 10 products by score in order
router.get('/', async (req, res) => {
  try {
    // Get all unique categories
    const categories = await Product.distinct('category');
    const results = {};

    // For each category, get top 10 products by score (descending)
    for (const category of categories) {
      const topProducts = await Product.find({ category })
        .sort({ score: -1 })
        .limit(10)
        .exec();
      results[category] = topProducts;
    }

    res.json(results);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
});

module.exports = router;


