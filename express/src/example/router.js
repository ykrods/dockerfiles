const express = require('express');
const router = express.Router();
const pass = require('../core/pass');

router.get('/', pass(async (req, res, next) => {
  // throw new Error('Someting went wrong!');
  res.json({a: "aaa"});
}));

module.exports = router;
