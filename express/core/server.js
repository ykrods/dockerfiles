const http = require('http');

const app = require('./app');
const env = require('./env');

const server = http.Server(app);

server.listen(env.SERVER_PORT, () => {
  console.log(`Example app listening on port ${env.SERVER_PORT}`);
});

process.on('SIGINT', () => {
  console.log('shutdown')
  process.exit()
});
