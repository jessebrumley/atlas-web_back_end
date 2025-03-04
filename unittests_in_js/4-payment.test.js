const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const assert = require('assert');

describe('sendPaymentRequestToApi', function () {
    it('should always return 10 when calling Utils.calculateNumber', function () {
        // Stub Utils.calculateNumber to always return 10
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

        // Spy on console.log
        const spyConsoleLog = sinon.spy(console, 'log');

        sendPaymentRequestToApi(100, 20);

        // Asserts that the stub was called with 100, 20
        sinon.assert.calledOnceWithExactly(stub, 'SUM', 100, 20);

        // Asserts that console.log displays stub result
        assert(spyConsoleLog.calledOnceWith('The total is: 10'));

        stub.restore();
        spyConsoleLog.restore();
    });
});
