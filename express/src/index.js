const express = require('express');
const http = require('http');

const app = express();
const server = http.Server(app);

app.get('/', (req, res) => {
  res.send('Hello World');
});

server.listen(3000, () => {
  console.log("Example app listening on port 3000!");
});

process.on('SIGINT', () => {
  console.log('shutdown')
  process.exit()
});
