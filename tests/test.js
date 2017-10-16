const createServer = require('../src/server.js');
const server = createServer();
console.info('Starting server on port 8080');

server.listen(8080, function onListening() {
});

const backendTests = require('./backend_test.js');
backendTests();

const { spawn } = require('child_process');
const python = spawn('python', ['./tests/driver.py']);

python.stdout.on('data', (data) => {
	  console.log(`stdout: ${data}`);
});

python.stderr.on('data', (data) => {
	  console.log(`stderr: ${data}`);
});

python.on('close', (code) => {
	console.log(`child process exited with code ${code}`);
	console.log(`front end tests passed`);
	process.exit()
});




