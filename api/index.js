require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connectDB = require('./db'); 

const app = express();
const port = 8000;

// Set allowed origins based on environment
const allowedOrigin = process.env.NODE_ENV === 'production'
  ? 'https://www.techshoppingbuddy.com'
  : 'http://localhost:5174';

app.use(cors({
  origin: allowedOrigin,
  credentials: true
}));

// Middleware to parse JSON
app.use(express.json());

connectDB();

// A simple route
app.get('/', (req, res) => {
  res.send('Server running!');
});

app.use('/api/products', require('./controller/products_controller'));

// Start the server
app.listen(port, () => {
  console.log(`Server listening on http://localhost:${port}`);
});
