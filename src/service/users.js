const URI = 'http://jsonplaceholder.typicode.com/users';
const http = require('http');

/** Returns all system users */
module.exports = function getUsers(userId) {

    return fetchAll().then(onGotUsers);

    /** Called once we have an array of all users */
    function onGotUsers(users) {
        if (userId) {
            return users.filter(u => u.id === userId)[0];
        } else {
            return users;
        }
    }

    /** Called to fetch an array of all users */
    function fetchAll() {
        return new Promise(function promiseHandler(resolve, reject) {
            http.get(URI, function onResponse(res) {
                const chunks = [];
                res.on('data', chunk => chunks.push(chunk));
                res.on('end', function sendResponse() {
                    const text = chunks.join('');
                    if (res.statusCode === 200) {
                        const data = JSON.parse(text);
                        resolve(data);
                    } else {
                        reject(new Error(text));
                    }
                });
            });
        });
    }

};
