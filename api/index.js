const express = require('express');
const app = express();
const connectDB = require('./db'); 

const port = 8000;

// Middleware to parse JSON
app.use(express.json());

connectDB();

// A simple route
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on http://localhost:${port}`);
});
