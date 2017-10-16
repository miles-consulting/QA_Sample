run tests with 'npm test'

Requirements:
Python3 in PATH
selenium-webdriver installed via pip
gecko-webdriver installed and in PATH

npm test executes ./tests/test.js
test.js starts the server and calls backendtest.js and calls python driver.py
backendtest.js just does a simple test of the users to make sure it actually returns something (isn't NULL)
driver.py conducts the front-end tests. This actually tests to make sure that each thing in the requirements is displayed
