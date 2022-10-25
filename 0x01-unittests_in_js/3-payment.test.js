const utils = require('./utils');
const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');



describe('sendPaymentRequestToApi', () => {
    it('tests sendPaymentRequestToApi function call to calculateNumber', () => {
        const bond007 = sinon.spy(utils, "calculateNumber")
        sendPaymentRequestToApi(100, 20)
        expect(bond007.calledWith('SUM', 100, 20)).to.be.true;
        bond007.restore();

    });
  });