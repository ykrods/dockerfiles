const express = require('express');
const exampleRouter = require('../example/router');

const app = express();

app.use((req, res, next) => {
  console.log('(1) Time:', Date.now());
  next();
});

app.use(exampleRouter);

// Error handler
app.use((err, req, res, next) => {
  if (res.headersSent) {
    return next(err);
  }
  res.status(500).json({ error: err.message });
});

module.exports = app;
