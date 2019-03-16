/**
 * envParse
 *
 * @example
 * const envParse = require('lib/envParse');
 * const SERVER_PORT = envParse.int('SERVER_PORT', 3000);
 */

const parser = (caster) => {
  return (name, _default) => {
    if (process.env[name] === undefined) {
      if (_default === undefined) {
        throw new Error(`Environment variable ${name} should be defined`);
      }
      return _default;
    }
    return caster(process.env[name]);
  };
}

module.exports = {
  int: parser(value => parseInt(value, 10)),
  bool: parser(value => {
    return ['1', 'y', 'yes', 'on', 'true', 't'].includes(value.toLowerCase());
  }),
};
