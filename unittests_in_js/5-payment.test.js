const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');
const assert = require('assert');

describe('sendPaymentRequestToApi', function () {
    let spyConsoleLog;

    beforeEach(function () {
        // Spy on console.log
        spyConsoleLog = sinon.spy(console, 'log');
    });

    it('should always return 10 when calling Utils.calculateNumber', function () {
        sendPaymentRequestToApi(100, 20);

        // Asserts that console.log displays stub result
        assert(spyConsoleLog.calledOnceWith('The total is: 120'));
    });

    it('should always return 10 when calling Utils.calculateNumber', function () {
        sendPaymentRequestToApi(10, 10);

        // Asserts that console.log displays stub result
        assert(spyConsoleLog.calledOnceWith('The total is: 20'));
    });

    afterEach(function () {
        // restores the console
        spyConsoleLog.restore();
    })
});
