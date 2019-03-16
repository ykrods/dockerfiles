const express = require('express');
const exampleRouter = require('./example/router');

const app = express();

// Request Logger
app.use((req, res, next) => {
  console.log(`[${(new Date()).toISOString()}] ${req.method} ${req.path}`);
  next();
});

app.use(exampleRouter);

// Global error handler
app.use((err, req, res, next) => {
  if (res.headersSent) {
    return next(err);
  }
  console.log(err);
  res.status(500).json({ error: 'Internal Server Error' });
});

module.exports = app;
