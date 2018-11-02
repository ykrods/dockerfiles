const calc = require('../../src/appmodels/calc')

beforeAll(() => {
  console.log("beforeall")
})

afterAll(() => {
  console.log("afterall")
})

beforeEach(() => {
  console.log("before each")
})

afterEach(() => {
  console.log("after each")
})

test('add 1 + 2 to equal 3', () => {
  console.log("test 1 + 2")
  expect(calc.sum(1, 2)).toBe(3);
})

test.each([
  [1, 1, 2],
  [1, 2, 3]
])('add %i and %i', (a, b, expected) => {
  console.log(`${a} + ${b}`);
  expect(calc.sum(a, b)).toBe(expected);
})
