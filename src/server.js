const express = require('express'),
    path = require('path'),
    home = require('./page/home.js'),
    account = require('./page/account.js');

module.exports = function createServer(config) {
    const server = express();

    // Configure the server
    server.set('views', path.join(__dirname, '../views'));
    server.set('view engine', 'jade');

    // Configure the routes
    server.get('/', home);
    server.get('/account', account);

    return server;
};
