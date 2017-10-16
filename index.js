const createServer = require('./src/server.js');
const server = createServer();
console.info('Starting server on port 8080');
server.listen(8080, function onListening() {
    console.info('Server listening on 8080');
    console.info('Visit http://localhost:8080');
});
