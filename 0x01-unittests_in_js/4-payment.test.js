const utils = require('./utils');
const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');



describe('sendPaymentRequestToApi', () => {
    it('tests sendPaymentRequestToApi function call to calculateNumber', () => {
        const bond007 = sinon.spy(utils, 'calculateNumber')
        sendPaymentRequestToApi(100, 20)
        expect(bond007.calledWith('SUM', 100, 20)).to.be.true;
        bond007.restore();

    });

    it('tests sendPaymentRequestToApi function call to calculateNumber using stubs', () => {
        const stub = sinon.stub(utils, 'calculateNumber').returns(10);
        const bond007 = sinon.spy(console, 'log');
        sendPaymentRequestToApi(100, 20)
        expect(bond007.calledWith('The total is: 10')).to.be.true;
        stub.restore();
        bond007.restore();

    });



  });