var express = require('express');
var models = require("../models");

var router = express.Router();

/**
 *  GET /users
 */
router.get('/', (req, res, next) => {
  models.User.findAll().then(users => {
    res.send(users);
  });
});

module.exports = router;
