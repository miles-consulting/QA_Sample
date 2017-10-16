const getUsers = require('../service/users.js');

module.exports = function homeRoute(req, res, next) {
    getUsers()
        .then(users => res.render('home', { users }))
        .catch(next);
};
