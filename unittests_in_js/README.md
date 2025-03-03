# Unittests in JS

## Description  
This project focuses on learning JavaScript unit testing. It involves writing tests to ensure that functions perform correctly. The project highlights the importance of testing for reliable, bug-free code.

## Resources
Read or watch:
 - Mocha documentation
 - Chai
 - Sinon
 - Express
 - Request
 - How to Test NodeJS Apps using Mocha, Chai and SinonJS

## Learning Objectives
By the end of this project, you should be able to:
 - How to use Mocha to write a test suite
 - How to use different assertion libraries (Node or Chai)
 - How to present long test suites
 - When and how to use spies
 - When and how to use stubs
 - What are hooks and when to use them
 - Unit testing with Async functions
 - How to write integration tests with a small node server

## Requirements
 - All of your code will be executed on Ubuntu 20.04 using Node 20.x.x
 - Allowed editors: vi, vim, emacs, Visual Studio Code
 - All your files should end with a new line
 - A README.md file, at the root of the folder of the project, is mandatory
 - Your code should use the js extension
 - When running every test with npm run test *.test.js, everything should pass correctly without any warning or error

## Tasks

### 0. Basic Test with Mocha and Node Assertion Library
- Install Mocha using npm.
- Configure `npm test` to run Mocha.
- Create `0-calcul.js` implementing `calculateNumber(a, b)`, which rounds both numbers and returns their sum.
- Write test cases in `0-calcul.test.js` using `assert`.
- Ensure tests pass without warnings.

### 1. Combining Descriptions
- Create `1-calcul.js`, modifying `calculateNumber` to accept a new first argument `type` (`SUM`, `SUBTRACT`, `DIVIDE`).
- Implement logic for each operation, rounding inputs.
- Return `"Error"` if division by zero occurs.
- Write test cases in `1-calcul.test.js` using `assert`.

### 2. Basic Test Using Chai Assertion Library
- Copy `1-calcul.js` to `2-calcul_chai.js`.
- Copy `1-calcul.test.js` to `2-calcul_chai.test.js` and rewrite using Chai's `expect`.
- Ensure all tests pass using `npm test 2-calcul_chai.test.js`.

### 3. Spies
- Install Sinon using npm.
- Create `utils.js` with a `Utils` module containing `calculateNumber`.
- Create `3-payment.js` implementing `sendPaymentRequestToApi(totalAmount, totalShipping)`, which calls `Utils.calculateNumber('SUM', totalAmount, totalShipping)`.
- Write `3-payment.test.js` using Sinon spies to validate function calls.

### 4. Stubs
- Copy `3-payment.js` to `4-payment.js`.
- Copy `3-payment.test.js` to `4-payment.test.js`.
- Stub `Utils.calculateNumber` to always return `10`.
- Verify correct function calls and log outputs using spies.

### 5. Hooks
- Copy `4-payment.js` to `5-payment.js`.
- Create `5-payment.test.js` with two tests:
  - Call `sendPaymentRequestToApi(100, 20)` and verify output.
  - Call `sendPaymentRequestToApi(10, 10)` and verify output.
- Use `beforeEach` and `afterEach` hooks to set up and restore spies.

### 6. Async Testing with Done
- Modify `Utils.calculateNumber` in `6-utils.js` to be asynchronous.
- Update `sendPaymentRequestToApi` in `6-payment.js` to handle async calls.
- Write `6-payment.test.js` using Mocha’s `done` callback for async testing.

### 7. Testing Promises
- Convert `calculateNumber` to return a Promise in `7-utils.js`.
- Update `sendPaymentRequestToApi` in `7-payment.js` to use Promises.
- Write `7-payment.test.js` using Chai’s `expect` with `eventually`.

### 8. Testing Async/Await
- Modify `calculateNumber` in `8-utils.js` to use `async/await`.
- Update `sendPaymentRequestToApi` in `8-payment.js` accordingly.
- Write `8-payment.test.js` using Mocha’s async handling.

### 9. Mocking APIs
- Create `9-api.js` simulating an external API call.
- Implement `fetchPaymentDetails(userId)`, returning mocked data.
- Write `9-api.test.js` using Sinon to mock API responses.

### 10. Full Test Suite with Coverage
- Ensure all functions are properly tested.
- Use `nyc` for test coverage analysis.
- Run `npm test` and verify full coverage.

**Repository:**  
GitHub: `atlas-web_back_end`  
Directory: `unittests_in_js`  

## Author
[Jesse Brumley](https://github.com/jessebrumley)
