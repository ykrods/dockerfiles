/**
 * settings
 *
 * - Resolve values depending on the environment.
 */
const envParse = require('./lib/envParse');

module.exports = {
  SERVER_PORT: envParse.int('SERVER_PORT', 3000),
};
