const users = require('../src/service/users.js');
const assert = require('assert');

//ensure users actually returns something
module.exports = function testUsers() {
	users().then(users => assert.notEqual(users, null));
	console.log("backend tests passed");
};

 
