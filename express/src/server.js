const http = require('http');

const app = require('./app');
const settings = require('./core/settings');

const server = http.Server(app);

server.listen(settings.SERVER_PORT, () => {
  console.log(`Listening on port ${settings.SERVER_PORT}`);
});

process.on('SIGINT', () => {
  console.log('shutdown')
  process.exit()
});
