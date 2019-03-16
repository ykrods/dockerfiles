/**
 * promisified sleep
 *
 * @param {Int} time - sleep time (ms)
 */
module.exports = (time) => {
  return new Promise(resolve => setTimeout(() => { resolve() }, time));
};
